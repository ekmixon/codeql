# valid class with return inside a function
class ValidClass1(object):
    def class_method(self):
        return False

# valid class with yield inside a function
class ValidClass2(object):
    def class_method(self):
        yield 1

# valid class with yield from inside a function
class ValidClass3(object):
    def class_method(self):
        yield from [1, 2]

# valid function with the return statement
def valid_func1():
    return True

# valid function with the yield statement
def valid_func2():
    yield 1

# valid function with the yield from statement
def valid_func3():
    yield from [1, 2]

# invalid class with return outside a function
class InvalidClass1(object):
    pass



class InvalidClass2(object):
    while True:
        pass




class InvalidClass3(object):
    while True:
        pass


# invalid statement with yield from outside a function
var = [1,2,3]