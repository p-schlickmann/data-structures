"""
Pedro Schlickmann Mendes - 20200635
Estruturas de Dados - INE5609-03238A (20212)

Implementação de fila em python com
encadeamento e alocação dinâmica de memória
"""


class EmptyQueueException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class QueueLimitReachedException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProtectedElementException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class QueueElement:
    def __init__(self, content, queue, next=None, is_tail=False, is_head=False):
        self.__content = content
        self.__queue = queue
        self.__next = next
        self.__is_head = is_head
        self.__is_tail = is_tail

    def __str__(self):
        return str(self.__content)

    def __repr__(self):
        return str(self.__content)

    @property
    def is_head(self):
        return self.__is_head

    @is_head.setter
    def is_head(self, is_head):
        self.__is_head = is_head

    @property
    def is_tail(self):
        return self.__is_tail

    @is_tail.setter
    def is_tail(self, is_tail):
        self.__is_tail = is_tail

    @property
    def content(self):
        return self.__content

    @property
    def next(self):
        if not self.__is_head and not self.__is_tail:
            raise ProtectedElementException
        return self.__next

    @next.setter
    def next(self, element):
        self.__next = element

    @property
    def queue(self):
        return self.__queue

    @queue.setter
    def queue(self, new_queue):
        self.__queue = new_queue


class Queue:
    def __init__(self, max_size=None):
        self.__max_size = max_size
        self.__size = 0
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def dequeue(self):
        if self.__size == 0:
            raise EmptyQueueException
        self.__head.queue = None
        self.__head = self.__head.next
        if self.__head is not None:
            self.__head.is_head = True
        self.__size = self.__size - 1
        if self.__size == 0:
            self.__tail = None

    def enqueue(self, content):
        if self.__size == self.__max_size:
            raise QueueLimitReachedException
        if self.__tail:
            self.__tail.is_tail = False
        new_element_should_be_head = self.__size == 0
        element = QueueElement(content, self, None, is_tail=True, is_head=new_element_should_be_head)
        if new_element_should_be_head:
            self.__head = element
        else:
            self.__tail.next = element
            self.__tail.is_tail = False
        self.__tail = element
        self.__size = self.__size + 1
