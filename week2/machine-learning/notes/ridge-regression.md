# Ridge Regression

## Why It's Used

#### The main reason we use ridge regression is to prevent overfitting of a dataset by adding a penalty to the weights so that there is less fit

## Procedure

#### Step 1: We take a few values of lambda to test on

#### `(i.e. lambdas = [0, 0.01, 0.1, 1, 10, 100])`

#### Step 2: For each value of lambda we will run gradient descent to find the optimal values of the weights with respect to the penalty

## Gradient Descent

#### NOTE: It's the same as the normal method, we just add a penalty to the loss to each gradient
#### `(i.e. weights -= learning_rate * (grad + 2 * lambda * weights))`