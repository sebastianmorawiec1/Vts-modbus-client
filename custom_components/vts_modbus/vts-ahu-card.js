/* vts-ahu-card — karta Lovelace dla integracji VTS Modbus.
 * Rysuje schemat centrali z podzespolami dobranymi wg kodu aplikacji
 * "Automatyka 2019" (litera AS/AD/AR/AG/AP/AE + cyfry funkcji).
 *
 * Konfiguracja karty:
 *   type: custom:vts-ahu-card
 *   prefix: vts_192_168_1_60      # prefiks entity_id (z hosta centrali)
 *   name: Centrala hala A          # opcjonalnie
 *   code: AP11000000610000101      # opcjonalnie - nadpisuje kod z sensora app_code
 */
(function () {
  const MODES = { 0: "AUTO", 1: "WYŁ", 2: "STANDBY", 3: "NISKI", 4: "EKONO", 5: "KOMFORT" };
  const ACT = { 0: "Wył", 1: "Grzanie wstępne", 2: "Rozruch", 3: "Standby grzanie", 4: "Standby chłodz.",
    5: "Szybkie grzanie", 6: "Szybkie chłodz.", 7: "Grzanie", 8: "Wentylacja", 9: "Chłodzenie",
    10: "Nocne chłodz.", 11: "Wybieg", 12: "TRYB POŻAROWY", 13: "Nocny test", 14: "AWARYJNY STOP",
    15: "Stop (alarm)", 16: "Stop (alarm kryt.)", 17: "Konfiguracja" };
  const LETTERS = { AS: "supply", AD: "supply_exhaust", AR: "rotary", AG: "glycol", AP: "plate_cross", AE: "exhaust" };
  const DIGITS = { recovery_mode: 1, redundant: 2, main_heater: 3, main_cooler: 4, rev_heater_cooler: 5,
    pre_heater: 6, re_heater: 7, fn_total: 8, upc3_config: 9, ch_base: 10, no_bypass: 11,
    economizer: 12, fast_heating: 13, humidifier: 14, drct: 15 };

  function decode(codeRaw) {
    const code = (codeRaw || "").toUpperCase().replace(/[\s-]/g, "");
    if (code.length < 4 || !LETTERS[code.slice(0, 2)] || !/^\d+$/.test(code.slice(2))) return null;
    const d = code.slice(2);
    const out = { code, letter: code.slice(0, 2), recovery: "none" };
    if (["AR", "AG", "AP"].includes(out.letter)) out.recovery = LETTERS[out.letter];
    out.has_supply = out.letter !== "AE";
    out.has_exhaust = out.letter !== "AS";
    for (const [k, pos] of Object.entries(DIGITS)) out[k] = pos <= d.length ? parseInt(d[pos - 1], 10) : 0;
    out.has_bypass = out.recovery !== "none" && out.no_bypass === 0;
    return out;
  }

  const HEATER_NAMES = { 1: "wodna", 2: "freonowa (DX)", 3: "elektryczna", 4: "parowa" };
  const COOLER_NAMES = { 1: "wodna", 2: "freonowa (DX)" };
  const HUM_NAMES = { 1: "ewaporacyjny", 2: "parowy" };

  class VtsAhuCard extends HTMLElement {
    setConfig(config) {
      if (!config.prefix) throw new Error("vts-ahu-card: wymagane pole 'prefix' (np. vts_192_168_1_60)");
      this._config = config;
      if (!this.shadowRoot) this.attachShadow({ mode: "open" });
    }
    getCardSize() { return 8; }
    set hass(hass) { this._hass = hass; this._render(); }

    _st(domain, reg) { return this._hass.states[`${domain}.${this._config.prefix}_${reg}`]; }
    _val(reg, dflt = "—") { const s = this._st("sensor", reg); return s && !["unknown", "unavailable"].includes(s.state) ? s.state : dflt; }
    _num(reg) { const v = parseFloat(this._val(reg, "NaN")); return isNaN(v) ? null : v; }
    _bin(reg) { const s = this._st("binary_sensor", reg); return s ? s.state === "on" : null; }
    _numEnt(reg) { return this._st("number", reg); }

    _setMode(v) {
      const e = this._numEnt("gopmode_bms");
      if (e) this._hass.callService("number", "set_value", { entity_id: e.entity_id, value: v });
    }
    _ackAlarm() {
      const e = this._hass.states[`switch.${this._config.prefix}_galarmackprg`];
      if (e) this._hass.callService("switch", "turn_on", { entity_id: e.entity_id });
    }

    _svg(f) {
      // Uklad: kanal nawiewny (gora, ->), kanal wywiewny (dol, <-), blok odzysku w srodku.
      const comp = [];
      const duct = (y, color) => `<rect x="20" y="${y}" width="660" height="70" rx="6" fill="#1c1f26" stroke="#3a3f4b"/>`;
      const label = (x, y, t, c = "#9aa4b2") => `<text x="${x}" y="${y}" fill="${c}" font-size="12" text-anchor="middle">${t}</text>`;
      const arrow = (x, y, dir, color) => `<path d="M${x} ${y} l${dir * 26} 0 l${-dir * 8} -7 m${dir * 8} 7 l${-dir * 8} 7" stroke="${color}" stroke-width="5" fill="none" stroke-linecap="round"/>`;
      const filter = (x, y) => `<g><rect x="${x}" y="${y + 8}" width="16" height="54" fill="none" stroke="#8892a0"/><path d="M${x} ${y + 8} ${Array.from({ length: 6 }, (_, i) => `L${x + (i % 2 ? 0 : 16)} ${y + 12 + i * 9}`).join(" ")}" stroke="#8892a0" fill="none"/></g>`;
      const fan = (x, y, on) => `<g class="${on ? "spin" : ""}" style="transform-origin:${x}px ${y}px"><circle cx="${x}" cy="${y}" r="20" fill="#252a33" stroke="#8892a0"/>${[0, 120, 240].map(a => `<path d="M${x} ${y} q 14 -6 18 -16" stroke="#cfd6e0" stroke-width="3" fill="none" transform="rotate(${a} ${x} ${y})"/>`).join("")}</g>`;
      const coil = (x, y, color, tag) => `<g><rect x="${x}" y="${y + 6}" width="26" height="58" fill="none" stroke="${color}" stroke-width="2"/>${[0, 1, 2].map(i => `<path d="M${x + 5 + i * 8} ${y + 10} v50" stroke="${color}" stroke-width="2"/>`).join("")}${label(x + 13, y + 80, tag, color)}</g>`;
      const humid = (x, y) => `<g>${[0, 1, 2].map(i => `<path d="M${x + i * 10} ${y + 20} q -5 10 0 14 q 5 -4 0 -14" fill="#4fc3f7"/>`).join("")}${label(x + 10, y + 52, "nawilż.", "#4fc3f7")}</g>`;

      // kanaly
      comp.push(duct(60), duct(210));
      comp.push(label(60, 50, f.has_supply ? "CZERPNIA" : ""), label(640, 50, f.has_supply ? "NAWIEW" : ""));
      comp.push(label(640, 300, f.has_exhaust ? "WYWIEW" : ""), label(60, 300, f.has_exhaust ? "WYRZUTNIA" : ""));
      if (f.has_supply) { comp.push(arrow(28, 95, 1, "#4a9eff"), arrow(640, 95, 1, "#4a9eff"), filter(120, 60), fan(560, 95, this._fanOn("sup"))); }
      if (f.has_exhaust) { comp.push(arrow(660, 245, -1, "#ff6b5e"), arrow(60, 245, -1, "#ff6b5e"), filter(560, 210), fan(140, 245, this._fanOn("exh"))); }

      // odzysk
      if (f.recovery === "rotary") {
        comp.push(`<circle cx="350" cy="170" r="78" fill="#232833" stroke="#c9a94a" stroke-width="3"/>`,
          `<circle cx="350" cy="170" r="12" fill="#c9a94a"/>`,
          ...[0,45,90,135].map(a => `<line x1="278" y1="170" x2="422" y2="170" stroke="#c9a94a" transform="rotate(${a} 350 170)"/>`),
          label(350, 268, "wymiennik obrotowy", "#c9a94a"));
      } else if (f.recovery === "plate_cross") {
        comp.push(`<rect x="288" y="108" width="124" height="124" fill="#232833" stroke="#c9a94a" stroke-width="3" transform="rotate(45 350 170)"/>`,
          `<line x1="288" y1="108" x2="412" y2="232" stroke="#c9a94a" transform="rotate(45 350 170)"/>`,
          label(350, 268, "wymiennik krzyżowy", "#c9a94a"));
      } else if (f.recovery === "glycol") {
        comp.push(coil(300, 60, "#c9a94a", ""), coil(374, 210, "#c9a94a", ""),
          `<path d="M313 128 v40 h74 v42" stroke="#c9a94a" stroke-width="2" fill="none" stroke-dasharray="5 4"/>`,
          label(350, 268, "odzysk glikolowy", "#c9a94a"));
      } else if (f.economizer) {
        comp.push(`<rect x="320" y="120" width="60" height="100" fill="#232833" stroke="#c9a94a"/>`,
          ...[0,1,2].map(i => `<line x1="326" y1="${132 + i * 30}" x2="374" y2="${146 + i * 30}" stroke="#c9a94a" stroke-width="3"/>`),
          label(350, 268, "komora mieszania", "#c9a94a"));
      }
      if (f.has_bypass) comp.push(label(350, 30, `By-pass: ${this._bypassState()}`, "#4fc3f7"));

      // nagrzewnice/chlodnice na kanale nawiewnym (za odzyskiem)
      let x = 450;
      if (f.pre_heater > 0) { comp.push(coil(180, 60, "#ff8a65", `nagrz. wst. ${HEATER_NAMES[f.pre_heater] || ""}`)); }
      if (f.main_heater > 0) { comp.push(coil(x, 60, "#ff5252", `nagrzewnica ${HEATER_NAMES[f.main_heater] || ""}`)); x += 44; }
      if (f.main_cooler > 0) { comp.push(coil(x, 60, "#40c4ff", `chłodnica ${COOLER_NAMES[f.main_cooler] || ""}`)); x += 44; }
      if (f.rev_heater_cooler > 0) { comp.push(coil(x, 60, "#ab7df6", "rewers. grz/chł")); x += 44; }
      if (f.re_heater > 0) { comp.push(coil(x, 60, "#ff8a65", "nagrz. wtórna")); x += 40; }
      if (f.humidifier > 0) { comp.push(humid(x + 6, 60)); }

      return `<svg viewBox="0 0 700 310" xmlns="http://www.w3.org/2000/svg">${comp.join("")}</svg>`;
    }

    _fanOn(which) {
      const v = this._num(which === "sup" ? "gfan_supoutputfreq_1" : "gfan_exhoutputfreq_1");
      return v !== null && v > 0.5;
    }
    _bypassState() {
      const reco = this._num("goutputao_reco");
      if (reco === null) return "—";
      return reco < 5 ? "Otwarty" : "Zamknięty";
    }

    _render() {
      if (!this._hass || !this._config) return;
      const cfg = this._config;
      const codeSensor = this._st("sensor", "app_code");
      const code = cfg.code || (codeSensor ? codeSensor.state : null);
      const f = decode(code) || { recovery: "none", has_supply: true, has_exhaust: true, has_bypass: false,
        main_heater: 0, main_cooler: 0, pre_heater: 0, re_heater: 0, rev_heater_cooler: 0, humidifier: 0, economizer: 0 };

      const act = this._num("gactopmode");
      const mode = this._num("gopmode_main");
      const alarm = this._bin("global_alarm");
      const supT = this._val("ginputai_1_sup"), exhT = this._val("ginputai_2_exh");
      const outT = this._val("ginputai_3_out"), recoT = this._val("ginputai_4_reco");
      const supF = this._val("gfan_supoutputfreq_1"), exhF = this._val("gfan_exhoutputfreq_1");
      const reco = this._val("goutputao_reco");
      const htg = this._val("goutputao_htg"), clg = this._val("goutputao_clg");
      const running = act !== null && act >= 1 && act <= 13 && act !== 0;
      const filterSup = this._bin("falarm_supfilters"), filterExh = this._bin("falarm_exhfilters");

      const chip = (icon, lab, val, color) => `<div class="chip"><span class="ic" style="background:${color}22;color:${color}">${icon}</span><div><div class="cl">${lab}</div><div class="cv">${val}</div></div></div>`;
      const modeBtn = (v, t) => `<button class="mb ${mode === v ? "on" : ""}" data-mode="${v}">${t}</button>`;

      this.shadowRoot.innerHTML = `
      <style>
        :host{display:block}
        .card{background:var(--ha-card-background,#14161b);border-radius:14px;padding:14px;color:#e6eaf0;font-family:var(--primary-font-family,Roboto,sans-serif)}
        .hdr{display:flex;align-items:center;gap:10px;margin-bottom:10px}
        .pw{width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:20px;background:${running ? "#2e7d3222" : "#55555522"};color:${running ? "#66bb6a" : "#9aa4b2"}}
        .hname{font-size:17px;font-weight:600}
        .hstate{font-size:12px;color:${running ? "#66bb6a" : "#9aa4b2"}}
        .badge{margin-left:auto;font-size:12px;padding:4px 10px;border-radius:20px;background:${alarm ? "#c6282833" : "#2e7d3222"};color:${alarm ? "#ff6b5e" : "#66bb6a"}}
        .chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:10px}
        .chip{display:flex;gap:8px;align-items:center;background:#1c1f26;border-radius:10px;padding:6px 10px;min-width:110px}
        .ic{width:28px;height:28px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:15px}
        .cl{font-size:10px;color:#9aa4b2}.cv{font-size:14px;font-weight:600}
        svg{width:100%;height:auto;background:#101218;border-radius:10px}
        .spin{animation:spin 1.6s linear infinite}
        @keyframes spin{to{transform:rotate(360deg)}}
        .row{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap;align-items:center}
        .mb{background:#1c1f26;border:1px solid #3a3f4b;color:#cfd6e0;padding:6px 12px;border-radius:8px;cursor:pointer;font-size:12px}
        .mb.on{background:#1565c0;border-color:#1565c0;color:#fff}
        .ack{margin-left:auto;background:#c62828;border:none;color:#fff;padding:6px 12px;border-radius:8px;cursor:pointer;font-size:12px}
        .code{font-size:10px;color:#5f6774;margin-top:8px}
      </style>
      <div class="card">
        <div class="hdr">
          <div class="pw">⏻</div>
          <div><div class="hname">${cfg.name || "Centrala VTS"}</div>
          <div class="hstate">${act !== null ? ACT[act] || act : "brak danych"} · tryb: ${mode !== null ? MODES[mode] || mode : "—"}</div></div>
          <div class="badge">${alarm ? "⚠ ALARM" : "✓ Brak alarmów"}</div>
        </div>
        <div class="chips">
          ${chip("🌡", "Nawiew", supT + " °C", "#4a9eff")}
          ${chip("🌡", "Wywiew", exhT + " °C", "#ff6b5e")}
          ${chip("🌡", "Czerpnia", outT + " °C", "#4fc3f7")}
          ${chip("🌡", "Za odzyskiem", recoT + " °C", "#c9a94a")}
          ${chip("𖣘", "Went. nawiew", supF + " Hz", "#4a9eff")}
          ${chip("𖣘", "Went. wywiew", exhF + " Hz", "#ff6b5e")}
          ${chip("♻", "Odzysk", reco + " %", "#66bb6a")}
          ${chip("🔥", "Grzanie", htg + " %", "#ff5252")}
          ${chip("❄", "Chłodzenie", clg + " %", "#40c4ff")}
          ${filterSup !== null ? chip("▤", "Filtr nawiew", filterSup ? "WYMIEŃ" : "OK", filterSup ? "#ff6b5e" : "#66bb6a") : ""}
          ${filterExh !== null ? chip("▤", "Filtr wywiew", filterExh ? "WYMIEŃ" : "OK", filterExh ? "#ff6b5e" : "#66bb6a") : ""}
        </div>
        ${this._svg(f)}
        <div class="row">
          ${modeBtn(0, "AUTO")}${modeBtn(1, "WYŁ")}${modeBtn(3, "NISKI")}${modeBtn(4, "EKONO")}${modeBtn(5, "KOMFORT")}
          ${alarm ? '<button class="ack">Kasuj alarmy</button>' : ""}
        </div>
        <div class="code">${f.code ? "Kod: " + f.code + " · odzysk: " + f.recovery : "Brak kodu aplikacji — schemat domyślny. Dodaj 'code:' w konfiguracji karty lub kod w integracji."}</div>
      </div>`;

      this.shadowRoot.querySelectorAll(".mb").forEach(b =>
        b.addEventListener("click", () => this._setMode(parseInt(b.dataset.mode, 10))));
      const ack = this.shadowRoot.querySelector(".ack");
      if (ack) ack.addEventListener("click", () => this._ackAlarm());
    }

    static getStubConfig() { return { prefix: "vts_192_168_1_60", name: "Centrala VTS" }; }
  }

  customElements.define("vts-ahu-card", VtsAhuCard);
  window.customCards = window.customCards || [];
  window.customCards.push({
    type: "vts-ahu-card",
    name: "VTS AHU Card",
    description: "Schemat centrali VTS z podzespołami wg kodu aplikacji (Automatyka 2019)",
  });
})();
