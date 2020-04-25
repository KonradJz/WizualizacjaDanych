def fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

wynik=fib(5)
for i in range(5):
    print(next(wynik))

