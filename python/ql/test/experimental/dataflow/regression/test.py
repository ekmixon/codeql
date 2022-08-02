
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
        SINK_F(t)
    else:
        t = SOURCE

def test7(cond):
    if cond:
        t = SOURCE
        SINK(t)
    else:
        t = "Safe"

def source2():
    return source()

def sink2(arg):
    sink(arg)

def sink3(cond, arg):
    if cond:
        sink(arg)

def test8(cond):  # This test currently adds nothing, as we only track SOURCE -> SINK, and previous tests already add flow from line 10 to line 13
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
    SINK_F(t)

import module

def test13():
    t = module.dangerous
    SINK(t)

def test14():
    t = module.safe
    SINK_F(t)

def test15():
    t = module.safe2
    SINK_F(t)

def test16():
    t = module.dangerous_func()
    SINK(t)

class C(object): pass

def x_sink(arg):
    SINK(arg.x)

def test17():
    t = C()
    t.x = module.dangerous
    SINK(t.x)

def test18():
    t = C()
    t.x = module.dangerous
    t = hub(t)
    x_sink(t)

def test19():
    t = CUSTOM_SOURCE
    t = hub(TAINT_FROM_ARG(t))
    CUSTOM_SINK(t)

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
        CUSTOM_SINK_F(t)
    else:
        SINK_F(t)

def test22(cond):
    t = CUSTOM_SOURCE if cond else SOURCE
    t = TAINT_FROM_ARG(t)  # Blocks data flow
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
    SANITIZE(s)  # Does not block data flow
    SINK_F(s)

def test_update_extend(x, y):
    l = [SOURCE]
    d = {"key" : SOURCE}
    x.extend(l)
    y.update(d)
    SINK(x[0])  # Flow not found
    SINK(y["key"])  # Flow not found
    l2 = list(l)
    d2 = dict(d)

def test_truth():
    t = SOURCE
    if t:
        SINK(t)
    else:
        SINK_F(t)  # False positive
    if not t:
        SINK_F(t)  # False positive
    else:
        SINK(t)

def test_early_exit():
    if t := FALSEY:
        t
    else:
        return

def flow_through_type_test_if_no_class():
    t = SOURCE
    SINK(t)  # Flows's both here..

def flow_in_iteration():
    t = [SOURCE]
    for i in t:
        SINK(i)
    SINK(i)

def flow_in_generator():
    yield from [SOURCE]

def flow_from_generator():
    for x in flow_in_generator():
        SINK(x)  # Flow not found
