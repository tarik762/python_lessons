from debounce import Debounce
import unittest
import time

""" This is a proper debounce function, the way a electrical engineer would think about it.
    This wrapper never calls sleep.  It has two counters: one for successful calls, and one for rejected calls.
    If the wrapped function throws an exception, the counters and debounce timer are still correct """


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
                    willcall = False
            else:
                willcall = True  # function has never been called before

            if willcall:
                # set these first incase we throw an exception
                self.last = now  # don't use time.time()
                self.count += 1
                f(*args, **kwargs)  # call wrapped function
            else:
                self.count_rejected += 1
        return wrapped


# unittests


class DebounceBasics(unittest.TestCase):
    def increment(self):
        self.success_count += 1

    def setUp(self):
        self.success_count = 0

    def test_debounce(self):
        # check we started correctly
        self.assertEqual(self.success_count, 0)

        # calls more often than 1.0 seconds will be rejected
        deb = Debounce(1.0)
        deb(self.increment)()
        self.assertEqual(self.success_count, 1)
        deb(self.increment)()
        deb(self.increment)()
        deb(self.increment)()
        deb(self.increment)()
        self.assertEqual(self.success_count, 1)
        self.assertEqual(self.success_count, deb.count)
        time.sleep(1)
        deb(self.increment)()
        self.assertEqual(self.success_count, 2)
        self.assertEqual(self.success_count, deb.count)
        deb.reset()
        deb(self.increment)()
        deb(self.increment)()
        self.assertEqual(self.success_count, 3)
        deb(self.increment)()
        deb(self.increment)()
        self.assertEqual(self.success_count, 3)
        self.assertEqual(self.success_count, deb.count)
        self.assertEqual(deb.count_rejected, 7)


class DebounceLoop(unittest.TestCase):
    def increment(self):
        self.success_count += 1

    def setUp(self):
        self.success_count = 0

    # test that Debounce calls when it's supposed to
    def test_loop(self):
        a = time.time()
        period = 0.2524
        deb = Debounce(period)
        deb(self.increment)()  # call it once to set the debounce timer

        # call it as fast as possible until it goes through
        while True:

            deb(self.increment)()
            if self.success_count != 1:
                b = time.time()
                break

        delta = b-a
        self.assertGreaterEqual(
            delta, period, "Debounce let a call through before it was supposed to")
        # this will probably be in the 100 thousands
        self.assertGreater(deb.count_rejected, 100,
                           "Debounce didn't reject anything")
        self.assertGreater(deb.count_rejected, deb.count,
                           "Debounce let more through than it rejected")
        self.assertEqual(
            deb.count, 2, "Debounce let more through than it should have")


class DebounceParams(unittest.TestCase):
    def remember(self, input):
        self.memory = input

    def setUp(self):
        self.memory = -1

    def test_debounce(self):
        # check we started correctly
        self.assertEqual(self.memory, -1)

        # calls more often than 1.0 seconds will be rejected
        deb = Debounce(0.1)
        deb(self.remember)(1)
        self.assertEqual(self.memory, 1)
        deb(self.remember)(42)
        self.assertEqual(self.memory, 1)
        deb(self.remember)(90)
        self.assertEqual(self.memory, 1)
        time.sleep(0.1)
        deb(self.remember)(42)
        self.assertEqual(self.memory, 42)
        self.assertEqual(deb.count, 2)

        time.sleep(0.1)
        with self.assertRaises(TypeError):
            deb(self.remember)(43, 43)  # throw for wrong number of params

        self.assertEqual(
            deb.count, 3, "Throwing an exception did not update counters")

        deb(self.remember)(43)
        self.assertEqual(
            self.memory, 42, "Throwing an exception did not update last called time")

        time.sleep(0.1)
        with self.assertRaises(TypeError):
            deb(self.remember)()  # throw for wrong number of params


if __name__ == '__main__':
    unittest.main()
