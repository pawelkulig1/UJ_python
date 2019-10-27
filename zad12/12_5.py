import numpy as np
from collections import defaultdict

def moda_py(L):#, left, right): - nie widze sensu
    dictionary = defaultdict(int)
    max_count = 0
    max_val = None

    for l in L:
        dictionary[l] += 1
        if dictionary[l] >= max_count:
            max_count = dictionary[l]
            max_val = l

    return max_val

L = list(np.random.randint(0, 10, size=10))
print(L)
print(moda_py(L))

