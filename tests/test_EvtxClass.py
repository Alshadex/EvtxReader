import pprint
from EvtxReader import EvtxFile
from .basetester import BaseTester


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

def test_file_header_getters(evtxFile):
    with EvtxFile(evtxFile) as test:
        # Test all file header getters
        assert test.get_Signature() == 'ElfFile\x00'
        assert test.get_First_chunk_number() == 0
        assert test.get_Last_chunk_number() == 52
        assert test.get_Next_record_identifier() == 5660
        assert test.get_Header_size() == 128
        assert test.get_Minor_version() == 1
        assert test.get_Major_version() == 3
        assert test.get_Header_block_size() == 4096
        assert test.get_NumberOfChunks() == 53
        assert test.get_File_flags() == 0
        assert test.get_Checksum() == 3014202741

def test_chunk_header_getters(evtxFile):
    with EvtxFile(evtxFile) as test:
        chunk_num = 0
        # Test all chunk header getters
        assert test.get_chunk_Signature(chunk_num) == 'ElfChnk\x00'
        assert test.get_First_event_record_number(chunk_num) == 1
        assert test.get_Last_event_record_number(chunk_num) == 118
        assert test.get_First_event_record_identifier(chunk_num) == 1
        assert test.get_Last_event_record_identifier(chunk_num) == 118
        assert test.get_chunk_Header_size(chunk_num) == 128
        assert test.get_Last_event_record_data_offset(chunk_num) == 64640
        assert test.get_Free_space_offset(chunk_num) == 65224
        assert test.get_Event_records_checksum(chunk_num) == 3637811879

def test_context_manager(evtxFile):
    # Test that the file is properly closed after use
    with EvtxFile(evtxFile) as test:
        assert not test.file.closed
    # After the with block, the file should be closed
    with EvtxFile(evtxFile) as test:
        test.file.close()
        assert test.file.closed

def test_invalid_chunk_number(evtxFile):
    with EvtxFile(evtxFile) as test:
        # Test with an invalid chunk number
        invalid_chunk = test.get_NumberOfChunks() + 1
        try:
            test.get_Chunk_header(invalid_chunk)
            assert False, "Should have raised an exception for invalid chunk number"
        except Exception:
            assert True

def test_invalid_event_number(evtxFile):
    with EvtxFile(evtxFile) as test:
        # Test with an invalid event number
        try:
            test.get_chunk_Event(0, 999999)
            assert False, "Should have raised an exception for invalid event number"
        except Exception:
            assert True