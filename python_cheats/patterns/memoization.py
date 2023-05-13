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


count = 0


@Memoized(cache_size=3)
def get_fibonacci(n: int) -> int:
    global count

    if n == 0:
        return 0
    elif n < 3:
        return 1
    count += 1
    return get_fibonacci(n - 1) + get_fibonacci(n - 2)


print(get_fibonacci(30))
print("Calls of factorial:", count)
