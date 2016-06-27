#!/usr/local/bin/python3

import argparse
from ent import *
from math import *
from pyx import *
from dxfwrite import DXFEngine as dxf

parser = argparse.ArgumentParser(description='Generate Vogel Spiral in DXF format')

parser.add_argument('-p', dest='points', type=int, action='store', help='Number of holes')
parser.add_argument('-o', dest='offset', type=int, action='store', help='Distance of the gap in the center')
parser.add_argument('-c', dest='constant', type=int, action='store', help='Distance between holes')
parser.add_argument('-f', dest='file', action='store', help='The file to write')

args = parser.parse_args()
print(args.file, args.points)
       
# number of points to plot

n = args.points
drawing = dxf.drawing(args.file)

# set unit of measurement to mm
drawing.header['$LUNITS'] = 4

phi = (1 + sqrt(5)) / 2.0
center_offset = args.offset
constant = args.constant

for j in range(n):   
    i = j + center_offset

    r = sqrt( i * constant)
    theta = i * 2 * pi / (phi*phi)

    x = cos(theta)*r
    y = sin(theta)*r      

    # draw the circle
    circle = dxf.circle(radius=6, center=(x, y)) 
    circle['color'] = 7
    drawing.add(circle)
    
    #ca.text(x,y,"\\Large "+str(i), [text.halign.boxcenter, text.valign.middle])

drawing.save()
