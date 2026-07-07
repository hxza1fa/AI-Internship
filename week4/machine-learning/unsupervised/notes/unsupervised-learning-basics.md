# Unsupervised Learning Basics

### Labels & Features

+ **Labels**: In supervised learning, the labels are the correct answer the model is trained on, or the column which the model must predict
+ **Features**: Features are the columns used to predict the label

##### Unsupervised learning drops the labels alltogether and the model must find relationships between the features on its own

---

### Types of Unsupervised Learning

#### 1. Clustering

Refers to finding relationships between features based on similarity metrics.

i) **Euclidean Distance:** $d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$

ii) **Manhattan Distance:** $d = |x_1 - x_2| + |y_1 - y_2|$

iii) **Cosine Similarity:** $\displaystyle \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \times \|\mathbf{b}\|}$

#### 2. Dimensionality Reduction 

## K Means Clustering

#### Terminology:
+ **K** - The number of clusters you want to make