# Dog-cost-predictor
Predict the cost of a dog based on its weight, breed, and age using a multiple linear regression model
In this example, the training data consists of three features: weight in pounds (X1), breed (encoded as a categorical variable: 0 for Bulldog, 1 for Labrador Retriever, etc.) (X2), and age in years (X3), and the corresponding dog costs (y_train).

We create a multiple linear regression model using the LinearRegression class and train it on the training data using the fit method. We can then use the model to predict the cost of a 25 lb Bulldog that is 3 years old using the predict method, and print out the predicted cost.

Note that in practice, you would likely want to use more training data and more features to create a more accurate model. You might also want to preprocess the data, for example by encoding categorical variables as one-hot vectors or scaling the features to have zero mean and unit variance.
