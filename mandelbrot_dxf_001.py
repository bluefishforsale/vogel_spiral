#!/usr/local/bin/python3

import argparse
from ent import *
from math import *
from pyx import *
import numpy as np
from dxfwrite import DXFEngine as dxf

parser = argparse.ArgumentParser(description='Generate Vogel Spiral in DXF format')

parser.add_argument('-p', dest='points', type=int, action='store', help='Number of holes')
parser.add_argument('-f', dest='file', action='store', help='The file to write')

args = parser.parse_args()
print(args.file, args.points)
       
# number of points to plot
n = args.points

drawing = dxf.drawing(args.file)

# set unit of measurement to mm
drawing.header['$LUNITS'] = 4

def draw_circles(drawing, x, y, points):
    circle = dxf.circle(radius=6, center=(x, y)) 
    circle['color'] = 7
    drawing.add(circle)
    

def mandelbrot(z, maxiter):
    c = z
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return maxiter


def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,[mandelbrot(complex(r, i),maxiter)
            for r in r1 for i in r2])

print(mandelbrot_set(0, 1000, 0, 1000, 10, 10, n))

#for x, y in mandelbrot_set(0, 1000, 0, 1000, 10, 10, n):
    #draw_circles(drawing, x, y)
  

drawing.save()

"""
(array([    0.        ,   111.11111111,   222.22222222,   333.33333333,
         444.44444444,   555.55555556,   666.66666667,   777.77777778,
         888.88888889,  1000.        ]), array([    0.        ,   111.11111111,   222.22222222,   333.33333333,
         444.44444444,   555.55555556,   666.66666667,   777.77777778,
         888.88888889,  1000.        ]), [170000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
"""
