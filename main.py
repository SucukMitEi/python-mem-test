from mem import MEM
from psutil import process_iter
import random

mem = MEM.fromName("konsole")

for map in mem.maps:
	print(
		mem.readString(map[0], map[1])
	)