#Preston Young 43798917

class TR:
    def __init__(self, all_data):
        self.all_data = all_data

    def calculate(self) -> list:
        '''
        Calculates and returns a list of all the indicators for true range.
        '''
        list_of_indicators = []
        for index, data_set in enumerate(self.all_data):

            if index != 0:
                true_range = max([self.all_data[index-1]['close'], data_set['high']]) - min([self.all_data[index-1]['close'], data_set['low']])

                indicator = true_range / self.all_data[index-1]['close'] * 100
                indicator = '{0:.4f}'.format(indicator)

                list_of_indicators.append(indicator)
            else:
                list_of_indicators.append('')
        return list_of_indicators


class MOV_AVG:
    def __init__(self, all_data, n_days, close_or_volume):
        self.all_data = all_data
        self.n_days = n_days
        self.close_or_volume = close_or_volume

    def calculate(self) -> list:
        '''
        Calculates and returns a list of all the indicators for moving average.
        '''
        list_of_indicators = []
        for index, data_set in enumerate(self.all_data):
        
            if index >= self.n_days - 1:

                sum = 0
                for num in range(self.n_days):
                    sum += self.all_data[index-num][self.close_or_volume]
                indicator = sum / self.n_days

                indicator = '{0:.4f}'.format(indicator)

                list_of_indicators.append(indicator)
            
            else:
                list_of_indicators.append('')
        return list_of_indicators


class DIR_IND:
    def __init__(self, all_data, n_days, close_or_volume):
        self.all_data = all_data
        self.n_days = n_days
        self.close_or_volume = close_or_volume

    def calculate(self) -> list:
        '''
        Calculates and returns a list of all the indicators for directional indicator.
        '''
        list_of_indicators = []
        for index, data_set in enumerate(self.all_data):

            if index >= self.n_days :
                counter = 0
                
                for i in range(10, 0, -1):
                    if self.all_data[index-i+1][self.close_or_volume] > self.all_data[index-i][self.close_or_volume]:
                        counter += 1

                    elif self.all_data[index-i+1][self.close_or_volume] < self.all_data[index-i][self.close_or_volume]:
                        counter -= 1

            elif 0 < index < self.n_days:
                if self.all_data[index][self.close_or_volume] > self.all_data[index-1][self.close_or_volume]:
                    counter += 1

                elif self.all_data[index][self.close_or_volume] < self.all_data[index-1][self.close_or_volume]:
                    counter -= 1

            else:
                counter = 0

            if counter > 0:
                indicator = '+{}'.format(counter)

            else:
                indicator = '{}'.format(counter)

            list_of_indicators.append(indicator)
        return list_of_indicators

        
