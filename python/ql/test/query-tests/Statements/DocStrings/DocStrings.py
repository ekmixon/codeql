#Modules should have docstrings

class OK:
    'Classes need doc strings'

    'Two strings'
    pass
    "Another string"
#All functions must be multi-line or there are ignored by the query


class _OK:
    'Unless they are private'
    pass
    pass

def f_ok(x, y):
    'And functions'
    pass

def _f_ok(y, z):
    pass

class OK2:
    'doc-string'

    def meth_ok(self):
        'Methods need docstrings'
        pass

    def _meth_ok(self):
        pass

class Not_OK:
    #No docstring

    def meth_ok(self):
        'Methods need docstrings'
        pass

    def meth_not_ok(self):
        pass

def not_ok(x, y):
    pass



