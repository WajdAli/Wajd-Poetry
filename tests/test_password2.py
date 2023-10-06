import password2

def is_acceptable_password(password: str) -> bool:

    # These "asserts" are used for self-checking
    assert password2.is_acceptable_password("short") == False
    assert password2.is_acceptable_password("muchlonger") == False
    assert password2.is_acceptable_password("ashort") == False
    assert password2.is_acceptable_password("muchlonger5") == True
    assert password2.is_acceptable_password("sh5") == False

    print("The mission is done! Click 'Check Solution' to earn rewards!")
