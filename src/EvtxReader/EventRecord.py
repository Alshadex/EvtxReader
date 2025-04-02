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

    '''
    find needs to loop through the number of events. Each iteration
    checks the size of the event and seeks to the next one
    if it is not the one we are searching for
    '''