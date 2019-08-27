""" Parser registration and management. """

_lookup = {}


def reg_parser(cls):
    """ Register parser class in lookup table. """
    _lookup[cls.id] = cls


def lookup(parser_id: str):
    """ Preform lookup in table and return matching parser (by three character id). """
    return _lookup.get(parser_id, None)
