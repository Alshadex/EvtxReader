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
    num = test.get_NumberOfChunks() 
    print('\nPrinting all chunks')
    for i in range(num):
        print(test.get_Chunk_header(i))
        print()
    print(test.get_chunk_Event(0,1))
