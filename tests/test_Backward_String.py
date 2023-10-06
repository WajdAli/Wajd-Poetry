import Backward_String as bs

def test_backward_string(val: str) -> str:

    # These "asserts" are used for self-checking
    assert bs.backward_string("val") == "lav"
    assert bs.backward_string("") == ""
    assert bs.backward_string("ohho") == "ohho"
    assert bs.backward_string("123456789") == "987654321"

    print("The mission is done! Click 'Check Solution' to earn rewards!")
