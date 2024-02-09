from array_1 import array


class orderedarray(array):
    def __find(self, item):
        low = 0
        high = self._nitem-1
        while low <= high:
            mid = (low+high)//2
            if self._arr[mid] == item:
                return mid
            elif self._arr[mid] < item:
                low = mid+1
            else:
                high = mid-1
        return low

    def append(self, item):
        if self._nitem == self.maxsize:
            raise ValueError('array is full')
        index = self.__find(item)
        self._nitem += 1
        for i in range(self._nitem, index, -1):
            self._arr[i] = self._arr[i-1]
        self._arr[index] = item


a1 = orderedarray(11)
for i in range(1, 9):
    a1.append(2**i)
a1.append(100)
print(a1)
