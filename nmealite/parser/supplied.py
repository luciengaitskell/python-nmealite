""" Pre-packaged NMEA parsers. """

from .base import NMEAParser
from . import parser


@parser
class GGA(NMEAParser):
    """ Standard GGA GPS data sentence. """
    id = "GGA"
    fields = (
        'timestamp',
        'lat',
        'lat_dir',
        'lon',
        'lon_dir',
        'gps_qual',
        'num_sats',
        'horizontal_dil',
        'altitude',
        'altitude_units',
        'geo_sep',
        'geo_sep_units',
        'age_gps_data',
        'ref_station_id'
    )
