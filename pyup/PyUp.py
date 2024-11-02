class PyUp:
    '''
    Creates the base LifeUp api interaction with a given host and port string.
    param: str host: the ip address of your LifeUp Cloud.
    param: str port: the port address of your LifeUp Cloud.
    '''
    host: str
    port: str

    def __init__(self,host:str,port:str):
        self.host = host
        self.port = port