def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.lower().replace(' ', '')  # Convert to lowercase and remove spaces
    return phrase == phrase[::-1]  # Check if the phrase is equal to its reverse

# Test cases
print(is_palindrome('tacocat'))  # Should print True
print(is_palindrome('noon'))  # Should print True
print(is_palindrome('robert'))  # Should print False
print(is_palindrome('taco cat'))  # Should print True
print(is_palindrome('Noon'))  # Should print True