#Preston Young 43798917

import Stocks_IEX_API as IEX_API
import Stocks_indicators as INDICATOR
import Stocks_signal_strategies as STRATEGY

def analyze_data(data, ind_and_strat) -> None:
    '''
    Takes the given data and desired indicator and strategy.
    Then, depending on the indicator, it passes that information
    to their corresponding indicator functions.
    '''
    if ind_and_strat.split()[0] == 'TR':
        calculate_true_range(data, ind_and_strat)
        
    elif ind_and_strat.split()[0] == 'MP':
        calculate_moving_average(data, ind_and_strat, 'close')

    elif ind_and_strat.split()[0] == 'MV':
        calculate_moving_average(data, ind_and_strat, 'volume')

    elif ind_and_strat.split()[0] == 'DP':
        calculate_directional_indicator(data, ind_and_strat, 'close')

    elif ind_and_strat.split()[0] == 'DV':
        calculate_directional_indicator(data, ind_and_strat, 'volume')


def calculate_true_range(data, ind_and_strat) -> None:
    '''
    Takes the given data and desired indicator and strategy for true range.
    By using the indicator and strategy classes defined in the
    other modules, the data, indicators, and signal strategies are
    passed to the print function to be printed for true range.
    '''
    true_range = INDICATOR.TR(data)
    indicators = true_range.calculate()

    strategy = STRATEGY.TR(indicators, ind_and_strat[3:])
    buys, sells = strategy.calculate()
        
    for index in range(len(data)):
        print_data(data[index], indicators[index], buys[index], sells[index])


def calculate_moving_average(data, ind_and_strat, close_or_volume) -> None:
    '''
    Takes the given data, desired indicator and strategy, and 'close' or 'volume' for moving average.
    By using the indicator and strategy classes defined in the
    other modules, the data, indicators, and signal strategies are
    passed to the print function to be printed for moving average.
    The function works for both close or volume calculations.
    '''
    moving_average = INDICATOR.MOV_AVG(data, int(ind_and_strat.split()[1]), close_or_volume)
    indicators = moving_average.calculate()

    strategy = STRATEGY.MOV_AVG(data, indicators, close_or_volume)
    buys, sells = strategy.calculate()

    for index in range(len(data)):
        print_data(data[index], indicators[index], buys[index], sells[index])


def calculate_directional_indicator(data, ind_and_strat, close_or_volume) -> None:
    '''
    Takes the given data, desired indicator and strategy, and 'close' or 'volume' for directional indicator.
    By using the indicator and strategy classes defined in the
    other modules, the data, indicators, and signal strategies are
    passed to the print function to be printed for directional indicator.
    The function works for both close or volume calculations.
    '''
    directional_indicator = INDICATOR.DIR_IND(data, int(ind_and_strat.split()[1]), close_or_volume)
    indicators = directional_indicator.calculate()
    
    strategy = STRATEGY.DIR_IND(data, indicators, ind_and_strat, close_or_volume)
    buys, sells = strategy.calculate()
    
    for index in range(len(data)):
        print_data(data[index], indicators[index], buys[index], sells[index])


def print_data(the_data, the_indicator, buy, sell) -> None:
    '''
    Prints out each row of the report.
    '''
    date = the_data['date']
    open_price = the_data['open']
    high_price = the_data['high']
    low_price = the_data['low']
    close_price = the_data['close']
    volume = the_data['volume']
    print('{0}\t{1:.4f}\t{2:.4f}\t{3:.4f}\t{4:.4f}\t{5}\t{6}\t{7}\t{8}'.format(date,
                                                                    open_price,
                                                                    high_price,
                                                                    low_price,
                                                                    close_price,
                                                                    volume,
                                                                               the_indicator,
                                                                               buy,
                                                                               sell))


def print_header(symbol) -> None:
    '''
    Prints out the header.
    '''
    company_data = IEX_API.get_response(IEX_API.build_search_url(symbol, None, 'stats'))
    print(symbol)
    print(company_data['companyName'])
    print(company_data['sharesOutstanding'])
    print('Date\tOpen\tHigh\tLow\tClose\tVolume\tIndicator\tBuy?\tSell?')


def print_citation() -> None:
    '''
    Prints out the citation.
    '''
    print('Data provided for free by IEX')
    print('View IEX\'s Terms of Use')
    print('https://iextrading.com/api-exhibit-a/')


def run() -> None:
    '''
    Runs the program based on the given inputs.
    Essentially, it produces all the outputs.
    '''
    stock_symbol = input()
    num_trading_days = int(input())
    indicator_and_strategy = input()

    result = IEX_API.get_response(IEX_API.build_search_url(stock_symbol, num_trading_days, 'chart'))
    interesting_data = result[len(result)-num_trading_days:]     

    print_header(stock_symbol)
    analyze_data(interesting_data, indicator_and_strategy)
    print_citation()
    

if __name__ == '__main__':
    run()
