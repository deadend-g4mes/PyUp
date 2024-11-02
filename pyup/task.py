from .pyup import PyUp
from .__main__ import *

self: PyUp

def add_task(todo: str, notes: str = None, coin: int = None, coin_var: int = None, exp: int = None, skills: list = None, category: int = None, frequency: int = None, importance: int = None, difficulty: int = None, item_id: int = None, item_name: str = None, item_amount: int = None, deadline: int = None, color: str = None, background_url: str = None, frozen: bool = None, freeze_until: int = None, coin_penality_factor: float = None, exp_pentalty_factor: float = None, write_feelings: bool = None) -> Response:
    '''
    Creates a task.
    
    :param
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
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

    return result
    
def complete_task(id: int = None, gid: int = None, name: str = None, ui: bool = None, count: int = None, count_set_type: CountSetType = None, count_force_sum_up: bool = None, reward_factor: float = None) -> Response:
    '''
    Completes a task. Only unfinished tasks will be searched.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    '''
    if id or gid or name == None:
        raise ValueError("OneOfType: id, gid or name must have a value.")
    
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

def give_up_task(id: int = None, gid: int = None, name: str = None) -> Response:

    '''
    Gives up a task.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    '''
    if id or gid or name == None:
        raise ValueError("OneOfType: id, gid or name must have a value.")
    
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

def freeze_task(id: int = None, gid: int = None, name: str = None) -> Response:

    '''
    Freezes a task, only for repeating tasks.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    '''
    if id or gid or name == None:
        raise ValueError("OneOfType: id, gid or name must have a value.")
    
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
        
def unfreeze_task(id: int = None, gid: int = None, name: str = None) -> Response:

    '''
    Unfreezes a task, only for repeating tasks.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    '''
    if id or gid or name == None:
        raise ValueError("OneOfType: id, gid or name must have a value.")
    
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

def delete_task(id: int = None, gid: int = None, name: str = None) -> Response:

    '''
    Deletes a task.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    '''
    if id or gid or name == None:
        raise ValueError("OneOfType: id, gid or name must have a value.")
    
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
