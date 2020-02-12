from PIL import Image
from imutils import paths
import requests
import cv2
import os


path = os.path.abspath(r"D:\capstone  data\New folder (2)/Maruthi Suzuki Swift") ###OLD FOLDER PATH
def get_imlist(path):
  lis = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.png')]
  return lis
c = get_imlist(path)

s = 0
for i in c:
    s +=1
    if i.endswith('.jpeg') or i.endswith('.jpg') or i.endswith('.png'):
        try:
            im = Image.open(i)
            im = im.resize((32, 32),Image.ANTIALIAS)
            im.save(r"D:\capstone  data\Resized\maruthi 32//01"+str(s)+".png") ###TO SAVE FOLDER OR NEW FOLDER PATH
        except IOError:
            print ("cannot create thumbnail for '%s'" % i)


for imagePath in paths.list_images(r"D:\capstone  data\Resized\Maruthi Suzuki Swift//"):  ####NEW FOLDER PATH
  
  delete = False
  
  try:
    image = cv2.imread(imagePath)
    
    if image is None:
      delete = True
      
  except:
    print("Except")
    delete = True
        
  if delete:
    print("[INFO] deleting {}".format(imagePath))
    os.remove(imagePath)
