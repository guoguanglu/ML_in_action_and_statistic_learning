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
![](/fig/svm2.png)   
