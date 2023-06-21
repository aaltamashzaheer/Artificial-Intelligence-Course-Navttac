import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel,QTextEdit,QVBoxLayout,QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.display=QLineEdit()
        self.display.setReadOnly(True)
        self.result=QLineEdit()
        self.result.setReadOnly(True)
        buttons =[
                "AC", "DEL", "%", "/",
                  "7", "8", "9", "*",
                  "4", "5", "6", "-",
                  "1", "2", "3", "+",
                  "0", "00", ".", "="
                  ]
        grid = QGridLayout()
        row=0
        col=0
        for button in buttons:
            if button == "=":
                btn= (QPushButton(button))
                btn.clicked.connect(self.calculate)
                grid.addWidget(btn,row,col)
            elif button == "AC":
                btn= (QPushButton(button))
                btn.clicked.connect(self.remove)
                grid.addWidget(btn,row,col)
            elif button=="DEL":
                btn= (QPushButton(button))
                btn.clicked.connect(self.delete)
                grid.addWidget(btn,row,col)
            elif button=="%":
                btn= (QPushButton(button))
                btn.clicked.connect(lambda oh, button=button: self.append_to_display(self.display.text()+"/100"))
                grid.addWidget(btn,row,col)
            else:
                btn= (QPushButton(button))
                btn.clicked.connect(lambda oh, button=button: self.append_to_display(self.display.text()+button))
                grid.addWidget(btn,row,col)
            col+=1
            if col>3:
                col=0
                row+=1
                


        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addWidget(self.result)
        layout.addLayout(grid)
        
        self.setLayout(layout)
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 300)
        self.show()
        
        
    def append_to_display(self,value):
        self.display.setText(value)
            
    def calculate(self):
        try:
            result=eval(self.display.text())
            self.result.setText(str(result))
        except:
            self.result.setText("Error")
    def remove(self):
        self.display.setText("")
        self.result.setText("")
            
    def delete(self):
        self.display.setText(self.display.text()[:-1])
            
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())