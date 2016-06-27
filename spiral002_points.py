#!/usr/local/bin/python3

from pyx import *
from ent import *
from math import *
import argparse
import json

parser = argparse.ArgumentParser(description='Generate Vogel Spiral ps file')
parser.add_argument('-p', dest='points', type=int, action='store', help='the number of points to plot')
parser.add_argument('-f', dest='file', action='store', help='the ps file to write')

args = parser.parse_args()

print(args.file, args.points)
       
n = args.points
ca = canvas.canvas()

phi = (1 + sqrt(5)) / 2.0

points=[]

for j in range(n):   
    i = j + 1 
    r = sqrt(i)
    theta = i * 2 * pi  / (phi*phi)
    x = cos(theta)*r
    y = sin(theta)*r      
    points.append({"point": [x, y, 0.00]})
    
           
d = document.document(pages = [document.page(ca, paperformat=document.paperformat.A4, fittosize=1)])
#d.writePSfile(args.file)
