# -*- coding: utf-8 -*-
from mock import mock
from tforms.control import Control
from tforms.validator import Validator
from tforms.form import Form


def test_version():
    assert Form.VERSION == "0.1"


def test_adding_components():

    form = Form()
    control = form.add_text("name", "Name:")
    assert control == form["name"]

def test_required_param():
    form = Form()
    control = form.add_text("first_name", "Enter your first name")\
        .set_required()

    assert control.required == True
    assert form["first_name"].required == True

def test_component_iteration():
    form = Form()
    form.add_text("text")
    form.add_text("first_name")
    form.add_text("last_name")

    for key, item in form:
        assert isinstance(item, Control)


def on_success_dummy():
    pass

def on_error_dummy():
    pass

def test_field_rules_and_callback():
    form = Form()
    form.add_text("description", "Description")\
        .add_rule(Validator.INTEGER, "Please provide integer")

    form.add_text("first_name", "First Name:")\
        .set_required()

    form.add_button("reset", "Reset")
    form.add_submit("save", "Save")

    response = {
        "description":1,
        "first_name": "Test",
        "save": True
    }

    with mock.patch("tests.form_test.on_success_dummy") as on_success_called:
        form.on_success.append(on_success_called)
        assert form.validate(response) == True
        on_success_called.assert_called_with()

    response = {
        "description": "test",
        "save": True
    }

    with mock.patch("tests.form_test.on_error_dummy") as on_error_called:
        form.on_error.append(on_error_called)
        assert form.validate(response) == False
        assert form["first_name"].is_valid() == False
        assert form["description"].is_valid() == False
        on_error_called.assert_called_with()

