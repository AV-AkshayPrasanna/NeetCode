class FreqStack:

    def __init__(self):
        self.freq = {}
        self.groups = {}
        self.max_freq = 0

    def push(self, val):
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]

        self.max_freq = max(self.max_freq, f)

        if f not in self.groups:
            self.groups[f] = []

        self.groups[f].append(val)

    def pop(self):
        val = self.groups[self.max_freq].pop()

        self.freq[val] -= 1

        if not self.groups[self.max_freq]:
            self.max_freq -= 1

        return val