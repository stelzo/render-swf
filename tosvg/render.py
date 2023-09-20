from swf.movie import SWF
from swf.export import SVGExporter
import sys

inp = sys.argv[1]
out = sys.argv[2]

# create a file object
file = open(inp, 'rb')

# load and parse the SWF
swf = SWF(file)

# create the SVG exporter
svg_exporter = SVGExporter()

# export!
svg = swf.export(svg_exporter)

# save the SVG
open(out, 'wb').write(svg.read())

