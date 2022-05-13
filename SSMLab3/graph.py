import matplotlib.pyplot as plt


def graph(lagrange_1, newton_1, x, lagrange_2, newton_2, f):
    plt.plot(x, lagrange_1, color='r', label='lagrange')
    plt.plot(x, newton_1, color='g', label='newton')
    plt.plot(x, list(map(f, x)), color='b', label='real')
    plt.legend()
    plt.show()

    plt.plot(x, lagrange_2, color='r', label='lagrange')
    plt.plot(x, newton_2, color='g', label='newton')
    plt.plot(x, list(map(f, x)), color='b', label='real')
    plt.legend()
    plt.show()