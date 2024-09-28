#This is an attempt to use unstructured as a way to read informatiton off of images for magic item stat-blocks

"""
TO-DO: 
pip install all relevant packadges
-unstructured[all-docs] Done
-libmagic-dev
-poppler-utils Done
-tesseract-ocr Installed Pytesseract instead
-libreoffice
-pandoc Donepip 

From there I need to make sure that my unstructured
is working using the following code block
"""
#%%

from unstructured.partition.auto import partition
import magic

elements = partition(filename=r"C:\Users\rebel\Downloads\6a8916901dbf9c79aec8ef388d34a848.jpg")
print("\n\n".join([str(el) for el in elements]))

#%%

#import block
import numpy as np
