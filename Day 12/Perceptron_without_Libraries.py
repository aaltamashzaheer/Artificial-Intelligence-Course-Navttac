import pandas as pd
class Perceptron:
    def __init__(self, num_features, learning_rate=0.01):
        self.weights = [0.0] * num_features
        self.bias = 0.0
        self.learning_rate = learning_rate

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return self.activation(weighted_sum)

    def train(self, training_data, num_epochs):
        for epoch in range(num_epochs):
            total_error = 0
            for inputs, target in training_data:
                prediction = self.predict(inputs)
                error = target - prediction
                total_error += abs(error)

                self.weights = [w + self.learning_rate * error * x for w, x in zip(self.weights, inputs)]
                self.bias += self.learning_rate * error

            # Check for early convergence
            if total_error == 0:
                print("Converged early at epoch", epoch + 1)
                break

# Load the dataset using pandas
data = pd.read_csv('dataset_500_final_binary.csv')
x = data.iloc[:, :-2].values
y = data.iloc[:, -1].values

# Combine inputs and targets into training_data
training_data = list(zip(x, y))

# Count the number of features in the training data
num_features = len(x[0])

# Create and train the perceptron
perceptron = Perceptron(num_features=num_features)
perceptron.train(training_data, num_epochs=100)

# Test the trained perceptron
test_data = [
    ([0, 0], "False"),
    ([0, 1], "False"),
    ([1, 0], "False"),
    ([1, 1], "True")
]

print("Input\t\tPredicted Output")
print("--------------------------")
for inputs, expected_output in test_data:
    prediction = perceptron.predict(inputs)
    print(f"{inputs}\t\t{prediction} ({expected_output})")