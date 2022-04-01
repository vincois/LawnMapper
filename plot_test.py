import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from mpl_toolkits.mplot3d import Axes3D
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
X, Y, Z = (mod_string.split())

float(X)
float(Y)
float(Z)

fig = plt.figure()
fig.set_size_inches(6, 6)
ax = fig.add_subplot(111, projection='3d')

ax.plot(X,Y,Z)

plt.show()