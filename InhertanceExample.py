
#Creating A user Defined Exception
class InvalidOperationError(Exception):
    pass

class Strem:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream Is Already Opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream Is Already Closed")
        self.opened = False

class FileStream(Strem):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Strem):
    def read(self):
        print("Reading data from a network")
