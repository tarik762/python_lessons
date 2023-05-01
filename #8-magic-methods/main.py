# __mul__ __add__ .......
d: int = 6
f: float = 4.5
print(f"{f:.3f} dfff")
print(f.__radd__(d))
print(f.__rmul__(d))

str: str = 'Taras'


print(d.__mul__(str))
print(d * str)
print(str.__mul__(d))


# Nest about magic methods

print(dir(bool))
print(dir(int))
print(dir(True))

print(abs(-5))

print(help(list.__eq__))
