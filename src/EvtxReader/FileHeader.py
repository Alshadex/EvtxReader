from .Errors import FileHeaderException

OFFSET =   0
SIZE   =   1
EXPECTED = 2

class FileHeader:

    env = {
        'Signature' :                 [0,8,'ElfFile\x00'],
        'First_chunk_number' :        [8,8,None],
        'Last_chunk_number' :         [16,8,None],
        'Next_record_identifier' :    [24,8,None],
        'Header_size' :               [32,4,128],
        'Minor_version' :             [36,2,1],
        'Major_version' :             [38,2,3],
        'Header_block_size' :         [40,2,4096],
        'NumberOfChunks' :            [42,2,None],
        'File_flags' :                [120,4,None],
        'Checksum' :                  [124,4,None]
    }
        
    
    def __init__(self, fp):
        self.file = fp
        self.cache = self.env.copy()
        for i in self.cache:
            self.cache[i] = None

    def seek_n_read(self, object: list):
        self.file.seek(object[OFFSET], 0)
        read_value = self.file.read(object[SIZE])
        if type(object[EXPECTED]) == type(str()):
            strVal = read_value.decode()
            if strVal != object[EXPECTED]:
                raise FileHeaderException(f'Got {strVal} instead of \
                                expected value {object[EXPECTED]}\
                                at offset {object[OFFSET]}')
            return strVal
        elif type(object[EXPECTED]) == type(int()):
            numVal = int.from_bytes(read_value, byteorder='little')
            if numVal != object[EXPECTED]:
                raise FileHeaderException(f'Got {numVal} instead of \
                                expected value {object[EXPECTED]}\
                                at offset {object[OFFSET]}')
            return numVal
        else:
            Val = int.from_bytes(read_value, byteorder='little')
            return Val

    def check_cache(self, key):
        if self.cache[key]:
            return self.cache[key]
        self.cache[key] = self.seek_n_read(self.env[key])
        return self.cache[key]

    def get_Signature(self) -> str:
        self.check_cache('Signature')
    
    def get_First_chunk_number(self) -> int:
        self.check_cache('First_chunk_number')
    
    def get_Last_chunk_number(self) -> int:
        self.check_cache('Last_chunk_number')

    def get_Next_record_identifier(self) -> int:
        self.check_cache('Next_record_identifier')

    def get_Header_size(self) -> int:
        self.check_cache('Header_size')

    def get_Minor_version(self) -> int:
        self.check_cache('Minor_version')

    def get_Major_version(self) -> int:
        self.check_cache('Major_version')

    def get_Header_block_size(self) -> int:
        self.check_cache('Header_block_size')
    
    def get_NumberOfChunks(self) -> int:
        self.check_cache('NumberOfChunks')

    def get_File_flags(self) -> int:
        self.check_cache('File_flags')

    def get_Checksum(self) -> int:
        self.check_cache('Checksum')

    def covert_to_dict(self) -> dict:
        for i in self.cache:
            self.check_cache(i)
        return self.cache
