##!FAIL: ForbiddenMultiAssign[b]@9:0

# a : int
a = 3

# b : bool
b = True


def f(x):
    """ int -> int """
    #y : int
    y = 1
    #a : int
    a = x + 1
    return y

assert(f(1) == 1)

