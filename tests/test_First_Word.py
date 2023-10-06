import First_Word as fw

def test_first_word(text: str) -> str:

    # These "asserts" are used for self-checking
    assert fw.first_word("Hello world") == "Hello"
    assert fw.first_word("a word") == "a"
    assert fw.first_word("greeting from CheckiO Planet") == "greeting"
    assert fw.first_word("hi") == "hi"

    print("The mission is done! Click 'Check Solution' to earn rewards!")
