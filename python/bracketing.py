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


def quadratic_fit_search(f, a, b, c, n):
    ya, yb, yc = f(a), f(b), f(c)
    for i in range(1, n - 2):
        x = 0.5 * (ya * (b**2 - c**2) + yb * (c**2 - a**2) + yc * (a**2 - b**2)) / (ya * (b -c) + yb * (c - a) + yc * (a - b))
        yx = f(x)
        if x > b:
            if yx > yb:
                c, yc = x, yx
            else:
                a, ya, b, yb = b, yb, x, yx
        elif x < b:
            if yx > yb:
                a, ya = x, yx
            else:
                c, yc, b, yb = b, yb, x, yx
    return a, b, c


def bisection(df, a, b, ϵ=1e-14):
    if a > b:
        a, b = b, a

    ya, yb = df(a), df(b)
    if ya == 0:
        b = a
    if yb == 0:
        a = b

    while b - a > ϵ:
        x = (a + b) / 2
        y = df(x)
        if y == 0:
            a, b = x, x
        elif y * ya > 0:
            a = x
        else:
            b = x
    return a, b


def bracket_sign_change(df, a, b, k=2):
    if a > b:
        a, b = b, a

    center, half_width = (a + b) / 2, (b - a) / 2
    while df(a) * df(b) > 0:
        half_width *= k
        a = center - half_width
        b = center + half_width
    return a, b


def f(x):
    return (x - 3.0) ** 2


def df(x):
    return 2. * (x - 3.0)


if __name__ == "__main__":
    from IPython import get_ipython
    ipython = get_ipython()
    ipython.magic("timeit quadratic_fit_search(f, 0., 2., 5., 10)")