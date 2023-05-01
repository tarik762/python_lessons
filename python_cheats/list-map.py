vlans = [100, 110, 150, 200, 201, 202]
l1 = list(map(lambda x: 'vlan {}'.format(x), vlans))
print(l1)

nums = [1, 2, 3, 4, 5]
nums2 = [100, 200, 300, 400, 500]
l2 = list(map(lambda x, y: x*y, nums, nums2))
print(l2)
