from pyup import PyUp
import os

host = os.environ.get('host')
port = os.environ.get('port')

lifeUp = PyUp(host=host,port=port)

lifeUp.toast("they're great!")