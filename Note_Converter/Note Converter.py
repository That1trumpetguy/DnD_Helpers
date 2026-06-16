from PIL import Image
import pytesseract
import enum
import re
import os

class OS(enum.Enum): 
    Mac = 0 
    Windows = 1

class Language(enum.Enum):
    ENG = 'eng'
    
    
class Image_Reader:
    
    def __innit__(self):
        t_path = r"C:\Users\That1trumpetguy\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
        pytesseract.pytesseract.tesseract_cmd = t_path
        print("Running on Windows like a proper program")
            
    def Extract(self, path, language = 'eng'):
        img = Image.open(path)
        extracted_text = pytesseract.image_to_string(img, lang = language)
        return extracted_text
    
    def Writer(self, input):
        """
        A Custom Method to write the items parsed to text files
        Arg: text, a formatted string that is generated from the Extract method

        Returns: Null, should instead title and write to a text file
        """
        first_line = re.match(r'^.*$', input, re.MULTILINE)

        if first_line: # I ned to midify this to catch invalid names it is erroring on the potion of greater probability!
            fline = first_line.group().strip().lower()

        save_path = "F:\Pictures\Items"

        title = os.path.join(save_path, fline + ".txt")

        if (fline + ".txt") not in os.listdir(save_path):
            note = open(f"{title}", "x")
            note.write(input)
            note.close()
            print(f"File {title} written!")
        else:
            print(f"{title} is already written")



    
if __name__ == '__main__':
    ir = Image_Reader()
    directory = "F:\Pictures\Raw_Item"

    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        text = ir.Extract(path)
        ir.Writer(text)
    #print(text)