from math import sqrt

EPS = 1e-15
EPS_STEP = sqrt(EPS)

def diff_forward(f, x, h = EPS_STEP):
    return (f(x + h) - f(x)) / h


def diff_central(f, x, h = EPS_STEP):
    return (f(x + h/2) - f(x - h/2)) / h


def diff_backward(f, x, h = EPS_STEP):
    return (f(x) - f(x - h)) / h
