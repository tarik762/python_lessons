my_fruits = {'apple', 'banana', 'lime'}
posts_ids = {150, 145, 145, 191}
print(my_fruits)

print(list(my_fruits))
print(len(my_fruits))

post_ids = {10, 25, 45, 95}
print(dir(post_ids))

# will throw error
# lests_set = {[1, 2], [2, 3]}


# practice
print('\n')
my_set = {10, '4', '', '', 10, 5, 5, 15, 15}
print(my_set)
my_set = {10, (3, 5), '34'}
print(my_set)
# create empty set
empty_set = set()
print(empty_set)


# set's methods
print('\n')
my_set = {'1280x1024', '800x600'}
my_set.add('1024x768')
print(my_set)

# union
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = s1.union(s2)
# or
s3 = s1 | s2
print(s3)

# intersection
s3 = s1.intersection(s2)
# or
s3 = s1 & s2
print(s3)

# issubset
ss1 = {1, 2, 3, 4, 5}
ss2 = {1, 2, 3}
ss3 = ss1.issubset(ss2)
print(ss3)

# issuperset
ss3 = ss1.issuperset(ss2)
print(ss3)


# practice of methods
print('\n')
s1 = {'abc', 'd', 'f', 'y'}
s2 = {'a', 'f', 'd'}
print(s1.intersection(['a', 'h']))
print(s1.union(s2))  # same as s1 | s2
print(s1.issubset(s2))  # same as s1 == s2
print(s1.difference(s2))  # same as s1 - s2

# deletion from set
s1.discard('d')
print(s1)
try:
    s1.remove('de')
except:
    print(1)

print(s1)

s3 = s1.copy()
s1.add('z')
s3.add('ww')
print(s1)
print(s3)


# practice - simmetrical difference in set's
print('\n')
s1 = {'a', 'd', 'g', 'y'}
s2 = {'a', 'd', 'g', 'v', 'r'}
print(s1.symmetric_difference(s2))
# or
print((s1 | s2)-(s1 & s2))


# home task
print('\n\n')
hw1 = {1, 3, 5, 7, 9}
hw1.add(11)
hw2 = {1, 2, 3, 4, 5}
hw3 = hw1 & hw2
print(hw3)
print(list(hw3))

hw3 = hw1.isdisjoint(hw2)
print(hw3)
