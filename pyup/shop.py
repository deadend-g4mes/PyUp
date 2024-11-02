from .pyup import PyUp
from .__main__ import *

self: PyUp

def add_item(name: str, desc: str = None, icon: str = None, price: int = None, action_text: str = None, disable_purchase: bool = None, stock_number: int = None, category: int = None, order: int = None, own_number: int = None, unlist: bool = None) -> Response:
    '''
    Adds a new item to the shop.
    
    :param
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    '''
    if price != None and price < 1 or price > 999999:
        raise ValueError("Type: price must have a value less than 999999 and greater than or equal to 1")
    elif stock_number != None and stock_number < -1 or stock_number > 999999:
        raise ValueError("Type: stock_number must have a value less than 999999 and greater than or equal to -1")
    elif category != None and category < 0:
            raise ValueError("Type: category must have a value greater than or equal to 0")
            
    params = vars()

    url = 'http://' + self.host + ':' + self.port + '/api?url=lifeup://api/add_item?'
    for key, value in params.items():
        if value is not None:
            url = url + key + '=' + str(value) + '%26'
        else:
            continue
    url = url[:-3]

    result = call(call=url)

    return result

