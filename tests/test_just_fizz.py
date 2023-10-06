def test_checkio(num: int) -> str:

    # These "asserts" are used for self-checking
    assert checkio(15) == "Fizz"
    assert checkio(6) == "Fizz"
    assert checkio(10) == "10"
    assert checkio(7) == "7"

    print("The mission is done! Click 'Check Solution' to earn rewards!")
