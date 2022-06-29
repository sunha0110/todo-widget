# ------- 1 -------
import sys
from PyQt5.QtWidgets import QApplication, QLabel

def tutorial_start():
    # QApplication object.
    # can receive arguments from command line, you may pass any argument to the QApplication object.
    app = QApplication(sys.argv)


    # QLabel object
    # widget that present text(simple, rich(html)), image
    # using show()
    label = QLabel("<font color=red size=40>Hello World!</font>")
    label.show()


    # enter the Qt main loop and start to execute the Qt code
    # the label is shown,
    app.exec()


# ------- 2 -------
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton

def tutorial_button():
    app = QApplication(sys.argv)

    # Create button, passing argument to label the button
    # click 했을 때 callback 함수 설정
    button = QPushButton("Click me")
    button.clicked.connect(say_hello)

    button.show()
    app.exec_()

# callback function
# @pyqtSlot() identifies a function as a slot...?
@pyqtSlot()
def say_hello():
    print("Button clicked, Hello!")


tutorial_button()

# ------- 3 -------

