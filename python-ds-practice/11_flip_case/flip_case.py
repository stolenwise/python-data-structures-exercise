def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = []
    for char in phrase:
        if char.lower() == to_swap.lower():
            # flip case here
            if char.islower():
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            #keep char as it is
            result.append(char)
    return ''.join(result) # make new lst into a string