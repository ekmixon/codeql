# Incorrect: equality method defined but class contains no hash method
class Point(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'Point(%r, %r)' % (self._x, self._y)

    def __eq__(self, other):
        return (
            self._x == other._x and self._y == other._y
            if isinstance(other, Point)
            else False
        )


# Improved: equality and hash method defined (inequality method still missing)
class PointUpdated(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'Point(%r, %r)' % (self._x, self._y)

    def __eq__(self, other):
        return (
            self._x == other._x and self._y == other._y
            if isinstance(other, Point)
            else False
        )

    def __hash__(self):  
        return hash(self._x) ^ hash(self._y)

# Improved: equality method defined and class instances made unhashable
class UnhashablePoint(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'Point(%r, %r)' % (self._x, self._y)

    def __eq__(self, other):
        return (
            self._x == other._x and self._y == other._y
            if isinstance(other, Point)
            else False
        )

    #Tell the interpreter that instances of this class cannot be hashed
    __hash__ = None

