# SVM  

## Introduction  
The basic model of SVM is a binary classsification model.By mapping data from input space to the feature space, find a hyperplane in the feature space to maximize the distance to the point closest to the sepearating hyperplane,where the the closest points are called 'support vector' and the distance is called 'margin'.   
Machine learning strategies can be equivalent to two problems:  
1. Convex quadratic programming problem  
2. Regularized hinge loss function minimization problem  

![](/fig/svm1.jpg)  
From easy to hard ,we can divide SVM into:  
1. linear separable SVM. It's dataset is linear separable, and the target of learning is to find a separating hyperplane in feature space.The model is similar to perception, however the most different is that the learning strategy not only classify correctly, but also has the maximum margin,which makes the model more stable.
2. linear SVM. Compared with linear separable SVM , its dataset has some outlier, so we need to add penalty factor to punish misclassification.  
3. non-linear SVM. the dataset is not linear separable, so we need use kernel function to learn non-linear SVM, which is equivalent to learn linear SVM in high dimension implicitly.  

## Linear separable SVM  
The separating hyperplane is defined by:   
![](/equation/svm1.png)   
and the corresponding the model can be defined by:   
![](/equation/svm2.png)   
Firstly, we learn about margin. The functional margin can be defined by:   
![](/equation/svm3.png)    
So we can get the minimal functional margin as follows:   
![](/equation/svm4.png)   
Since functional margin is proportional to w and b, so we can define geometric margin by:   
![](/equation/svm5.png)  
where positive yi=1, negative yi=-1   
The figure is following:  
![](/fig/svm2.jpg)   
**find maximum margin**  
To get the maximum margin, we can obain following constraint optimal problem:  
![](/equation/svm6.png)  
From above equation, we can get:  
![](/equation/svm7.png)  
Since funcitonal margin don't affect the constraint optimal problem, so we let it equal 1, and finding max 1/||w|| is equal to finding min 1/2 * ||w||^2, so we can get below equation:  
![](/equation/svm8.png)  
Here we can convert into convex quadratic proramming problem. We can use Lagrange function to solve by KKT conditions, here omit intermediate steps, directly give the final function and linear separable SVM algorithm process.  
1. construct constraint optimal problem to solve Lagrange parameters.  
![](/equation/svm9.png)  
2. By Lagrange parameters to compute w* and b*  
![](/equation/svm10.png)  
![](/equation/svm11.png)  
3. Get the classification function:  
![](/equation/svm12.png)

**Support Vector**:  
From below figure, the points on the H1 and H2 are called support vectors. we can find the support vectors play an important role in the model  
![](/fig/svm3.jpg)  
## Linear SVM  
for the linear SVM, we just say about differece. The most difference is to add penalty factor C, similar to regularization item.  
The bigger C is, the less misclassified data is, more complicated the model is.  
The smaller C is, the less misclassified data is , the simpler mode is.  
![](/fig/svm4.jpg)  
## Kernel function  
Kernel function is the mapping function from the input space to the feature space. we use kernel function to make non-linear dataset map to high dimension linear feature space.Therefore we can use separating hyperplane to classify.  
The common kernel function:  
1. polynomial kernel function  
![](/equation/svm13.png)  
2. Gaussian kernel function  
![](/equation/svm14.png)  
