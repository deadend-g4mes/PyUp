import requests
from enum import Enum
import json

class Type(Enum):
    COIN = 'coin'
    EXP = 'exp'
    ITEM = 'item'

def call(call):
    return requests.get(url=call)


class PyUp:
    
    host = str
    port = str

    def __init__(self,host,port):
        self.host = host
        self.port = port

    def reward(self, content: str, type: str, number: int, skills: list = None, item_id: int = None, item_name: str = None, silent: bool = None):
        '''
        Provide the reward directly. The reason for the reward can be customized.

        :param str content: text that appears on the reward notification.
        :param str type: reward type (must be either 'coin', 'exp' or 'item').
        :param int number: amount of reward given.
        :param (optional) list skills: array of numbers greater than 0. dicates what skills recieve the exp reward.
        :param (optional) int item_id: the numerical id of the item the user recieves as a reward.
        :param (optional) str item_name: the name of the item the user recieves as a reward.
        :param (optional) bool silent: wether the UI notification appears or not.
        '''
        if type is not 'coin' or 'exp' or 'item':
            raise ValueError("param: content: must be a value of 'coin', 'exp' or 'item'.")
        if type == 'item' and item_id == 0 and item_name == '':
            raise ValueError("param: type: 'item' requires item_id and item_name to have values.")
        
        params = vars()

        url = 'http://' + self.host + ':' + self.port + '/api?url=lifeup://api/reward?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]
        call(call=url)

    def toast(self, text: str, type: int = 0, isLong: bool = False):
        '''
        Various styles of messages pop up.
        
        :param str text: the message that appears on the prompt.
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
        
        result = call(call=url)

        return result

    def penality(self, content: str, type: str, number: int, skills: list = None, item_id:int = None, item_name: str = None, silent: bool = None):
        '''
        Provide a penalty directly. The reason for the penalty can be customized.
        
        :param str content: text that appears on the reward notification.
        :param str type: reward type (must be either 'coin', 'exp' or 'item').
        :param int number: amount of reward given.
        :param (optional) list skills: array of numbers greater than 0. dicates what skills recieve the exp reward.
        :param (optional) int item_id: the numerical id of the item the user recieves as a reward.
        :param (optional) str item_name: the name of the item the user recieves as a reward.
        :param (optional) bool silent: wether the UI notification appears or not.
        '''

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

        result = call(call=url)
        
        return result

    def add_task(self, todo: str, notes: str = None, coin: int = None, coin_var: int = None, exp: int = None, skills: list = None, category: int = None, frequency: int = None, importance: int = None, difficulty: int = None, item_id: int = None, item_name: str = None, item_amount: int = None, deadline: int = None, color: str = None, background_url: str = None, frozen: bool = None, freeze_until: int = None, coin_penality_factor: float = None, exp_pentalty_factor: float = None, write_feelings: bool = None):
        '''
        Creates tasks automatically.
        
        :param
        '''

        params = vars()

        url = 'http://' + self.host + ':' + self.port + '/api?url=lifeup://api/add_task?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url)
        result_dict = json.loads(result.content)
        print(result_dict)

        return result
        
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

        result = call(call=url)
            
        return result
    

    
class Task:
    task_id = None
    task_gid = None

    def __init__(self, task_id, task_gid):
        self.task_id = task_id
        self.task_gid = task_gid

    def get_task_id(self):
        return self.task_id
    
    def get_task_gid(self):
        return self.task_gid

