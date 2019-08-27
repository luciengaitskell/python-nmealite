from .util import reg_parser, lookup


def parser(cls):
    """ Decorator to define new parser class. """
    reg_parser(cls)
    return cls


