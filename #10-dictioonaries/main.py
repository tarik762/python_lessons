my_bike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2,
}

print(my_bike['brand'])
# del (my_bike['brand'])
print(my_bike)
print(my_bike.items())

my_bike['year'] = 2015
print(my_bike)

# dict lenght
print(len(my_bike))

# absent key in dict
iskey = my_bike.get('model')  # None
iskey = my_bike.get('model', 100)  # 100
print(iskey)


# practice
print('\n')
my_disk = {

}

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

print(type(my_disk.items()))
print(my_disk.items())

print(list(my_disk.keys()))
print(my_disk.popitem())
print(my_disk.pop('brand'))
print(my_disk)

# copy of dict
my_disk2 = dict(my_disk)
print(id(my_disk), " - ", id(my_disk2))
my_disk2 = my_disk.copy()

# create dict

l1 = [['first', 0], ['second', True], ['a', 'abc']]
d1 = dict(l1)
print(d1)


# home task
print('\n')

hw = {}
key_1 = input("enter 1 key: ")
val_1 = input("enter 1 value: ")
key_2 = input("enter 2 key: ")
val_2 = input("enter 2 value: ")
key_3 = input("enter 3 key: ")
val_3 = input("enter 3 value: ")

hw[key_1] = val_1
hw[key_2] = val_2
hw[key_3] = val_3

hw['rt'] = 766

print(hw)
