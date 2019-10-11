#from 11_1 import *
import numpy as np

def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item

def quicksort(L, left, right, compare_function=None):
    """Sortowanie szybkie wg Cormena str. 169."""
    if left >= right:
        return
    pivot = partition(L, left, right, compare_function)
    # pivot jest na swoim miejscu.
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

def partition(L, left, right, compare_function=None):
    """Zwraca indeks elementu rozdzielającego."""
    # Element rozdzielający to ostatni z prawej,
    # dlatego na końcu trzeba go przerzucić do środka.
    # Będzie on na docelowej pozycji ze względu na sortowanie.
    x = L[right]   # element rozdzielający
    i = left

    for j in range(left, right):
        do_swap = False
        if compare_function is None:
            do_swap = L[j] <= x
        else:
            do_swap = compare_function(L[j], x)
        if do_swap:
            swap(L, i, j)
            i += 1
    swap(L, i, right)
    return i

def compare(v1, v2):
    return v1 <= v2

not_sorted_array = np.random.random(10)

quicksort(not_sorted_array, 0, 9)
print(not_sorted_array)

not_sorted_array = np.random.random(10)

quicksort(not_sorted_array, 0, 9, compare)
print(not_sorted_array)

