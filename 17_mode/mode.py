def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # Create a dictionary to store the count of each number
    count_dict = {}

    # Iterate through the numbers and count their occurrences
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find the number with the maximum count
    max_count = max(count_dict.values())
    
    # Return the number with the maximum count
    for key, value in count_dict.items():
        if value == max_count:
            return key

# Test cases
print(mode([1, 2, 1]))          # Should print 1
     