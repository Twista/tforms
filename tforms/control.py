# -*- coding: utf-8 -*-

class Control(object):

    def __init__(self, name, label):
        self.name = name
        self.label = label
        self.required = False
        self.rules = []
        self.errors = []


    def set_required(self, message=None):
        self.required = True
        if message is None:
            message = "Field {} is mandatory.".format(self.name)
        self.required_message = message
        return self

    def is_required(self):
        return self.required

    def is_valid(self):
        return len(self.errors) == 0

    def add_rule(self, type, message, arguments=None):
        self.rules.append((type, message, arguments))

    def add_error(self, message):
        self.errors.append(message)

class Input(Control):
    _tag = "input"

class TextField(Input):
    _type = "text"

class TextArea(Control):
    _tag = "textarea"

class Button(Control):
    _tag = "button"
    _type = "button"


class Submit(Button):
    _type = "submit"
