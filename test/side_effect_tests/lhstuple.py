#y,a: int * int
y,a = 5,6

def test_side_effect(x):
    """ int -> int """

    y,a = 1,0
    #z: int
    z = x

    return z
