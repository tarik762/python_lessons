fruits = ['apple', 'banana', 'lime']
quantities = [100, 200, 300, 500]
avail = [True, False, True, True, False]
fr_qvn_zip = zip(fruits, quantities)
print(fr_qvn_zip)

fr_lst = list(fr_qvn_zip)
print(fr_lst)


fr_dict = dict(fr_qvn_zip)
print(fr_dict)

print(type(fr_qvn_zip))
