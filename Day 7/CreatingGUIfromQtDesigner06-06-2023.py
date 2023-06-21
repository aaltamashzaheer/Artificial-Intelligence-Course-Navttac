# import sys
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout
# import  MainWindow

# class MainWindow(QMainWindow):

#     def __init__(self):
        
#         super().__init__()
#         self.init_ui()
        
#     def init_ui(self):
#         self.title = "Image Viewer"
#         self.setWindowTitle(self.title)
#         self.setGeometry(100, 100, 400, 400)
#         label = QLabel(self)
#         pixmap = QPixmap('cat.jpg')
#         label.setPixmap(pixmap)
#         self.resize(pixmap.width(),pixmap.height())
        
        
#         layout = QVBoxLayout()
#         layout.addWidget(label)
#         self.setLayout(layout)
#         self.show()
        

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
        
# from PyQt5 import uic
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication
# import sys
# import helloworld

# class ExampleApp(QtWidgets.QMainWindow, helloworld.Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(ExampleApp, self).__init__(parent)
#         self.setupUi(self)

# def main():
#     app = QApplication(sys.argv)
#     form = ExampleApp()
#     form.show()
#     app.exec_()

# if __name__ == '__main__':
#     main()

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("MainWindow.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.setGeometry(100, 100, 400, 400 )
window.show()
app.exec()