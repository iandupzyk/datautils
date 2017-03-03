ALL = [
        'NoTypeError'
        , 'UnknownTypeError'
        , 'MissingCredentialsError'
    ]
 
class NoTypeError(Exception) :
    def __init__(self, message) :
        self.value = message
    def __str__(self) :
        return repr(self.value)

class UnknownTypeError(Exception) :
    def __init__(self, message) :
        self.value = message
    def __str__(self) :
        return repr(self.value)

class MissingCredentialsError(Exception) :
    def __init__(self, message) :
        self.value = message
    def __str__(self) :
        return repr(self.value)


