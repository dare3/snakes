def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    return lst.count(search_term)
print(frequency([1, 4, 3, 4, 4], 4))  # Should print 3
print(frequency([1, 4, 3], 7))  # Should print 0