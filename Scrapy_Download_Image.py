from imutils import paths
import requests
import cv2
import os

rows = open(os.getcwd()+r"/swift.txt").read().strip().split("\n")
print(len(rows))
total = 2600

for url in rows:
    try:
        r = requests.get(url, timeout=60)
        p = os.path.sep.join([r"/swift", "{}.jpg".format(str(total).zfill(8))])
        f = open(p, "wb")
        f.write(r.content)
        f.close()
        print("[INFO] downloaded: {}".format(p))
        total += 1
        
    except:
        print("[INFO] error downloading {}...skipping".format(p))
        print("Exception")
        
for imagePath in paths.list_images(r"/swift"):
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
