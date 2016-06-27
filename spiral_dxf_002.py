#!/usr/local/bin/python3

import argparse
import json
from ent import *
from math import *
from pyx import *
from dxfwrite import DXFEngine as dxf

parser = argparse.ArgumentParser(description='Generate Vogel Spiral in DXF format')

parser.add_argument('-p', dest='points', type=int, action='store', help='Number of holes')
parser.add_argument('-c', dest='constant', type=int, action='store', help='Magic constant for spacing')
parser.add_argument('-o', dest='offset', type=int, action='store', help='Distance of the gap in the center')
parser.add_argument('-f', dest='file', action='store', help='The file to write')
parser.add_argument('--color', dest='rgb_mode', default=False, action='store_true', help='Turn on RGB mode')

args = parser.parse_args()
print(args.file, args.points)

# number of points to plot

n = args.points
drawing = dxf.drawing("%s.dxf" % args.file)

# set unit of measurement to mm
drawing.header['$LUNITS'] = 4

phi = (1 + sqrt(5)) / 2.0

offset = args.offset
constant = args.constant

rgb = args.rgb_mode
color = [1, 5, 3]

radius = 6
# buckets for the inner / outer circle radii, so we can choose a good min
z1 = []
z2 = []

points=[]

# All the small holes
for j in range(n):
    i = j + offset

    r = sqrt( i * constant)
    theta = i * 2 * pi / (phi*phi)

    x = cos(theta)*r
    y = sin(theta)*r

    points.append({"point": [x/100, y/100, 0.00]})

    # inner / outer circle radii population
    z1.append(sqrt(x**2 + y**2))
    z2.append(sqrt(x**2 + y**2))

    # draw a small circle
    circle = dxf.circle(radius=radius, center=(x, y))

    if rgb == True:
      circle['color'] = color[j % 3]
    else:
      circle['color'] = 0
    drawing.add(circle)

# inner / outer circle radii chooser
inner_perimiter = min(z1) - (radius*2)
outer_perimiter = max(z2) + (radius*2)

for value in inner_perimiter, outer_perimiter:
    circle = dxf.circle(radius=value, center=(0, 0))
    circle['color'] = 9
    drawing.add(circle)

# save the DXF file
drawing.save()

with open('%s.json' % args.file, 'w') as jsonfile:
    json.dump(points, jsonfile)
