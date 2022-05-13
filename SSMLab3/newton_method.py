def divided_difference(k, x_list, y_list):
    result = 0

    for i in range(k + 1):
        dom = 1

        for j in range(k + 1):
            if i != j:
                dom *= x_list[i] - x_list[j]

        result += y_list[i] / dom

    return result

def find(x, x_list, y_list):
    result = y_list[0]

    for k in range(1, len(y_list)):
        dom = 1
        for i in range(k):
            dom *= x - x_list[i]

        result += divided_difference(k, x_list, y_list) * dom

    return result
