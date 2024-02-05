class array():
    def __init__(self, maxsize: int):
        self.maxsize = maxsize
        self.arr = [None for _ in range(self.maxsize)]
        self.nitem = 0

    def __contains__(self, item):
        for i in range(self.nitem):
            if self.arr[i] == item:
                return True
        return False

    def append(self, item):
        if self.nitem != self.maxsize:
            self.arr[self.nitem] = item
            self.nitem += 1
        else:
            print('full')

    def delete(self, item):
        for i in range(self.nitem):
            if self.arr[i] == item:
                self.nitem -= 1
                for j in range(i, self.nitem):
                    self.arr[j] = self.arr[j+1]

    def __repr__(self) -> str:
        s = '['
        for i in range(self.nitem):
            s += str(self.arr[i])+', '
        s += '\b\b]'
        return s
