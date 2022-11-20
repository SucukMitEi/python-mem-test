from mem import MEM

mem = MEM.fromName("konsole")

for map in mem.maps:
	print(
		f"""Map: {map}

First 4 Bytes: {mem.readBytes(map[0], 4)}

Int32: {mem.readInt32(map[0])}
UInt32: {mem.readUInt32(map[0])}

Int64: {mem.readInt64(map[0])}
UInt64: {mem.readUInt64(map[0])}
First 40 Characters of String: {mem.readString(map[0], 40)}
""")

	print()
