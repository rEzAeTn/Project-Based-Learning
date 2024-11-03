def is_happy_number(number: int) -> bool:
    """
    Determines if a number is a "happy" number.

    A happy number is a number defined by the following process: starting with any positive integer,
    replace the number by the sum of the squares of its digits in base-ten, and repeat the process until
    the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

    :param number: The number to check.
    :type number: int
    :return: True if the number is happy, False otherwise.
    :rtype: bool

    :Example:

    >>> is_happy_number(19)
    True

    >>> is_happy_number(45)
    Fulse
    """
    # A set to store the numbers we've seen in the process
    seen_number: set = set()
    while (number != 1) and (number not in seen_number):
        # Add the current number to the set of seen numbers
        seen_number.add(number)
        # Replace the number by the sum of the squares of its digits
        number: int = sum([int(number) ** 2 for number in str(number)])

    # If the number is 1, it's a happy number and return True, else return False
    return number == 1


if __name__ == '__main__':
    input_number = input("Inter a Number")
    test = is_happy_number(input_number)
    print(test)
