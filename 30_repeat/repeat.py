def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    return phrase * num if isinstance(num, int) and num >= 1 else None

# Test cases
print(repeat('*', 3))       # Should print '***'
print(repeat('abc', 2))      # Should print 'abcabc'
print(repeat('abc', 0))      # Should print ''
print(repeat('abc', -1) is None) # Should print True
print(repeat('abc', 'nope') is None) # Should print True
