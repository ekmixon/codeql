


def f(x):
    return 1 if x else None
    
def g(x, y):
    return f(y) if x else 0.7
    
def h(a, b, c, d):
    t = f(a)
    v = g(b, c)
    return t if d else v
    
h(1,2,3,4)

def not_none(a, b):
    if a:
        return True
    elif b:
        return False
    #No fall through
    raise Exception()

def gen():
    yield 0
