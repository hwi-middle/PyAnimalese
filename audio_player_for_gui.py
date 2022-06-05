from PyQt6.QtCore import QRunnable, pyqtSlot
from pydub.playback import play


class myplayer(QRunnable):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound

    @pyqtSlot()
    def run(self):
        print('시작')
        play(self.sound)
        print('끝')
