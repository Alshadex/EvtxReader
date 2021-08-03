import struct
from environment import env

class EventRecord:
    def __init__(self, fp, size, id, datetime):
        self.__fp = fp
        self.__size = struct.unpack('I', size)[0]
        self.__id = struct.unpack('Q', id)[0]
        self.__datetime = struct.unpack('I', datetime)[0]

        self.__parse()
    
    def __parse(self):
        print(self.__id)

    def getID(self):
        return self.__id

    def getSize(self):
        return self.__size
    
    def getDateTime(self): # check formatting
        return self.__datetime