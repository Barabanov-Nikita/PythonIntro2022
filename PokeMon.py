decks, owners = {}, {}
while s := input():
    s = s.split("/")
    s[0], s[1] = s[0].strip(), s[1].strip()
    operate = decks if s[0].isdigit() else owners
    operate.setdefault(s[0], set())
    operate[s[0]].add(s[1])

for owner in owners:
    owner_pull = set()
    for deck in owners[owner]:
        owner_pull |= decks[deck]
    owners[owner] = len(owner_pull)

top = sorted(owners.items(), key=lambda x: x[1], reverse=True)
if top:
    top_count = top[0][1]
    i = 0
    while i < len(top) and ((cur_count := top[i][1]) == top_count):
        i += 1
    print(*sorted(_[0] for _ in top[:i]), sep="\n")