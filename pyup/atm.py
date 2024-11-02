from .pyup import PyUp
from .__main__ import *

class ATM(PyUp):

    def __init__(self, pyup:PyUp):
        '''
        Some api calls for communicating with the shop in LifeUp.
        '''
        super().__init__(pyup.host, pyup.port)
        self.host = pyup.host
        self.port = pyup.port

    def deposit(self, amount: int):

        params = vars()
        try:
            params.pop('self')
        finally:
            pass
        
        if amount < 1:
            raise ValueError('param: amount: value must be greater than 0')
        
        url = 'url=lifeup://api/deposit?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)

        return result
    
    def withdraw(self, amount: int):

        params = vars()
        try:
            params.pop('self')
        finally:
            pass

        if amount < 1:
            raise ValueError('param: amount: value must be greater than 0')

        url = 'url=lifeup://api/withdraw?'
        for key, value in params.items():
            if value is not None:
                url = url + key + '=' + str(value) + '%26'
            else:
                continue
        url = url[:-3]

        result = call(call=url,host=self.host,port=self.port)

        return result