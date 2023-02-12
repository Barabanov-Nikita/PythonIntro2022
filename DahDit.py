class morse:
    def __init__(self, str=""):
        self.words = ["di", "dit", "dah", "."]
        if str and len(str.split(" ")) == 1:
            symbols = [c for c in str]
            n = len(str)
            self.sep, self.end = "", " "
            self.words[3] = ""
        else:
            symbols = str.split(" ")
            n = len(symbols) if str else 0
            self.sep, self.end = " ", ", "

        if n == 2:
            self.words[0] = self.words[1] = symbols[0]
            self.words[2] = symbols[1]
        else:
            for i in range(n):
                self.words[i] = symbols[i]
        self.s = self.words[3]
        self.wordend = True

    def __pos__(self):
        if self.wordend:
            self.s = self.words[1] + self.s
            self.wordend = False
        else:
            self.s = self.words[0] + self.sep + self.s
        return self

    def __neg__(self):
        if self.wordend:
            self.s = self.words[2] + self.s
            self.wordend = False
        else:
            self.s = self.words[2] + self.sep + self.s
        return self

    def __invert__(self):
        self.wordend = True
        self.s = self.end + self.s
        return self

    def __str__(self):
        return self.s


