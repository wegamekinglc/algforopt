import numpy as np
from math import sqrt
import numba as nb


def f(x):
    return 3 * (x ** 2) + 5 * x + 2


def vec(x):
    return f(2 * (x ** 2) + 6 * (x ** 3) - np.sqrt(x))


def devec(x):
    for i in range(len(x)):
        x_bar = x[i]
        x[i] = f(2 * x_bar ** 2 + 6 * x_bar ** 3 - sqrt(x_bar))
    return x


@nb.njit(cache=True)
def f_nb(x):
    return 3 * (x ** 2) + 5 * x + 2


@nb.njit(cache=True)
def devec_nb(x):
    x_new = np.zeros_like(x)
    for i in range(len(x)):
        x_new[i] = f_nb(2 * x[i] ** 2 + 6 * x[i] ** 3 - sqrt(x[i]))
    return x_new


x = np.abs(np.random.randn(1000000))

