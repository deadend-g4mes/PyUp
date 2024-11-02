import requests
from requests import Response
from enum import Enum

class Type(Enum):
    COIN = 'coin'
    EXP = 'exp'
    ITEM = 'item'

class CountSetType(Enum):
    ABSOLUTE = 'absolute'
    RELATIVE = 'relative'
        

def call(call) -> Response:
    return requests.get(url=call)
    
    

