# 참고: https://wikidocs.net/21920

# ui 기본 구성요소는 QtWidgets에 포함
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

# Qwidget의 모든 스팩을 상속받음... 미리 정의된 method 사용 가능, 변수 입력가능..
class start(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # setWindowTitle() 메서드는 타이틀바에 나타나는 창의 제목을 설정합니다.
        # move() 메서드는 위젯을 스크린의 x=300px, y=300px의 위치로 이동시킵니다.
        # resize() 메서드는 위젯의 크기를 너비 400px, 높이 200px로 조절합니다.
        # show() 메서드는 위젯을 스크린에 보여줍니다.
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        
        self.show()


        # setStyleSheet()을 이용하면 어플리케이션 안의 다양한 구성 요소들의 스타일을 자유롭게 꾸밀 수 있습니다.
        # 고유 layout: https://wikidocs.net/images/page/21928/mainwindowlayout.png
        # PyInstaller를 이용하면 파이썬과 PyQt5로 제작한 GUI 프로그램을 간단하게 실행파일 (exe)로 만들 수 있습니다.