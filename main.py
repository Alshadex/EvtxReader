import sys
import struct
from evtxClass import evtxFile
from environment import env


# print(sys.byteorder)


if len (sys.argv) < 2 :
    print("Usage: python3 main.py <evtx files>")
    sys.exit(1)


allFiles = sys.argv[1:]

for f in allFiles:
    with evtxFile(f) as file:
        # print(file.getNumOfChunks())
        # print(file.getNumOfEvts())
        file.parseAllEventsToCsv()