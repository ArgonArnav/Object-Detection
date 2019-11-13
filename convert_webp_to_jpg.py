import os
from PIL import Image

# images = []
# for filename in os.listdir('/home/rajat/Downloads/test/'):
# 	if filename.endswith(".webp"):
# 		im = Image.open(filename).convert("RGB")
# 		im.save("./","jpeg")
# 		print("Converted Successfully")
ctr = 1 
for (dirname, dirs, files) in os.walk("."):
	error_list = []
	for filename in files:
		try:
			if filename.endswith('.webp'):
				print('Found: ' + os.path.splitext(filename)[0])
				print('Converting to: ' + os.path.splitext(filename)[0] + '.jpg')
				im = Image.open(filename).convert("RGB")
				im.save(os.path.splitext(filename)[0] + '.jpg', "jpeg")
				print('Done converting\n')
				ctr=ctr+1
				print("count is : {}".format(str(ctr)))
		except:
			error_list.append(os.path.splitext(filename)[0])

print(error_list)	



