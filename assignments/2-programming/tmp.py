par_1:tuple = ()

def largest_pair(par_1:tuple, par_2:tuple)->tuple:
    return par_2 if par_1[-1] < par_2[-1] else par_1