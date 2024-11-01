from pyup import PyUp
import os

host = '192.168.86.64'
port = "13276"

lifeUp = PyUp.PyUp(host,port)


lifeUp.toast("they're great!")