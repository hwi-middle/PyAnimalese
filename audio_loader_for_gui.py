from PyQt6.QtCore import *
from pydub import AudioSegment


class WorkerSignals(QObject):
    result = pyqtSignal(object, object)  # create a signal that gets an object as argument


class myloader(QRunnable):
    def __init__(self, path, char):
        super().__init__()
        self.char = char
        self.path = path
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        data = AudioSegment.from_mp3(self.path)
        self.signals.result.emit(data, self.char)
