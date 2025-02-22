def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    output_result = 1
    for num in nums:
        if num % 2 == 0:
            result *= num
    return output_result

# Test cases
print(multiply_even_numbers([2, 3, 4, 5, 6]))  # Should print 48
print(multiply_even_numbers([3, 4, 5]))        # Should print 4
print(multiply_even_numbers([1, 3, 5]))        # Should print 1