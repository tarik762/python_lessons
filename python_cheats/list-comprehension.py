vlans = [100, 110, 150, 200, 201, 202]
l1 = [f'vlan {x}' for x in vlans]
print(l1)

# pairs of elements
nums = [1, 2, 3, 4, 5]
nums2 = [100, 200, 300, 400, 500]
l2 = [x * y for x, y in zip(nums, nums2)]
print(l2)
