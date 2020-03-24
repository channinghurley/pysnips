#!/usr/bin/env python3

def decorator(func):
    def wrapper():
        """This function should mirror the signature of the decoratred 
        function. It wraps the call to the decorated function, thereby allowing
        for extension of the wrapped function's functionality before and after
        the call
        """
        print("Some extra functionality prior to call of {}".format(func))
        func()
        print("Some extra functionality after call of {}\n".format(func))
    return wrapper

# Equivalent to foo = decorator(foo), then every time you call foo you're 
# really calling decorator(foo)
@decorator
def foo():
    print("foo")

def flexible_decorator(func):
    def wrapper(*args, **kwargs):
        """Defining args and kwargs for the wrapper allows us to match the 
        signature of any function passed to the decorator
        """
        print("before call of {}".format(func))
        func(*args, **kwargs)
        print("after call of {}\n".format(func))
    return wrapper

# @decorator -- This will break as the wrapper within decorator does not match
# the signature of this function, so we need a more flexible decorator
@flexible_decorator
def bar(arg):
    print("bar" + str(arg))

@flexible_decorator
def foobar(*args, **kwargs):
    print("foobar", args, kwargs)

@flexible_decorator
def foobar2(x, y, z=10):
    print(x, y, z)

foo()
bar(1)
foobar(1, 2, x=3)
foobar2(1, 2)

# Note the order here, equivalent to multi_dec = decorator(flexible_decorator(multi_dec))
@decorator
@flexible_decorator
def multi_dec():
    print("multiple decrators!")

multi_dec()