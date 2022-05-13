from integration_methods import left_rectangle_method, right_rectangle_method, trapezoidal_method, simpson_method, runge

# root = 0.0158274
# a = -2
# b = 2
# h1 = 1
# h2 = 0.25

root = 0.0158274
a = 0
b = 2
h1 = 1
h2 = 0.5

left_rectangle_method_1 = left_rectangle_method(a, b, h1)
right_rectangle_method_1 = right_rectangle_method(a, b, h1)
trapezoidal_method_1 = trapezoidal_method(a, b, h1)
simpson_method_1 = simpson_method(a, b, h1)

print('-----------------[For h1]-----------------')
print("left_rectangle_method: ", round(left_rectangle_method_1, 10))
print("right_rectangle_method: ", round(right_rectangle_method_1, 10))
print("trapezoidal_method: ", round(trapezoidal_method_1, 10))
print("simpson_method: ", round(simpson_method_1, 10))

print()
print("---------[Absolute errors]---------")
absolute1_1 = round(abs(root - left_rectangle_method_1), 10)
absolute1_2 = round(abs(root - right_rectangle_method_1), 10)
absolute1_3 = round(abs(root - trapezoidal_method_1), 10)
absolute1_4 = round(abs(root - simpson_method_1), 10)
print("1: ", absolute1_1, "\n2:", absolute1_2, "\n3:", absolute1_3, "\n4:", absolute1_4)

left_rectangle_method_2 = left_rectangle_method(a, b, h2)
right_rectangle_method_2 = right_rectangle_method(a, b, h2)
trapezoidal_method_2 = trapezoidal_method(a, b, h2)
simpson_method_2 = simpson_method(a, b, h2)

print('-----------------[For h2]-----------------')
print("left_rectangle_method: ", round(left_rectangle_method_2, 10))
print("right_rectangle_method: ", round(right_rectangle_method_2, 10))
print("trapezoidal_method: ", round(trapezoidal_method_2, 10))
print("simpson_method: ", round(simpson_method_2, 10))

print()
print("---------[Absolute errors]---------")
absolute2_1 = round(abs(root - left_rectangle_method_2), 10)
absolute2_2 = round(abs(root - right_rectangle_method_2), 10)
absolute2_3 = round(abs(root - trapezoidal_method_2), 10)
absolute2_4 = round(abs(root - simpson_method_2), 10)
print("1: ", absolute2_1, "\n2:", absolute2_2, "\n3:", absolute2_3, "\n4:", absolute2_4)

runge_1 = runge(left_rectangle_method_1, left_rectangle_method_2, 1, absolute1_1)
runge_2 = runge(right_rectangle_method_1, right_rectangle_method_2, 1, absolute1_2)
runge_3 = runge(trapezoidal_method_1, trapezoidal_method_2, 2, absolute1_3)
runge_4 = runge(simpson_method_1, simpson_method_2, 4, absolute1_4)

print('-----------------[For Runge]-----------------')
print(round(runge_1, 10))
print(round(runge_2, 10))
print(round(runge_3, 10))
print(round(runge_4, 10))

print()
print("---------[Absolute errors]---------")
absolute3_1 = round(abs(root - runge_1), 10)
absolute3_2 = round(abs(root - runge_2), 10)
absolute3_3 = round(abs(root - runge_3), 10)
absolute3_4 = round(abs(root - runge_4), 10)
print("1: ", absolute3_1, "\n2:", absolute3_2, "\n3:", absolute3_3, "\n4:", absolute3_4)