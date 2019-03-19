def sum_array(array):
    """Return sum of all items in array
    Args:
        array(list): an array of elements to be summed
    Returns:
        int
    """
    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    """Calculate nth term in fibonacci sequence
    Args:
        n (int): nth term in fibonacci sequence to calculate
    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    """

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    """Return n!"""
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):
    """Return word in reverse"""
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
