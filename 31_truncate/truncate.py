def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    return 'Truncation must be at least 3 characters.' if n < 3 else (phrase[:n - 3] + '...') if len(phrase) > n else phrase

# Test cases
print(truncate("Hello World", 6))               # Should print 'Hel...'
print(truncate("Problem solving is the best!", 10)) # Should print 'Problem...'
print(truncate("Yo", 100))                      # Should print 'Yo'
print(truncate('Cool', 1))                      # Should print 'Truncation must be at least 3 characters.'
print(truncate("Woah", 4))                      # Should print 'W...'
print(truncate("Woah", 3))                      # Should print '...'