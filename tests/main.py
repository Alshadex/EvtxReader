import sys
from EvtxReader import EvtxFile


# print(sys.byteorder)


if len (sys.argv) < 2 :
    print("Usage: python3 main.py <evtx files>")
    sys.exit(1)


allFiles = sys.argv[1:]

with EvtxFile(allFiles[0]) as test:
    print('Printing file header info')
    print(test.get_File_header())
    print('\nPrinting chunk: 1')
    print(test.get_Chunk_header(1))
    print('\nPrinting chunk out of bound:')
    print(test.get_Chunk_header(1000))