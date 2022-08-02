
#AST nodes: Classes, Functions, Modules, expr, stmts

class C:

    def stmts(self, p1):
        global x
        assert x == 2
        y = 3 + 4
        while True:
            break
        while x > 0:
            x -= 1
        f()
        for x in y:
            pass
        if x:
            print(y)
        import a
        import a.b as c
        import a as b
        from a.b import c


        with open("file") as f:
            pass
        try:
            1/0
        except Exception as ex:
            del y
        finally:
            del x
        if x:
            raise Exception()
        else:
            return

    def exprs(self, p3):
        self.x = 2
        a = p3.y
        x = 1 + 2
        y = b'h4tpvhsa'
        call(arg0, arg1, name0="Hi", name1=y, *(), **{})
        x < y
        {1:1, 2: 2}

        x[a, ..., 7]
        iter(y)
        17 if x < y else 16
        lambda x : x * y
        [ 1, 2, a, x.b, p1.c ]
        [f"{a}Hi" for a in str(y)]



        #a, *b = y
        u"Hi"
        x[0]
        x[y[0]]
        (self, p3, 7)

#Some multiline strings
'''
Single quotes string'''

"""
Double-quotes
string"""

r'''
Bytes
'''

U"""
Raw
Unicode
"""

#Decorated function
@deco
def f():
    pass

#Inner function (see ODASA-1774)
def outer():
    def inner():
        pass

#Oddly laid out comprehension
[list(y) for _ in b]

#Nested binary operations
"Hello" + " " + "world"
1+2+f()
1+(2+3)

