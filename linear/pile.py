"""
Pedro Schlickmann Mendes - 20200635
Estruturas de Dados - INE5609-03238A (20212)

Implementação de pilha em python com
encadeamento e alocação dinâmica de memória
"""


class EmptyPileException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PileLimitReachedException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProtectedElementException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PileElement:
    def __init__(self, content, pile, previous=None, is_top=False):
        self.__content = content
        self.__pile = pile
        self.__previous = previous
        self.__is_top = is_top

    def __str__(self):
        return str(self.__content)

    def __repr__(self):
        return str(self.__content)

    @property
    def is_top(self):
        return self.__is_top

    @is_top.setter
    def is_top(self, is_top):
        self.__is_top = is_top

    @property
    def content(self):
        return self.__content

    @property
    def previous(self):
        if not self.__is_top:
            raise ProtectedElementException
        return self.__previous

    @previous.setter
    def previous(self, element):
        self.__previous = element

    @property
    def pile(self):
        return self.__pile

    @pile.setter
    def pile(self, new_pile):
        self.__pile = new_pile


class Pile:
    def __init__(self, max_size=None):
        self.__max_size = max_size
        self.__size = 0
        self.__top = None

    @property
    def top(self):
        return self.__top

    def pop(self):
        if self.__size == 0:
            raise EmptyPileException
        self.__top.pile = None
        self.__top = self.__top.previous
        if self.__top is not None:
            self.__top.is_top = True
        self.__size = self.__size - 1

    def push(self, content):
        if self.__size == self.__max_size:
            raise PileLimitReachedException
        if self.__top:
            self.__top.is_top = False
        element = PileElement(content, self, self.__top, is_top=True)
        self.__top = element
        self.__size = self.__size + 1
