from sklearn.linear_model import LinearRegression
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel,QVBoxLayout


class GuiModel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        
        # Asked About the number of data sets user wants to enter and made arrays (of labels and editing of inputs and outputs  
        self.NumberOfSamples_label = QLabel("Enter the Number of Data Points:")
        self.NumberOfSamples_edit = QLineEdit()
        self.x_labels = []
        self.inputs = []
        self.y_labels = []
        self.outputs = []
        
        # Training Button
        self.train_button = QPushButton("Train Your Model")
        self.train_button.clicked.connect(self.train_model)
    
        # Prediction Button
        self.predict_button = QPushButton("Predict")
        self.predict_button.clicked.connect(self.predict_output)

        # Prediction Input
        self.prediction_input_label = QLabel("Enter input value to test the Model: ")
        self.prediction_input_edit = QLineEdit()
        #Prediction Output
        self.prediction_output_label = QLabel("Output of Model after training is: ")
        self.prediction_output_value = QLabel()       
        

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.NumberOfSamples_label)
        layout.addWidget(self.NumberOfSamples_edit)
        
        #for user to enter a large number of data points
        for i in range(5):
            #Taking Inputs to train data and storig in arrays initialized at line 17
            x_label = QLabel("Enter Input Value: ")
            inputs = QLineEdit()
            y_label = QLabel("Enter Output Value: ")
            outputs = QLineEdit()
            self.x_labels.append(x_label)
            self.inputs.append(inputs)
            self.y_labels.append(y_label)
            self.outputs.append(outputs)
            
            #Adding the labels and edits to the layout
            layout.addWidget(x_label)
            layout.addWidget(inputs)
            layout.addWidget(y_label)
            layout.addWidget(outputs)
            
        
        layout.addWidget(self.train_button)
        layout.addWidget(self.prediction_input_label)
        layout.addWidget(self.prediction_input_edit)
        layout.addWidget(self.prediction_output_label)
        layout.addWidget(self.prediction_output_value)
        layout.addWidget(self.predict_button)
        
        self.setWindowTitle("Model Creation")
        self.setGeometry(300, 50, 500, 500)
        self.setLayout(layout)
    
        
        
    def train_model(self):
        
        #Takes the number of data points from gui line edit as above mentioned in line 16
        NumberofDataPoints = int(self.NumberOfSamples_edit.text())
        input_array = []
        output_array = []
        
        #creation of input and output array by checking user input and output values reiceved from gui
        for i in range(NumberofDataPoints):
            x = float(self.inputs[i].text())
            y = float(self.outputs[i].text())
            input_array.append(x)
            output_array.append(y)
        
        # Training the model
        input_train = np.array(input_array).reshape(-1, 1)
        output_train = np.array(output_array)
        
        model = LinearRegression()
        model.fit(input_train, output_train)
        
        
        # Displaying the trained model
        self.trained_model = model
        
    def predict_output(self):
        if not hasattr(self, 'trained_model'):
            return

        # Get the input value from the user
        input_value = float(self.prediction_input_edit.text())
        
        # Perform prediction using the trained model
        predicted_output = self.trained_model.predict([[input_value]])
        self.prediction_output_value.setText(str(predicted_output[0]))

        
        
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    window = GuiModel()
    window.show()
    sys.exit(app.exec_())