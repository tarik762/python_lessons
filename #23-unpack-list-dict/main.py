# example list, tuples
my_fruits = ['apple', 'banana', 'lime']

my_apple, my_banana, my_lime = my_fruits

print(my_apple)  # apple


mf = (1, 2, 3)

f, s, t = mf

print(f, s, t)  # 1 2 3
ff, *rest = mf
print(rest)  # [2, 3]


# unpack dict

user_profile = {
    'name': 'Taras',
    'comments_qnt': 23,
}


def user_info(name, comments_qnt=0):
    if not comments_qnt:
        return f"{name} has no comments."

    return f"{name} has {comments_qnt} comments."


print(user_info(**user_profile))

# unpack list to arguments
print('\n')
user_data = ['Taras', 33]
print(user_info(*user_data))

# home task
list_of_dicts = [
    {
        'name': 'Taras',
        'age': 33
    },
    {
        'name': "Sofia",
        'age': 5
    },
    {
        'name': 'Mary',
        'age': 4
    }
]

one, *other = list_of_dicts


def print_if(name, age):
    print(f"Name: {name} has {age} years old")
    return None


for el in list_of_dicts:
    print_if(**el)
