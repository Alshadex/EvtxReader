
'''
    This file holds hardcoded offsets from
    https://github.com/libyal/libevtx/blob/master/documentation/Windows%20XML%20Event%20Log%20(EVTX).asciidoc#file_flags
'''

class env:

    FHEADER_SIZE = 4096
    CHUNK_SIZE = 65536

    class FileHeader:
        # File Header is exactly 4096 bytes long
        NumberOfChunks = [42,2]
    
    class Chunk:
        # The chunk is 65536 bytes of size and consists of:
        #     chunk header (512 Bytes)
        #     array of event records
        #     unused space
        # HeaderSize = 512
        FirstEvtRcdNum = [8,8]
        LastEvtRcdNum = [16,8]
        HeaderSize = [40,4]
        LastEvtRcdOffset = [44,4]
        CommonStrOffarray = [128,256] # At offset 128 is the offsets of strings that are common in the event records.
        TemplatePtr = [384,128] # not sure what this is exactly.

    class EventRecordHeader:
        Signature = [0,8]
        Size = [4,4] #  The size of the event record including the signature and the size. Seems like every event record has an arbitrary size.
        EvtRcdID = [8,8]
        DateTime = [16,4]
        EventXML = [24, None]

    class BinaryXml:
        pass