from graph import graph
import math
import numpy as np
import lagrange_method
import newton_method

def f(x):
    return math.asin(x) + x

def y_list_creator(x_list):
    y_list = []

    for x in x_list:
        y_list.append(f(x))

    return y_list


x_list_1 = [-0.4, -0.1, 0.2, 0.5]
y_list_1 = y_list_creator(x_list_1)
x_list_2 = [-0.4, 0.0, 0.2, 0.5]
y_list_2 = y_list_creator(x_list_2)

x = np.arange(-1.0, 1.0, 0.01)

lagrange_1 = lagrange_method.find(x, x_list_1, y_list_1)
lagrange_2 = lagrange_method.find(x, x_list_2, y_list_2)
newton_1 = newton_method.find(x, x_list_1, y_list_1)
newton_2 = newton_method.find(x, x_list_2, y_list_2)
graph(lagrange_1, newton_1, x, lagrange_2, newton_2, f)

print("RESULTS \n" + "List 1")
print("Interpolation error in the Lagrange method (1): " + str(f(0.1) - lagrange_method.find(0.1, x_list_1, y_list_1)))
print("Interpolation error in the Newton method (1): " + str(f(0.1) - newton_method.find(0.1, x_list_1, y_list_1)))
print("Error difference: " + str(lagrange_method.find(0.1, x_list_1, y_list_1) - newton_method.find(0.1, x_list_1, y_list_1)))
print("List 2")
print("Interpolation error in the Lagrange method (2): " + str(f(0.1) - lagrange_method.find(0.1, x_list_2, y_list_2)))
print("Interpolation error in the Newton method (2): " + str(f(0.1) - newton_method.find(0.1, x_list_2, y_list_2)))
print("Error difference: " + str(lagrange_method.find(0.1, x_list_2, y_list_2) - newton_method.find(0.1, x_list_2, y_list_2)))
