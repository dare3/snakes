def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here
    char_positions = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
    char_positions.update({chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)})
    
    # Calculate the sum of character positions
    sum_positions = sum(char_positions[char] for char in word)
    
    # Check if the sum is odd
    return sum_positions % 2 == 1

# Test cases
print(is_odd_string('a'))         # True
print(is_odd_string('A'))         # True
print(is_odd_string('aaaa'))      # False
print(is_odd_string('AAaa'))      # False
print(is_odd_string('amazing'))   # True