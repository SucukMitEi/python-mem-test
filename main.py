from mem import MEM

PID = 40507


mem = MEM(PID)

mem.readBytes
mem.writeBytes

mem.readInt32
mem.writeInt32

mem.readUInt32
mem.writeUInt32

mem.readInt64
mem.writeInt64

mem.readUInt64
mem.writeUInt64

# TODO
mem.readString
mem.writeString
