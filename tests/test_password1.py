import rp_poetry.password1

def test_is_acceptable_password():

    # These "asserts" are used for self-checking
    assert password1.is_acceptable_password("short") == False
    assert password1.is_acceptable_password("muchlonger") == True
    assert password1.is_acceptable_password("ashort") == False

