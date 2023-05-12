import time
import graphics as gr


def inc_age(person):
    person['age'] += 1
    return person


person_1 = {
    'name': 'Bob',
    'age': 10,
}
inc_age(person_1)
print(person_1)  # {'name': 'Bob', 'age': 11}


# how to avoid changes in mutable object that transfer into function as parameter
# .copy()
# deepcopy() from copy import deepcopy
def inc_age2(person):
    person = person.copy()
    person['age'] += 1
    return person


person_2 = inc_age2(person_1)
print(person_1)
print(person_2)


# practice
def merge_lists_to_dict(list1, list2):
    return dict(zip(list2.copy(), list1.copy()))


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

print(merge_lists_to_dict(list1, list2))

######################################################################
# fucntion arguments
print('\n')


def sum1(a, b):  # positional and specific implemented
    return a + b


def sum2(*args):  # positional and not specific
    print(sum(args))


def sum3(*args, **kwargs):  # non positional - named by keywords
    print(kwargs)


sum3(45, 98, g=5, j='Taras')


# default parameters
def mult_by_factor(value, multiplier=2):
    return value*multiplier


print(mult_by_factor(20, multiplier=50))
print(mult_by_factor(20))


def get_week_day():
    ...  # returns like 'Sunday'
    pass


def create_new_post(post, weekday=get_week_day()):
    post = post.copy()
    post['weekday'] = weekday
    return post


post = {
    'id': 1243,
    'author': 'Taras'
}

print(create_new_post(post))

# home task


def merge_lists_to_dict2(**lists):
    return dict(zip(lists['list1'].copy(), lists['list2'].copy()))


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge_lists_to_dict(list1=list1, list2=list2))


def merge_lists_to_dict3(*list_p, **list_n):
    return dict(zip(list_p[0].copy(), list_n['list2'].copy()))


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge_lists_to_dict(list1, list2=list2))


def update_car_info(**car):
    car["is_available"] = True
    return car


print(update_car_info(brand="BMW", price=25_000))


# #####################################
# callback functions
def other_fn():
    ...


def fn_with_callback(callback_fn):
    callback_fn()


fn = fn_with_callback(other_fn)

# practice
print('\n')


def print_num_info(num):
    if (num % 2) == 0:
        print("Num is even.")
    else:
        print("Num is odd.")
    return 0


def print_square_num(num):
    print(num**2)


def process_num(num, num_info_callback):
    num_info_callback(num)
    return 0


# entered_num = int(input("Enter number: "))
# process_num(entered_num, print_num_info)
# process_num(entered_num, print_square_num)


# docstrings
# use to tooltips of function
def mult_by_factor(value, mult=2):
    """_summary_

    Args:
        value (_type_): _description_
        mult (int, optional): _description_. Defaults to 2.

    Returns:
        _type_: _description_
    """
    return value*mult


print(mult_by_factor.__doc__)


# field of view
value1 = "1111111"


def f1():
    global value1
    value1 = 9999

    def inner_fn():
        value1 = '------'
        print(value1)
    inner_fn()
    print(value1)


f1()
print(value1)

# practice
print('\n')


def f2(a, b):
    z = 90
    print(value1)
    print(a, b)
    print(dir())


f2('abc', 'xyz')

x = [1, 2, 3]


def f2(x):
    a = 42
    x[1] = a
    x = a
    print(x)


f2(x)
print(x)

# recursion
# recursion
window = gr.GraphWin("Recursion test", 1000, 1000)
alpha = 0.2
window.setBackground('white')


def draw_fractal_rectangle(A, B, C, D, dept=400):
    if dept < 1:
        return
    time.sleep(.2)
    for M, N in ((A, B), (B, C), (C, D), (D, A)):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)

    A_next = (A[0]*(1 - alpha) + B[0] * alpha, A[1]*(1 - alpha) + B[1] * alpha)
    B_next = (B[0]*(1 - alpha) + C[0] * alpha, B[1]*(1 - alpha) + C[1] * alpha)
    C_next = (C[0]*(1 - alpha) + D[0] * alpha, C[1]*(1 - alpha) + D[1] * alpha)
    D_next = (D[0]*(1 - alpha) + A[0] * alpha, D[1]*(1 - alpha) + A[1] * alpha)
    draw_fractal_rectangle(A_next, B_next, C_next, D_next, dept - 1)


draw_fractal_rectangle((50, 50), (600, 50), (600, 600), (50, 600))

window.getMouse()
