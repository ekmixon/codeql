
from somwhere import may_raise, value, SomeException

def f(cond1, cond2):
    try:
        may_raise()
        var = value()
    except Exception:
        if cond2:
            var = 7
    if var == 1:
        var = var + 1
    elif var == 2:
        var +- 3
    var = var + 4 # var must be defined to have passed line 11
