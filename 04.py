
# --- Day 4: Secure Container ---
# 
# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.
# 
# However, they do remember a few key facts about the password:
# 
#     It is a six-digit number.
#     The value is within the range given in your puzzle input.
#     Two adjacent digits are the same (like 22 in 122345).
#     Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# 
# Other than the range rule, the following are true:
# 
#     111111 meets these criteria (double 11, never decreases).
#     223450 does not meet these criteria (decreasing pair of digits 50).
#     123789 does not meet these criteria (no double).
# 
# How many different passwords within the range given in your puzzle input meet these criteria?


def test_password(password, tests):
    digits = [int(d) for d in str(password)]
    # print([type(d) for d in digits])
    #print(digits)
    #print([test(digits) for test in tests])
    return all([test(digits) for test in tests])

def test_adjacent_digits(digits):
    last = None
    for digit in digits:
        if digit == last:
            return True
        last = digit
    return False

def test_adjacent_digits_double(digits):
    last = None
    count = 0
    for digit in digits:
        if digit == last:
            count += 1
        else:
            if count == 1:
                return True
            count = 0
        last = digit
    if count == 1:
        return True
    return False

def test_length(digits, desired_len = 6):
    if len(digits) == desired_len:
        return True
    return False

def test_increasing(digits):
    last = None
    for digit in digits:
        if last and last > digit:
            return False
        last = digit
    return True

def main():
    start, stop = [int(d) for d in '134792-675810'.split('-')]
    print(start, stop)
    tests = [test_adjacent_digits, test_length, test_increasing]
    count = 0
    total = 0
    for num in range(start, stop):
        if test_password(num, tests):
            count += 1
        total += 1
    return count

def main2():
    start, stop = [int(d) for d in '134792-675810'.split('-')]
    print(start, stop)
    tests = [test_adjacent_digits_double, test_length, test_increasing]
    count = 0
    total = 0
    for num in range(start, stop):
        if test_password(num, tests):
            count += 1
        total += 1
    return count

all_tests = [test_adjacent_digits, test_length, test_increasing]

if __name__ == "__main__":
    print(test_password(111111, all_tests))
    print(test_password(223450, all_tests))
    print(test_password(123789, all_tests))
    print(test_password(123799, all_tests))
    print(test_password(134792, all_tests))
    print(test_password(675810, all_tests))
    # print('80')
    print(test_password(80, [test_increasing]))
    print(test_password(111122, [test_adjacent_digits_double]))
    print(test_password(111222, [test_adjacent_digits_double]))
    print(main())
    print(main2())
