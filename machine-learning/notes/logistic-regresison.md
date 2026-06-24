# Logistic Regression

**NOTE: Linear Regresison was used to find out the output to a dataset with a continuous result.**
**Logistic regression is used to find out the output to a dataset with a discrete result**

## Formulas

### 1. z = w1.x1 + w2.x2 + w3.x3 +... wn.xn
### 2. y_pred = sigmoid(z) (i.e. sigmoid = 1 / 1 + e**-z) [Makes output from 0 - 1]
### 3. We check whether the prediction is > or < a specific threshold (e.g. 0.5)

#### Loss Function
$$
L = -\frac{1}{n} \sum_{i=1}^{n} \left[ y_i \log(\hat{y}_i) + (1 - y_i)\log(1 - \hat{y}_i) \right]
$$

#### We take the derivative of this loss function and we get:

#### 1. Bias:
$$
\frac{\partial L}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)
$$

#### 2. Weights:
$$
\frac{\partial L}{\partial w} = \frac{1}{n} X^T (\hat{y} - y)
$$

#### NOTE: We can also prepend or append the bias as a list of 1s to only use the second formula

**NOTE: In computation it's the same formula as the one for linear regression**