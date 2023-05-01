my_fruits: list = ['apple', 'banana', 'lime']

post_ids: list = [123, 322, 444]

user_inputs: list = [True, 'hi!', '🥰', 10.45]

print(','.join(my_fruits))  # only str elements in list

# polifill to join any of type of list element
print(','.join([str(el) for el in post_ids]))

del post_ids[-1]

print(post_ids)

list_of_dict = [
    {
        'q': 67
    },
    {
        'd': 56,
        'll': 'Ll'
    }
]

print(dir(list_of_dict[1]))


# methods of LIST
print("\n\n\n")
my_list = [4, 5, 6, 7, 8, 9]
print(my_list)
my_list.pop()
removed = my_list.pop(0)
print(removed)
print(my_list)

my_list.insert(0, 100)
print(my_list)
my_list.append(100)
print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)


# operations with lists

print()
print()
# convert str to list
list2 = list("taras")
print(list2)
# conver dict to list
d1 = {'a': 100, 'b': 300}
print(list(d1))
print(min(my_list))
print(sum(my_list))
print(max(my_list))

print()
print()

# sum of lists
l3 = [3.4, 5.6]
l4 = [4, 5]
print(l3+l4)

# cut of list
l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l5[:2])
print(l5[1:-1])
print(l5[2:])
print(l5[-2:])


# copying lists
print("\n\n\n")
l6 = [1, 2]
copy_l6 = l6
print(id(l6), "-", id(copy_l6))

copy_l6 = l6[:]
print(id(l6), "-", id(copy_l6))

copy_l6 = list(l6)
print(id(l6), "-", id(copy_l6))

copy_l6 = l6.copy()
print(id(l6), "-", id(copy_l6))


# practice
print("\n\n\n")
my_nums = [10, 50, 45, 67, 11, 10]
print(dir(my_nums))

my_nums.append(11)
print(my_nums)
my_nums.insert(2, 100)
print(my_nums)
print(my_nums.count(10))

my_nums.clear()
print(my_nums)

my_nums.extend((10, 20))
print(my_nums)


# own task
# 1
print('\n\n\n')
lst = [1, '2', True, [1, 2], {'a': 6}]
print(lst)
lst.pop(2)
print("Lenght of lst: {} - {}".format(len(lst), lst))
lst.reverse()
print(lst)
lst2 = [1, 2]
lst.extend(lst2)
print(lst)

# 2
print('\n')
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = lst1.__add__(lst2)
# lst3 = lst1+lst2
print(lst3)
