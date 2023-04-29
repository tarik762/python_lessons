# dynamic typization
def my_func(name):
    print(name)


my_func('Taras')
my_func = 10
# my_func('t') - Error


# types nd structures of data
print('\n', dir(15), '\n')
# mutable objects - list, dict, set, <user-defined-classes>
# immutable objects - str, int, bool, float, tuple, None, range


# name of variable - is a ref to object in memory


# integrated function id() - result is ID of object (address) in memory
var = 10
print(id(var))

# a few variables may ref to the ame object
one = 1
two = one
three = __annotations__
print('\n', id(one), '\n', id(two), '\n', id(three))
