def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    return ''.join(char.lower() if char == to_swap.lower() else char.upper() if char == to_swap.upper() else char for char in phrase)

# Test cases
print(flip_case('Aaaahhh', 'a'))  # Should print 'aAAAhhh'
print(flip_case('Aaaahhh', 'A'))  # Should print 'aAAAhhh'
print(flip_case('Aaaahhh', 'h'))  # Should print 'AaaaHHH'