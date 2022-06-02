# GUI를 통해 음원을 생성할 수 있도록 하는 파일 (작업중)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        gen_btn = QPushButton(self)
        gen_btn.setText('생성')

        qle = QLineEdit(self)
        qle.move(60, 100)
        # qle.textChanged[str].connect(self.onChanged)

        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
