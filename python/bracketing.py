from math import sqrt


def bracket_minmimum(f, x=0, s=1e-2, k=2.0):
    a, ya = x, f(x)
    b, yb = a + s, f(a + s)
    if yb > ya:
        a, b = b, a
        ya, yb = yb, ya
        s = -s

    while True:
        c, yc = b + s, f(b + s)
        if yc > yb:
            return (a, c) if a < c else (c, a)
        a, ya, b, yb = b, yb, c, yc
        s *= k


φ = (1 + sqrt(5)) / 2


def fibonacci_search(f, a, b, n, ϵ=0.02):
    s = (1 - sqrt(5)) / (1 + sqrt(5))
    ρ = 1 / (φ * (1 - s**(n + 1)) / (1 - s**n))
    d = ρ * b + (1 - ρ) * a
    yd = f(d)
    for i in range(1, n):
        if i == n - 1:
            c = ϵ * a + (1 - ϵ) * d
        else:
            c = ρ * a + (1 - ρ) * b
        yc = f(c)
        if yc < yd:
            b, d, yd = d, c, yc
        else:
            a, b = b, c
        ρ = 1 / (φ * (1 - s**(n - i + 1)) / (1 - s**(n - i)))
    return (a, b) if a < b else (b, a)


def golden_section_search(f, a, b, n):
    ρ = φ-1
    d = ρ * b + (1 - ρ) * a
    yd = f(d)
    for i in range(1, n):
        c = ρ * a + (1 - ρ) * b
        yc = f(c)
        if yc < yd:
            b, d, yd = d, c, yc
        else:
            a, b = b, c
    return (a, b) if a < b else (b, a)


def f(x):
    return (x - 3.0) ** 2