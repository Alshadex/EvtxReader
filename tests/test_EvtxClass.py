import pprint
from EvtxReader import EvtxFile
from .basetester import BaseTester

# print(sys.byteorder)


# if len (sys.argv) < 2 :
#     print("Usage: python3 main.py <evtx files>")
#     sys.exit(1)


# allFiles = sys.argv[1:]

# with EvtxFile(allFiles[0]) as test:
#     print('Printing file header info')
#     print(test.get_File_header())
#     num = test.get_NumberOfChunks() 
#     print('\nPrinting all chunks')
#     for i in range(num):
#         print(test.get_Chunk_header(i))
#         print()
#     print(test.get_chunk_Event(0,1))

def test_get_File_header(evtxFile):
    with EvtxFile(evtxFile) as test:
        assert test.get_File_header() == {  'Checksum': 3014202741,
                                            'File_flags': 0,
                                            'First_chunk_number': 0,
                                            'Header_block_size': 4096,
                                            'Header_size': 128,
                                            'Last_chunk_number': 52,
                                            'Major_version': 3,
                                            'Minor_version': 1,
                                            'Next_record_identifier': 5660,
                                            'NumberOfChunks': 53,
                                            'Signature': 'ElfFile\x00'
                                        }

def test_get_Chunk_header(evtxFile):
    with EvtxFile(evtxFile) as test:
        # pprint.pprint(test.get_Chunk_header(52))
        assert test.get_Chunk_header(0) == {'Checksum': 4275004840,
                                            'Event_records_checksum': 3637811879,
                                            'First_event_record_identifier': 1,
                                            'First_event_record_number': 1,
                                            'Free_space_offset': 65224,
                                            'Header_size': 128,
                                            'Last_event_record_data_offset': 64640,
                                            'Last_event_record_identifier': 118,
                                            'Last_event_record_number': 118,
                                            'Signature': 'ElfChnk\x00'
                                            }

def test_get_chunk_Event(evtxFile):
    with EvtxFile(evtxFile) as test:
        pprint.pprint(test.get_chunk_Event(0,2))
        # assert test.get_chunk_Event(0,1) == {   'EventIdentifier': 1,
                                            #     'EventRecordId': 1,
                                            #     'EventSize': 0,
                                            #     'EventTime': '2019-10-01T00:00:00.000000Z',
                                            #     'EventType': 'EventLog',
                                            #     'EventVersion': 1,
                                            #     'ExecutionProcessId': 0,
                                            #     'ExecutionThreadId': 0,
                                            #     'Keywords': 0,
                                            #     'Level': 4,
                                            #     'Opcode': 0,
                                            #     'ProviderId': '{00000000-0000-0000-0000-000000000000}',
                                            #     'ProviderName': 'Microsoft-Windows-Eventlog',
                                            #     'Qualifiers': 0,
                                            #     'RecordNumber': 1,
                                            #     'Task': 0,
                                            #     'TimeCreated': '201,
                                            #     'Version': 0
                                            # }