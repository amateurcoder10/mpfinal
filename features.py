#training program for pattern recognition

import argparse as ap
# Importing library that supports user friendly commandline interfaces
import cv2
# Importing the opencv library
import imutils
# Importing the library that supports basic image processing functions
import numpy as np
# Importing the array operations library for python
import os
# Importing the library which supports standard systems commands
from scipy.cluster.vq import *
# Importing the library which classifies set of observations into clusters
from sklearn.preprocessing import StandardScaler
# Importing the library that supports centering and scaling vectors
from imutils import paths
import sys
sys.path.append('/home/pra/.virtualenvs/cv/lib/python2.7/site-packages/')
import matplotlib.pyplot as plt

# Get the path of the training set
parser = ap.ArgumentParser()
parser.add_argument("-t", "--trainingSet", help="Path to Training Set", required="True")
args = vars(parser.parse_args())

# Get the training classes names and store them in a list
train_path = args["trainingSet"]
training_names = os.listdir(train_path)  # Listing the train_path directory

# Get all the path to the images and save them in a list
# image_paths and the corresponding label in image_paths
image_paths = []  # Inilialising the list
image_classes = []  # Inilialising the list
class_id = 0
for training_name in training_names:  # Iterate over the training_names list
    
    dir = os.path.join(train_path, training_name)
    class_path = list(paths.list_images(dir))
    image_paths+=class_path
    image_classes+=[class_id]*len(class_path)
    class_id+=1
SURF=cv2.xfeatures2d.SURF_create()

# Create feature extraction and keypoint detector objects
# List where all the descriptors are stored
des_list = []
print(len(image_paths))
i=0
#print(image_paths)
# Reading the image and calculating the features and corresponding descriptors
for image_path in image_paths:
    im = cv2.imread(image_path)
    #l=l+1
    #print(im)
    #cv2.imshow('im',im)
    
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    kpts, des =SURF.detectAndCompute(im, None)  # Computing the key points and the descriptors
    #plt.imshow(cv2.drawKeypoints(im, kpts,im.copy()))
    #print(des.shape)
    if(des==None):
	i+=1
        print(image_path,des)
	continue
   
    des_list.append((image_path, des))  # Appending all the descriptors into the single list
print(i)
print(len(des_list))
# Stack all the descriptors vertically in a numpy array
descriptors = des_list[0][1]
print(descriptors.shape)
i=0
for image_path, descriptor in des_list[1:]:
   descriptors = np.vstack((descriptors, descriptor))
 

# Perform k-means clustering
k = 500  # Number of clusters
voc, variance = kmeans(descriptors, k, 1)  # Perform Kmeans with default values

# Calculate the histogram of features
im_features = np.zeros((len(image_paths), k), "float32")
for i in xrange(len(des_list)):
    words, distance = vq(des_list[i][1],voc)
    for w in words:
        im_features[i][w] += 1

# Perform Tf-Idf vectorization
nbr_occurences = np.sum( (im_features > 0) * 1, axis = 0)
# Calculating the number of occurrences
idf = np.array(np.log((1.0*len(image_paths)+1) / (1.0*nbr_occurences + 1)), 'float32')
# Giving weight to one that occurs more frequently

# Scaling the words
stdSlr = StandardScaler().fit(im_features)
im_features = stdSlr.transform(im_features)  # Scaling the visual words for better Prediction

# Saving the contents into a file
np.savetxt("samples.data",im_features)
np.savetxt("responses.data",np.array(image_classes))
np.save("training_names.data",training_names)
np.save("stdSlr.data",stdSlr)
np.save("voc.data",voc)

