def f_linear(x):
    return x

def one_branch(x):
    return 1 if x else 2

def two_branch(x, y):
    y += 1 if x else 2
    return 1 if y else 2


def nested(x, y):
    if x:
        return 0 if y else 1
    else:
        return 2 if y else 3

def exceptions(x, y):
    try:
        x.attr
        x + y
        x[y]
        read()
    except IOError:
        pass

#ODASA-5114
def must_be_positive(self, obj, value):
    try:
        return int(value)
    except:
        self.error(obj, value)
