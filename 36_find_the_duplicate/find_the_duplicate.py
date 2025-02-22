def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    duplicate = set()
    for num in nums:
        if num in duplicate:
            return num
        duplicate.add(num)
    return None

# Test cases
print(find_the_duplicate([1, 2, 1, 4, 3, 12]))   # Should print 1
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9])) # Should print 9
print(find_the_duplicate([2, 1, 3, 4]))          # Should print None
