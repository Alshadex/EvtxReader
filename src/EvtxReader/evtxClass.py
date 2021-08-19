from .environment import env
from .EventRecordClass import EventRecord

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


    def __seek_n_read_Chunk(self, object: list, chunk_num: int ):
        self.__fp.seek(env.CHUNK_SIZE * chunk_num + env.FHEADER_SIZE + object[0], 0)
        temp1 = self.__fp.read(object[1])
        numVal = int.from_bytes(temp1, byteorder='little')
        return numVal

    # def __seek_n_read_Event(self, object: list, event_num: int):
    #     self.__fp.seek(env.Chunk)
    # Public Method start here

    def getNumOfEvts(self):
        return self.__numOfEvtRcds

    def getNumOfChunks(self):
        return self.__numOfChnks

    # def getEvtRcdFromId(self, id):
    #     pass

    def parseAllEventsToCsv(self):

        # Goes through every chunk and prints how many event records are stored in the chunk.
        for chunk in range(self.__numOfChnks):
            first = self.__seek_n_read_Chunk(env.Chunk.FirstEvtRcdNum, chunk)
            last = self.__seek_n_read_Chunk(env.Chunk.LastEvtRcdNum, chunk)
            NumOfRecordsInChunk = last - first + 1
            print("There are " + str(NumOfRecordsInChunk)+ " event records in Chunk number " + str(chunk+1))

            # for record in range(NumOfRecordsInChunk):
            self.__fp.seek(env.CHUNK_SIZE * chunk + env.FHEADER_SIZE + 512 + env.EventRecordHeader.Size[0], 0)
            size_bytes = self.__fp.read(env.EventRecordHeader.Size[1])
            size = int.from_bytes(size_bytes, byteorder='little')
            print(size)
            
            print(env.CHUNK_SIZE * chunk + env.FHEADER_SIZE + 512 + (size - env.EventRecordHeader.EventXML[0]))
            self.__fp.seek(env.CHUNK_SIZE * chunk + env.FHEADER_SIZE + 512 + (size - env.EventRecordHeader.EventXML[0]), 0)
            with open('eventrecord.xml', 'w') as f:
                binxml = self.__fp.read(size - env.EventRecordHeader.EventXML[0])


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__fp.close()
