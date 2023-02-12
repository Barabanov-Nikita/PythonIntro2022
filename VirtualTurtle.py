def turtle(coord, direction):
    x, y = coord
    vec = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    cur_dir = direction
    while True:
        command = yield x, y
        if command == "f":
            x += vec[cur_dir][0]
            y += vec[cur_dir][1]
        elif command == "l" or command == "r":
            cur_dir = (cur_dir + (-1 if command == "r" else 1)) % 4
