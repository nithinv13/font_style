#!/usr/bin/env python
for i in range(10):
	f = open('extracted_test'+str(i+1)+'.txt')
	f1 = open('font_features_test.html', 'a')

	#doIHaveToCopyTheLine=False

	for line in f.readlines():

	        f1.write(line)

	f1.close()
	f.close()