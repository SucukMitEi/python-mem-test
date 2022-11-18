from mem import MEM
from psutil import process_iter


mem = MEM.fromName("konsole")

# TODO
print(mem.readString(0x7f9f13281000, 10))
