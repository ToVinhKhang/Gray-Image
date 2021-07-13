import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Pic_input.jpg',0);					#Input to Read your image.
hist,bins = np.histogram(image.flatten(),500,[0,500]);
														#CDF (Cumulative Distribution Function).
CDF = hist.cumsum();									#cumsum() : Sum of pixel elements
CDF_normal = CDF * hist.max()/ CDF.max();				#Formula

plt.plot(CDF_normal, color = 'g') 						#Change color CDF line (green).
plt.hist(image.flatten(),500,[0,500], color = 'y');		#Change color  line (yellow).
plt.xlim([0,300])										#Make x axis = 300.
plt.legend(('CDF','HISTOGRAM'), loc = 'center right');	
plt.show();

equal = cv2.equalizeHist(image);						
SideBySide = np.hstack((image,equal));					#Stack sidebyside 2 images
cv2.imwrite('Pic_output.png',SideBySide);				#Output your image.


