import  rp_poetry.is_even as ie

def test_is_even():

    # These "asserts" are used for self-checking
    assert ie.is_even(2) == True
    assert ie.is_even(5) == False
    assert ie.is_even(0) == True

    print("The mission is done! Click 'Check Solution' to earn rewards!")
