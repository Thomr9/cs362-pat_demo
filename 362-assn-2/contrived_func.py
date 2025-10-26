import math


def contrived_func(val):

    a = val + math.sqrt(abs(val*3)) < 20
    b = val ** 5 % 3 != 0
    c = val * 5 + val / 3 > 200
    d = val ** 2 < 2

    if a or b:
        if (a and b) or (b and c) and d:
            pass
        else:
            pass
    else:
        if (a or b) or (b or c):
            pass
        else:
            pass
    
    if a and b:
        pass
    else:
        pass