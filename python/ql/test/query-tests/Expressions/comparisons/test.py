

def f(w, x, y, z):
    if x < 0 or z < 0:
        raise Exception()
    y += 1
    if z >= 0: # Useless test due to z < 0 being false 
        y += 1
    while w >= 0:
        if y < 10:
            z += 1
            if y == 15: # Useless test due to y < 10 being true
                z += 1
        elif y > 7: # Useless test 
            y -= 1
    if y < 10:
        y += 1
    if y == 5 and z > 0:
        w = 0 if y < 3 else 1 #Useless test as y is 5

def g(w, x, y, z):
    if w < x or y < z+2:
        raise Exception()
    if cond and z > y - 2 or not cond and z >= y - 2: # Useless test due to y < z+2 being false 
        y += 1

#ODASA-5643
def validate_series(start, end):
    # Check that the values 'make sense'
    if end < start:
        raise click.BadParameter('The start value must be less than the end value.')
    if start == end:
        raise click.BadParameter('The start value and the end value most not be the same.')
    return start, end

#Overflow
def medium1(x, y):
    if x + 1000000000000000 > y + 1000000000000000:
        return

def medium2(x, y):
    if x + 1000000000000000 > y + 1000000000000001:
        return

def big1(x, y):
    if x + 10000000000000000 > y + 10000000000000000:
        return

def big2(x, y):
    if x + 10000000000000000 > y + 10000000000000001:
        return

def odasa6782_v1(protocol):
    if protocol < 0:
        protocol = HIGHEST_PROTOCOL

def odasa6782_v2(protocol):
    if protocol < 0:
        protocol = HIGHEST_PROTOCOL
    elif not 0 <= protocol <= HIGHEST_PROTOCOL:
        raise ValueError()

def odasa6782_v3(protocol):
    if protocol < 0:
        protocol = HIGHEST_PROTOCOL
    elif not 0 <= protocol <= HIGHEST_PROTOCOL:
        raise ValueError()

#Inverted complex test
pass

