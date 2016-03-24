dataFile = open("train_images10.txt", "w")
for line in range(400):
    dataFile.write("/home/nithin/deep-learning/caffe/data/font_style/images/verdana/"+str(line+1)+".tif\n")
dataFile.close()