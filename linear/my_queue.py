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


class QueueElement:
    def __init__(self, content, queue, next=None):
        self.__content = content
        self.__queue = queue
        self.__next = next

    def __str__(self):
        return str(self.__content)

    def __repr__(self):
        return str(self.__content)

    @property
    def content(self):
        return self.__content

    @property
    def next(self):
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
        if self.__head:
            return self.__head.content

    @property
    def tail(self):
        if self.__tail:
            return self.__tail.content

    def dequeue(self):
        if self.__size == 0:
            raise EmptyQueueException
        self.__head = self.__head.next
        self.__size = self.__size - 1
        if self.__size == 0:
            self.__tail = None

    def enqueue(self, content):
        if self.__size == self.__max_size:
            raise QueueLimitReachedException
        element = QueueElement(content, self)
        if self.__size == 0:  # new element should be head
            self.__head = element
        else:
            self.__tail.next = element
        self.__tail = element
        self.__size = self.__size + 1
