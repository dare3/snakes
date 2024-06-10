def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count = 0

    for char in parens:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        # fast fail: too many right parens
        if count < 0:
            return False

    return count == 0
# Test cases
print(valid_parentheses("()"))      # True
print(valid_parentheses("()()"))    # True
print(valid_parentheses("(()())"))  # True
print(valid_parentheses(")()"))     # False
print(valid_parentheses("())"))     # False
print(valid_parentheses("((())"))   # False
print(valid_parentheses(")()("))    # False
