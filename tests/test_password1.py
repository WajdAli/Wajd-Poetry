import rp_poetry.password1 as p1

def test_is_acceptable_password():

    # These "asserts" are used for self-checking
    assert p1.is_acceptable_password("short") == False
    assert p1.is_acceptable_password("muchlonger") == True
    assert p1.is_acceptable_password("ashort") == False

