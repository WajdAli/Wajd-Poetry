def test_first_word(text: str) -> str:

    # These "asserts" are used for self-checking
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("greeting from CheckiO Planet") == "greeting"
    assert first_word("hi") == "hi"

    print("The mission is done! Click 'Check Solution' to earn rewards!")
