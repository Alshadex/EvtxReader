import struct
from environment import env
from EventRecordClass import EventRecord

# This class will become a python module that people can 
# import into their own code for parsing single evtx files.

class evtxFile:
    def __init__(self, filePath):
        self.__fpPath = filePath
        self.__AllEvents = []


    def __enter__(self):
        '''
        Executed when object is initiated using "with" statement.
        Need to test without with statement. aka manual opening and closing.
        '''
        self.__fp = open(self.__fpPath, 'rb')
        self.__numOfChnks = self.__getNumOfChnks() # stores the total number of chunks in a single file
        self.__numOfEvtRcds = self.__countAllEvtRcds() # contains all of the event records as a list
        return self


    def __getNumOfChnks(self):
        '''
        Return: (int) Number of Chunks in evtx file
        '''
        self.__fp.seek(env.FileHeader.NumberOfChunks[0], 0)
        temp = self.__fp.read(env.FileHeader.NumberOfChunks[1])
        return struct.unpack('H', temp)[0] 


    def __countAllEvtRcds(self):
        '''
        Return: (int) Total number of Event Records in evtx file
        '''
        self.__fp.seek((self.__numOfChnks-1) * env.CHUNK_SIZE + env.FHEADER_SIZE + env.Chunk.LastEvtRcdNum[0], 0)
        return struct.unpack('Q', self.__fp.read(env.Chunk.LastEvtRcdNum[1]))[0]


    # Public Method start here

    def getNumOfEvts(self):
        return self.__numOfEvtRcds

    def getEvtRcdFromId(self, id):
        pass

    def parseAllEvents(self):
        self.__fp.seek(env.Chunk.HeaderSize + env.FHEADER_SIZE + env.EventRecordHeader.Size[0], 0)
        temp = self.__fp.read(env.EventRecordHeader.Size[1])
        self.__fp.seek(env.Chunk.HeaderSize  +env.FHEADER_SIZE + env.EventRecordHeader.EvtRcdID[0])
        temp1 = self.__fp.read(env.EventRecordHeader.EvtRcdID[1])
        self.__fp.seek(env.Chunk.HeaderSize  +env.FHEADER_SIZE + env.EventRecordHeader.DateTime[0])
        temp2 = self.__fp.read(env.EventRecordHeader.DateTime[1])
        self.__AllEvents.append(EventRecord(self.__fp, temp, temp1, temp2))


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__fp.close()