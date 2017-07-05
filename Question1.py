# http://www.bbc.co.uk/programmes/articles/5wkxjTtqRvq8Cyrrjxtk7tc/puzzle-for-today

# Puzzle No.1 – Monday 3 July
# Take the digits 1,2,3 up to 9 in numerical order and put either a plus sign or a minus sign or neither between
#  the digits to make a sum that adds up to 100.
#  For example, one way of achieving this is: 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100, which uses six plusses and minuses.
#  What is the fewest number of plusses and minuses you need to do this?

# Brute force baby

# Take a number and produce a string with its value at a given base
def display_by_base(n, base):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, base)
        nums.append(str(r))

    return ''.join(reversed(nums))

min_operator_count = 8
# We are going to cycle through all the combinations of the eight operators that could be in the equation
# Three operators (hence the 3^8 combinations) are '' (ie nothing), '+', or '-'
# Then we'll add the numbers 1 to 9 into the mix
for number in range(0, 3**8):
    # Get the base three number
    base = display_by_base(number, 3)
    # pad it to be eight digits so we end up with something like '02100201'
    padded = base.rjust(8, '0')

    current_int = 1
    to_evaluate = ''
    operator_count = 0

    # Interweave integers 1 to 9 into the operator list
    for operator in padded:
        to_evaluate = to_evaluate + str(current_int)
        if operator == '1':
            to_evaluate = to_evaluate + '+'
            operator_count += 1

        if operator == '2':
            to_evaluate = to_evaluate + '-'
            operator_count += 1

        current_int += 1

    # Should now have a string like '123+45-67+8-9'
    to_evaluate = to_evaluate + str(current_int)

    # Check what it give us... if it's 100.. yay!
    result = eval(to_evaluate)
    if result == 100:
        if operator_count <= min_operator_count:
            print("Current best is ", operator_count, " operators in ", to_evaluate)
            min_operator_count = operator_count
