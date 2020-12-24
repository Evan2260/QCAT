class BootCampTask(QCAlgorithm):

    def Initialize(self):

            #1-2. Set Date Range
            self.SetStartDate(2013, 10, 7)
            self.SetEndDate(2013, 10, 11)
            self.AddEquity("SPY", Resolution.Daily)

    def OnData(self, data):
        pass


# 1. Set start date for the backtest to January 1st, 2017
# 2. Set ending date for the backtest to October 31st, 2017

class BootCampTask(QCAlgorithm):

    def Initialize(self):

        #1-2. Set Date Range
        self.SetStartDate(2017, 1, 1)
        self.SetEndDate(2017, 10, 31)
        self.AddEquity("SPY", Resolution.Daily)

    def OnData(self, data):
        pass
