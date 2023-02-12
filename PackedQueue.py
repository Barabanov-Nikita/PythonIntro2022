q = []
cmds = eval(input())

for cmd in cmds:
    if type(cmd) == tuple:
        q = list(cmd)[::-1] + q
    elif type(cmd) == int:
        if cmd > len(q):
            break
        elif not cmd:
            print(())
        else:
            print(tuple(q[-1 * cmd:])[::-1])
            del q[-1 * cmd:]