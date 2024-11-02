from requests import Response, Session
from enum import Enum
import re
from datetime import datetime

http = Session()
class Type(Enum):
  COIN = 'coin'
  EXP = 'exp'
  ITEM = 'item'

class CountSetType(Enum):
  ABSOLUTE = 'absolute'
  RELATIVE = 'relative'
        

def call(call,host,port) -> Response:
  
  url = 'http://' + host + ':' + port + '/api?' + call
  return http.get(url=url)

def color_check(hex: str):
  match = re.seach(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex)

  if match:                      
    return True
  else:
    return False

def time_to_epoch(date:datetime):

  return int(date.timestamp()) * 1000

