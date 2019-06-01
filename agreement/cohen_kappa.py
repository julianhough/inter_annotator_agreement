from __future__ import division
from collections import defaultdict
import math


#A script to do Kappa comparison for a given number of annotators

# -*- coding: utf-8 -*-
"""
file   multikappa.py
author Ernesto P. Adorio, Ph.D.
       UPDEPP Pampanga at Clarkfield
email  ernesto.adorio@gmail.com
license educational use only.
           attribution or citation requested.
references
     Siegel and Castellan, "Nonparametric Statistics for the
       Behavioral Sciences", 2nd Ed., McGraw-Hill Book Co., 1988
       Sec. 9.8, pp 284-291
"""


 
def multikappa(Data, k):
    """
    Computes kappa for the multi raters case with k raters.
    
    Data is a two-dimensional matrix
    where the columns represent categories
    and rows the subject/object being tested.
    
    In Data, each row is for a particular object and category. Each column is the given category
    for example in data below, the first row 0, there was perfect agreement among 4 raters in category 5 (column 4) for object 1, 
    on the other hand in the second row , there were two raters agreed on it being category 1, and two raters agreed on putting it in category 3
    >>data = [[0,0,0,0,4],
    >>        [2,0,2,0,0]]
    """
    
    N = len(Data)
    m = len(Data[0])
 
    C =[0] * m
    P =[0] * m
 
    # OPTIMIZATION WILL BE DONE LATER.
    tot  = 0.0
    tot2 = 0.0
    PA   = 0.0
    K = 1/((k-1.0)*k)
    for i, d in enumerate(Data):
        t  = 0.0
        for j, e in enumerate(d):
            if e > 0:
                t  += e * (d[j]- 1.0)
 
        Si = K * t
        PA += Si
 
        tot  += sum([e for e in d])
        tot2 += sum([e*e for e in d])
        for j in range(m):
            C[j]+= d[j]
    for j in range(m):
        P[j] = C[j] / float(tot)
    PE = sum([ p * p for p in P])
    PA /= N
    if PE == 1.0:
        Kappa = 0
    else:
        Kappa = (PA- PE)/(1.0 - PE)
 
    # Test statistic for large N.
    if PE == 1.0:
        varK = 0
        z = 0
    else:
        varK = 2.0/(N*k*(k-1.0))* (PE-(2*k-3)*PE**2 +\
           2 * (k-2) * sum([pj**3 for pj in P]))/ \
           (1 - PE)**2
        z = Kappa/math.sqrt(varK)
    print "Kappa = ", Kappa
    print "z = ", z
    print "PA = ", PA
    print "PE = ", PE
    return Kappa, z, varK,  PA, PE
 
def Test():
    """
     Example data from Siegel and Castellan, Nonparametrics Statistics for
     the Behavioral Sciences 
     each row is for a particular object and category. each column is the given category
     for example in the first row 0, there was perfect agreement among 4 raters in category 5 (column 4) for object 1, 
     on the other hand in the second row , there were two raters agreed on it being category 1, and two raters agreed on putting it in category 3
     
     """
    #===========================================================================
    data = [[0,0,0,0,4],
            [2,0,2,0,0],
            [0,0,0,0,4],
            [2,0,2,0,0],
            [0,0,0,1,3],
            [1,1,2,0,0],
            [3,0,1,0,0],
            [3,0,1,0,0],
            [0,0,2,2,0],
            [3,0,1,0,0],
            [0,0,0,0,4],
            [4,0,0,0,0],
            [4,0,0,0,0],
            [4,0,0,0,0],
            [0,0,3,1,0],
            [1,0,2,1,0],
            [0,0,0,2,2],
            [0,0,0,0,4],
            [0,0,3,0,1],
            [0,1,3,0,0],
            [0,0,1,0,3],
            [0,0,3,1,0],
            [4,0,0,0,0],
            [4,0,0,0,0],
            [2,0,2,0,0],
            [1,0,3,0,0],
            [2,0,2,0,0],
            [2,0,2,0,0],
            [0,1,2,0,1]
            ]
    k = 4
    multikappa(data, k)

if __name__ == "__main__":
    Test()