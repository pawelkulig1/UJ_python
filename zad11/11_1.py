import random

def random_numbers(N):
    temp = [i for i in range(N)]
    random.shuffle(temp)
    return temp

def swap_in_list(temp):
    pos = random.randint(0, len(temp)-2)
    temp[pos], temp[pos+1] = temp[pos + 1], temp[pos]
    return temp

def almost_sorted(N):
    temp = [i for i in range(N)]
    return swap_in_list(temp)

def almost_sorted_reverse(N):
    temp = [i for i in range(N, 0, -1)]
    return list(swap_in_list(temp))

def random_floats_gaussian(N):
    return [random.gauss(1, 3) for i in range(N)]

def random_repeating_k(N, k=4):
    #k = random.randint(1, N-1)
    temp = [i%k for i in range(N)]
    random.shuffle(temp)
    return temp


#tests:
print(random_numbers(10))
print(almost_sorted(10))
print(almost_sorted_reverse(10))
print(random_floats_gaussian(10))
print(random_repeating_k(10))



