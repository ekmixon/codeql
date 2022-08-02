
#OK
a = b = 1
a == b
a.x == b.x

#Same variables
True
a.x == a.x

#Compare constants
True
1 == 2

#Maybe missing self
class X(object):
    
    def __init__(self, x):
        self.x = x
        
    def missing_self(self, x):
        if x == x:
            print ("Yes")

#Compare constants in assert -- ok
pass
