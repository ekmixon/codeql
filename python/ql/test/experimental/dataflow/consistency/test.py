# This is currently a copy of the integration tests.
# It should contain many syntactic constructs, so should
# perhaps be taken from coverage once that is done.
# (We might even put the consistency check in there.)

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

def test_early_exit():
    if t := FALSEY:
        t
    else:
        return

def flow_through_type_test_if_no_class():
    t = SOURCE
    SINK(t)

def flow_in_iteration():
    t = ITERABLE_SOURCE
    for i in t:
        i
    return i

def flow_in_generator():
    yield from [SOURCE]

def flow_from_generator():
    for x in flow_in_generator():
        SINK(x)

def const_eq_clears_taint():
    tainted = SOURCE
    if tainted == "safe":
        SINK(tainted) # safe
    SINK(tainted) # unsafe

def const_eq_clears_taint2():
    tainted = SOURCE
    if tainted != "safe":
        return
    SINK(tainted) # safe

def non_const_eq_preserves_taint(x):
    tainted = SOURCE
    if tainted == tainted:
        SINK(tainted) # unsafe
    if tainted == x:
        SINK(tainted) # unsafe

def overflowCallee(*args, p="", **kwargs):
    print("args", args)
    print("p", p)
    print("kwargs", kwargs)

def synth_arg_posOverflow():
    overflowCallee(42)

def synth_arg_kwOverflow():
    overflowCallee(foo=42)

def synth_arg_kwUnpacked():
    overflowCallee(**{"p": "42"})

def split_lambda(cond):
    foo = lambda x: False
