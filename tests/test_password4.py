import password4

def is_acceptable_password(password: str) -> bool:

    # These "asserts" are used for self-checking
    assert password4.is_acceptable_password("short") == False
    assert password4.is_acceptable_password("short54") == True
    assert password4.is_acceptable_password("muchlonger") == True
    assert password4.is_acceptable_password("ashort") == False
    assert password4.is_acceptable_password("notshort") == False
    assert password4.is_acceptable_password("muchlonger5") == True
    assert password4.is_acceptable_password("sh5") == False
    assert password4.is_acceptable_password("1234567") == False
    assert password4.is_acceptable_password("12345678910") == True

    print("The mission is done! Click 'Check Solution' to earn rewards!")
