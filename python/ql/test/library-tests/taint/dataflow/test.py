
def test1():
    SINK(SOURCE)

def test2():
    s = SOURCE
    SINK(s)

def source():
    return SOURCE

def sink(arg):
    SINK(arg)

def test3():
    t = source()
    SINK(t)

def test4():
    t = SOURCE
    sink(t)

def test5():
    t = source()
    sink(t)

def test6(cond):
    if cond:
        t = "Safe"
        SINK(t)
    else:
        t = SOURCE

def test7(cond):
    if cond:
        t = SOURCE
        SINK(t)
    else:
        t = "Safe"

def source2(arg):
    return source(arg)

def sink2(arg):
    sink(arg)

def sink3(cond, arg):
    if cond:
        sink(arg)

def test8(cond):
    t = source2()
    sink2(t)

#False positive
def test9(cond):
    t = "Safe" if cond else SOURCE
    sink3(cond, t)

def test10(cond):
    t = SOURCE if cond else "Safe"
    sink3(cond, t)

def hub(arg):
    return arg

def test11():
    t = SOURCE
    t = hub(t)
    SINK(t)

def test12():
    t = "safe"
    t = hub(t)
    SINK(t)

import module

def test13():
    t = module.dangerous
    SINK(t)

def test14():
    t = module.safe
    SINK(t)

def test15():
    t = module.safe2
    SINK(t)

def test16():
    t = module.dangerous_func()
    SINK(t)


def test20(cond):
    if cond:
        t = CUSTOM_SOURCE
        CUSTOM_SINK(t)
    else:
        t = SOURCE
        SINK(t)

def test21(cond):
    t = CUSTOM_SOURCE if cond else SOURCE
    if not cond:
        CUSTOM_SINK(t)
    else:
        SINK(t)

def test22(cond):
    t = CUSTOM_SOURCE if cond else SOURCE
    t = TAINT_FROM_ARG(t)
    if cond:
        CUSTOM_SINK(t)
    else:
        SINK(t)

from module import dangerous as unsafe
SINK(unsafe)

def test23():
    with SOURCE as t:
        SINK(t)

def test24():
    s = SOURCE
    SANITIZE(s)
    SINK(s)

def test_update_extend(x, y):
    l = [SOURCE]
    d = {"key" : SOURCE}
    x.extend(l)
    y.update(d)
    SINK(x[0])
    SINK(y["key"])
    l2 = list(l)
    d2 = dict(d)

def test_truth():
    t = SOURCE
    SINK(t)
    SINK(t)

