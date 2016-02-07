# -*- coding: utf-8 -*-
from tforms.control import TextField, Button, Submit
from tforms.validator import Validator


class Form(object):

    VERSION = "0.1"

    def __init__(self):
        self.components = {}
        self.on_success = []
        self.on_error = []

    def add_text(self, name, label=""):
        """
        :param name: string
        :param label: string
        :return: TextField
        """
        component = TextField(name, label)
        return self._add_component(name, component)

    def add_button(self, name, label=""):
        component = Button(name, label)
        return self._add_component(name, component)

    def add_submit(self, name, label=""):
        component = Submit(name, label)
        return self._add_component(name, component)

    def _add_component(self, name, component):
        self.components[name] = component
        return component

    def validate(self, response):
        valid = True
        for field, component in self.components.items():
            Validator.validate(component, response)
            if not component.is_valid():
                valid = False

        if valid:
            for callback in self.on_success:
                callback()
            return True

        for callback in self.on_error:
            callback()
        return False

    def __getitem__(self, item):
        if item in self.components:
            return self.components[item]


    def __iter__(self):
        for field, value in self.components.items():
            yield field, value

