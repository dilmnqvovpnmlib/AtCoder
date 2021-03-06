from math import factorial

def permutations_count(n, r):
    ''' 順列 '''
    return factorial(n) // factorial(n - r)

def combinations_count(n, r):
    ''' 組み合わせ '''
    return factorial(n) // (factorial(n - r) * factorial(r))
