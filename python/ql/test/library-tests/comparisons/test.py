
def simple_tests(x):
    pass

def f(w, x, y, z):
    if x < 0 or z < 0:
        raise Exception()
    y += 1
    if z >= 0: # Useless test due to z < 0 being false 
        y += 1
    while w >= 0:
        if y < 7:
            z += 1
            if y == 15: # Useless test due to y < 10 being true
                z += 1
        elif y > 10:
            y -= 1
    if y < 10:
        y += 1
    if y == 5 and z > 0:
        w = 0 if y < 3 else 1 #Useless test as y is 5

def simple_tests2(x, y):
    pass

def g(w, x, y, z):
    if (w < x or 
        y < z+2):
        raise Exception()
    if z > y-2: # Useless test due to y < z+2 being false 
        y += 1

#Complex things we can't analyse
def h(a,b,c,d):
    if a < b - g(c):
        pass
    if a(c) < b(d):
        pass
    if a > 20 - g(c):
        pass
    if a + 10 > g(c):
        pass


#ODASA-5643
def validate_series(start, end):
    if end < start:
        raise error()
    if start == end:
        raise error()
    return start, end

def big1(x, y):
    if x + 10000000000000000 > y + 10000000000000001:
        return

def big2(x, y):
    if x + 10000000000000000 > y + 10000000000000001:
        return
