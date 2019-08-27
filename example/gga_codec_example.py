from nmealite import NMEASentence
from nmealite.parser.supplied import GGA

# Create example NMEA sentence (GPS GGA):
s = GGA('GP', ('184353.07', '1929.045', 'S', '02410.506', 'E', '1', '04', '2.6', '100.00', 'M', '-33.9', 'M', '', '0000'))
print(s.render())  # Print as ascii string

print("\nRe-Parse Data:")

# Attempt to parse output:
new = NMEASentence.parse(s.render())
print(new.data)  # Print all data extracted
print("ts: ", new.get('timestamp'))  # Isolate 'timestamp'

