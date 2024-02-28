class Node():
    def __init__(self, data, next=None) -> None:
        """
        Initializes a Node with a value and an optional link to the next node.

        Args:
            value: The value to store in the Node.
            next: Reference to the next Node (default is None).
        """
        self._data = data
        self._next = next


class LinkedList():

    def __init__(self) -> None:
        self._first = Node(None)
        self._head = self._first
        self._nitem = 0

    def append(self, item):
        """
        Appends a new node with the given data to the end of the list.

        Args:
            item: The item to be added to the list.
        """
        new_node = Node(item)
        if not self._nitem:
            self._first = new_node
        self._head._next = new_node
        self._head = new_node
        self._nitem += 1

    def delete(self, item):
        node = self._first
        if node._data == item:
            self._first = node._next
            self._nitem -= 1
        else:
            prev_node = node
            while node._next:
                if node._data == item:
                    prev_node._next = node._next
                    self._nitem -= 1
                    break
                prev_node = node
                node = node._next
            else:
                if node._data == item:
                    self._nitem -= 1
                    prev_node._next = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            A string showing the nodes in the list.
        """
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
