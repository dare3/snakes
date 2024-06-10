def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    frequency = {}
    for char in phrase:
        if char.lower() in vowels:
            frequency[char.lower()] = frequency.get(char.lower(), 0) + 1
    return frequency

# Test cases
print(vowel_count('rithm school'))                  # Should print {'i': 1, 'o': 2}
print(vowel_count('HOW ARE YOU? i am great!'))      # Should print {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}