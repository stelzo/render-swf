import cairosvg
import sys

inp = sys.argv[1]
out = sys.argv[2]
size = sys.argv[3]

width = size
height = size
output_png_path = out
input_svg_path = inp

# read svg file -> write png file
cairosvg.svg2png(url=input_svg_path, write_to=output_png_path, output_width=width, output_height=height)
