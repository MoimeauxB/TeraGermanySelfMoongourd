import numpy as np
import os
from PIL import Image
from os import listdir



x,y = round(50),round(50)


#récup les imgs
#changer le path pour vos usages
classname = "berzerker"
folder_dir = "C:\\Users\\astek\\Desktop\\TERA-Germany\\autre\\moongourdSelf\\skillsImg\\"+classname+"\\"
for image in os.listdir(folder_dir):
	print("image : ", image)
	if image.endswith(".PNG") or  image.endswith(".webp"):
		imageF = Image.open(image)
		imageF = imageF.convert('RGB')
		imageF = imageF.resize((x,y))
		imageF.save(fp=image[2:])
