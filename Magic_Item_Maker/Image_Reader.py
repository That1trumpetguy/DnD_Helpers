#This is an attempt to use unstructured as a way to read informatiton off of images for magic item stat-blocks

"""
TO-DO: 
pip install all relevant packadges
-unstructured[all-docs]
-libmagic-dev
-poppler-utils
-tesseract-ocr
-libreoffice
-pandoc

From there I need to make sure that my unstructured
is working using the following code block
"""
#%%

from unstructured.partition.auto import partition

elements = partition(filename="example-docs/eml/fake-email.eml")
print("\n\n".join([str(el) for el in elements]))

#%%

#import block
import numpy as np
