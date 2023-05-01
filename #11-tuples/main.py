my_fruits = ('apple', 'banana', 'lemon')

d = 4

my_nums = (d, 3, 4, 5)
print(list(my_nums))

users = (
    {
        'user_id': 100,
        'user_name': 'taras',
    },
    {
        'user_name': 101,
        'user_id': 'Mom',
    },
    {

    }
)

users[0]['user_city'] = 'Sarny'
print(users)

# check exists index in tuple
print(len(users))

# addition tuples
print(my_nums+my_fruits)

# methods
print(users.count({}))
print(my_nums.index(3))


# practice
index_one = my_nums.index(4)
index_two = my_nums.index(4, index_one + 1)
