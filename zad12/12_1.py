import random
def create_list(N, k):
    L = []
    for i in range(N):
        L.append(random.randint(0, k-1))

    return L

def find_occurences(L, k):
    positions = []
    for i, el in enumerate(L):
        if el == k:
            positions.append(i)

    return positions

k = 10
N = 20
val_to_find = 3
L = create_list(N, k)
print(L)
print(find_occurences(L, val_to_find))

        



