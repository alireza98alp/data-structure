class node():
    def __init__(self, data, next=None) -> None:
        """
        Initializes a Node with a value and an optional link to the next node.

        Args:
            value: The value to store in the Node.
            next_node: Reference to the next Node (default is None).
        """
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

    def delete(self, item):
        pass

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
