# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:57:08 2023

@author: That1trumpetguy
"""


#imports the ability to randomy assign an integer
from random import randint

#custom classes to make and read from databases

#import DBMaker 
import DBReader
import APICaller

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
    #I need to make the API query return a dict of names in the same format as the db query
    
    #a dict. of names with the name as the key and null as the value
    resultsAPI = APICaller.CALLAPI()
    
    # A dict. of names, with the name as the key and null as the value
    resultsDB = DBReader.DbtoDict()
    
    lookAPI = randint(0, len(resultsAPI)-1)
    lookDB = randint(0, len(resultsDB)-1)
    
    lname = resultsAPI[lookAPI]
    fname = resultsDB[lookDB]
    
    print(fname, lname)
    
   
 
    
main()

