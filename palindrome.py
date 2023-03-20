def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """

    value = value.lower().replace(" ","")
    rev_value = reversed(value)
    if list(value) == list(rev_value):
        return True
    else:
        return False
