import struct

s = struct.pack('i', 12311211)

r = struct.unpack('i', s)
print(r)