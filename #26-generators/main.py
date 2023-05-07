from sys import getsizeof
nums = (1, 2, 3, 4)
nums_new = (elem**2 for elem in nums)
print(nums_new)  # generator object

# why to use generators
sq_gen = (elem**2 for elem in range(10000))

print(getsizeof(sq_gen))

sq_list = [elem**2 for elem in range(10000)]

print(getsizeof(sq_list))


# function generator
def generate_test():
    for i in range(100):
        yield i
    pass


gen_var = generate_test()
print(next(gen_var))
print(next(gen_var))
