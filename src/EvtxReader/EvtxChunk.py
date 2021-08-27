from .EventRecord import EventRecord
from .Constants import Constants
from .Errors import FileHeaderException


class Chunk:
    

    '''
    environment hardcoded offsets for Chunk object.
    '''
    env = {
        'Signature' :                        [0,8,'ElfChnk\x00'],
        'First_event_record_number' :        [8,8,None],
        'Last_event_record_number' :         [16,8,None],
        'First_event_record_identifier' :    [24,8,None],
        'Last_event_record_identifier' :     [32,8,None],
        'Header_size' :                      [40,4,128],
        'Last_event_record_data_offset' :    [44,4,None],
        'Free_space_offset' :                [48,4,None],
        'Event_records_checksum' :           [52,4,None],
        'Checksum' :                         [124,4,None],
        # 'Common_string_offset_array' :       [128, 256, None], # 64 x 4
        # 'TemplatePtr' :                      [384, 128, None], # 32 x 4
    }

    def __init__(self, fp):
        self.file = fp
        self.cache = self.env.copy()
        for i in self.cache:
            self.cache[i] = None
        self.activeChunk = None
        self.eventrecords = EventRecord(fp)

    def seek_n_read(self, object: list, chunk_num: int):
        self.file.seek( Constants.FHEADER_SIZE +
                        (chunk_num - 1) * Constants.CHUNK_SIZE + 
                        object[Constants.OFFSET], 0 )
        read_value = self.file.read(object[Constants.SIZE])
        if type(object[Constants.EXPECTED]) == type(str()):
            strVal = read_value.decode()
            if strVal != object[Constants.EXPECTED]:
                raise FileHeaderException(f'Got {strVal} instead of \
                                expected value {object[Constants.EXPECTED]}\
                                at offset {object[Constants.OFFSET]}')
            return strVal
        elif type(object[Constants.EXPECTED]) == type(int()):
            numVal = int.from_bytes(read_value, byteorder='little')
            if numVal != object[Constants.EXPECTED]:
                raise FileHeaderException(f'Got {numVal} instead of \
                                expected value {object[Constants.EXPECTED]}\
                                at offset {object[Constants.OFFSET]}')
            return numVal
        else:
            Val = int.from_bytes(read_value, byteorder='little')
            return Val

    def check_cache(self, key, chunk_num):
        if self.activeChunk == chunk_num:
            if self.cache[key]:
                return self.cache[key]
            self.cache[key] = self.seek_n_read(self.env[key], chunk_num)
        else:
            for i in self.cache:
                self.cache[i] = None
            self.cache[key] = self.seek_n_read(self.env[key], chunk_num)
            self.activeChunk = chunk_num
        return self.cache[key]

    def get_Signature(self, chunk_num: int) -> str:
        self.check_cache('Signature', chunk_num)

    def get_First_event_record_number(self, chunk_num: int) -> int:
        self.check_cache('First_event_record_number', chunk_num)

    def get_Last_event_record_number(self, chunk_num: int) -> int:
        self.check_cache('Last_event_record_number', chunk_num)

    def get_First_event_record_identifier(self, chunk_num: int) -> int:
        self.check_cache('First_event_record_identifier', chunk_num)

    def get_Last_event_record_identifier(self, chunk_num: int) -> int:
        self.check_cache('Last_event_record_identifier', chunk_num)

    def get_chunk_Header_size(self, chunk_num: int) -> int:
        self.check_cache('Header_size', chunk_num)

    def get_Last_event_record_data_offset(self, chunk_num: int) -> int:
        self.check_cache('Last_event_record_data_offset', chunk_num)

    def get_Free_space_offset(self, chunk_num: int) -> int:
        self.check_cache('Free_space_offset', chunk_num)

    def get_Event_records_checksum(self, chunk_num: int) -> int:
        self.check_cache('Event_records_checksum', chunk_num)

    def get_Checksum(self, chunk_num: int) -> int:
        self.check_cache('Checksum', chunk_num)

    def get_Common_string_offset(self, chunk_num: int):
        self.check_cache('Common_string_offset_array', chunk_num)

    def get_TemplatePtr(self, chunk_num: int):
        self.check_cache('TemplatePtr', chunk_num)

    def covert_to_dict(self, chunk_num: int) -> dict:
        for i in self.cache:
            self.check_cache(i, chunk_num)
        return self.cache


    def get_chunk_Event(self, chunk_num: int, event_num: int) -> dict:
        pass