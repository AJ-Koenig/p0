#!/usr/bin/env python3

# Gets the last 8 digits from the integer and returns them as a string.
def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """
    string_int = str(some_int)
    return string_int[-8:]

 # Cache for the optimized_fibonacci so that we don't have to recompute
 # values for the same inputs.
cache = [None] * 1000000

# O(n) time and space complexity.
def optimized_fibonacci(i):
    cache[0] = 0
    cache[1] = 1
    if i == 0:
        return 0
    if i == 1:
        return 1
    j = 2
    while j <= i:
        cache[j] = cache[j - 1] + cache[j - 2]
        j = j + 1
    return cache[i]


#  Generalized SummableSequence where fib algorithms
# is a special case.   e.g:   (1,2,3) can  be the
# base cases to start the sequence,  everyone number afterwards
# is a sum of the previous three.
class SummableSequence(object):

    # *initial   an array of initial values,  for the recurrance relation.
    # i.e: it is the first n numbers which start the sequence, and from
    # which all futher numbers are generated from.
    def __init__(self, *initial):
        count = 0
        params = []
        for num in initial:
            params.append(num)
            count = count + 1
        self.params = params

    # NOTE Sorry it looks it messy,  will refactor soon.
    def __call__(self, i):
        length = len(self.params)
        if i < length:
            return self.params[i]
        k = 0
        for num in self.params:
            cache[k] = num
            k = k + 1

        j = length
        while j <= i:
            m = 1
            sum = 0
            while m <= length:
                sum = sum + cache[j - m]
                m += 1
            j = j + 1
        return sum

# manual runner.
if __name__ == "__main__":
    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    # new_seq is an instance of SummableSequence.
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
