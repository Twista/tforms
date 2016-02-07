# -*- coding: utf-8 -*-
from tforms.validator import Validator


def test_validator():

    # integer
    assert Validator.validate_integer("1", None) == False
    assert Validator.validate_integer(1, None) == True
    assert Validator.validate_integer(None, None) == False

    assert Validator.validate_blank("", None) == True
    assert Validator.validate_blank(None, None) == True
    assert Validator.validate_blank("test", None) == False

    assert Validator.validate_max_length("12345", 3) == False
    assert Validator.validate_max_length("12345", 5) == True

    assert Validator.validate_min_length("12345", 5) == True
    assert Validator.validate_min_length("12345", 6) == False

    assert Validator.validate_range(10, [0, 1]) == False
    assert Validator.validate_range(10, [0, 10]) == True

    assert Validator.validate_equal(10, 10) == True
    assert Validator.validate_equal(10, 20) == False

    assert Validator.validate_not_equal(10, 20) == True
    assert Validator.validate_not_equal(10, 10) == False



