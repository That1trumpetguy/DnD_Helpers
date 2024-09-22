<<<<<<< Updated upstream:Name_Generator/Name_Generator.py
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

TO-DO:
    Implement a web scraper to try to acheve a larger variation of names

    Implement a gender tag/filter so that I can get a better handle on the names that I need

    Implement some level of cultural filter/association as an additional flag in DB so that I can generate more relevant names

    I could implement some level of UI so that this is more easily usable

    I also need a way to generate names more so from a fantasy standpoint -- I need rules and examles for this

STRETCH GOALS:

    Implement some level of location name generation logic

    Implement an NPC description generation logic to go with this

    Tie some level of this into WA and if possible, even into foundry
 """
        
def main ():
    #I need to make the API query return a dict of names in the same format as the db query
    
    #a dict. of names with the name as the key and null as the value
    resultsAPI = APICaller.CALLAPI()
    
    # A dict. of names, with the name as the key and null as the value
    resultsDB = DBReader.DbtoDict()
    
    lookAPI = randint(0, len(resultsAPI)-1)
    lookDB = randint(0, len(resultsDB)-1)
    #making comment for fun 
    lname = resultsAPI[lookAPI]
    fname = resultsDB[lookDB]
    
    print(fname, lname)
    
   
 
    
main()

=======

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
    #making comment for fun 
    lname = resultsAPI[lookAPI]
    fname = resultsDB[lookDB]
    
    print(fname, lname)
    
   
 
    
main()

>>>>>>> Stashed changes:Name_Generator.py
