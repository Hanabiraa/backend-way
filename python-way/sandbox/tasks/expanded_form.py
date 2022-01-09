def expanded_form(num):
    """
    You will be given a number and you will need to return it as a string in Expanded Form. For example:

    expanded_form(12) # Should return '10 + 2'
    expanded_form(42) # Should return '40 + 2'
    expanded_form(70304) # Should return '70000 + 300 + 4'
    NOTE: All numbers will be whole numbers greater than 0.
    """
    num = str(num)
    len_ = len(num)

    result = [
        dig + '0' * (len_ - shift)
        for shift, dig in enumerate(num, 1)
        if dig != '0'
    ]
    return(' + '.join(result))


for num in (12, 42, 105, 70304):
    print(expanded_form(num))
