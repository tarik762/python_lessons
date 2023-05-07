# for in
print('\n')
for i in range(10):
    print(i)

print('\n')
for i in [True, {}, {2, 3, 4, 6, 6}, 'abc']:
    print(i)

print('\n')
for i in (True, {}, {2, 3, 4, 6, 6}, 'abc'):
    print(i)

print('\n')
for i in {'a': 1, 'b': 2, 'h': 100}:
    print(i)


print('\n')
my_list = [1, 'abc', True]
for elem in my_list:
    print(type(elem))
    print(elem)
print(elem)


# key and values in dicts
print('\n')
dict1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

for key, value in dict1.items():
    print(key, value)


# set()
print('\n')

st1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for value in st1:
    print(value)


# home task
# 1
print('\n')


def transform_dict_to_list(dict, mult):
    return [(key, value * mult if type(value) is int else value)
            for key, value in dict.items()]


dct1 = {
    'a': True,
    'b': 'Some string',
    'c': 10,
    'd': [1, 2, 3, 4]
}

lst = transform_dict_to_list(dct1, 6)
print(lst)

# 2
print('\n')


def filter_list(list_to_filter, filter_type=int):
    return [
        element for element in list_to_filter
        if type(element) is filter_type
    ]


lst2 = [1, 4, True, 'abc', [1, 5, 9, 8], 90]
print(filter_list(lst2, int))


# integrated finction filter()
def filter_list2(list_to_filter, value_type=int):
    return list(
        filter(
            lambda el: type(el) is value_type,
            list_to_filter
        )
    )


print(filter_list2(lst2))


# while
print('\n')
i = 1
while i < 10:
    print(i)
    i += 1


# while True:
#     user_case = input("Enter yes or no: ")
#     if user_case == 'y' or user_case == 'n':
#         break

# print('\n')
# while True:
#     user_case = input("Enter yes or no: ")
#     if user_case != 'y' and user_case != 'n':
#         continue
#     print('Yahoo!')
#     break


# Home Task While

# print('\n')
# while True:
#     print("Please input two numbers: 'a' and 'b' to divide a/b.")

#     num_a = input("a = ")
#     while True:
#         try:
#             num_a = float(num_a)
#             break
#         except:
#             print("Number 'a' is not a float or integer, try again!")
#             num_a = input("a = ")
#             continue

#     num_b = input("b = ")
#     while True:
#         try:
#             num_b = float(num_b)
#             break
#         except:
#             print("Number 'b' is not a float or integer, try again!")
#             num_b = input("b = ")
#             continue
#     while True:
#         if num_b != 0:
#             break
#         else:
#             print(
#                 "Number 'b' can not be '0' - will be division by zero, please enter 'b' again.")
#             num_b = input("b = ")
#             while True:
#                 try:
#                     num_b = float(num_b)
#                     break
#                 except:
#                     print("Number 'b' is not a float or integer, try again!")
#                     num_b = input("b = ")
#                     continue
#     print(f"a/b = {num_a}/{num_b} = {num_a/num_b}")

#     # ask for quit
#     quit = ''
#     while quit != 'y' and quit != 'n':
#         quit = str(input("Do you want to quit - type 'y' or 'n': "))

#     if quit == 'y':
#         continue
#     else:
#         print("Goodbye!!!!")
#         break


# short loop - for in (comprehensions)
print('\n')

lst = [x**2 for x in range(10) if x % 2 == 0]
print(lst)

lst2 = [-1, -20, -50, 4, 50, 100, 10, -99]
abs_lst = [abs(x) for x in lst2]
print(abs_lst)

set1 = {1, 10, 15}
new_set1 = {x**2 for x in set1}
print(new_set1)


dict1 = {
    'a': 2,
    'c': 10,
    'n': 100,
}

new_dict1 = {f"{key}-new": value**2 for key, value in dict1.items()}
print(new_dict1)

# practice
print('\n')
# create set from dict
new_set1 = {value*10 for key, value in dict1.items()}
print(new_set1)

# create dict from list
lst2 = [1, 3, 4, 6, 8]
new_dict2 = {key: value for key, value in enumerate(lst2)}
print(new_dict2)


# Home Task
# 1
h_dict = {
    'a': 'tiger',
    'b': 'bear',
    'c': 'elephant',
    'd': 'kangaro',
}

animals = {key: value.upper() for key, value in h_dict.items()}
print(animals)

# 2
h_list = ['abc', 'Taras', "dog", "Europe", "UNO"]
h_list2 = [elem for elem in h_list if len(elem) > 3]
print(h_list2)
