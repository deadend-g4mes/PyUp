from .pyup import PyUp
from .__main__ import *

class Pomodoro(PyUp):

    def __init__(self, pyup: PyUp):
        '''
        Some api calls for communication with the Pomodoro record in LifeUp.
        '''
        super().__init__(pyup.host, pyup.port)
        self.host = pyup.host
        self.port = pyup.port

    def add_record(self, start_time: datetime = None, duration: int = None, end_time: datetime = None, reward_tomatoes: bool = None, task_id: int = None, task_gid: int = None, task_name: str = None):
        '''
        Adds new Pomodoro record to LifeUp.


        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if start_time is not None:
            start_time = time_to_epoch(start_time)

        if end_time is not None:
            if duration is not None:
                if start_time is not None and not duration <= start_time - end_time:
                    raise ValueError("param: duration: value must be less than or equal to start_time - end_time if all three params are given.")
                elif duration < 30:
                    raise ValueError("param: duration: value must be greater than or equal to 30.")
                else:
                    duration = duration * 1000
            elif start_time is not None:
                if end_time <= start_time:
                    raise ValueError("param: end_time: value must be greater than start_time.")
                elif end_time - start_time < 30:
                    raise ValueError("param: end_time or start_time: the value of end_time - start_time must be greater than or equal to 30.")
            else:
                raise ValueError("param: end_time: requires a value given to either start_time or duration.")            
            end_time = time_to_epoch(end_time)
        elif duration is not None and duration >= 30:
            duration = duration * 1000
        else:
            raise ValueError("OneOfType: duration, end_time or start_time must have a value.")

        if task_gid or task_id or task_name is None:
            raise ValueError("OneOfType: task_id, task_gid or task_name must have a value.")            
        if task_id is not None and task_id < 1:
            raise ValueError("param: task_id: value must be greater than 0")
        
        if task_gid is not None and task_gid < 1:
            raise ValueError("param: task_gid: value must be greater than 0")

        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/add_pomodoro?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)
            
        return result
    
    def edit_pomodoro(self, edit_item_id: int, start_time: datetime = None, duration: int = None, end_time: datetime = None, reward_tomatoes: bool = None, task_id: int = None, task_gid: int = None, task_name: str = None, ui: bool = None):
        '''
        Edits a record with the given edit_item_id. If not record is found, a new one will be created.


        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        if start_time is not None:
            start_time = time_to_epoch(start_time)

        if end_time is not None:
            if duration is not None:
                if start_time is not None and not duration <= start_time - end_time:
                    raise ValueError("param: duration: value must be less than or equal to start_time - end_time if all three params are given.")
                elif duration < 30:
                    raise ValueError("param: duration: value must be greater than or equal to 30.")
                else:
                    duration = duration * 1000
            elif start_time is not None:
                if end_time <= start_time:
                    raise ValueError("param: end_time: value must be greater than start_time.")
                elif end_time - start_time < 30:
                    raise ValueError("param: end_time or start_time: the value of end_time - start_time must be greater than or equal to 30.")
            else:
                raise ValueError("param: end_time: requires a value given to either start_time or duration.")            
            end_time = time_to_epoch(end_time)
        elif duration is not None and duration >= 30:
            duration = duration * 1000
        else:
            raise ValueError("OneOfType: duration, end_time or start_time must have a value.")

        if task_gid or task_id or task_name is None:
            raise ValueError("OneOfType: task_id, task_gid or task_name must have a value.")            
        if task_id is not None and task_id < 1:
            raise ValueError("param: task_id: value must be greater than 0")
        
        if task_gid is not None and task_gid < 1:
            raise ValueError("param: task_gid: value must be greater than 0")

        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        url = 'url=lifeup://api/edit_pomodoro?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)
            
        return result