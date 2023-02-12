prev = int(input())
max_length = 1
length = 1
while (cur := int(input())) != 0:
    if cur >= prev:
        length += 1
    else:
        length = 1
    max_length = length if length > max_length else max_length
    prev = cur

print(max_length)
