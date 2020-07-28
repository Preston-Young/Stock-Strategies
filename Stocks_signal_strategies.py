#Preston Young 43798917

class TR:
    def __init__(self, indicators, strategy):
        self.indicators = indicators
        self.strategy = strategy

    def calculate(self) -> (list, list):
        '''
        Calculates and returns two lists of the buy and sell
        signal strategies for true range.
        '''
        buy_threshold = self.strategy.split()[0]
        sell_threshold = self.strategy.split()[1]
        buys = ['']
        sells = ['']
        for indicator in self.indicators:
            if indicator != '':
                should_buy = ''
                should_sell = ''
                    
                if buy_threshold[0] == '<':      
                    if float(indicator) < float(buy_threshold[1:]):
                        should_buy = 'BUY'

                elif buy_threshold[0] == '>':      
                    if float(indicator) > float(buy_threshold[1:]):
                        should_buy = 'BUY'

                if sell_threshold[0] == '<':      
                    if float(indicator) < float(sell_threshold[1:]):
                        should_sell = 'SELL'

                elif sell_threshold[0] == '>':      
                    if float(indicator) > float(sell_threshold[1:]):
                        should_sell = 'SELL'

                buys.append(should_buy)
                sells.append(should_sell)

        return buys, sells

class MOV_AVG:
    def __init__(self, all_data, indicators, close_or_volume):
        self.all_data = all_data
        self.indicators = indicators
        self.close_or_volume = close_or_volume

    def calculate(self) -> (list, list):
        '''
        Calculates and returns two lists of the buy and sell
        signal strategies for moving average.
        '''
        buys = []
        sells = []
        for index in range(len(self.all_data)): 
            if self.indicators[index] != '':
                should_buy = ''
                should_sell = ''

                if previous_indicator == None:
                    pass
                    
                elif (self.all_data[index-1][self.close_or_volume] < previous_indicator) and (self.all_data[index][self.close_or_volume] > float(self.indicators[index])):
                    should_buy = 'BUY'

                elif (self.all_data[index-1][self.close_or_volume] > previous_indicator) and (self.all_data[index][self.close_or_volume] < float(self.indicators[index])):
                    should_sell = 'SELL'

                previous_indicator = float(self.indicators[index])
                buys.append(should_buy)
                sells.append(should_sell)
            
            else:
                previous_indicator = None
                buys.append('')
                sells.append('')
        return buys, sells


class DIR_IND:
    def __init__(self, all_data, indicators, strategy, close_or_volume):
        self.all_data = all_data
        self.indicators = indicators
        self.strategy = strategy
        self.close_or_volume = close_or_volume

    def calculate(self) -> (list, list):
        '''
        Calculates and returns two lists of the buy and sell
        signal strategies for directional indicator.
        '''
        buys = []
        sells = []
        buy_threshold = int(self.strategy.split()[2])
        sell_threshold = int(self.strategy.split()[3])
        
        for index in range(len(self.all_data)):
            should_buy = ''
            should_sell = ''

            if index > 0:            
                if int(self.indicators[index]) > buy_threshold and previous_indicator <= buy_threshold:
                    should_buy = 'BUY'

                elif int(self.indicators[index]) < sell_threshold and previous_indicator >= sell_threshold:
                    should_sell = 'SELL'

                previous_indicator = int(self.indicators[index])

            else:
                previous_indicator = int(self.indicators[index])

            buys.append(should_buy)
            sells.append(should_sell)
        return buys, sells


    
