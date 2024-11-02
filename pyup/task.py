from .pyup import PyUp
from .__main__ import *

class Task(PyUp):

    def __init__(self, pyup:PyUp):
        '''
        Some api calls for communicating with task objects in LifeUp.
        '''
        super().__init__(pyup.host, pyup.port)
        self.host = pyup.host
        self.port = pyup.port

    def add_task(self, todo: str, notes: str = None, coin: int = None, coin_var: int = None, exp: int = None, skills: list = None, category: int = None, frequency: int = None, importance: int = None, difficulty: int = None, item_id: int = None, item_name: str = None, item_amount: int = None, deadline: int = None, color: str = None, background_url: str = None, frozen: bool = None, freeze_until: int = None, coin_penality_factor: float = None, exp_pentalty_factor: float = None, write_feelings: bool = None) -> Response:
        '''
        Creates a task.
        
        :param
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if not color_check(color):
            raise ValueError("param: title_color_string: value must be a valid hex color code.")
        
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/add_task?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)

        return result
        
    def complete_task(self, id: int = None, gid: int = None, name: str = None, ui: bool = None, count: int = None, count_set_type: CountSetType = None, count_force_sum_up: bool = None, reward_factor: float = None) -> Response:
        '''
        Completes a task. Only unfinished tasks will be searched.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if id or gid or name == None:
            raise ValueError("OneOfType: id, gid or name must have a value.")
        
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/complete?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)
            
        return result

    def give_up_task(self, id: int = None, gid: int = None, name: str = None) -> Response:

        '''
        Gives up a task.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if id or gid or name == None:
            raise ValueError("OneOfType: id, gid or name must have a value.")
        
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/give_up?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)
            
        return result

    def freeze_task(self, id: int = None, gid: int = None, name: str = None) -> Response:

        '''
        Freezes a task, only for repeating tasks.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if id or gid or name == None:
            raise ValueError("OneOfType: id, gid or name must have a value.")
        
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/freeze?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)
            
        return result
            
    def unfreeze_task(self, id: int = None, gid: int = None, name: str = None) -> Response:

        '''
        Unfreezes a task, only for repeating tasks.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if id or gid or name == None:
            raise ValueError("OneOfType: id, gid or name must have a value.")
        
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/unfreeze?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)
            
        return result

    def delete_task(self, id: int = None, gid: int = None, name: str = None) -> Response:

        '''
        Deletes a task.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if id or gid or name == None:
            raise ValueError("OneOfType: id, gid or name must have a value.")
        
        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/delete_task?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)
            
        return result
