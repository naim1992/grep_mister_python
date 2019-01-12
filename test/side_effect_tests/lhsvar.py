# b : int
b = 0

def test(y):
    """ int -> int """
    #x : int
    x = 1
    #b : int
    b = x + 1
    return x

assert (test(1) == 1)
assert (b == 0)
