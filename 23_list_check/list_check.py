def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    return all(isinstance(item, list) for item in lst)

# Test cases
print(list_check([[1], [2, 3]]))   # Should print True
print(list_check([[1], "nope"]))   # Should print False
