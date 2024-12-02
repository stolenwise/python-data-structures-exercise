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
#Start with result = 1.
# Loop through each number in the list.
# Check if the number is even:
# If yes, multiply it into result.
# After the loop, return result.
result = 1
for num in nums:
    if num % 2 == 0:
        result *= num
return result



