def reverse_vowels(str):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = set('aeiouAEIOU')
    str = list(str)
    i, j = 0, len(str) - 1
    while i < j:
        if str[i] in vowels and str[j] in vowels:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
        elif str[i] in vowels:
            j -= 1
        elif str[j] in vowels:
            i += 1
        else:
            i += 1
            j -= 1
    return ''.join(str)

# Test cases
print(reverse_vowels("Hello!"))                  # Holle!
print(reverse_vowels("Tomatoes"))                # Temotaos
print(reverse_vowels("Reverse Vowels In A String"))  # RivArsI Vewols en e Streng
print(reverse_vowels("aeiou"))                   # uoiea
print(reverse_vowels("why try, shy fly?"))        # why try, shy fly?