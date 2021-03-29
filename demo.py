def linear_congruence(x):
    value = (22695477*(x)+1)%(2**32)
    if value > 2**31: comp_move = 1
    else: comp_move = 0
    return comp_move, value