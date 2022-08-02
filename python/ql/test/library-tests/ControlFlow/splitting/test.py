
def split1(cond):
    pass

def dont_split1(cond):
    cond = f()

def dont_split2(cond):
    pass


def split2():
    try:
        call()
        x = True
    except:
        x = False

def unclear_split3():
    try: # May be arguably better to split here.
        call()
        x = True
    except:
        x = False
    if cond: # Currently split here 
        x = False

def split4(x):
    if x is None:
        x = not_none()
    c if b else c
    return x

def split_carefully_5(x):
    if x is None:
        x = not_none()
    return x


def dont_split_globals():
    call_could_alter_any_global()

def limit_splitting1(a,b,c,d):
    if a is None: a = "a"
    if b is None: b = "b"
    if c is None: c = "c"
    if d is None: d = "d"







def limit_splitting2(a,b,c,d):
    #These should be pruned
    if a:
        a1
    if b:
        b1
    #But not these
    if c:
        c1
    if d:
        d1

def split_on_numbers():
    try:
        call()
        x = -1
    except:
        x = 0

def split_try_except_else():
    try:
        call()
    except:
        x = 0
    else:
        x = 1

#Example taken from logging module
#Splitting should allow us to deduce that module2 is defined at point of use
def logging():
    try:
        import module1
        import module2

    except ImportError:
        module1 = None

    if module1:
        inst = module2.Class()

#Handle 'not' as well.
def split5():
    try:
        call()
        x = True
    except:
        x = False

def split6():
    try:
        call()
        x = True
    except:
        x = False

def split7():
    try:
        call()
        x = not True
    except:
        x = not False

def split8(cond):
    t = bool(cond)


def split9(var):
    if var is None:
        a1
        b2
    else:
        a2
        b1

def split10(var):
    if var:
        a1
    else:
        a2
    if var is not None:
        b1
    else:
        b2

def split11(var):
    if var is None:
        a1
    else:
        a2
    if var:
        b1
    else:
        b2

def dont_split_on_unrelated_variables(var1, var2):
    if var1 is None:
        a1
    else:
        a2
    if var2 is not None:
        b1
    else:
        b2

def split12():
    try:
        call()
        x = None
    except:
        import x

def split13():
    var = cond()
    if var:
        a1
    else:
        a2
    try:
        b1
    finally:
        if var:
            a3


def split14():
    flag = False
    try:
        x = something()
    except Exception:
        99
        flag = True

def split15(var):
    if var:
        other = 0

def split16():
    x = None if cond else True
    if x:
        use(x)

def dont_split_on_different_ssa(var):
    if var:
        a1
    else:
        a2
    var = func()
    if var is not None:
        b1
    else:
        b2

def split17(var):
    if var:
        a1
        b2
        c1
        d1
        e1
    else:
        a2
        b1
        c2
        d2
        e2

def split18(var):
    #Should only be split once
    if var:
        a1
    else:
        a2
    if var is None:
        b2
        c1
    else:
        b1
        c2
    if var:
        d1
        e1
    else:
        d2
        e2

def split_on_boolean_only(x):
    if x:
        a1
    else:
        a2
    if x is not None:
        b1
    else:
        b2
    if x:
        c1
    else:
        c2

def split_on_none_aswell(x):
    if x:
        a1
    else:
        a2
    if x is None:
        b2
        c1
    else:
        b1
        c2

def split_on_or_defn(var):
    if var:
        obj = thing()
    if not var or obj.attr: # obj is defined if reached
        x

def split_on_exception():
    flag = False
    try:
        x = do_something()
    except Exception:
        flag = True
    if not flag:
        x # x is defined here

def partially_useful_split(cond):
    x = None if cond else something_or_none()
    other_stuff()
    if x:
        a1
    else:
        a2

def dont_split_not_useful(cond, y):
    x = None if cond else something_or_none()
    other_stuff()
    if y:
        a1
    else:
        a2

#Splittings with boolean expressions:
def f(x,y):
    if x and y:
        raise
    if not (x or y):
        raise

def g(x,y):
    if x and y:
        raise
    if x or y:
        # Either x or y is true here (exclusive).
        here
    end

def h(x, y):
    if (
        (x and
         not y) or
        (x and
         y.meth())
        ):
        pass

def j(a, b):
    if a:
        here
    elif b:
        there

def split_on_strings():
    try:
        might_fail()
        x = "yes+"
    except:
        x = "no"


def scipy_stylee(x):
    assert x in ("a", "b", "c")

def odasa_6674(x):
    valid = True
    if dont_understand_this():
        try:
            may_raise()
            score = 0
        except KeyError:
            valid = False
        if not valid:
            raise ValueError()
    else:
        score = 1
    return score

def odasa_6625(k):
    value = 0 if k.endswith('_min') or k.endswith('_max') else "hi"
    if k == 'tags':
        return f"{value} there"


def avoid_redundant_split(a):
    x = unknown_thing() if a else None
    other_stuff()
    try: # we want to split here
        import foo
        var = True
    except:
        var = False
    if var:
        foo.bar()


