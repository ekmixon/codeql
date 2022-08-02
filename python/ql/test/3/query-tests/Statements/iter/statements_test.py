








#This is OK
if __name__ == "__main__":
    for _ in range(10):
        print ("Hello World")

#Iteration over string or list
def f(x):
    s = u"Hello World" if x else [ u'Hello', u'World']
    for thing in s:
        print (thing)


from enum import Enum
class Color(Enum):
     RED = 1
     GREEN = 2
     BLUE = 3

def colors():
    for color in Color:
        print(color)
    for color in 1:
        print(color)

colors()

