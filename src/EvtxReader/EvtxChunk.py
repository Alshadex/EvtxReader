from .Errors import FileHeaderException

OFFSET =   0
SIZE   =   1
EXPECTED = 2

class Chunk:
    
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
        'Checksum' :                         [124,4,None]
    }

    def __init__(self, fp):
        self.file = fp
        self.cache = self.env.copy()
        for i in self.cache:
            self.cache[i] = None
        