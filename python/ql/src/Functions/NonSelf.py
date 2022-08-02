class Point:
    def __init__(self, x, y):  # first parameter is mis-named 'val'
        self._x = x
        self._y = y

class Point2:
    def __init__(self, x, y):  # first parameter is correctly named 'self'
        self._x = x
        self._y = y