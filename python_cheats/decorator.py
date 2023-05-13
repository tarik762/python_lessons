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


# one more example
def repeat_decorator(num_repeats=2):
    # repeat_decorator should return a function that's a decorator
    def inner_decorator(fn):
        def decorated_fn(*args, **kwargs):
            for i in range(num_repeats):
                fn(*args, **kwargs)
        # return the new function
        return decorated_fn
    # return the decorator that actually takes the function in as the input
    return inner_decorator

# use the decorator with num_repeats argument set as 5 to repeat the function call 5 times


@repeat_decorator(5)
def hello_world(*args):
    print(args)
    print("Hello world!")


# call the function
hello_world(1, 2, ['2', 4])


# Class decorator
if __name__ == '__main__':
    from collections import deque

    class Memoized:
        def __init__(self, cache_size=100):
            self.cache_size = cache_size
            self.call_args_queue = deque()
            self.call_args_to_result = {}

        def __call__(self, fn):
            def new_func(*args, **kwargs):
                memoization_key = self._convert_call_arguments_to_hash(
                    args, kwargs)
                if memoization_key not in self.call_args_to_result:
                    result = fn(*args, **kwargs)
                    self._update_cache_key_with_value(memoization_key, result)
                    self._evict_cache_if_necessary()
                return self.call_args_to_result[memoization_key]
            return new_func

        def _update_cache_key_with_value(self, key, value):
            self.call_args_to_result[key] = value
            self.call_args_queue.append(key)

        def _evict_cache_if_necessary(self):
            if len(self.call_args_queue) > self.cache_size:
                oldest_key = self.call_args_queue.popleft()
                del self.call_args_to_result[oldest_key]

        @staticmethod
        def _convert_call_arguments_to_hash(args, kwargs):
            return hash(str(args) + str(kwargs))


@Memoized(cache_size=5)
def get_not_so_random_number_with_max(max_value):
    import random
    return random.random() * max_value
