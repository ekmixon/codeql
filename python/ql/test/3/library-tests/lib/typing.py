#Fake typing module for testing.

class ComplexMetaclass(type):

    def __new__(cls):
        pass

class ComplexBaseClass(metaclass=ComplexMetaclass):

    def __new__(cls):
        pass

class _Optional(ComplexBaseClass, extras=...):

    def __new__(cls):
        pass

Optional = _Optional("Optional")

class Collections(ComplexBaseClass, extras=...):
    pass

class Set(Collections):
    pass

class List(Collections):
    pass

Optional
