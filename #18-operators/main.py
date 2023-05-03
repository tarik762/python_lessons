a = set(range(10))
b = set(range(10, 20))
print(a)
print(b)
print(a == b)

print(isinstance(a, set))

print(100 in a)

print(not not not bool({}))


# logic oerators
# not and or
if not int('0'):
    print('Hello')

# 'a' and 'b' -> 'a' if a=False else 'b'
# 'a' or 'b' -> 'a' if a=True else 'b'

# practice
print('\n')

my_list = [1, 3]
print(not my_list)

other_list = []

print(len(my_list) or other_list)
my_dict = {}

print(my_list and my_dict)

# good practice
my_list2 = [1, 2]
my_list2 and print("my_list is NOT empty")

# home task
dict1 = {
    'one': 1,
    'two': 2,
}

dict2 = {
    'one': 1,
    'two': 2,
}
print(dict1 == dict2)
dict1 == dict2 and print("Dicts are equal!!")


# unpack dictionaries '**'
button = {
    'width': 200,
    'text': 'button',
    'color': 'grey'
}

red_button = {
    **button,
    'color': 'red',
}

print(red_button)

# concat dictionaries
but_info = {
    'text': 'info',
    'width': 200,
    'color': 'grey'
}

but_help = {
    'text2': 'Help',
    'width': 300,
}

but_all = but_help | but_info

print(but_all)
