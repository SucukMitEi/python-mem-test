from mem import MEM
from psutil import process_iter
import random

mem = MEM.fromName("konsole")
while True:
	randmap = random.choice(mem.maps)

	print(
		mem.readString(
			randmap[0],
			randmap[1]-randmap[0]
		)
	)
