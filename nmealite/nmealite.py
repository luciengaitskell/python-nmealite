"""
nmealite: a lightweight NMEA en/decoder for Python and MicroPython.

Written by Lucien Gaitskell (2019), intended for BoatX.
Used work by Knio on pynmea2 [https://github.com/Knio/pynmea2].
"""

from .codec import *  # Message en/decoder regex strings
from .verif import checksum as gen_checksum
from .parser import lookup


class NMEASentence:
    """ Base NMEA sentence, and handler """
    data = ValueError  # Data value is set in subclass instantiation

    @staticmethod
    def parse(raw: str):
        """ Parse a raw sentence string, and return appropriate parser class. """
        match = SENTENCE_RE.match(raw)
        if not match:
            raise ValueError('invalid data: ', raw)

        nmea_str = match.group('nmea_str')
        checksum = match.group('checksum')
        sentence_type = match.group('sentence_type').upper()
        data = match.group('data').split(',')

        if checksum:
            cs1 = int(checksum, 16)
            cs2 = gen_checksum(nmea_str)
            if cs1 != cs2:
                raise ValueError(
                    'checksum does not match: %02X != %02X' % (cs1, cs2), data)

        talker_match = TALKER_RE.match(sentence_type)
        if talker_match:
            talker = talker_match.group('talker')
            sentence = talker_match.group('sentence')
            talker_cls = lookup(sentence)

            if not talker_cls:
                # TODO instantiate base type instead of fail
                raise ValueError(
                    'Unknown sentence type %s' % sentence_type, raw)
            return talker_cls(talker, data)

        raise ValueError(
            'could not parse sentence type: %r' % sentence_type, raw)

    def identifier(self):
        """ To be implemented by subclassing parser. """
        raise NotImplementedError

    def render(self, checksum=True, dollar=True, newline=False):
        """ Render NMEA sentence in string form. """
        res = self.identifier() + ','.join(self.data)
        if checksum:
            res += '*%02X' % gen_checksum(res)
        if dollar:
            res = '$' + res
        if newline:
            res += (newline is True) and '\r\n' or newline
        return res

    def __str__(self):
        return self.render()
