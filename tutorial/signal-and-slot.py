import sys
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class siganl_and_slot(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 생성자 (QPushButton())의 첫 번째 파라미터에는 버튼에 표시될 텍스트를 입력하고, 두 번째 파라미터에는 버튼이 위치할 부모 위젯을 입력합니다.
        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        # PyQt5에서의 이벤트 처리는 시그널과 슬롯 메커니즘으로 이루어집니다.
        # instance() 메서드는 현재 인스턴스를 반환합니다.
        # 이 예제에서 발신자는 푸시버튼 (btn)이고, 수신자는 어플리케이션 객체 (app)입니다.
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()