import Image
import numpy as np
import scipy.misc
import webbrowser
from skimage.io import imread


webbrowser.open("test_document.jpg")   


im = imread("test_document.jpg")

im1 = np.random.randint(0, 255, (50, im.shape[1],3))
word_im = np.random.randint(0, 255, (50, 200 ,3))
for i in range(im1.shape[0]):
	for j in range(im1.shape[1]):
		for k in range(im1.shape[2]):
			im1[i][j][k]=255
for i in range(word_im.shape[0]):
	for j in range(word_im.shape[1]):
		for k in range(word_im.shape[2]):
			im1[i][j][k]=255


# for i in range(im.shape[0]):
#  for j in range(im.shape[1]):
#   for k in range(3):
#    if(im[i][j])
#     im1[i][j][k]=im[i][j][k]

# for i in range(175,205):
#  for j in range(300,im.shape[1]-300):
# 	im1[i-175][j]=im[i][j]


# for i in range(im.shape[0]):
# 	for j in range(im.shape[1]):	
#  		if (im[i][j][0]<150) and (im[i][j][1]<150) and (im[i][j][2]<150) :
#  			line_num_pix.append(i)
#  			#i=i+1
#  			for k in range(i+1,im.shape[0]):
#  		   		for l in range(im.shape[1]):
#  		 			if(im[k][l][0]<150) and (im[k][l][1]<150) and (im[i][j][2]<150):
#  		 				#k=k+1
#  		 				break
#             		if(l==im.shape[1]) or (l==im.shape[1]-1) or (l==im.shape[1]-2):
#                 		i=k+1
#                 		set_bit=1
#                 		break
#          		if (set_bit==1) :
#           			break
#     	if (set_bit==1) : 
#      		set_bit=0
#      		break
set_bit=0
count=0
im_count=0
line_count=0
i=0
k=0
while i<im.shape[0] :
	set_bit=0
	for j in range(im.shape[1]):	
 		if (im[i][j][0]<150) and (im[i][j][1]<150) and (im[i][j][2]<150) :
 			for k in range(i,im.shape[0]):
 				count=0
 		   		for l in range(im.shape[1]):
 		 				im1[k-i+10][l]=im[k][l]
 		 				if (im[k][l][0]<150) and (im[k][l][1]<150) and (im[k][l][2]<150) :
 		 					count=count+1
 		 		if (count==0):
 		 			scipy.misc.imsave("outfile"+str(im_count)+".jpg", im1)
 					webbrowser.open("outfile"+str(im_count)+".jpg")
 					im_count=im_count+1
 					i=k+1  
 					set_bit=1
 					line_count=line_count+1
 					for a in range(im1.shape[0]):
						for b in range(im1.shape[1]):
							for c in range(im1.shape[2]):
								im1[a][b][c]=255	
 					break
 		if (set_bit==1):
 			break	
 	i=i+1 			
word_count=0
black_count=0
set_bit=0
while i<line_count :
	line_im = imread("outfile"+str(i)+".jpg")
	while (j<line_im[1]) :
		set_bit=0
		for k in range(line_im[0]) :
			if (im[k][j][0]<150) and (im[k][j][1]<150) and (im[k][j][2]<150) :
				for l in range(j,line_im[1]) :
					black_count=0
					for m in range(line_im[0]) :
						word_im[m][l-j+5]=line_im[m][l]
						if (im[m][l][0]<150) and (im[m][l][1]<150) and (im[m][l][2]<150) :
							black_count=black_count+1
				     		# if (im[m][l+1][0]<150) and (im[m][l+1][1]<150) and (im[m][l+1][2]<150) :
				     		# 	black_count=black_count+1
				    if (black_count < 2) :
				     	scipy.misc.imsave("word"+str(word_count)+".jpg", word_im)
 						webbrowser.open("word"+str(word_count)+".jpg")
 						word_count=word_count+1
 						j=j+l
 						set_bit=1
 						word_count=word_count+1
 						for i in range(word_im.shape[0]) :
							for j in range(word_im.shape[1]) :
								for k in range(word_im.shape[2]) :
									im1[i][j][k]=255
						break
			if (set_bit==1) :
 				break
 		j=j+1
 	i=i+1




# for i in range(300,im.shape[1]-300):
#  print(im[180][i])
 

#for i in range(1):
#for j in range(30):
# print(im1[15][j])

#print(im.shape)  
