xi = [1.2, 2.1, 3.1, 3.9, 4.8]
yi = [3.4142, 2.9818, 3.3095, 3.8184, 4.3599]
h = [0, 0.9, 1, 0.8, 0.9]

def spline_interpolate(x, y, new):
    di = [0]
    for i in range(1, len(y) - 1):
        di.append((y[i + 1] - y[i]) / h[i + 1] - (y[i] - y[i - 1]) / h[i])
    di.append(0)

    def bi(b):
        return (h[b] + h[b + 1]) / 3

    def ai(a):
        if a == 1:
            return 0
        else:
            return h[a] / 6

    def ci(c):
        if c == 3:
            return 0
        return h[c + 1] / 6

    A = [0]
    B = [0]

    for j in range(1, len(y) - 1):
        A_el = -ci(j) / (bi(j) + ai(j) * A[j - 1])
        B_el = (di[j] - ai(j) * B[j - 1]) / (bi(j) + ai(j) * A[j - 1])
        A.append(A_el)
        B.append(B_el)
    A.append(0)

    print("A: ", A)
    print("B: ", B)

    q = [0, 0, 0, 0, 0]
    q[3] = A[3] * q[4] + B[3]
    q[2] = A[2] * q[3] + B[2]
    q[1] = A[1] * q[2] + B[1]

    print("q: ", q)

    S = {}
    for k in range(1, len(y)):
        S[x[k - 1], x[k]] = (q[k - 1] / (6 * h[k])) * ((x[k] - new) ** 3) + (
                    (q[k] / (6 * h[k])) * ((new - x[k - 1]) ** 3)) + ((y[k - 1] / h[k]) - (q[k - 1] * (h[k] / 6))) * (
                                        x[k] - new) + ((y[k] / h[k]) - (q[k] * (h[k] / 6))) * (new - x[k - 1])
    return S


print(spline_interpolate(xi, yi, 1))
