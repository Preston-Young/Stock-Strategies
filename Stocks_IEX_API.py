#Preston Young 43798917

import json
import urllib.request

BASE_URL = 'https://www.googleapis.com/youtube/v3'

GOOGLE_API_KEY = 'AIzaSyBMgiJSuu8fFBTqk82huM-wr_j216xll1M'

def build_search_url(symbol, trading_days, documentation) -> str:
    '''
    Builds the search url based on the given stock symbol and trading days.
    '''
    if documentation == 'chart':
        data_range = '1m'
        search_url = BASE_URL + '/{}/chart/{}'.format(symbol, data_range)
        enough_data = False
        
        while not enough_data:
            if len(get_response(search_url)) < trading_days:
                data_range = '3m'
                search_url = BASE_URL + '/{}/chart/{}'.format(symbol, data_range)

            if len(get_response(search_url)) < trading_days:
                data_range = '6m'
                search_url = BASE_URL + '/{}/chart/{}'.format(symbol, data_range)

            if len(get_response(search_url)) < trading_days:
                data_range = '1y'
                search_url = BASE_URL + '/{}/chart/{}'.format(symbol, data_range)

            if len(get_response(search_url)) < trading_days:
                data_range = '2y'
                search_url = BASE_URL + '/{}/chart/{}'.format(symbol, data_range)

            if len(get_response(search_url)) < trading_days:
                data_range = '5y'
                search_url = BASE_URL + '/{}/chart/{}'.format(symbol, data_range)
                enough_data = True

            else:
                enough_data = True

        return search_url

    elif documentation == 'stats':
        search_url = BASE_URL + '/{}/stats'.format(symbol)
        return search_url
    
    
def get_response(url) -> list:
    '''
    Sends the url request to the Web API and returns the response.
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()
