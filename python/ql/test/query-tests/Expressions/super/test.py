import sys

#Container inheriting from builtin
class MyDict(dict):
    pass

class NotMyDict(object):

    def f(self):
        super(MyDict, self).f()

#Splitting
PY2 = sys.version_info[0] == 2


class InSplit(MyDict):

    def __init__(self):
        super(InSplit, self).f()

pass
