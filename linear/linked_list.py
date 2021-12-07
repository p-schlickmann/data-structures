"""
Pedro Schlickmann Mendes - 20200635
Estruturas de Dados - INE5609-03238A (20212)

Implementação de lista duplamente encadeada com cursor
"""


class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    """
    Two way linked list with cursor
    """

    def __init__(self):
        self.__cursor = None
        self.__head = None

    @property
    def head(self):
        return self.__head

    # cursor operations
    def __forward(self, n):
        """
        Fowards cursor n times
        """
        for _ in range(n):
            next = self.__cursor.next
            if not next:
                break
            self.__cursor = self.__cursor.next

    def __back(self, n):
        """
        Goes back with the cursor n times
        """
        for _ in range(n):
            prev = self.__cursor.prev
            if not prev:
                break
            self.__cursor = self.__cursor.prev

    def __go_to_first(self):
        """
        Sets cursor to the first element
        """
        self.__cursor = self.__head

    def __go_to_last(self):
        """
        Sets cursor to the last element
        """
        next = self.__cursor.next
        while next:
            self.__cursor = self.__cursor.next
            next = self.__cursor.next

    # public operations
    def search(self, key):
        """
        Searches for node with the passed key,
        which will be the node value in this simple example
        """
        self.__go_to_first()
        result = None
        while self.__cursor and not result:
            if self.__cursor.val == key:
                result = self.__cursor
                break
            self.__cursor = self.__cursor.next
        return result

    def get_current(self):
        """
        Returns the element that the cursor is pointing to
        """
        return self.__cursor

    def insert_before_current(self, node_val):
        """
        Inserts node before current element that the cursor is pointing to.
        After insertion cursor points to the added element.
        """
        if self.__cursor:
            node = ListNode(node_val, next=self.__cursor, prev=self.__cursor.prev)
            self.__cursor.prev = node
            if self.__cursor.prev.prev:
                self.__cursor.prev.prev.next = node
            self.__back(1)
        else:
            self.__head = self.__cursor = ListNode(node_val)

    def insert_after_current(self, node_val):
        """
        Inserts node after current element that the cursor is pointing to.
        After insertion cursor points to the added element.
        """
        if self.__cursor:
            node = ListNode(node_val, prev=self.__cursor, next=self.__cursor.next)
            self.__cursor.next = node
            if self.__cursor.next.next:
                self.__cursor.next.next.prev = node
            self.__forward(1)
        else:
            self.__head = self.__cursor = ListNode(node_val)

    def insert_at_the_end(self, node_val):
        """
        Inserts node at the end of the list
        """
        self.__go_to_last()
        self.insert_after_current(node_val)

    def insert_at_the_start(self, node_val):
        """
        Inserts node at the start of the list
        """
        self.__go_to_first()
        self.insert_before_current(node_val)
        self.__head = self.__cursor

    def insert_at(self, position, node_val):
        """
        Inserts node at the passed position
        """
        self.__go_to_first()
        self.__forward(position)
        self.insert_before_current(node_val)

    def __delete(self, node_ref):
        """
        Deletes node from list.
        Points cursor to previous node if exists.
        If previous node does not exist, point cursor to the next node.
        """
        self.__cursor = node_ref
        if not self.__cursor.prev:
            self.__cursor = self.__cursor.next
            self.__cursor.prev = None
        else:
            self.__cursor.prev.next = self.__cursor.next
            if self.__cursor.next:
                self.__cursor.next.prev = self.__cursor.prev
            self.__cursor = self.__cursor.prev

    def delete_current(self):
        """
        Deletes the node that the cursor is pointing to
        """
        if self.__cursor == self.__head:
            self.delete_first()
        elif not self.__cursor.next:
            self.delete_last()
        else:
            self.__delete(self.__cursor)

    def delete_first(self):
        """
        Deletes the first node of the list
        """
        if self.__head:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__go_to_first()

    def delete_last(self):
        """
        Deletes the last node of the list
        :return:
        """
        self.__go_to_last()
        self.__delete(self.__cursor)

    def delete(self, key):
        """
        Deletes the node found with the given key
        """
        node = self.search(key)
        self.__delete(node)

    def delete_at(self, position):
        """
        Deletes node at passed position
        """
        self.__go_to_first()
        self.__forward(position)
        self.__delete(self.__cursor)
