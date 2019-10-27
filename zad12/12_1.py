import random
def create_list(N, k):
    return [random.randint(0, k-1) for i in range(N)]

def find_occurences(L, k):
    return [i for i, e in enumerate(L) if e == k]

k = 10
N = 20
val_to_find = random.randint(0, k-1)
print("value to fing: ", val_to_find)
L = create_list(N, k)
print("Full list: ", L)
print("Found on positions: ", find_occurences(L, val_to_find))

        



