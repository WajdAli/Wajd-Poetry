def test_is_acceptable_password(password: str) -> bool:

    # These "asserts" are used for self-checking
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False

    print("The mission is done! Click 'Check Solution' to earn rewards!")
