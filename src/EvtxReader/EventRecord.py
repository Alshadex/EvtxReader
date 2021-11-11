import struct

from .Constants import Constants
from .Errors import FileHeaderException

class EventRecord:
    
    '''
    Environment hardcoded offsets for Event Record object.
    '''
    env = {
        'Signature' :                        [0,4,'\x2a\x2a\x00\x00'],
        'Size' :                             [4,4,None],
        'Event_record_identifier' :          [8,8,None],
        'Written_date_and_time' :            [16,8,None],
        'Event' :                            [24,None,None],
    }


    def __init__(self, fp):
        self.file = fp
        #self.cache = dict.fromkeys(self.env, None)

        # self.__size = struct.unpack('I', size)[0]
        # self.__id = struct.unpack('Q', id)[0]
        # self.__datetime = struct.unpack('I', datetime)[0]

    def seek_n_read(self, object: list, event_num: int):
        pass

    
    '''
    find needs to loop through the number of events. Each iteration
    checks the size of the event and seeks to the next one
    if it is not the one we are searching for
    '''
    def find(self, event_num: int) -> dict:
        for i in range(event_num):
            self.file.seek(self.env['Size'][Constants.OFFSET], 1)
            event_size = struct.unpack('I', self.file.read(self.env['Size'][Constants.SIZE]))[0]
            event_id = struct.unpack('Q', self.file.read(self.env['Event_record_identifier'][Constants.SIZE]))[0]
            if event_id == event_num:
                break
            self.file.seek(event_size - 16, 1)

        event_dnt = struct.unpack('Q', self.file.read(self.env['Written_date_and_time'][Constants.SIZE]))[0]
        event_data = self.file.read(event_size - 24)
        print(event_data)




