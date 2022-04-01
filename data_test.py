#from ast import pattern
#from cgi import test
#import pyperclip
import re

#Example of what comes from /showlocation into the clipboard
cord = "Coordinates: x:-19023554105.376129 y:-2613925949.476050 z:-1802.328174"
#pyperclip.copy(s)

#Stripping the text from the string
pattern = r'[a-zA-Z]+:'
mod_string = re.sub(pattern,'', cord )

#making a full coordinate string with no leading space
fullCord = re.sub(r'^\s+', '', mod_string)
print(fullCord)

#seperating x,y,z into their respective float strings
cordX,cordY,cordZ = (mod_string.split())

float(cordX)
float(cordY)
float(cordZ)


"""
print(cord)

def useRegex(cord):
    pattern = re.compile(r"[a-zA-Z]+: x:([+-]?(?=\\.\\d|\\d)(?:\\d+)?(?:\\.?\\d*))(?:[eE]([+-]?\\d+))? y:([+-]?(?=\\.\\d|\\d)(?:\\d+)?(?:\\.?\\d*))(?:[eE]([+-]?\\d+))? z:([+-]?(?=\\.\\d|\\d)(?:\\d+)?(?:\\.?\\d*))(?:[eE]([+-]?\\d+))?")
    return pattern.match(cord, re.IGNORECASE)


print(useRegex)
"""