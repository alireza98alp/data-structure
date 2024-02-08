class array():
    def __init__(self, maxsize: int):
        self.maxsize = maxsize
        self.__arr = [None for _ in range(self.maxsize)]
        self.__nitem = 0

    def __contains__(self, item):
        for i in range(self.__nitem):
            if self.__arr[i] == item:
                return True
        return False

    def append(self, item):
        if self.__nitem != self.maxsize:
            self.__arr[self.__nitem] = item
            self.__nitem += 1
        else:
            print('full')

    def delete(self, item):
        for i in range(self.__nitem):
            if self.__arr[i] == item:
                self.__nitem -= 1
                for j in range(i, self.__nitem):
                    self.__arr[j] = self.__arr[j+1]

    def __repr__(self) -> str:
        s = '['
        for i in range(self.__nitem):
            s += str(self.__arr[i])+', '
        s += '\b\b]'
        return s

    def __len__(self) -> int:
        return self.__nitem
