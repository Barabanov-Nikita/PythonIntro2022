friends = {}
while (pair := eval(input())) != (0, 0):
    friends.setdefault(pair[0], set())
    friends[pair[0]].add(pair[1])
    friends.setdefault(pair[1], set())
    friends[pair[1]].add(pair[0])

print(*sorted(_ for _ in friends if friends[_] == set(friends.keys()) - {_}))