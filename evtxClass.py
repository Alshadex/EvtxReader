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
        num = int.from_bytes(temp, byteorder='little')
        return num


    def __countAllEvtRcds(self):
        '''
        Return: (int) Total number of Event Records in evtx file
        '''
        self.__fp.seek((self.__numOfChnks-1) * env.CHUNK_SIZE + env.FHEADER_SIZE + env.Chunk.LastEvtRcdNum[0], 0)
        temp = self.__fp.read(env.Chunk.LastEvtRcdNum[1])
        num = int.from_bytes(temp, byteorder='little')
        return num


    # Public Method start here

    def getNumOfEvts(self):
        return self.__numOfEvtRcds

    def getNumOfChunks(self):
        return self.__numOfChnks

    def getEvtRcdFromId(self, id):
        pass

    def parseAllEventsToCsv(self):
        # for chunk in self.__numOfChnks:
            pass
        # Size = int.from_bytes(Size, byteorder='big')
        # self.__AllEvents.append(EventRecord(self.__fp, Size, EvtRcdID, temp2))


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__fp.close()