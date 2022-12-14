from typing import List
from re import split
from psutil import process_iter
from struct import pack, unpack


class MemoryReadException(Exception):
	pass


class MemoryWriteException(Exception):
	pass


class ProcessNotFoundException(Exception):
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
	def __init__(self, pid: int) -> None:
		self.pid = pid

		self.memfd = open(f"/proc/{pid}/mem", "r+b")

		self.mapfd = open(f"/proc/{pid}/maps", "r")

		self.maps = []
		for line in self.mapfd.read().strip().split("\n"):
			line = split(r" +", line)

			_from, to = [int(i, base=16) for i in line[0].split("-")]
			rights = [i for i in list(line[1][:-1]) if i != "-"]
			print(rights)
			if "[" in line[5]:  # heap, stack, vvar, vdso, vsyscall
				continue

			self.maps.append([_from, to, rights])

	@classmethod
	def fromName(cls, name: str) -> "MEM":
		for proc in process_iter():
			if proc.name() == name:
				return cls(proc.pid)
		raise ProcessNotFoundException(f"Couldn't find process {name}")

	def addrValid(self, addr: Int32 | Int64, size: int, right: str) -> bool:
		for _range in self.maps:
			# check if address is in the map
			if addr in range(*_range[:-1]) and addr + size not in range(*_range[:-1]):
				return True

			# check for rights
			if right in _range[2]:
				return True
		return False

	def readBytes(self, addr: Int32 | Int64, size: int) -> List[Byte]:
		# check if address `addr` is valid for reading `size` bytes
		if not self.addrValid(addr, size, "r"):
			raise MemoryReadException("You can not read this address.")

		# set position to `addr`
		self.memfd.seek(addr)

		# read `size` bytes
		return self.memfd.read(size)

	def writeBytes(self, addr: Int32 | Int64, content: bytes) -> None:
		# check if address `addr` is valid for writing `size` bytes
		if not self.addrValid(addr, len(content), "w"):
			raise MemoryWriteException("You can not read this address.")

		# set position to `addr`
		self.memfd.seek(addr)

		# write `content` to memory
		self.memfd.write(content)

	def readInt32(self, addr: Int32 | Int64) -> Int32:
		return unpack("i", self.readBytes(addr, 4))[0]

	def writeInt32(self, addr: Int32 | Int64, value: Int32) -> None:
		self.writeBytes(addr, pack("i", value))

	def readUInt32(self, addr: Int32 | Int64) -> UInt32:
		return unpack("I", self.readBytes(addr, 4))[0]

	def writeUInt32(self, addr: Int32 | Int64, value: UInt32) -> None:
		self.writeBytes(addr, pack("I", value))

	def readInt64(self, addr: Int32 | Int64) -> Int64:
		return unpack("q", self.readBytes(addr, 8))[0]

	def writeInt64(self, addr: Int32 | Int64, value: Int64) -> None:
		self.writeBytes(addr, pack("q", value))

	def readUInt64(self, addr: Int32 | Int64) -> UInt64:
		return unpack("Q", self.readBytes(addr, 8))[0]

	def writeUInt64(self, addr: Int32 | Int64, value: UInt64) -> None:
		self.writeBytes(addr, pack("Q", value))

	def readString(self, addr: Int32 | Int64, size: int = -1) -> str:
		if size == -1:  # read until NULL character
			x = b""
			y = b""
			z = 0
			while x != b"\x00":
				x = self.readBytes(addr+z, 1)
				y += x
				z += 1
			return y.decode("utf-8", "ignore")
		else:
			return self.readBytes(addr, size).decode("utf-8", "ignore")
