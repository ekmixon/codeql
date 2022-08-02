import sys
import six

def _f():
    assert (yield 3)
    x = [ 1 ]
    assert len(x)   #Call without side-effects
    assert sys.exit(1) #Call with side-effects
    expected_types = (Response, six.text_type, six.binary_type)
    assert isinstance(
        obj, expected_types
    ), f'obj must be {" or ".join((t.__name__ for t in expected_types))}, not {type(obj).__name__}'

def assert_tuple(x, y):
    assert False














def error_assert_true(x):
    pass

def error_assert_false(x):
    if x:
        assert False, "Bad"

def error_assert_zero(x):
    if x:
        assert 0, "Bad"

def error_assert_one(x):
    if x:
        assert 1, "Bad"

def error_assert_empty_string(x):
    if x:
        assert "", "Bad"

def error_assert_nonempty_string(x):
    if x:
        assert "X", "Bad"
    else:
        assert "X"

def ok_assert_false(x):
    if x:
        assert 0==1, "Ok"

class TestCase:
    pass

class MyTest(TestCase):
    def test_ok_assert_in_test(self, x):
        if x:
            assert False, "Ok"

def ok_assert_in_final_branch3(x):
    if foo(x):
        return
    if bar(x):
        pass
    elif not quux(x):
        assert False, "Ok"

def ok_assert_in_final_branch2(x):
    if foo(x):
        pass
    elif not bar(x):
        assert False, "Ok"

def error_assert_in_final_branch1(x):
    if not foo(x):
        assert False, "Error"

def error_assert_in_intermediate_branch(x):
    if foo(x):
        return
    if bar(x):
        pass
    elif quux(x):
        assert False, "Error"
