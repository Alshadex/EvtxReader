from .Constants import Constants

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
        for i in self.cache:
            self.cache[i] = None
        # self.__size = struct.unpack('I', size)[0]
        # self.__id = struct.unpack('Q', id)[0]
        # self.__datetime = struct.unpack('I', datetime)[0]

    def seek_n_read(self, object: list, event_num: int):
        pass