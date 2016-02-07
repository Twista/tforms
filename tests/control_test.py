# -*- coding: utf-8 -*-
from tforms.control import Control

def test_control_attributes():

    control = Control("name", "Label")
    assert control.name == "name"
    assert control.label == "Label"
    assert control.errors == []
    control.add_error("Label is required")
    assert len(control.errors) == 1
    assert control.is_required() == False
    control.set_required("This Field Is Required")
    assert control.is_required() == True

