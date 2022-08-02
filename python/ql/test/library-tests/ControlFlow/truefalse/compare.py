
def contains1(item, cont):
    assert item in cont
    return 1

def contains2(item, cont):
    assert item not in cont
    return 2

def contains3(item, cont):
    return 3 if item in cont else 3.0

def contains4(item, cont):
    return 4 if item not in cont else 4.0
