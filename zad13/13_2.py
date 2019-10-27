# Problem ośmiu hetmanów.
# Znajdowanie jednego rozwiązania.
# Wiersze i kolumny mają zakres od 0 do N-1.


def rysuj():
    for w in range(N):
        for k in range(N):
            if x[k] == w:
                print("H", end="")
            else:
                print(".", end="")
        print("")

def dopuszczalny(w, k):
    return a[w] and b[w+k] and c[w-k]

def zapisz(w, k):
    x[k] = w
    a[w] = False
    b[w+k] = False
    c[w-k] = False

def wymaz(w, k):
    a[w] = True
    b[w+k] = True
    c[w-k] = True

def probuj(k):
    # Sprawdzanie wszystkich kandydatow (wiersze).
    for w in range(N):
        if dopuszczalny(w, k):
            zapisz(w, k)
            if k < (N-1):
                probuj(k+1)
            else:
                rysuj()
                print("================================")
            wymaz(w, k)
    

for N in range(3, 9):
    print("Szachownica ", N, "x", N)
    #N = 8  # bok szachownicy i jednocześnie liczba hetmanów
    
    # x[i] to pozycja hetmana w kolumnie i
    x = N * [None]
    
    # a[j] == True to brak hetmana w wierszu j
    a = N * [True]
    
    # b[k] == True to brak hetmana na przekątnej k [/].
    # Suma wiersz+kolumna od 0 do (2N-2).
    b = (2*N-1) * [True]
    
    # c[k] == True to brak hetmana na przekątnej k [\].
    # Różnica wiersz-kolumna od (-N+1) do (N-1).
    c = (2*N-1) * [True]
   
    probuj(0)
