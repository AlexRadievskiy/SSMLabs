import math


def f(x):
    return x / (256 - math.pow(x, 4))

def n(a, b, h):
    return int((b - a) / h)

# 1
def left_rectangle_method(a, b, h):
    res = 0
    for i in range(n(a, b, h)):
        res += h * f(a + i * h)
    return res

# 2
def right_rectangle_method(a, b, h):
    res = 0
    for i in range(1, n(a, b, h) + 1):
        res += h * f(a + i * h)
    return res

# 3
def trapezoidal_method(a, b, h):
    sum = f(a) + f(b)
    for i in range(1, n(a, b, h)):
        sum += 2 * f(a + i * h)
    res = (h / 2) * sum
    return res

# 4
def simpson_method(a, b, h):
    sum = f(a) + f(b)
    for i in range(1, n(a, b, h)):
        if i % 2 == 0:
            sum += 2 * f(a + i * h)
        else:
            sum += 4 * f(a + i * h)
        print(sum)
    res = (h / 3) * sum
    return res

# 5
def runge(I_h1, I_h2, p, O):
    return I_h2 + (I_h2 - I_h1) / (2 ** p - 1)
