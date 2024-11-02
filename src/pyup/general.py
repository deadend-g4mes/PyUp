from .pyup import PyUp
from .__main__ import *

class General(PyUp):

    def __init__(self, pyup: PyUp):
        '''
        Some general api calls for communication with LifeUp.
        '''
        super().__init__(pyup.host, pyup.port)
        self.host = pyup.host
        self.port = pyup.port

    def reward(self, content: str, type: str, number: int, skills: list = None, item_id: int = None, item_name: str = None, silent: bool = None) -> Response:
        '''
        Provide the reward directly. The reason for the reward can be customized.

        :param str content: text that appears on the reward notification.
        :param str type: reward type (must be either 'coin', 'exp' or 'item').
        :param int number: amount of reward given.
        :param (optional) list skills: array of numbers greater than 0. dicates what skills recieve the exp reward.
        :param (optional) int item_id: the numerical id of the item the user recieves as a reward.
        :param (optional) str item_name: the name of the item the user recieves as a reward.
        :param (optional) bool silent: wether the UI notification appears or not.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if type != 'coin' or 'exp' or 'item':
            raise ValueError("param: content: value must be a value of 'coin', 'exp' or 'item'.")
        if type == 'item' and item_id == 0 or item_name == '':
            raise ValueError("param: type: value 'item' requires item_id and item_name to have values.")
        
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/reward?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]
        result = call(call=url)
        return result

    def toast(self, text: str, type: int = 0, isLong: bool = False) -> Response:
        '''
        Various styles of messages pop up.
        
        :param str text: the message that appears on the prompt.
        :param (optional) int type: a number from 0-6 defining the text style.
        :param (optional) bool isLong: display duration, True = long, False = short.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if type < 0 or type > 6 or not isinstance(type,int):
            raise ValueError('param: type: value must be a whole number between 0 and 6')
        
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/toast?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]
        
        result = call(call=url)

        return result

    def penality(self, content: str, type: str, number: int, skills: list = None, item_id:int = None, item_name: str = None, silent: bool = None) -> Response:
        '''
        Provide a penalty directly. The reason for the penalty can be customized.
        
        :param str content: text that appears on the reward notification.
        :param str type: reward type (must be either 'coin', 'exp' or 'item').
        :param int number: amount of reward given.
        :param (optional) list skills: array of numbers greater than 0. dicates what skills recieve the exp reward.
        :param (optional) int item_id: the numerical id of the item the user recieves as a reward.
        :param (optional) str item_name: the name of the item the user recieves as a reward.
        :param (optional) bool silent: wether the UI notification appears or not.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        if type == 'item' and item_id == 0 and item_name == '':
            raise ValueError("param: type: value 'item' requires item_id and item_name.")

        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/penality?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url)
        
        return result