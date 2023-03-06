from sklearn.linear_model import LinearRegression

# Define the training data
X_train = [[10, 0, 2], [20, 1, 4], [30, 2, 6], [40, 3, 8], [50, 4, 10]]
y_train = [500, 750, 1000, 1250, 1500]

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Use the model to predict the cost of a 25 lb, Bulldog, 3 year old dog
price = model.predict([[25, 1, 3]])

# Print the predicted price
print("The predicted cost of a 25 lb, Bulldog, 3 year old dog is $", round(price[0]))
