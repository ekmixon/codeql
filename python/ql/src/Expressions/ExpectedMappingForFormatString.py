
def unsafe_format():
    args = (1, 2, 3) if unlikely_condition() else {a:1,b:2,c:3}
    return "%(a)s %(b)s %(c)s" % args