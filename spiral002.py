#!/usr/local/bin/python3

from pyx import *
from ent import *
from math import *
import argparse

parser = argparse.ArgumentParser(description='Generate Vogel Spiral ps file')
parser.add_argument('-p', dest='points', type=int, action='store', help='the number of points to plot')
parser.add_argument('-f', dest='file', action='store', help='the ps file to write')

args = parser.parse_args()

print(args.file, args.points)
       
n = args.points
ca = canvas.canvas()

phi = (1 + sqrt(5)) / 2.0
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]

#text.defaulttexrunner.set(mode="latex")
#text.defaulttexrunner.preamble("\\usepackage{palatino}")

for j in range(n):   
    i = j + 1 
    r = sqrt(i)
    theta = i * 2 * pi  / (phi*phi)
    x = cos(theta)*r
    y = sin(theta)*r      
    #if i in fibs:
    #    ca.fill(path.circle(x,y,0.2), [color.rgb(0.6, 0.6,1.0)])
    #else:
    ca.fill(path.circle(x,y,0.6), [color.rgb(0.6, 0.6, 1.0)])
    ca.stroke(path.circle(x,y,0.6))
    
    #ca.text(x,y,"\\Large "+str(i), [text.halign.boxcenter, text.valign.middle])
    
           
d = document.document(pages = [document.page(ca, paperformat=document.paperformat.A4, fittosize=1)])
d.writePSfile(args.file)
