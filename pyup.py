import requests
from enum import Enum

class Type(Enum):
    COIN = 'coin'
    EXP = 'exp'
    ITEM = 'item'

def call(call):
    
    output = requests.get(url=call)
    
    return output.content

class PyUp():
    host = str
    port = str
    
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def reward(self, content: str, type: str, number: int, skills: list = None, item_id: int = None, item_name: str = None, silent: bool = None):
        '''Provide the reward directly. The reason for the reward can be customized.'''

        if type == 'item' and item_id == 0 and item_name == '':
            raise ValueError("type: item requires item_id and item_name.")
        
        params = vars()

        url = 'http://' + self.host + ':' + self.port + '/api?url=lifeup://api/reward?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]
        return call(call=url)
    
    def toast(self, text: str, type: int = 0, isLong: bool = False):
        '''
        Various styles of messages pop up.
        
        :param str text: the message that appears on the prompt
        :param (optional) int type: a number from 0-6 defining the text style.
        :param (optional) bool isLong: display duration, True = long, False = short.
        '''
        if type < 0 or type > 6 or not isinstance(type,int):
            raise ValueError('type must be a whole number between 0 and 6')
        params = vars()

        url = 'http://' + self.host + ':' + self.port + '/api?url=lifeup://api/toast?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]
        return call(call=url)
    
    def penality(self, content: str, type: str, number: int, skills: list = None, item_id:int = None, item_name: str = None, silent: bool = None):
        '''Provide a penalty directly. The reason for the penalty can be customized.'''

        if type == 'item' and item_id == 0 and item_name == '':
            raise ValueError("type: item requires item_id and item_name.")

        params = vars()

        url = 'http://' + self.host + ':' + self.port + '/api?url=lifeup://api/toast?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]
        return call(call=url)
    
    def add_task(self, todo, notes, coin, coin_var, exp, skills, category, frequency, importance, difficulty, item_id, item_amount, deadline, color, background_url, frozen, freeze_until, coin_penality_factor, exp_pentalty_factor, write_feelings):
        '''Creates tasks automatically.'''

        params = vars()

        url = 'http://' + self.host + ':' + self.port + '/api?url=lifeup://api/add_task?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]
        return call(call=url)    
    
    def complete_task(self):
        '''Trigger task completion. Only unfinished tasks will be searched.'''

        params = vars()

        url = 'http://' + self.host + ':' + self.port + '/api?url=lifeup://api/complete?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]
        return call(call=url)            



