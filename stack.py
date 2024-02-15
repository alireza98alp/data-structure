class Stack():
    def __init__(self, maxsize):
        self._nitem = 0
        self._stack = [None for _ in range(maxsize)]
        self._maxitem = maxsize

    def pop(self):
        if self._nitem == 0:
            raise Exception('stack is empty')
        else:
            self._nitem -= 1
            return self._stack[self._nitem]

    def Push(self, item):
        if self._nitem == self._maxitem:
            raise Exception('stack is full')
        else:

            self._stack[self._nitem] = item
            self._nitem += 1

    def __len__(self):
        return self._nitem
