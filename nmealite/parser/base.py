from ..nmealite import NMEASentence


class NMEAParser(NMEASentence):
    """ Standard NMEA parser super class. """
    id = str  # Three character identification for NMEA string
    fields = tuple  # Tuple[str]  --  data fields

    def __init__(self, talker: str, data: tuple):
        """
        Initialize parser

        :param talker: Two character talker identification
        :param data: (List[str]) Supplied sentence data
        """
        self.talker = talker
        self.sentence_type = self.id
        self.data = list(data)

    def identifier(self):
        """ Generate full five character NMEA sentence identifier """
        return '%s%s,' % (self.talker, self.sentence_type)

    def get(self, data_id):
        """ Get data value by field name. """
        i = self.fields.index(data_id)
        return self.data[i]

