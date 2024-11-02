from .pyup import PyUp
from .__main__ import *

class Shop(PyUp):

    def __init__(self, pyup:PyUp):
        '''
        Some api calls for communicating with the shop in LifeUp.
        '''
        super().__init__(pyup.host, pyup.port)
        self.host = pyup.host
        self.port = pyup.port

    def add_item(self, name: str, desc: str = None, icon: str = None, price: int = None, action_text: str = None, disable_purchase: bool = None, stock_number: int = None, category: int = None, order: int = None, own_number: int = None, unlist: bool = None) -> Response:
        '''
        Adds a new item to the shop.
        
        :param
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if price != None and price < 1 or price > 999999:
            raise ValueError("param: price: must have a value less than 999999 and greater than or equal to 1")
        elif stock_number != None and stock_number < -1 or stock_number > 999999:
            raise ValueError("param: stock_number: must have a value less than 999999 and greater than or equal to -1")
        elif category != None and category < 0:
                raise ValueError("param: category: must have a value greater than or equal to 0")
                
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/add_item?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)

        return result

    def edit_item(self, id: int = None, name: str = None, set_name: str = None, set_desc: str = None, set_icon: str = None, set_price: int = None, set_price_type: CountSetType = None, action_text: str = None, disable_purchase: bool = None, disable_use: bool = None, stock_number: int = None, stock_number_type: CountSetType = None, title_color_string: str = None, category_id: int = None, order: int = None, own_number: int = None, own_number_type: CountSetType = None, unlist: bool = None) -> Response:
        '''
        Edits the specified item in the shop.
        
        :param
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if set_price != None and set_price < 1 or set_price > 999999:
            raise ValueError("param: price: must have a value less than 999999 and greater than or equal to 1")
        elif stock_number != None and stock_number < -1 or stock_number > 999999:
            raise ValueError("param: stock_number: must have a value less than 999999 and greater than or equal to -1")
        elif category_id != None and category_id < 0:
                raise ValueError("param: category: must have a value greater than or equal to 0")
        elif not color_check(title_color_string):
            raise ValueError("param: title_color_string: must be a valid hex color code.")
                
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/item?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)

        return result

    def edit_loot_box(self, id: int = None, name: str = None, sub_id: int = None, sub_name: str = None, set_type: CountSetType = None, amount: int = None, probability: int = None, fixed: bool = None) -> Response:
        '''
        Modify the loot box effect of the specified box item, support adjustment of probability, number of rewards and increase content.
        
        :param
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
                
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        if id or name is None:
            raise ValueError("param: id || name: must have a value.")
        if sub_id or sub_name is None:
            raise ValueError("param: sub_id || sub_name: must have a value.")
        if id is not None and id < 1:
            raise ValueError("param: id: must have a value greater than 0")
        if sub_id is not None and sub_id < 1:
            raise ValueError("param: sub_id: must have a value greater than 0")

        url = 'url=lifeup://api/loot_box?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)

        return result

    def use_item(self, id: int = None, name: str = None, use_times: int = None) -> Response:
        '''
        Modify the loot box effect of the specified box item, support adjustment of probability, number of rewards and increase content.
        
        :param
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
                
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        if id or name is None:
            raise ValueError("param: id || name: must have a value.")
        if id is not None and id < 1:
            raise ValueError("param: id: must have a value greater than 0")
        if use_times is not None and use_times < 1:
            raise ValueError("param: use_times: must have a value greater than 0")

        url = 'url=lifeup://api/use_item?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)

        return result
