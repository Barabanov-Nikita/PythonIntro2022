sample, find = input(), input()
start = sample.find(find[0])

while start != -1:
    for step in range(1, len(sample)):
        if find in sample[start::step]:
            print("YES")
            break
    else:
        start = sample.find(find[0], start + 1)
        continue
    break
else:
    print("NO")



