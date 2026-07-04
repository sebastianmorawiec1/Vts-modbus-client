# Mapa rejestrow Modbus TCP/IP dla sterownikow VTS typu VS...uPC
# z modulem rozszerzen Carel TCP/IP.
# Zrodlo: instrukcja VTS, https://vtsgroup.com/files/document-files/151/TCP_IP_Carel_expension_module_pl.pdf
#
# Adresowanie: pole `address` = kolumna 'Modbus Index' z dokumentacji (bez -1).
# Jesli odczyty beda przesuniete o 1 rejestr, odejmij 1 od wszystkich adresow.
# Analog/Integer -> rejestry holding; Digital -> coile.

gFan_ExhFreqRef:
  address: 1
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwośc odniesienia dla Wywiewu (zależna od trybu Low/Econo/Comf)"

gFan_ExhOutputCurr_1:
  address: 2
  table: holding
  data_type: int16
  scale: 0.1
  unit: "A"
  access: read
  description: "Prąd na wyjściu FC1 Wywiewu"

gFan_ExhOutputCurr_2:
  address: 3
  table: holding
  data_type: int16
  scale: 0.1
  unit: "A"
  access: read
  description: "Prąd na wyjściu FC2 Wywiewu"

gFan_ExhOutputCurr_3:
  address: 4
  table: holding
  data_type: int16
  scale: 0.1
  unit: "A"
  access: read
  description: "Prąd na wyjściu FC3 Wywiewu"

gFan_ExhOutputCurr_4:
  address: 5
  table: holding
  data_type: int16
  scale: 0.1
  unit: "A"
  access: read
  description: "Prąd na wyjściu FC4 Wywiewu"

gFan_ExhOutputFreq_1:
  address: 6
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwość wyjściowa FC1 Wywiewu"

gFan_ExhOutputFreq_2:
  address: 7
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwość wyjściowa FC2 Wywiewu"

gFan_ExhOutputFreq_3:
  address: 8
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwość wyjściowa FC3 Wywiewu"

gFan_ExhOutputFreq_4:
  address: 9
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwość wyjściowa FC4 Wywiewu"

gFan_SupFreqRef:
  address: 10
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwośc odniesienia dla Nawiewu (zależna od trybu Low/Econo/Comf)"

gFan_SupOutputCurr_1:
  address: 11
  table: holding
  data_type: int16
  scale: 0.1
  unit: "A"
  access: read
  description: "Prąd na wyjściu FC1 Nawiewu"

gFan_SupOutputCurr_2:
  address: 12
  table: holding
  data_type: int16
  scale: 0.1
  unit: "A"
  access: read
  description: "Prąd na wyjściu FC2 Nawiewu"

gFan_SupOutputCurr_3:
  address: 13
  table: holding
  data_type: int16
  scale: 0.1
  unit: "A"
  access: read
  description: "Prąd na wyjściu FC3 Nawiewu"

gFan_SupOutputCurr_4:
  address: 14
  table: holding
  data_type: int16
  scale: 0.1
  unit: "A"
  access: read
  description: "Prąd na wyjściu FC4 Nawiewu"

gFan_SupOutputFreq_1:
  address: 15
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwość wyjściowa FC1 Nawiewu"

gFan_SupOutputFreq_2:
  address: 16
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwość wyjściowa FC2 Nawiewu"

gFan_SupOutputFreq_3:
  address: 17
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwość wyjściowa FC3 Nawiewu"

gFan_SupOutputFreq_4:
  address: 18
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwość wyjściowa FC4 Nawiewu"

gInputAI_1_Sup:
  address: 19
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Wejście analogowe AI 1 jako czujnik temp. nawiewu"
  device_class: temperature

gInputAI_2_Exh:
  address: 20
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Wejście analogowe AI 2 jako czujnik temp. wywiewu"
  device_class: temperature

gInputAI_2_Room:
  address: 21
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Wejście analogowe AI 2 jako czujnik temp. w pomieszczeniu"
  device_class: temperature

gInputAI_3_Out:
  address: 22
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Wejście analogowe AI 3 jako czujnik temp. zewnętrznej"
  device_class: temperature

gInputAI_4_Reco:
  address: 23
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Wejście analogowe AI 4 jako czujnik temp.za odzyskiem"
  device_class: temperature

gInputAI_5_RetHW:
  address: 24
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Wejście analogowe AI 5 jako czujnik temp. wody powrotnej nagrzewnicy"
  device_class: temperature

gInputAI_6_PHHW:
  address: 25
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Wejście analogowe AI 6 jako czujnik temp. powietrza za nagrzewnicą wstępną"
  device_class: temperature

gInputAI_7_RetPHHW:
  address: 26
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Wejście analogowe AI 7 jako czujnik temp. wody powrotnej nagrzewnicy wstępnej"
  device_class: temperature

gInputAI_7_User:
  address: 27
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read
  description: "Wejście analogowe AI 7 jako wejście uniwersalne AI"

gInputAI_MainSensor:
  address: 28
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Wejście analogowe - czujnik wiodący (zależy od nastawy aplikacji)"
  device_class: temperature

gInputAI_Offset_1:
  address: 29
  table: holding
  data_type: int16
  scale: 0.1
  unit: "K"
  access: read_write
  description: "Offset for AI 1"
  min: -10.0
  max: 10.0
  step: 0.1

gInputAI_Offset_2:
  address: 30
  table: holding
  data_type: int16
  scale: 0.1
  unit: "K"
  access: read_write
  description: "Offset for AI 2"
  min: -10.0
  max: 10.0
  step: 0.1

gInputAI_Offset_3:
  address: 31
  table: holding
  data_type: int16
  scale: 0.1
  unit: "K"
  access: read_write
  description: "Offset for AI 3"
  min: -10.0
  max: 10.0
  step: 0.1

gInputAI_Offset_4:
  address: 32
  table: holding
  data_type: int16
  scale: 0.1
  unit: "K"
  access: read_write
  description: "Offset for AI 4"
  min: -10.0
  max: 10.0
  step: 0.1

gInputAI_Offset_5:
  address: 33
  table: holding
  data_type: int16
  scale: 0.1
  unit: "K"
  access: read_write
  description: "Offset for AI 5"
  min: -10.0
  max: 10.0
  step: 0.1

gInputAI_Offset_6:
  address: 34
  table: holding
  data_type: int16
  scale: 0.1
  unit: "K"
  access: read_write
  description: "Offset for AI 6"
  min: -10.0
  max: 10.0
  step: 0.1

gInputAI_Offset_7:
  address: 35
  table: holding
  data_type: int16
  scale: 0.1
  unit: "K"
  access: read_write
  description: "Offset for AI 7"
  min: -10.0
  max: 10.0
  step: 0.1

gLimit_DZ_Comf:
  address: 36
  table: holding
  data_type: int16
  scale: 0.1
  unit: "K"
  access: read_write
  description: "Strefa nieczułości dla regulacji temp. w trybie Komfort"
  min: 1.0
  max: 10.0
  step: 0.1

gLimit_DZ_Eco:
  address: 37
  table: holding
  data_type: int16
  scale: 0.1
  unit: "K"
  access: read_write
  description: "Strefa nieczułości dla regulacji temp. w trybie Ekono"
  min: 1.0
  max: 10.0
  step: 0.1

gLimit_DZ_Low:
  address: 38
  table: holding
  data_type: int16
  scale: 0.1
  unit: "K"
  access: read_write
  description: "Strefa nieczułości dla regulacji temp. w trybie Niski"
  min: 1.0
  max: 10.0
  step: 0.1

gLimit_FireTempLimit:
  address: 39
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read_write
  description: "Ograniczenie temp. powietrza nawiewu/wywiewu dla aktywacji alarmu pożarowego"
  device_class: temperature
  min: 70.0
  max: 97.0
  step: 0.1

gLimit_MinOutTempForClg:
  address: 40
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Min temp. zewnętrzna dla funkcji chłodzenia"
  device_class: temperature

gLimit_MinOutTempForPumpHW:
  address: 41
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Temp. zewnętrzna startu pompy recyrkulacyjnej nagrzewnicy wodnej"
  device_class: temperature

gLimit_MinOutTempForPumpPHHW:
  address: 42
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Temp. zewnętrzna startu pompy recyrkulacyjnej wstępnej nagrzewnicy wodnej"
  device_class: temperature

gLimit_MixCmbrAtComf:
  address: 43
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Ograniczenie min. ilości powietrza świeżego dla komory mieszania w trybie Komfort"
  min: 0.0
  max: 100.0
  step: 0.1

gLimit_MixCmbrAtEcono:
  address: 44
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Ograniczenie min. ilości powietrza świeżego dla komory mieszania w trybie Ekono"
  min: 0.0
  max: 100.0
  step: 0.1

gLimit_MixCmbrAtLow:
  address: 45
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Ograniczenie min. ilości powietrza świeżego dla komory mieszania w trybie Niski"
  min: 0.0
  max: 100.0
  step: 0.1

gLimit_RRGFreqHi:
  address: 46
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read_write
  description: "Górne ograniczenie częstotliwości dla przemiennika wymiennika obrotowego"
  min: 40.0
  max: 70.0
  step: 0.1

gLimit_RRGFreqLo:
  address: 47
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read_write
  description: "Dolne ograniczenie częstotliwości dla przemiennika wymiennika obrotowego"
  min: 10.0
  max: 25.0
  step: 0.1

gLimit_SupTempHi:
  address: 48
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read_write
  description: "Górne ograniczenie dla temperatury powietrza nawiewu"
  device_class: temperature
  min: 5.0
  max: 40.0
  step: 0.1

gLimit_SupTempLo:
  address: 49
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read_write
  description: "Dolne ograniczenie dla temperatury powietrza nawiewu"
  device_class: temperature
  min: 5.0
  max: 40.0
  step: 0.1

gOutputAO_1:
  address: 50
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read
  description: "Wyjście analogowe 1 wartość"

gOutputAO_2:
  address: 51
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read
  description: "Wyjście analogowe 2 wartość"

gOutputAO_3:
  address: 52
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read
  description: "Wyjście analogowe 3 wartość"

gOutputAO_Clg:
  address: 53
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read
  description: "Stopień chłodzenia z regulatora PI"

gOutputAO_Htg:
  address: 54
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read
  description: "Stopieć grzania z regulatora PI"

gOutputAO_PreHtg:
  address: 55
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read
  description: "Stopień grzania nagrzewnicy wstępnej z regulatora PI"

gOutputAO_Reco:
  address: 56
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read
  description: "Stopień odzysku z regulatora PI"

gRRG_FreqRef:
  address: 57
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwość odniesienia dla przemiennika wymiennika obrotowego (zależna od regulatora PI odzysku)"

gRRG_OutputCurr:
  address: 58
  table: holding
  data_type: int16
  scale: 0.1
  unit: "A"
  access: read
  description: "Prąd wyjściowy przemiennika wymiennika obrotowego"

gRRG_OutputFreq:
  address: 59
  table: holding
  data_type: int16
  scale: 0.1
  unit: "Hz"
  access: read
  description: "Częstotliwość wyjściowa przemiennika wymiennika obrotowego"

gSet_ManMixCmbrAtComf:
  address: 60
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Stopień odzysku sterowania ręcznego recyrkulacji dla trybu Komfort"
  min: 0.0
  max: 100.0
  step: 0.1

gSet_ManMixCmbrAtEcono:
  address: 61
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Stopień odzysku sterowania ręcznego recyrkulacji dla trybu Ekono"
  min: 0.0
  max: 100.0
  step: 0.1

gSet_ManMixCmbrAtLow:
  address: 62
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Stopień odzysku sterowania ręcznego recyrkulacji dla trybu Niski"
  min: 0.0
  max: 100.0
  step: 0.1

gSet_ManSetpFreqExh_1:
  address: 63
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Nastawa dla wentylatora Wywiewu w trybie Niski"
  min: 10.0
  max: 100.0
  step: 0.1

gSet_ManSetpFreqExh_2:
  address: 64
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Nastawa dla wentylatora Wywiewu w trybie Ekono"
  min: 10.0
  max: 100.0
  step: 0.1

gSet_ManSetpFreqExh_3:
  address: 65
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Nastawa dla wentylatora Wywiewu w trybie Komfort"
  min: 10.0
  max: 100.0
  step: 0.1

gSet_ManSetpFreqSup_1:
  address: 66
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Nastawa dla wentylatora Nawiewu w trybie Niski"
  min: 10.0
  max: 100.0
  step: 0.1

gSet_ManSetpFreqSup_2:
  address: 67
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Nastawa dla wentylatora Nawiewu w trybie Ekono"
  min: 10.0
  max: 100.0
  step: 0.1

gSet_ManSetpFreqSup_3:
  address: 68
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Nastawa dla wentylatora Nawiewu w trybie Komfort"
  min: 10.0
  max: 100.0
  step: 0.1

gSet_ManSetpParametricComf:
  address: 69
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Nastawa dla parametru PI regulatora wydajności powietrza w trybie Komford"
  min: -100.0
  max: 100.0
  step: 0.1

gSet_ManSetpParametricEco:
  address: 70
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Nastawa dla parametru PI regulatora wydajności powietrza w trybie Ekono"
  min: -100.0
  max: 100.0
  step: 0.1

gSet_ManSetpParametricLow:
  address: 71
  table: holding
  data_type: int16
  scale: 0.1
  unit: "%"
  access: read_write
  description: "Nastawa dla parametru PI regulatora wydajności powietrza w trybie Niski"
  min: -100.0
  max: 100.0
  step: 0.1

gThTune_TempSensor:
  address: 72
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Odczyt temp. z HMI Basic uPC (thTune device)"
  device_class: temperature

gTSetp_RecoFrostProt:
  address: 73
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read_write
  description: "Nastawa temp. dla zabezpieczenia przeciwzamrożeniowego odzysku"
  device_class: temperature
  min: -15.0
  max: 10.0
  step: 0.1

gTSetp_Main:
  address: 74
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read_write
  description: "Nastawa temp. głównej"
  device_class: temperature
  min: -99.9
  max: 99.9
  step: 0.1

gInputDI_1:
  address: 46
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wejścia cyfrowego DI 1"

gInputDI_2:
  address: 47
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wejścia cyfrowego DI 2"

gInputDI_3:
  address: 48
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wejścia cyfrowego DI 3"

gInputDI_4:
  address: 49
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wejścia cyfrowego DI 4"

gInputDI_5:
  address: 50
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wejścia cyfrowego DI 5"

gInputDI_6:
  address: 51
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wejścia cyfrowego DI 6"

gInputDI_7:
  address: 52
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wejścia cyfrowego DI 7"

GLOBAL_ALARM:
  address: 53
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Ogólny znacznik alarmu: 0 = brak aktywnych alarmów, 1 = alarmy wymagające potwierdzenia"

gOpMode_SummerWinter:
  address: 54
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Wyświetlanie aktualnego trybu pracy"

gOutputREL_1:
  address: 55
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wyjścia przekaźnikowego 1"

gOutputREL_2:
  address: 56
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wyjścia przekaźnikowego 2"

gOutputREL_3:
  address: 57
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wyjścia przekaźnikowego 3"

gOutputREL_4:
  address: 58
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wyjścia przekaźnikowego 4"

gOutputREL_5:
  address: 59
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wyjścia przekaźnikowego 5"

gOutputREL_6:
  address: 60
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wyjścia przekaźnikowego 6"

gOutputREL_7:
  address: 61
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Stan wyjścia przekaźnikowego 7"

fAlarm_AftRecoSens:
  address: 1
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu awarii czujnika temp. powietrza za odzyskiem"

fAlarm_Chillers:
  address: 2
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu dla chillera"

fAlarm_ExhFanComm_1:
  address: 3
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu błędu komunikacji przemiennika wywiewu FC 1"

fAlarm_ExhFanComm_2:
  address: 4
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu błędu komunikacji przemiennika wywiewu FC 2"

fAlarm_ExhFanComm_3:
  address: 5
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu błędu komunikacji przemiennika wywiewu FC 3"

fAlarm_ExhFanComm_4:
  address: 6
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu błędu komunikacji przemiennika wywiewu FC 4"

fAlarm_ExhFanOvld_1:
  address: 7
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu przeciążenia przemiennika Wywiewu FC 1"

fAlarm_ExhFanOvld_2:
  address: 8
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu przeciążenia przemiennika Wywiewu FC 2"

fAlarm_ExhFanOvld_3:
  address: 9
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu przeciążenia przemiennika Wywiewu FC 3"

fAlarm_ExhFanOvld_4:
  address: 10
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu przeciążenia przemiennika Wywiewu FC 4"

fAlarm_ExhFilters:
  address: 11
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu filtra Wywiewu"

fAlarm_ExhSens:
  address: 12
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu awarii czujnika temp. powietrza Wywiewu"

fAlarm_ExternalSens:
  address: 13
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu awarii czujnika temp. powietrza zewnętrznego"

fAlarm_Fire:
  address: 14
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu zabezpieczenia p.poż"

fAlarm_Heating:
  address: 15
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu dla nagrzewnic (wspólny dla nagrzewnic wodnych i elektrycznych)"

fAlarm_Heating3xLocked:
  address: 16
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu zabezpieczenia nagrzewnic aktywowany 3x i blokowany"

fAlarm_HEOvht:
  address: 17
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu zabezpieczenia przegrzaniowego nagrzewnicy elektrycznej"

fAlarm_HMIBasicComm:
  address: 18
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu błędu komunikacji HMI Basic (thTune device)"

fAlarm_HMIBasicInit:
  address: 19
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu dla inicjalizacji błędu HMI Basic (thTune device)"

fAlarm_HW_BackW:
  address: 20
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu spadku temp. wody powrotnej nagrzewnicy"

fAlarm_HW_Th:
  address: 21
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu termostatu przeciwzamrożeniowego"

fAlarm_HWWaterSens:
  address: 22
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu awarii czujnia temp. wody powrotnej nagrzewnicy"

fAlarm_ManualMode:
  address: 23
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu ręcznego nadpisania wyjść I/O sterownika"

fAlarm_PreHeating3xLocked:
  address: 24
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu zabezpieczenia przeciwzamrożeniowego nagrzewnic aktywowany 3x i blokowany"

fAlarm_PreHW_BackW:
  address: 25
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu spadku temp. wody powrotnej nagrzewnicy wstępnej"

fAlarm_PreHW_Th:
  address: 26
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu termostatu przeciwzamrożeniowego nagrzewnicy wstępnej"

fAlarm_PreHWSens:
  address: 27
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu awarii czujnika temp. powietrza za nagrzewnicą wstępną"

fAlarm_PreHWWaterSens:
  address: 28
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu awarii czujnika temp. wody powrotnej nagrzewnicy wstępnej"

fAlarm_RoomSens:
  address: 29
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu awarii pomieszczeniowego czujnika temp."

fAlarm_RRGComm:
  address: 30
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu komunikacji napędu wym. obrotowego"

fAlarm_RRGOvld:
  address: 31
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu przeciążenia napędu wymiennika obrotowego"

fAlarm_SupFanComm_1:
  address: 32
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu błędu komunikacji przemiennika Nawiewu FC 1"

fAlarm_SupFanComm_2:
  address: 33
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu błędu komunikacji przemiennika Nawiewu FC 2"

fAlarm_SupFanComm_3:
  address: 34
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu błędu komunikacji przemiennika Nawiewu FC 3"

fAlarm_SupFanComm_4:
  address: 35
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu błędu komunikacji przemiennika Nawiewu FC 4"

fAlarm_SupFanOvld_1:
  address: 36
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu przeciążenia przemiennika Nawiewu FC1"

fAlarm_SupFanOvld_2:
  address: 37
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu przeciążenia przemiennika Nawiewu FC2"

fAlarm_SupFanOvld_3:
  address: 38
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu przeciążenia przemiennika Nawiewu FC3"

fAlarm_SupFanOvld_4:
  address: 39
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu przeciążenia przemiennika Nawiewu FC4"

fAlarm_SupFilters:
  address: 40
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu filtrów nawiewu"

fAlarm_SupSens:
  address: 41
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Znacznik alarmu awarii czujnika temp. powietrza nawiewanego"

gAlarmAckPRG:
  address: 42
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read_write
  description: "Potwierdzenie alarmu (0->1 kasuje alarm, automatyczny powrót do 0 po 2s)"

gBMS_SummerWinter:
  address: 43
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read_write
  description: "Przełączenie trybu dla uniwersalnego wymiennika grzania/chłodzenia: 0=Lato 1=Zima"

gConf_AppCodeERR:
  address: 44
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "Ostrzeżenie dla złej konfiguracji sterownika"

gConf_AppState:
  address: 45
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read
  description: "0=Konfig 1=Praca"

gSched_ExcEnable_1:
  address: 63
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read_write
  description: "Kalendarz uPC: włączone wyjątki nr 1"

gSched_ExcEnable_2:
  address: 64
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read_write
  description: "Kalendarz uPC: włączone wyjątki nr 2"

gSched_ExcEnable_3:
  address: 65
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read_write
  description: "Kalendarz uPC: włączone wyjątki nr 3"

gSched_ExcEnable_4:
  address: 66
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read_write
  description: "Kalendarz uPC: włączone wyjątki nr 4"

gSched_ExcEnable_5:
  address: 67
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read_write
  description: "Kalendarz uPC: włączone wyjątki nr 5"

gSched_ExcEnable_6:
  address: 68
  table: coil
  data_type: bitmask
  scale: 1.0
  unit: ""
  access: read_write
  description: "Kalendarz uPC: włączone wyjątki nr 6"

gConf_AppCodeLtr:
  address: 5001
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Litera kodu aplikacji"

gConf_AppCodeNum:
  address: 5002
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Numer kodu aplikacji"

gFan_ExhFireSetp:
  address: 5003
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read_write
  description: "Nastawa pracy wentylatora wywiewu podczas alarmu p.poż: 0=stop 1=20% 2=40% 3=60% 4=80% 5=100%"
  min: 0.0
  max: 6.0
  step: 1.0

gFan_ExhStartCommand:
  address: 5004
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Polecenie startu wentylatora Wywiewu: 1=Stop 2=Praca"

gFan_ExhStatus_1:
  address: 5005
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Status przemiennika częstotliwości: 0=OK 1=błąd komunikacji 2=alarm falownika"

gFan_ExhStatus_2:
  address: 5006
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Status przemiennika częstotliwości: 0=OK 1=błąd komunikacji 2=alarm falownika"

gFan_ExhStatus_3:
  address: 5007
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Status przemiennika częstotliwości: 0=OK 1=błąd komunikacji 2=alarm falownika"

gFan_ExhStatus_4:
  address: 5008
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Status przemiennika częstotliwości: 0=OK 1=błąd komunikacji 2=alarm falownika"

gFan_SupFireSetp:
  address: 5009
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read_write
  description: "Nastawa pracy wentylatora nawiewu podczas alarmu p.poż: 0=wył 1=20% 2=40% 3=60% 4=80% 5=100%"
  min: 0.0
  max: 6.0
  step: 1.0

gFan_SupStartCommand:
  address: 5010
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Polecenie startu wentylatora Nawiewu: 1=Stop 2=Praca"

gFan_SupStatus_1:
  address: 5011
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Status przemiennika częstotliwości: 0=OK 1=błąd komunikacji 2=alarm falownika"

gFan_SupStatus_2:
  address: 5012
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Status przemiennika częstotliwości: 0=OK 1=błąd komunikacji 2=alarm falownika"

gFan_SupStatus_3:
  address: 5013
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Status przemiennika częstotliwości: 0=OK 1=błąd komunikacji 2=alarm falownika"

gFan_SupStatus_4:
  address: 5014
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Status przemiennika częstotliwości: 0=OK 1=błąd komunikacji 2=alarm falownika"

gOpMode_BMS:
  address: 5015
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read_write
  description: "Nastawa trybu pracy z BMS: 0=Auto 1=Wył 2=Standby 3=Niski 4=Ekono 5=Komfort (nietrwałe, RAM)"
  min: 0.0
  max: 5.0
  step: 1.0

gOpMode_DI:
  address: 5016
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Tryb pracy wynikający z wejść cyfrowych (0..5 jak wyżej)"

gOpMode_Main:
  address: 5017
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Główny tryb pracy wynikający ze wszystkich źródeł (0..5 jak wyżej)"

gOpMode_PGD:
  address: 5018
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Tryb pracy z HMI Advanced pGD1 (0..5 jak wyżej)"

gOpMode_Scheduler:
  address: 5019
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Tryb pracy z Kalendarza uPC (0..5 jak wyżej)"

gOpMode_thTune:
  address: 5020
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Tryb pracy z HMI Basic thTune (0..5 jak wyżej)"

gOpMode_thTuneScheduler:
  address: 5021
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Tryb pracy z Kalendarza HMI Basic (0..5 jak wyżej)"

gSet_IdleDelayExh:
  address: 5022
  table: holding
  data_type: int16
  scale: 1.0
  unit: "s"
  access: read_write
  description: "Czas rozruchu - wentylatory wyciągowe na min. prędkości"
  min: 0.0
  max: 180.0
  step: 1.0

gSet_IdleDelaySup:
  address: 5023
  table: holding
  data_type: int16
  scale: 1.0
  unit: "s"
  access: read_write
  description: "Czas rozruchu - wentylatory nawiewne na min. prędkości"
  min: 0.0
  max: 180.0
  step: 1.0

gSet_MixCmbrMode:
  address: 5024
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read_write
  description: "Tryb komory mieszania: 0=max wymiana energii (PI) 1=manualny 2=wg AI7"
  min: 0.0
  max: 2.0
  step: 1.0

gSet_OffDelayExh:
  address: 5025
  table: holding
  data_type: int16
  scale: 1.0
  unit: "s"
  access: read_write
  description: "Czas wybiegu - wentylatory wywiewne na min. prędkości"
  min: 0.0
  max: 180.0
  step: 1.0

gSet_OffDelaySup:
  address: 5026
  table: holding
  data_type: int16
  scale: 1.0
  unit: "s"
  access: read_write
  description: "Czas wybiegu - wentylatory nawiewne na min. prędkości"
  min: 0.0
  max: 180.0
  step: 1.0

gSet_OnDelayExh:
  address: 5027
  table: holding
  data_type: int16
  scale: 1.0
  unit: "s"
  access: read_write
  description: "Czas opóźnienia startu - wentylatory wywiewne czekają"
  min: 0.0
  max: 180.0
  step: 1.0

gSet_OnDelaySup:
  address: 5028
  table: holding
  data_type: int16
  scale: 1.0
  unit: "s"
  access: read_write
  description: "Czas opóźnienia startu - wentylatory nawiewne czekają"
  min: 0.0
  max: 180.0
  step: 1.0

gActOpMode:
  address: 5029
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Aktualny tryb pracy centrali: 0=Wył 1=Grzanie wstępne 2=Rozruch 3=Standby Grzanie 4=Standby Chłodzenie 5=Szybkie grzanie 6=Szybkie chłodzenie 7=Grzanie 8=Wentylacja 9=Chłodzenie 10=Nocne chłodzenie 11=Wybieg 12=Tryb pożarowy 13=Nocny test 14=Awaryjne zatrzymanie 15=Zatrzymanie alarmem 16=Zatrzymanie alarmem krytycznym 17=Konfiguracja"

gRRG_Status:
  address: 5030
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read
  description: "Status przemiennika częstotliwości: 0=OK 1=błąd komunikacji 2=alarm falownika"

CURRENT_DAY:
  address: 5197
  table: holding
  data_type: int16
  scale: 1.0
  unit: "d"
  access: read_write
  description: "Aktualny dzień"
  min: 1.0
  max: 31.0
  step: 1.0

CURRENT_HOUR:
  address: 5198
  table: holding
  data_type: int16
  scale: 1.0
  unit: "h"
  access: read_write
  description: "Aktualna godzina"
  min: 0.0
  max: 23.0
  step: 1.0

CURRENT_MINUTE:
  address: 5199
  table: holding
  data_type: int16
  scale: 1.0
  unit: "min"
  access: read_write
  description: "Aktualna minuta"
  min: 0.0
  max: 59.0
  step: 1.0

CURRENT_MONTH:
  address: 5200
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read_write
  description: "Aktualny miesiąc"
  min: 1.0
  max: 12.0
  step: 1.0

CURRENT_YEAR:
  address: 5201
  table: holding
  data_type: int16
  scale: 1.0
  unit: ""
  access: read_write
  description: "Aktualny rok"
  min: 0.0
  max: 99.0
  step: 1.0
