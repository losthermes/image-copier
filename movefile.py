import os
import shutil

source = os.walk(r'C:\Users\losth\Desktop\New folder')
destnation = r"C:\Users\losth\Desktop\copied"
num = 0


for root, dirs, files in source:
   for name in files:
       item = os.path.join(root, name)
       newName = "picture" + str(num) + ".png"
       newdest = os.path.join(destnation, newName)    
       shutil.copy2(item , newdest)
       num += 1
       



