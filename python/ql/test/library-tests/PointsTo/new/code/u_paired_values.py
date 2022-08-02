
def return_if_true(cond, val):
    if cond:
        return val
    raise Exception()

def test(cond):
    return return_if_true(True, 1) if cond else return_if_true(False, 2)

y = test(True)
y

z = test(False)
z
