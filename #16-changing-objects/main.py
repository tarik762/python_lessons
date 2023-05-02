# int
from copy import deepcopy
a = 10
b = a
print(b)
print(id(a))
print(id(b))
b += 1
print(id(b))


# float
print('\n')
c = 4.5
b = c
print(id(c))
print(id(b))
b += .1
print(id(c))
print(id(b))


# list
print('\n')
ls1 = [1, 2, 3]
ls2 = [1, 2, 3]
print(id(ls1))
print(id(ls2))
ls2.append(5)
print(id(ls2))


# dict
print('\n')
info = {
    'name': 'taras',
    'is_student': True,
}
info_copy = info

print(id(info))
print(id(info_copy))

info['age'] = 33
print(info)
print(info_copy)
info2 = info.copy()
print(id(info))
print(id(info2))

# prevent copy id of object
# use .copy() method but inside been the same ex. list
print('\n')
info = {
    'name': 'Taras',
    'age': 33,
    'reviews': [],
    'tells': {
        'test': ...
    },
}

# info2 = info.copy()
# print(id(info))
# print(id(info2))
# print(info)
# print(info2)
# info2['reviews'].append('Hook')
# print(info)
# print(info2)

# how to create full copy with deepcopy

info2 = deepcopy(info)
info2['reviews'].append('Hook')
info2['tells']['test'] = 100
info2['tells']['test2'] = 10008
print(info)
print(info2)
