import sys
import base64
import struct


types = {1: "B", -1: "b", 2: "H", -2: "h", 4: "I", -4: "i", 8: "Q", -8: "q"}
txt = base64.b85decode(sys.stdin.buffer.read()[:-1])
pos = txt.find(b"\x00")
record = struct.unpack(f"{'b'* pos}", txt[:pos])
record = "".join(map(lambda x: types[x], record)) * (len(txt[pos+1:]) // sum(map(abs, record)))
numbers = sum(struct.unpack("!" + record, txt[pos+1:]))
print(numbers)
