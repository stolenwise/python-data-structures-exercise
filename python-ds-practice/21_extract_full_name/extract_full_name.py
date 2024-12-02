def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    
    # think in code:
    # create an empty list full_names.
    # loop through each dictionary in teh people list
    # for each dictionary:
    #     extract the 'first' Value
    #     extract the 'last' value 
    #     combine them into a full name (e.g. "first last")
    # append the full name to full_names.
    # return full_names after the loop.    
    
    full_names = []

    for person in people:
        first = person['first']
        last = person['last']
        full_name = f"{first} {last}"
        full_name.append(full_name)
    
    return full_names