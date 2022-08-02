

def f():
    while 0:
        pass
    return 1

def g():
    while 1:
        pass
    return unreachable

def h(x):
    return x or None




def k(a, b):
    return 0

def l(a, b, c):
    return a or b or c or None

def m(a, b, c):
    return a and b and c or None