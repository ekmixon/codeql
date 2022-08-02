#-*- coding: utf-8 -*-

class Point(object):

    def __init__(self, x, y):
        self.x
        self.y

    def __add__(self, other):
        return (
            Point(self.x + other.x, self.y + other.y)
            if isinstance(other, Point)
            else NotImplemented
        )

    def __str__(self, style): #Spurious extra parameter
        if style == 'polar':
            u"%s @ %s\u00b0" % (abs(self), self.angle())
        else:
            return f"[{self.x}, {self.y}]"
