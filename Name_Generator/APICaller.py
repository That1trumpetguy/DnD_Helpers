# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:49:14 2023

@author: rebel
"""

import requests



def CALLAPI():
    
    url = 'https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61766&view=co'
    req = requests.get(url)
    
    #this gives a fill list, with the names concentiated on each other
    tname = req.text
    #print(tname)
    
    #this saves the names as individual entries in a list
    indiv = tname.split()
    #making an empty dictionary where we will store the names
    dictA = {}
    for i in range(len(indiv)):
        name = indiv[i]
        dictA[i] = name
        
   
    return dictA