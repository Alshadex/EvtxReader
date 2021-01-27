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
        # self.__fp.seek(env.Chunk.HeaderSize + env.FHEADER_SIZE + env.EventRecordHeader.EventXML[0], 0)
        # self.__binaryXMLsize = self.__size - 28
        # temp = self.__fp.read(3)
        # for i in temp:
        #     print(i)
        # with open("test.xml", 'w') as f:
        #     f.write(str(temp))
        print(self.__id)

    def getID(self):
        return self.__id

    def getSize(self):
        return self.__size
    
    def getDateTime(self): # check formatting
        return self.__datetime