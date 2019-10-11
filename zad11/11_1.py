import numpy as np
import random

def random_numbers(N):
    return list(np.random.random(N))

def swap_in_list(temp):
    pos = random.randint(0, len(temp)-2)
    temp[pos], temp[pos+1] = temp[pos + 1], temp[pos]
    return temp

def almost_random(N):
    temp = np.arange(N)
    return swap_in_list(temp)

def almost_random_reverse(N):
    temp = np.arange(N-1, 0, -1)
    return list(swap_in_list(temp))

def random_floats_gaussian(N):
    return np.random.normal(size=N)

