from start import start
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    # QApplication 객체 생성
    app = QApplication(sys.argv)
    # widget show
    ex = start()
    sys.exit(app.exec_())