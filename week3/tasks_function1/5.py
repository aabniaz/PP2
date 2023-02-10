import itertools 
def per(st): 
    perm = itertools.permutations(st) 
    for i in perm: 
        print(i) 
s = str(input()) 
per(s) 
