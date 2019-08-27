""" Data verification tools """


def checksum(raw):
    """
    Generate checksum for command string.
    :param raw: str
        Input command string

    taken from my own library: https://github.com/luciengaitskell/row-plat/blob/feature/simplified/coproc/devices/xa1110.py
    """
    t = 0

    raw = raw.encode('ascii')

    for i in range(0, len(raw)):
        t = t ^ raw[i]

    return t

