from rp_poetry import mult_two as mt
import pytest
def test_mult_two():

    assert mt.mult_two(3, 2) == 6
    assert mt.mult_two(0, 1) == 0

