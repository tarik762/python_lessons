
def decorator_function(origin_function):
    def wrapper(*args, **kwargs):
        print('This is debounce function!')
        print(f'Function which has been debounced: {format(origin_function)}')
        # print('Function which has been debounced: {}'.format(func))
        print('Run debounced function...')
        return_value = origin_function(*args, **kwargs)
        print('Exit from debounce')
        return return_value
    return wrapper


@decorator_function
def origin_f(*args):
    print(args)
    return None


origin_f(1, 2, ['2', 4])
