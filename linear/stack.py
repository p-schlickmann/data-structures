"""
Pedro Schlickmann Mendes - 20200635
Estruturas de Dados - INE5609-03238A (20212)

Implementação de pilha em python com
encadeamento e alocação dinâmica de memória
"""


class EmptyStackException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StackLimitReachedException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StackElement:
    def __init__(self, content, stack, previous=None):
        self.__content = content
        self.__stack = stack
        self.__previous = previous

    def __str__(self):
        return str(self.__content)

    def __repr__(self):
        return str(self.__content)

    @property
    def content(self):
        return self.__content

    @property
    def previous(self):
        return self.__previous


class Stack:
    def __init__(self, max_size=None):
        self.__max_size = max_size
        self.__size = 0
        self.__top = None

    @property
    def top(self):
        if self.__top:
            return self.__top.content

    def pop(self):
        if self.__size == 0:
            raise EmptyStackException
        self.__top = self.__top.previous
        self.__size = self.__size - 1

    def push(self, content):
        if self.__size == self.__max_size:
            raise StackLimitReachedException
        element = StackElement(content, self, self.__top)
        self.__top = element
        self.__size = self.__size + 1
