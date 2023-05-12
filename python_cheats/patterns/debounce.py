import time


class Debounce(object):

    def __init__(self, period):
        # never call the wrapped function more often than this (in seconds)
        self.period = period
        self.count = 0  # how many times have we successfully called the function
        self.count_rejected = 0  # how many times have we rejected the call
        self.last = None  # the last time it was called

    # force a reset of the timer, aka the next call will always work
    def reset(self):
        self.last = None

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            now = time.time()
            willcall = False
            if self.last is not None:
                # amount of time since last call
                delta = now - self.last
                if delta >= self.period:
                    willcall = True
                else:
                    # print("willcall false")
                    willcall = False
            else:
                willcall = True  # function has never been called before

            if willcall:
                # set these first incase we throw an exception
                self.last = now  # don't use time.time()
                self.count += 1
                print("before call f()")
                f(*args, **kwargs)  # call wrapped function
            else:
                self.count_rejected += 1
        return wrapped


if __name__ == '__main__':
    deb = Debounce(.4)

    def print_str(char):
        print(next(char))

    def generate_char():
        i = 50
        while True:
            if i >= 140:
                i = 50
            yield chr(i)
            i += 1

    chars = generate_char()
    print("Debounced generator started!")

    for i in range(3000000):
        deb(print_str)(chars)

    print("Count successed: ", deb.count)
    print("Count rejected: ", deb.count_rejected)
    print("Debounced generator end!")
