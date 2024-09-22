# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:24:29 2024

@author: That1trumpetguy
"""

#%% 
import matplotlib as mp
import pandas as pd
import numpy as np
#import Path

#%%
def read_csv (path):
    """
    Parameters
    ----------
    path : TYPE
        DESCRIPTION.

    Returns
    -------
    dframe : TYPE
        DESCRIPTION.

    """
    temp = pd.read_csv(path)
    dframe = temp.transpose()
    
    execute_time = dframe.iloc[1,0]
    clock_time = dframe.iloc[1,1]
    
    return execute_time, clock_time

#%%
def main():
    paths = ["F:/Documents/500_7_PythonResults.csv"]
    my_dict ={}
    f = 1
    for item in paths:
        execute, clock = read_csv(item)
        my_dict[f"example name {f}"] = [execute, clock]
        f += 1
    
    working = pd.DataFrame(my_dict)
    
    print("You are done")
#%%    
main()