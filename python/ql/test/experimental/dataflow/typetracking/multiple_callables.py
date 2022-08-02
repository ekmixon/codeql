def foo(foo_x):  # $tracked
    print("foo", foo_x)  # $tracked


def bar(bar_x):  # $tracked
    print("bar", bar_x)  # $tracked


f = foo if len(__file__) % 2 == 0 else bar
x = tracked  # $tracked
f(x)  # $tracked
