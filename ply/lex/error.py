# Exception thrown when invalid token encountered and no default error
# handler is defined.

class LexError(Exception):
    def __init__(self, message, text):
        super(LexError, self).__init__(message)

        self.__text = text

    @property
    def text(self):
        return self.__text
