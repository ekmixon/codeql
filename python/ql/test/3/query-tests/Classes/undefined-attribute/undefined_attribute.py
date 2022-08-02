
#Defined in metaclass
class Meta(type):
    def __init__(self, name, bases, dct):
        type.__init__(self, name, bases, dct)
        self.defined_in_meta = 1

class HasMeta(object, metaclass=Meta):  
    def ok5(self):
        return self.defined_in_meta
