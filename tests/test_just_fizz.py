import  rp_poetry.just_fizz as jf

def test_checkio():

    # These "asserts" are used for self-checking
    assert jf.checkio(15) == "Fizz"
    assert jf.checkio(6) == "Fizz"
    assert jf.checkio(10) == "10"
    assert jf.checkio(7) == "7"

    print("The mission is done! Click 'Check Solution' to earn rewards!")
