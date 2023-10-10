import rp_poetry.password2

def test_is_acceptable_password():

    # These "asserts" are used for self-checking
    assert password2.is_acceptable_password("short") == False
    assert password2.is_acceptable_password("muchlonger") == False
    assert password2.is_acceptable_password("ashort") == False
    assert password2.is_acceptable_password("muchlonger5") == True
    assert password2.is_acceptable_password("sh5") == False

