import struct
from typing import List
import re


class MemoryError(Exception):
	pass


class Int32(int):
	def __init__(self, *p, **kw) -> None:
		super().__init__(*p, **kw)


class UInt32(int):
	def __init__(self, *p, **kw) -> None:
		super().__init__(*p, **kw)


class Int64(int):
	def __init__(self, *p, **kw) -> None:
		super().__init__(*p, **kw)


class UInt64(int):
	def __init__(self, *p, **kw) -> None:
		super().__init__(*p, **kw)


class Byte(bytes):
	def __init__(self, *p, **kw) -> None:
		super().__init__(*p, **kw)


class MEM:
	def __init__(self, pid):
		self.pid = pid

		self.memfd = open(f"/proc/{pid}/mem", "r+b")

		self.mapfd = open(f"/proc/{pid}/maps", "r")

		self.maps = []
		for match in re.findall(r"([a-f0-9]+)-([a-f0-9]+) (...)", self.mapfd.read().strip()):
			match[0] = int(match[0], base=16)
			match[1] = int(match[1], base=16)
			match[2] = [i for i in match[2] if i != "-"]

			self.maps.append(match)

	def addrValid(self, addr, size, right):
		return any(addr in range(*_range[:-1]) and addr+size in range(*_range[:-1]) and right in _range[2] for _range in self.maps)

	def readBytes(self, addr, size) -> List[Byte]:
		if not self.addrValid(addr, size, "r"):
			raise MemoryError("You can not read this address.")
		self.memfd.seek(addr)
		return self.memfd.read(size)

	def writeBytes(self, addr, content) -> None:
		if not self.addrValid(addr, len(content), "w") or not self.addrValid:
			raise MemoryError("You can not read this address.")

		self.memfd.seek(addr)
		self.memfd.write(content)

	def readInt32(self, addr) -> Int32:
		return struct.unpack("i", self.readBytes(addr, 4))[0]

	def writeInt32(self, addr, value):
		self.writeBytes(addr, struct.pack("i", value))

	def readUInt32(self, addr) -> UInt32:
		return struct.unpack("I", self.readBytes(addr, 4))[0]

	def writeUInt32(self, addr, value):
		self.writeBytes(addr, struct.pack("I", value))

	def readInt64(self, addr) -> Int64:
		return struct.unpack("q", self.readBytes(addr, 4))[0]

	def writeInt64(self, addr, value):
		self.writeBytes(addr, struct.pack("q", value))

	def readUInt64(self, addr) -> UInt64:
		return struct.unpack("Q", self.readBytes(addr, 4))[0]

	def writeUInt64(self, addr, value):
		self.writeBytes(addr, struct.pack("Q", value))

	def readString(self, addr) -> str:
		return
