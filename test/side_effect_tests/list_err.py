#h : List[int]
h = [1,2,3]
def side_effect_list():
    """ -> NoneType """
    # h : List[int]
    h[0] = 5
    
    #r: set[int]
    r = {1}
    r.add(1)
    r.add(5)
    r.remove(0)

    # h : list[int]
    h.append(4)
    

