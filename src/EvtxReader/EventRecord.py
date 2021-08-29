from .Constants import Constants
from .Errors import FileHeaderException

class EventRecord:
    
    '''
    Environment hardcoded offsets for Event Record object.
    '''
    env = {
        'Signature' :                        [0,8,'\x2a\x2a\x00\x00'],
        'Size' :                             [4,4,None],
        'Event_record_identifier' :          [8,8,None],
        'Written_date_and_time' :            [16,8,None],
        'Event' :                            [32,8,None],
    }


    def __init__(self, fp):
        self.file = fp
        self.cache = self.env.copy()
        self.cache = dict.fromkeys(self.env, None)

        # self.__size = struct.unpack('I', size)[0]
        # self.__id = struct.unpack('Q', id)[0]
        # self.__datetime = struct.unpack('I', datetime)[0]

    def seek_n_read(self, object: list, event_num: int):
        pass

    def find(self, event_num: int, last_id: int) -> dict:
        for event in range(1,last_id):
            self.file.seek(self.env['Size'][Constants.OFFSET], 1)
            event_size = self.file.read(self.env['Size'][Constants.SIZE])
            event_id = self.file.read(self.env['Event_record_identifier'][Constants.SIZE])
            
