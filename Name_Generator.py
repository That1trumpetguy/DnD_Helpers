# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:57:08 2023

@author: That1trumpetguy
"""
#Look into exactly what this does
import requests

#imports the ability to randomy assign an integer
from random import randint
import sqlite3
import csv

"""
 IDEAS:
     
     I can make a set of 3 lists, each one containing first, middle, and last names respectivley
     I can then start bu pulling from the API as I am currently doing
     
     Then I can attempt to find a text document and and excel sheet of names and pull from those as well
     Then I can step through the general list and reduce its size by sorting out the duplicates (This would 
    be some optimization practice)
     
     Finally from that trimmed list I can select a number of random names to generate for NPC's
     
     
 
 """
        
 

# Step 1: Convert Excel CSV to SQLite database
csv_file = 'Popular_Baby_Names.csv'
db_file = 'DnD_Namer1.db'

# Create a SQLite database and establish a connection
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Step 2: Define the table structure
create_table_query = '''
CREATE TABLE IF NOT EXISTS excel_data (
    Year_of_Birth INTEGER,
    Gender TEXT,
    Ethnicity TEXT,
    Childs_First_Name TEXT,
    Count INTEGER,
    Rank INTEGER
);
'''
cursor.execute(create_table_query)

# Step 3: Import data from CSV into the SQLite database
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cursor.execute('INSERT INTO excel_data (Year_of_Birth, Gender, Ethnicity, Childs_First_Name, Count, Rank) VALUES (?, ?, ?, ?, ?, ?)',
                       (int(row['Year of Birth']), row['Gender'], row['Ethnicity'], row['Child\'s First Name'], int(row['Count']), int(row['Rank'])))

conn.commit()

# Step 4: Query the database using Python
query = "SELECT Year_of_Birth, Gender, Ethnicity, Childs_First_Name FROM excel_data WHERE Year_of_Birth = ?"
year_of_birth = 1990  # Example: Replace with your desired year of birth
cursor.execute(query, (year_of_birth,))
results = cursor.fetchall()

for result in results:
    print(result)

# Close the connection


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
    print(indiv[fname] + " " + indiv[lname])
 
    
main()
conn.close()
