class Array():
    def __init__(self, maxsize: int):
        self.maxsize = maxsize
        self._arr = [None for _ in range(self.maxsize)]
        self._nitem = 0

    def __contains__(self, item):
        for i in range(self._nitem):
            if self._arr[i] == item:
                return True
        return False

    def append(self, item):
        if self._nitem != self.maxsize:
            self._arr[self._nitem] = item
            self._nitem += 1
        else:
            raise ValueError('array is full')

    def delete(self, item):
        for i in range(self._nitem):
            if self._arr[i] == item:
                self._nitem -= 1
                for j in range(i, self._nitem):
                    self._arr[j] = self._arr[j+1]

    def __str__(self) -> str:
        if self._nitem:
            s = '['
            for i in range(self._nitem):
                s += str(self._arr[i])+', '
            s += '\b\b]'
            return s
        else:
            return '[ ]'

    def __len__(self) -> int:
        return self._nitem
