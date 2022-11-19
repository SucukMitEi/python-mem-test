from mem import MEM

mem = MEM.fromName("konsole")

for map in mem.maps:
	print(f"""From: {hex(map[0])[2:]}
To: {hex(map[1])[2:]}
Rights: {map[2]}""")
