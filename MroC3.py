import sys


def merge(mros):
    i = 0
    ans = []
    while mros:
        if i >= len(mros):
            break
        candidate = mros[i][0]
        for mro in mros:
            if not (mro[0] == candidate or candidate not in mro):
                i += 1
                break
        else:
            ans.append(candidate)
            new_mros = []
            for mro in mros:
                if mro[0] == candidate:
                    mro = mro[1:]
                if mro:
                    new_mros.append(mro)
            mros = new_mros
            i = 0
        continue
    else:
        return ans
    return None


prog = sys.stdin.readlines()
mros = {}
for line in prog:
    if line.startswith("class"):
        i = line.find(":")
        parents = "".join(line[line.find("(")+1:i-1].split(",")).split(" ") if line.find("(") != -1 else []
        obj = line[6:i] if line.find("(") == -1 else line[6:line.find("(")]
        if not parents:
            mros[obj] = [obj, ]
        elif mro := merge([mros[parent] for parent in parents] + [parents, ]):
            mros[obj] = [obj, ] + mro
        else:
            print("No")
            break
else:
    print("Yes")

for _, __ in mros.items():
    print(_, __)

