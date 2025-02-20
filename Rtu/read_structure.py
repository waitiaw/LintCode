class StData:
    data = [
            ('pcsStatus', 'UINT', 0, 1),
            ('cdStatus', 'UINT', 1, 1),
            ('remoteMode', 'UINT', 2, 1),
            ('opMode', 'UINT', 3, 1),
            ('referenceFeedBack', 'UINT', 4, 1),
            ('mmcStatus', 'UINT', 5, 1),
            ('fault1', 'UINT', 6, 1),
            ('fault2', 'UINT', 7, 1),
            ('fault3', 'UINT', 8, 1),
            ('fault4', 'UINT', 9, 1),
            ('fault5', 'UINT', 10, 1),

            ('igbtTemp1', 'INT', 11, 1),
            ('igbtTemp2', 'INT', 12, 1),
            ('igbtTemp3', 'INT', 13, 1),
            ('igbtTemp4', 'INT', 14, 1),
            ('acFilter1Temp', 'INT', 15, 1),
            ('acFilter2Temp', 'INT', 16, 1),
            ('acFilter3Temp', 'INT', 17, 1),
            ('acFilter4Temp', 'INT', 18, 1),

            ('acVolt1', 'UINT', 19, 1),
            ('acVolt2', 'UINT', 20, 1),
            ('acVolt3', 'UINT', 21, 1),
            ('acCnt1', 'UINT', 22, 1),
            ('acCnt2', 'UINT', 23, 1),
            ('acCnt3', 'UINT', 24, 1),
            ('acFreq', 'UINT', 25, 0.1),

            ('acActive', 'INT', 26, 0.1),
            ('acReactive', 'INT', 27, 0.1),
            ('acPf', 'INT', 28, 1),

            ('todayDischargeEnergy', 'UINT', 29, 1000),
            ('todayChargeEnergy', 'UINT', 30, 1000),
            ('totalDEnergyH', 'UINT', 31, 1),
            ('totalDEnergyL', 'UINT', 32, 1),
            ('totalCEnergyH', 'UINT', 33, 1),
            ('totalCEnergyL', 'UINT', 34, 1),
            ('dcLinkVoltage', 'UINT', 35, 1),
            ('dcVoltage', 'UINT', 36, 1),

            ('dcCurrent', 'INT', 37, 1),
            ('dcPower', 'INT', 38, 1)
]