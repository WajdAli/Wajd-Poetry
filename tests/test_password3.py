import rp_poetry.password3

def is_acceptable_password():

    # These "asserts" are used for self-checking
    assert password3.is_acceptable_password("short") == False
    assert password3.is_acceptable_password("muchlonger") == False
    assert password3.is_acceptable_password("ashort") == False
    assert password3.is_acceptable_password("muchlonger5") == True
    assert password3.is_acceptable_password("sh5") == False
    assert password3.is_acceptable_password("1234567") == False

    print("The mission is done! Click 'Check Solution' to earn rewards!")
