from pyup import pyup, general, task, shop


host = '192.168.86.64'
port = "13276"

base = pyup.PyUp(host,port)

general.self = base

general.toast('test')