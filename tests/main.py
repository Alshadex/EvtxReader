import sys
from EvtxReader import EvtxFile


# print(sys.byteorder)


if len (sys.argv) < 2 :
    print("Usage: python3 main.py <evtx files>")
    sys.exit(1)


allFiles = sys.argv[1:]

with EvtxFile(allFiles[0]) as test:
    print(test.get_file_header())

test = EvtxFile(allFiles[0])
print(test.get_file_header())

