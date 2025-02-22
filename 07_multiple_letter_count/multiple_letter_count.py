def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    return {letter: phrase.count(letter) for letter in phrase}
print(multiple_letter_count('yay'))  # Should print {'y': 2, 'a': 1}
print(multiple_letter_count('Yay'))  #{'Y': 1, 'a': 1, 'y': 1}