class Reader:
    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.curr = None
        self.futu = next(self.iterator)
        self.tofutu()

    def tofutu(self):
        try:
            self.curr = self.futu
            self.futu = next(self.iterator)
        except StopIteration:
            self.futu = None
        return self.curr, self.futu