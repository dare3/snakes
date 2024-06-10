def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    return min(d, key=d.get), max(d, key=d.get)

# Test cases
print(min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))  # Should print (1, 10)
print(min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"}))  # Should print ('apple', 'cherry')