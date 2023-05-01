num_float: float = 4.567

print("This is first method: %.5f" % num_float)
print("This is second method: {:.6f}".format(num_float))
print(f"This is third method: {num_float:.10f}")

str: str = 'Taras'
list: list = [1, 2, 3]

print("this is str:'{}' and this is list:'{}'".format(str, list))
