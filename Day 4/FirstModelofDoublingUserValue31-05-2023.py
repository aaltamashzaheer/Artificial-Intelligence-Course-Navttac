from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
Input = np.array([[1], [2], [3], [4], [5]])
Output = np.array([2, 4, 6, 8, 10])

# Train the linear regression model
model = LinearRegression()
model.fit(Input, Output)

while True:
    user_input = int(input("Enter a value you want to double: "))
    input_array = np.array([[user_input]])
    prediction = model.predict(input_array)
    print(prediction)


