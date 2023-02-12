class Pushpull:
    positions = [0]

    def __init__(self, pos=0):
        self.positions.append(pos)

    def push(self, steps=1):
        self.positions.append(self.positions[-1] + steps)

    def pull(self, steps=1):
        self.positions.append(self.positions[-1] - steps)

    def __iter__(self):
        pos = self.positions[-1]
        return iter(range(0, pos, 1 if pos >= 0 else -1))

    def __str__(self):
        pos = self.positions[-1]
        return f"{'<' if pos <= 0 else '>'}{pos * (1 if pos > 0 else -1)}{'>' if pos >= 0 else '<'}"
