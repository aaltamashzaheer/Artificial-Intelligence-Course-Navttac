import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import  QRegularExpressionValidator

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.DisplayingDictionary = {}
        self.init_ui()
        
    def init_ui(self):
        # labels
        Namelabel = QLabel("Kindly Enter Your Name")
        Agelabel = QLabel("Enter Your Age")
        # Input fields
        self.name = QLineEdit()
        self.ageLineEdit = QLineEdit()
        
        regex = QRegularExpression('[0-9]+')
        validator = QRegularExpressionValidator(regex)
        self.ageLineEdit.setValidator(validator)

        # buttons
        Addbutton = QPushButton('App or Update Data')
        Removebutton = QPushButton('Remove Data')
        Showbutton = QPushButton('Show Existing Data')
        Clearbutton = QPushButton('Clear Text Field')
        Savebutton = QPushButton('Save Data in csv')
        Quitbutton = QPushButton('Quit')

        self.text_field = QTextEdit()
        self.text_field.setReadOnly(True)


#         Buttons
        Addbutton.clicked.connect(self.add_update)
        Removebutton.clicked.connect(self.remove)
        Showbutton.clicked.connect(self.show_value)
        Clearbutton.clicked.connect(self.Clear)
        Savebutton.clicked.connect(self.save_to_csv)
        Quitbutton.clicked.connect(self.qut)



        layout = QVBoxLayout()
        layout.addWidget(Namelabel)
        layout.addWidget(self.name)
        layout.addWidget(Agelabel)
        layout.addWidget(self.ageLineEdit)
        layout.addWidget(Addbutton)
        layout.addWidget(Removebutton)
        layout.addWidget(Showbutton)
        layout.addWidget(Clearbutton)
        layout.addWidget(Savebutton)
        layout.addWidget(self.text_field)

        self.setLayout(layout)

        self.setWindowTitle('CRUD APP in PYQT5')
        self.setGeometry(300, 300, 300, 300)
        self.show()



    def add_update(self):
        name = self.name.text()
        value = self.ageLineEdit.text()
        self.DisplayingDictionary[name] = value
        self.text_field.append(f"Added/Update:{name},{value}")

    def remove(self):
        name = self.name.text()
        self.DisplayingDictionary.pop(name)
        self.text_field.append(f"Removed:{name}")
    def show_value(self):
        name = self.name.text()
        if name in self.DisplayingDictionary:
            value = self.DisplayingDictionary
            self.text_field.append(f"Your Name and age data is: {value}")
        else:
            self.text_field.append(f"No data Found")


    def save_to_csv(self):
        filename = 'SavedFile.csv'
        with open (filename, 'w', newline="")as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["name", "value"])
            for name, value in self.DisplayingDictionary.items():
                writer.writerow([name, value])
            self.text_field.append(f'Your Data is saved to {filename}')



    def qut(self):
        exit()


    def Clear(self):
        self.text_field.clear()
        
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())