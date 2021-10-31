class EmptyPileException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PileLimitReachedException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Pile:
    def __init__(self, size=None):
        self.size = size
        self.__data = []

    def is_empty(self):
        return len(self.__data) > 0

    def top(self):
        if self.is_empty():
            raise EmptyPileException()
        return self.__data[len(self.__data) - 1]

    def push(self, element):
        if self.size and len(self.__data) >= self.size:
            raise PileLimitReachedException()
        self.__data = self.__data.append(element)

    def pop(self):
        if self.is_empty():
            raise EmptyPileException()
        return self.__data.pop()
