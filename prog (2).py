import sys

txt = bytearray(sys.stdin.buffer.read())
size = txt[0:1]
txt = txt[1:]
part_size = len(txt) // size[0]
if len(txt) % size[0]:
    part_size += 1

res = sorted(txt[i*part_size:(i + 1) * part_size] for i in range(size[0]))

sys.stdout.buffer.write(bytes(size))
for i in res:
    sys.stdout.buffer.write(bytes(i))