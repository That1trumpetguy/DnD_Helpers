# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:26:23 2023

@author: rebel
"""

import sqlite3
import csv


def DataGetter ():

    # Step 1: Convert Excel CSV to SQLite database
    csv_file = 'Popular_Baby_Names.csv'
    db_file = 'DnD_Namer1.db'
    
    # Create a SQLite database and establish a connection
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Step 2: Define the table structure
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS DnD_Namer1 (
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
            cursor.execute('INSERT INTO DnD_Namer1 (Year_of_Birth, Gender, Ethnicity, Childs_First_Name, Count, Rank) VALUES (?, ?, ?, ?, ?, ?)',
                           (int(row['Year of Birth']), row['Gender'], row['Ethnicity'], row['Child\'s First Name'], int(row['Count']), int(row['Rank'])))
    
    conn.commit()
    
    # Step 4: Query the database using Python
    query = "SELECT Gender, Ethnicity, Childs_First_Name FROM DnD_Namer1"
    #year_of_birth = 2011  # Example: Replace with your desired year of birth
    cursor.execute(query)
    
    #returns results which is in the form of a list of tuples
    results = cursor.fetchall()
    
    #close the connection
    conn.close()
    return results