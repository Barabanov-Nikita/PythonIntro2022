participants = []
while s := input():
    first, second, cmd, time = *s.split(maxsplit=2), tuple(map(int, s.rsplit(maxsplit=1)[-1].split(":")))
    cmd = cmd.rsplit(maxsplit=1)[0]
    participants.append((time, second, first, cmd))

participants.sort()
c, idx, prev = 0, 0, participants[0][0]

while idx < len(participants) and c < 3:
    if participants[idx][0] != prev:
        c += 1
        prev = participants[idx][0]
    idx += 1

if idx == len(participants):
    idx += 1
    
leaders = participants[:idx - 1]
maxlens = [len(max(leaders, key=lambda x: len(x[i]))[i]) for i in range(1, 4)]
k = [2, 1, 3]
for leader in leaders:
    ans = [leader[i].ljust(maxlens[i - 1] + 1) for i in k]
    ans.append(":".join([str(_) for _ in leader[0]]))
    print("".join(ans))
