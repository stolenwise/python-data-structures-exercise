def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    string1 = str(num1)
    string2 = str(num2)

    if len(string1) != len(string2):
        return False


    count1 = {}
    count2 = {}

    for digit in string1:
        count1[digit] = count1.get(digit, 0) + 1
    
    for digit in string2:
        count2[digit] = count2.get(digit, 0) + 1

    return count1 == count2