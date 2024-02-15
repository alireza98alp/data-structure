from array_ import Array


class OrderedArray(Array):
    def __contains__(self, item: int):
        if not self._arr[0] < item < self._arr[self._nitem-1]:
            return False
        else:
            low = 1
            high = self._nitem-1
            while low < high:
                mid = (low + high)//2
                if self._arr[mid] == item:
                    return True
                elif self._arr[mid] < item:
                    low = mid+1
                else:
                    high = mid-1
            return self._arr[mid] == item

    def __find(self, item: int):
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

    def append(self, item: int):
        if self._nitem == self.maxsize:
            raise Exception('array is full')
        index = self.__find(item)
        for i in range(self._nitem, index, -1):
            self._arr[i] = self._arr[i-1]
        self._nitem += 1
        self._arr[index] = item

    def delete(self, item: int):
        index = self.__find(item)
        self._nitem -= 1
        for i in range(index, self._nitem):
            self._arr[i] = self._arr[i+1]
