#Abstract Class 
from abc import ABC, abstractclassmethod

#Creating A user Defined Exception
class InvalidOperationError(Exception):
    pass


class Strem(ABC):
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
    
    @abstractclassmethod
    def read(self):
        pass

class FileStream(Strem):
    def read(self):
        print("Reading data from a file")

class MemoryStream(Strem):
    def read(self):
        print("Reading data from a memory stream..")


class NetworkStream(Strem):
    def read(self):
        print("Reading data from a network")
