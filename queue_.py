class Queue_():
    def __init__(self, maxsize: int) -> None:
        self._maxsize = maxsize
        self._queue = [None] * maxsize
        self._first = 0
        self._last = 0
        self._nitems = 0

    def insert(self, item):
        if self._nitems >= self._maxsize:
            raise Exception('queue is full')
        else:
            self._nitems += 1
            if self._last == self._maxsize-1:
                self._last = 0
            else:
                self._last += 1
            self._queue[self._last] = item

    def remove(self):
        if self._nitems == 0:
            raise Exception('queue is empty')
        else:
            self._nitems -= 1
            tmp = self._queue[self._first]
            if self._first == self._maxsize-1:
                self._first = 0
            else:
                self._first += 1
            return tmp


q = Queue_(10)
for i in range(9):
    q.insert(i)
    print(i)
