coords = []
while (coord := input()) != "":
    coords.append(eval(coord))

h = [*zip(*coords)]
max_coord, min_coord = [*map(max, h)], [*map(min, h)]
s = 1
for i in range(3):
    s *= max_coord[i] - min_coord[i]

print(s)
