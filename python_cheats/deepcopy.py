# prevent copy id of object
# use .copy() method but inside been the same ex. list
from copy import deepcopy
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
print(info)
print(info2)
