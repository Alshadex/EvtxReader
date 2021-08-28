from .FileHeader import FileHeader
from .EvtxChunk import Chunk

# This class will become a python module that people can 
# import into their own code for parsing single evtx files.
# All methods here should be public.

class EvtxFile:
    def __init__(self, filePath):
        self.file = open(filePath, 'rb')
        self.fileheader = FileHeader(self.file)
        self.chunks = Chunk(self.file)
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


    '''
    Getters for file header information.
    '''
    def get_File_header(self) -> dict():
        return self.fileheader.convert_to_dict()

    def get_Signature(self) -> str:
        return self.fileheader.get_Signature()

    def get_First_chunk_number(self) -> int:
        return self.fileheader.get_First_chunk_number()

    def get_Last_chunk_number(self) -> int:
        return self.fileheader.get_Last_chunk_number()

    def get_Next_record_identifier(self) -> int:
        return self.fileheader.get_Next_record_identifier()

    def get_Header_size(self) -> int:
        return self.fileheader.get_Header_size()

    def get_Minor_version(self) -> int:
        return self.fileheader.get_Minor_version()

    def get_Major_version(self) -> int:
        return self.fileheader.get_Major_version()

    def get_Header_block_size(self) -> int:
        return self.fileheader.get_Header_block_size()
    
    def get_NumberOfChunks(self) -> int:
        return self.fileheader.get_NumberOfChunks()

    def get_File_flags(self) -> int:
        return self.fileheader.get_File_flags()

    def get_Checksum(self) -> int:
        return self.fileheader.get_Checksum()


    
    '''
    Getters for every chunk header.
    '''
    def get_Chunk_header(self, chunk_num: int) -> dict:
        return self.chunks.covert_to_dict(chunk_num)

    def get_chunk_Signature(self, chunk_num: int) -> str:
        return self.chunks.get_Signature(chunk_num)

    def get_First_event_record_number(self, chunk_num: int) -> int:
        return self.chunks.get_First_event_record_number(chunk_num)

    def get_Last_event_record_number(self, chunk_num: int) -> int:
        return self.chunks.get_Last_event_record_number(chunk_num)

    def get_First_event_record_identifier(self, chunk_num: int) -> int:
        return self.chunks.get_First_event_record_identifier(chunk_num)

    def get_Last_event_record_identifier(self, chunk_num: int) -> int:
        return self.chunks.get_Last_event_record_identifier(chunk_num)

    def get_chunk_Header_size(self, chunk_num: int) -> int:
        return self.chunks.get_chunk_Header_size(chunk_num)

    def get_Last_event_record_data_offset(self, chunk_num: int) -> int:
        return self.chunks.get_Last_event_record_data_offset(chunk_num)

    def get_Free_space_offset(self, chunk_num: int) -> int:
        return self.chunks.get_Free_space_offset(chunk_num)

    def get_Event_records_checksum(self, chunk_num: int) -> int:
        return self.chunks.get_Event_records_checksum(chunk_num)

    def get_Common_string_offset(self, chunk_num: int):
        return self.chunks.get_Common_string_offset(chunk_num)

    def get_TemplatePtr(self, chunk_num: int):
        return self.chunks.get_TemplatePtr(chunk_num)


    '''
    Getter for specific event record in specifc chunk.
    '''
    def get_chunk_Event(self, chunk_num: int, event_id: int) -> dict:
        return self.chunks.get_chunk_Event(chunk_num, event_id)





    def get_num_records(self) -> int:
        '''
        Return: (int) Total number of Event Records in evtx file
        '''
        self.file.seek((self.__numOfChnks-1) * env.CHUNK_SIZE + env.FHEADER_SIZE + env.Chunk.LastEvtRcdNum[0], 0)
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
