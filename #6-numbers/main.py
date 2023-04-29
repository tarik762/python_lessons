# for math operates complex nubers
import cmath

# int
fr_qnt = 50
print(type(fr_qnt))
num = 0
# convert str to int
try:
    num = int('6h7')
except:
    print("error input number")
print(num)

# powing
print(6**7.6)

mil = 1_000_000
print(mil+1)

# float
float_str = 4.888_999
print(dir(float_str))
print(type(float('13.6')))
print(round(7.7))

# complex numbers
com_a = 3 + 5j
com_b = 3j + 5
print(com_a ** com_b)


# practice

# input_str = input("Enter any number: ")
# print(int(input_str))
# print(type(3**7))
# print(type(pow(4, 5.4)))

print(cmath.polar(3j + 5))


arr = [1, 2, 3, 4, 5, 6]
arr = [19] + arr
print()
print()
print()
print(arr)
