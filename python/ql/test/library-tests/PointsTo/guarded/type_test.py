
def f(d = {}):

    use(d)

def g(cond):

    x = 0 if cond else 1.0

    use(x)

def h(arg=int):
    use(arg)

class D(object):
    pass

class E(D):
    pass

def j(arg=E()):

    use(arg)

def k(arg=E()):

    use(arg)


def l(arg=E):
    use(arg)

def m(arg=E):
    use(arg)

number = int, float

def n(cond):
    x = 0 if cond else 1.0

    use(x)

import sys
if sys.version < "3":
    from collections import Iterable, Sequence, Set
else:
    from collections.abc import Iterable, Sequence, Set

def p():
    if issubclass(list, Iterable):
        use(0)
    else:
        use(1)

def q():
    if issubclass(list, Sequence):
        use(0)
    else:
        use(1)

def p():
    if isinstance({0}, Iterable):
        use(0)
    else:
        use(1)

def q():
    if isinstance({0}, Set):
        use(0)
    else:
        use(1)
