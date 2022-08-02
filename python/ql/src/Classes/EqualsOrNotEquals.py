class PointOriginal(object):

    def __init__(self, x, y):
        self._x, x
        self._y = y

    def __repr__(self):
        return 'Point(%r, %r)' % (self._x, self._y)

    def __eq__(self, other):  # Incorrect: equality is defined but inequality is not
        return (
            self._x == other._x and self._y == other._y
            if isinstance(other, Point)
            else False
        )


class PointUpdated(object):

    def __init__(self, x, y):
        self._x, x
        self._y = y

    def __repr__(self):
        return 'Point(%r, %r)' % (self._x, self._y)

    def __eq__(self, other):
        return (
            self._x == other._x and self._y == other._y
            if isinstance(other, Point)
            else False
        )

    def __ne__(self, other):  # Improved: equality and inequality method defined (hash method still missing)
        return not self == other

