def basic_polinomial(x, x_list, i):
    dom = 1
    counter = 1

    for j in range(len(x_list)):
        if i != j:
            counter *= (x - x_list[j])
            dom *= (x_list[i] - x_list[j])

    return counter / dom


def find(x, x_list, y_list):
    result = 0

    for i in range(len(x_list)):
        result += y_list[i] * basic_polinomial(x, x_list, i)

    return result
