import Rectangle_Perimeter as rp

def test_rectangle_perimeter(length: int, width: int) -> int:

    # These "asserts" are used for self-checking
    assert rp.rectangle_perimeter(2, 4) == 12
    assert rp.rectangle_perimeter(3, 5) == 16
    assert rp.rectangle_perimeter(10, 20) == 60
    assert rp.rectangle_perimeter(7, 2) == 18
    assert rp.rectangle_perimeter(1, 1) == 4
    assert rp.rectangle_perimeter(1, 5) == 12
    assert rp.rectangle_perimeter(4, 1) == 10
    assert rp.rectangle_perimeter(100, 100) == 400
    assert rp.rectangle_perimeter(0.5, 2) == 5

    print("The mission is done! Click 'Check Solution' to earn rewards!")
