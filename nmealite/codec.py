""" Decoding expressions for NMEA 0183"""
import re


#  Wonderful regex string
#   Head banging done by Knio: https://github.com/Knio/pynmea2
#   Slightly modified/simplified
SENTENCE_RE = re.compile(r'''
        # start of string, optional whitespace, optional '$'
        ^\s*\$?

        # message (from '$' or start to checksum or end, non-inclusve)
        (?P<nmea_str>
            # sentence type identifier
            (?P<sentence_type>
                # query sentence, ie: 'CCGPQ,GGA'
                # NOTE: this should have no data
                (\w{2}\w{2}Q,\w{3})|

                # talker sentence, ie: 'GPGGA'
                (\w{2}\w{3},)
            )

            # rest of message
            (?P<data>[^*]*)

        )
        # checksum: *HH
        (?:[*](?P<checksum>[A-F0-9]{2}))?

        # optional trailing whitespace
        \s*[\r\n]*$
        ''', re.X | re.IGNORECASE)

TALKER_RE = \
    re.compile(r'^(?P<talker>\w{2})(?P<sentence>\w{3}),$')
QUERY_RE = \
    re.compile(r'^(?P<talker>\w{2})(?P<listener>\w{2})Q,(?P<sentence>\w{3})$')
