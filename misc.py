----------------------------------------
----------- FIBONACCI -----------------
----------------------------------------

def fib_bad(n):
    # O(n!) time
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib(n):
    # O(n) time, i.e. polynomial time
    if n == 0:
        return 0
    if n == 1:
        return 1
    grandparent = 0
    parent = 1
    current = 1
    for i in range(1,n):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current

----------------------------------------
----------- EXPONENTIAL GROWTH -----------------
----------------------------------------


def exponential_growth(n, factor, days):
    # initial value n grows by factor every day for days
    # O(n) for days input (i.e. O(days), it's confusing to use n for initial input when that's not the thing used for big O)
    growth_sequence = [n]
    
    for i in range(1, days+1):
        print(f"n: {n}, factor: {factor}, day: {i}")
        growth_sequence.append(n*(factor**i))
    return growth_sequence
