#!/bin/env python3.5

import math

def test_func(x):
    return x*x*x+1.1*x*x+0.9*x-1.4

def df_test_func(x):
    return 3*x*x+2.2*x+0.9

    
# binary seperation
def binary_seperation(func, x, ap=0.001):
    list(x).sort()
    x2 = x.pop()
    x1 = x.pop()
    y1 = func(x1)
    y2 = func(x2)
    if y1 == 0:
        return x1
    if y2 == 0:
        return x2
    if y1*y2 > 0:
        return "" 
    while True:
        avg_x = (x1 + x2)/2
        avg_y = func(avg_x)
        if avg_y*y1 > 0:
            x1 = avg_x
        elif avg_y*y2 > 0:
            x2 = avg_x
        elif avg_y == 0:
            return avg_x
        elif abs(x1-x2) < ap:
            return x1
        else:
            return ""

# tan line method          
def tanline(func, dfunc, x, ap=0.0001):
     list(x).sort()
     x2 = x.pop()
     x1 = x.pop()
     y1 = func(x1)
     y2 = func(x2)
     if y1 == 0:
         return x1
     if y2 == 0:
         return x2
     if y1*y2 > 0:
         return ""
     mid_y1 = func((x1+x2)/2)
     mid_y2 = (y1+y2)/2
     if mid_y1 < mid_y2:
         convex = -1
     else:
         convex = 1
     if y1*convex > 0:
         delta_x = x1
     elif y2*convex > 0:
         delta_x = x2
     while True:
         delta_y = func(delta_x)
         if abs(delta_y) < ap:
             return delta_x
         delta_x = delta_x - func(delta_x)/dfunc(delta_x)
     
                
if __name__ == '__main__':
    print(binary_seperation(test_func,[0,1] ))
    print(tanline(test_func, df_test_func, [0,1]))
            

    
        
