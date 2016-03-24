dataFile = open("test_images10.txt", "w")
for line in range(100):
    dataFile.write("/home/nithin/deep-learning/caffe/data/font_style/images/verdana/"+str(line+401)+".tif\n")
dataFile.close()