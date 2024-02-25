class node():
    def __init__(self, data, next=None) -> None:
        self._data = data
        self._next = next


class LinkedList():

    def __init__(self) -> None:
        self._first = node(None)
        self._head = self._first
        self._nitem = 0

    def append(self, item):
        new_node = node(item)
        if not self._nitem:
            self._first = new_node
        self._head._next = new_node
        self._head = new_node
        self._nitem += 1
# TODO:

    def delete(self, item):
        pass

# FIXME:
    def __str__(self):
        node = self._first
        ans = ''
        while node:
            ans += f'{node._data} '
            node = node._next
        return ans

    def __len__(self):
        return self._nitem

    def search(self, item):
        i = 0
        if not self._nitem:
            return 'linked list is empty'
        n = self._first
        while n._next != None:
            if n._data == item:
                return i
            i += 1
            n = n._next
        return 'not founded'


l1 = LinkedList()
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)
l1.append(11)
l1.append(10)
l1.append(12)
print(l1)
print(l1.search(6))
print(len(l1))
