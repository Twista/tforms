# -*- coding: utf-8 -*-

class Validator(object):

    INTEGER = ":integer"
    MIN_LENGTH = ":min_length"
    MAX_LENGTH	= ":max_length"
    LENGTH	= ":length"
    RANGE	= ":range"
    BLANK	= ":blank"
    NOT_EQUAL	= ":not_equal"
    EQUAL = ":equal"


    @classmethod
    def validate(self, component, request_values):
        name = component.name

        if component.is_required() and name not in request_values:
            component.add_error(component.required_message)

        value = None
        if name in request_values:
            value = request_values[name]

        validation_methods = {
            Validator.INTEGER: Validator.validate_integer,
            Validator.BLANK: Validator.validate_blank,
            Validator.MIN_LENGTH: Validator.validate_min_length,
            Validator.MAX_LENGTH: Validator.validate_max_length,
            Validator.RANGE: Validator.validate_range,
            Validator.EQUAL: Validator.validate_equal,
            Validator.NOT_EQUAL: Validator.validate_not_equal,

        }
        for (rule, message, arguments) in component.rules:

            if not validation_methods[rule](value, arguments):
                component.add_error(message)


    @classmethod
    def validate_integer(cls, value, _):
        return isinstance(value, (int, long))

    @classmethod
    def validate_blank(cls, value, _):
        return value is None or value == ""

    @classmethod
    def validate_min_length(cls, value, count):
        return len(value) >= count

    @classmethod
    def validate_max_length(cls, value, count):
        return len(value) <= count

    @classmethod
    def validate_range(cls, value, rng):
        return value >= rng[0] and value <= rng[1]

    @classmethod
    def validate_equal(cls, value, eq):
        return value == eq

    @classmethod
    def validate_not_equal(cls, value, eq):
        return not Validator.validate_equal(value, eq)
