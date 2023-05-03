# lambda x, y: x**y
def my_lambda(x, y):
    return x**y


print(lambda x, y: x**y, 3, 4)


# closure

def get_greeting(greeting):
    return lambda name: f"{greeting}, {name}"


morning_gr = get_greeting('Good morning')
evening_gr = get_greeting('Good night')

print(morning_gr('Taras'))
print(evening_gr('Mary'))
