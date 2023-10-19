# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:57:08 2023

@author: That1trumpetguy
"""
#Look into exactly what this does
import requests

#imports the ability to randomy assign an integer
from random import randint

#custom classes to make and read from databases
import DBMaker 
import DBReader

"""
 IDEAS:
     
     I can make a set of 3 lists, each one containing first, middle, and last names respectivley
     I can then start bu pulling from the API as I am currently doing
     
     Then I can attempt to find a text document and and excel sheet of names and pull from those as well
     Then I can step through the general list and reduce its size by sorting out the duplicates (This would 
    be some optimization practice)
     
     Finally from that trimmed list I can select a number of random names to generate for NPC's
     
     
 
 """
        
def main ():
    
    
    url = 'https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61766&view=co'
    req = requests.get(url)
    
    #this gives a fill list, with the names concentiated on each other
    tname = req.text
    #print(tname)
    
    #this saves the names as individual entries in a list
    indiv = tname.split()
    #print(indiv)
    
    #this chooses a random name from the list based on its numbered position in the list
    fname = randint(0, len(indiv))
    lname = randint(0, len(indiv))
    
    results = DBReader.DbtoDict()
    
    
    print(indiv[fname] + " " + indiv[lname])
    
   
 
    
main()

