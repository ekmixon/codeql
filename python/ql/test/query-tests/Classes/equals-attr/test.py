
class GenericEquality(object):

    def __eq__(self, other):
        if type(other) is not type(self):
            return False
        return all(
            getattr(other, attr) == getattr(self, attr) for attr in self.__dict__
        )


class AddAttributes(GenericEquality):

    def __init__(self, args):
        self.a, self.b = args
