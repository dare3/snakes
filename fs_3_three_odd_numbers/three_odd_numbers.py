def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
     # Iterate through the list up to the third-last element
    for i in range(len(nums) - 2):
        # Check if the sum of the current three numbers is odd
        if sum(nums[i:i+3]) % 2 != 0:
            return True
    return False

# Test cases
print(three_odd_numbers([1, 2, 3, 4, 5]))                    # True
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))      # True
print(three_odd_numbers([5, 2, 1]))                          # False
print(three_odd_numbers([1, 2, 3, 3, 2]))                    # False
