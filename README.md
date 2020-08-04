# Image-Quality-Identification
Content Based Image Retreival Project on Image Quality Identification

## Index
1. Abstract
2. Problem Statement
3. Project Design and Approach
4. Challenges
5. Essence of my Approach
6. Statements of Assumption
7. Summary of Results


## Problem Statement

Given an image of any dimension, scientifically identify the quality of the image in an independent manner, i.e., without any reference images.

Here the basic ojective of this project is to identify the quality of an image and validate it through automation for reduced human efforts and intervention, bringing efficiency and reduced time for analysis.

## Project Design and Approach

### Approach
This project aims to scientifically identify the quality of an image given in any dimension and without any reference images. The methods used were Histograms, Entropy, Laplacian Blur, Sharpness, MSCN, Sobel edge with ANOVA validation of the results. I had identified two viable approaches which were Laplacian blur and sharpness, which could be used to detect the quality of an image, which were further validated by using ANOVA test to make sure the data set was distinct. Thus, if given two identical input images of different quality, we would be able to identify which image is of better quality.

### Tools/Components

The various tools/components of this project are:

- Programming language – Python
- Libraries – Opencv, Numpy, Matplotlib, PIL, Pandas, scikit, scipy, sklearn

Dataset: 
- image frames from video quality of 360p, 720p and 1080p – Animation video
- image frames from video quality of 360p, 720p and 1080p – Movie trailer
- image frames from video quality of 360p, 720p and 1080p – Nature

- image frames from video quality of 144p, 240p and 360p – Animation video
- image frames from video quality of 144p, 240p and 360p – Movie trailer
- image frames from video quality of 144p, 240p and 360p – Nature
- image frames from video quality of 144p (webm), 144p (mp4) – Movie trailer

### Methodologies

I have used the following methodologies to identify and validate the quality of images:

**A.	Histogram**

**B.	Entropy**

**C.	Laplacian Blur**

**D.	Sharpness**

**E.	MSCN**

**F.	BRISQUE**

**G.	Skewness**

**H.	Kurtosis**

**I.	Acutance**

**J.	Sobel Edge Detection**

**K.	Using ML techniques to predict accuracy of identifying Image Quality.**

### Histograms

Histograms are nothing but the plotting of the number of pixels vs the tonal distribution/tone variations from 0 to 255. Thus, there could be a co-relation between the tonal distributions of an image as resolution changes. 

Various experiments were tried upon, with different types of data sets, from resizing of images, change in display of images like colour or grey scale, etc. 

Some of the key experiments carried out using Histogram are given
The overall objective of the three experiments is:

- To see if any difference exists between the three, when the initial image used differs in resolution and are not identical.

### Entropy

Entropy was considered to be a major feature because it could bring out the pattern or trend from two identical images that differ in resolution as noticed from a slide.
Entropy refers to the image standard deviation or image intensity. When an image is blurred, the entropy changes accordingly. So entropy changes when the quality or resolution of an image differs as well.  Hence, it was concluded that Entropy could be a factor to identify image variance.

### Laplacian Blur

Using OpenCV, in specific the Laplacian function, the blurriness value of an image was calculated. If this function could be used to differentiate between clear and blurred images, could it also be applicable to images of varying resolutions, where high resolutions have high clarity and low resolutions have low clarity and can be said to be even blurry. With this function, the blur value was calculated and experimented on different images with varying resolutions. 

### Anova

Anova is statistical term that is used to see the extent to which two datasets are similar in this case. We will be assigning a value of significance say ‘0.05’, if there is a total of 100 data, then 1 – 0.05 = 0.95 * 100 = 95% of the data is what we will be evaluating against.
A quick example is if our datasets are identical then our ‘p’ value be equal to ‘1’. If our p value is less than our significance value which is in this case 0.05, then 95% of our data is distinguished. Now If our p value is greater than that our significance value, then we our data sets are useless and not viable for comparison and further analysis to be used in ML techniques to solve the problem statement.

### Sharpness

Sharpness can be considered as the inverse of blur. It determines the amount of detail that can be produced in an image. If the blur value of images vary according to the quality of an image, then surely sharpness should also vary according to image quality. Upon experimenting and analysis, I found out that sharpness does indeed vary according to the quality of an image, and it even shows a trend. 

### MSCN

Mean Subtracted Contrast Normalization
I broke down the process of MSCN step by step, in order to understand how they calculated the MSCN coefficients.

My understanding is that, upon taking the original image, they subtract the local mean field from it, then divide the result by local variance field, which is equal to the respective MSCN coefficients.

Local Mean Field () is the Gaussian Blur of the original image(I).
Local Variance Field () is the Gaussian Blur of the square of the difference of original image(I)

Let W be Gaussian Blur, and original image be I, then,
Local Mean Field () = W(I)
Local Variance Field() = sqrt( W ( (I - ) ^2))

- Original image in b/w
- Gaussian Blur applied to the original image
- Difference between the original image and Blurred image 
- Local Variance Field 
- Coefficient of MSCN 

### Image Quality Classification using Machine Learning Techniques

With the help of ML techniques, I was able to predict the accuracy of identifying the image according to its quality, given the metrics, Blur and Sharpness. I used the iris classification experiment for reference and simply substituted the metrics used for a different classification, in this case, it being classification of the quality of an image.

I took three identical videos, which varied in quality, 144p, 480p and 1080p. Each video had 4290 frames each, making total of 12870 frames.

Then calculating its blur value and sharpness, I gave a csv file as the input which had three columns, Blur value, Sharpness Value and Quality. For quality I assigned the value 'A' for 1080p, 'B' for 480p, and 'C' for 144p.

I then split the data into two, 80% of which will be used to train the model, and 20% which will be held back as a validation data set. We are going to hold back the 20% data that the algorithms will not get to see and we will use this data to get a second and independent idea of how accurate the best model might actually be. 

We will use 10-fold cross validation to estimate accuracy.

This will split our data set (80% data that we split for training) into 10 parts, train on 9 and test on 1 and repeat for all combinations of train-test splits.
I used 6 different algorithms to predict the accuracy (using library sklearn):
1.	Logistic Regression (LR)
2.	Linear Discriminant Analysis (LDA)
3.	K-Nearest Neighbors (KNN).
4.	Classification and Regression Trees (CART).
5.	Gaussian Naive Bayes (NB).
6.	Support Vector Machines (SVM).
I got the following accuracy values for the above algorithms:
•	LR - 0.673
•	LDA - 0.662
•	KNN - 0.757
•	CART - 0.799
•	NB - 0.563
•	SVM - 0.755
Finally we run the KNN model directly on the validation set (20% data we split initially).

Accuracy = 0.756

Confusion Matrix for 1080p, 480p and 144p in KNN model

[[667 169  21]
 [174 563 146]
 [ 30  86 718]]
 
Here accuracy refers to the ratio of number of correctly predicted instances divided by total number of instances in the data set multiplies by 100 to give a percentage.

I have copied the URL of the website I used for reference below.
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/


## Challenges

The challenges in this project is identifying and utilizing the correct dataset, for example, the correct type of image container format should be used, that is if we use jpeg, it will be a major problem as JPEG applies compression, that destroys a lot of data by removing the identical and similar pixels, hence we use PNG, which does not use compression and keeps the data intact. 

Furthermore, we cannot compare two different images, which are not identical in nature, it has to be completely similar in appearance (object in frame should be the same, i.e., an exact image) and only varying in quality, only then will we be able to identify which has a better and poorer quality.

In case we are taking frames from a video, there is the possibility of colour frames, such as completely white frames, where blur value and sharpness will be useless as there are no objects in the image at all, the entire image is of the same RGB value without any change, homogenous in nature.

## Essence of my Approach

I am using two image quality metrics to identify and distinguish between the quality of images, namely Laplacian Blur and Sharpness of an image. With these two values the trend is that, higher the value, lower the quality of an image, and lower the value, higher its quality. They have been validated by using both ANOVA test and a google survey form.

## Statement of Assumptions

The input image has to be identical to each other and of varying quality.
They have to be of PNG container format (the container should not use any compression such as JPEG). There cannot be images of just one plain colour with no objects, i.e., a plain white image.

## Summary of Results

Blur value can be used as an image metric for identifying its quality, and to differentiate between images of different qualities. It follows the trend, greater the blur value, poorer the image quality, and lower the blur value, better the image quality.

Sharpness value can be used as an image metric for identifying its quality, and to differentiate between images of different qualities. It follows the trend, greater the sharpness value, poorer the image quality, and lower the sharpness value, better the image quality.

This enables us to validate the quality of images, thereby identifying the right source of an image.



