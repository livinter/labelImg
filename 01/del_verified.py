import glob
import os
xmls = glob.glob("*.xml")
for file in xmls:
   jpg = file.replace(".xml",".jpg")
   if os.path.isfile(jpg):
     if open(file).read().find('annotation verified="yes"')>0:
       print ("del ",file)
       print ("del ", jpg)
       os.remove(file)
       os.remove(jpg)
   else:
     os.remove(file)  # delete .xml if there is not jpg
     print ("del ", file)

