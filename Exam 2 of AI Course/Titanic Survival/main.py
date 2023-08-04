import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

# Load the Titanic dataset and preprocess the data
data = pd.read_csv('titanic_data.csv')
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data['Embarked'] = data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
data['Age'].fillna(data['Age'].mean(), inplace=True)
data['Fare'].fillna(data['Fare'].mean(), inplace=True)

# Split data into features (X) and target (y)
X = StandardScaler().fit_transform(data.drop(['Survived', 'Name', 'Ticket', 'Cabin'], axis=1))
y = data['Survived']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train the ANN model
model = Sequential([Dense(64, activation='relu', input_dim=X.shape[1]),
                    Dense(32, activation='relu'),
                    Dense(1, activation='sigmoid')])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100, batch_size=10, validation_split=0.2)

# Evaluate the model
print(f'Test Loss: {model.evaluate(X_test, y_test)[0]:.4f}, Test Accuracy: {model.evaluate(X_test, y_test)[1]:.4f}')