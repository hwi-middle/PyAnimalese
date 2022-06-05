# Form implementation generated from reading ui file 'PyAnimalese.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os.path
import traceback
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QThreadPool
import random
from pydub import AudioSegment
from pydub.playback import play
from audio_player_for_gui import myplayer

from audio_loader_for_gui import myloader

try:
    from jamo import h2j, j2hcj
except:
    from __jamo import h2j, j2hcj

    is_debug = False
else:
    is_debug = True


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        MainWindow.setMinimumSize(QtCore.QSize(700, 400))
        MainWindow.setMaximumSize(QtCore.QSize(700, 400))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.help_label = QtWidgets.QLabel(self.centralwidget)
        self.help_label.setGeometry(QtCore.QRect(20, 20, 331, 41))
        self.help_label.setObjectName("help_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 531, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.source_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.source_text.setObjectName("source_text")
        self.horizontalLayout.addWidget(self.source_text)
        self.convert_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.convert_btn.setObjectName("convert_btn")
        self.horizontalLayout.addWidget(self.convert_btn)
        self.progress_label = QtWidgets.QLabel(self.centralwidget)
        self.progress_label.setGeometry(QtCore.QRect(20, 120, 531, 41))
        self.progress_label.setObjectName("progress_label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 280, 451, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.play_or_save_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.play_or_save_label.setObjectName("play_or_save_label")
        self.horizontalLayout_2.addWidget(self.play_or_save_label)
        self.play_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.play_btn.setObjectName("play_btn")
        self.horizontalLayout_2.addWidget(self.play_btn)
        self.save_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        # self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        # self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 310, 451, 41))
        # self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        # self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        # self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.set_path_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        # self.set_path_btn.setObjectName("set_path_btn")
        # self.horizontalLayout_3.addWidget(self.set_path_btn)
        # self.github_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        # self.github_btn.setObjectName("github_btn")
        # self.horizontalLayout_3.addWidget(self.github_btn)
        self.contact_label = QtWidgets.QLabel(self.centralwidget)
        self.contact_label.setGeometry(QtCore.QRect(20, 360, 341, 41))
        self.contact_label.setObjectName("contact_label")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(20, 100, 531, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 250, 531, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.connect_events()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", f"PyAnimalese {self.version}"))
        self.help_label.setText(_translate("MainWindow", "동물의 숲 NPC 목소리로 읽고 싶은 문장을 입력하세요."))
        self.convert_btn.setText(_translate("MainWindow", "변환"))
        self.progress_label.setText(_translate("MainWindow", "대기중..."))
        self.play_or_save_label.setText(_translate("MainWindow", "생성된 음성을..."))
        self.play_btn.setText(_translate("MainWindow", "재생하기"))
        self.save_btn.setText(_translate("MainWindow", "저장하기"))
        # self.set_path_btn.setText(_translate("MainWindow", "저장경로 설정하기"))
        # self.github_btn.setText(_translate("MainWindow", "GitHub Repo 확인하기"))
        self.contact_label.setText(_translate("MainWindow", "개발자: 주휘중 (contact@jbstudio.xyz)"))

    # My codes below
    def __init__(self):
        self.version = "1.0.0"
        self.threadpool = QThreadPool()
        self.root_dir = '\\'.join(sys.executable.split('\\')[0:-1])
        self.is_processing = False
        self.result_sound = None
        self.source_string = ""
        self.char_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', ' ']

        self.char_sounds = {}
        # self.char_sounds_high = {}
        self.loading_audio_files = False
        self.loaded_audio_num = 0

    def connect_events(self):
        self.convert_btn.clicked.connect(self.convert_to_animalese)
        self.play_btn.clicked.connect(self.play_sound)
        self.save_btn.clicked.connect(lambda: self.save_sound(self.source_string))

    def initialize_audio_files(self):
        if self.loading_audio_files:
            return

        self.loading_audio_files = True
        self.progress_label.setText(f"데이터 파일을 불러오고 있어요. 검은색 창이 나와도 놀라지 마세요! ({self.loaded_audio_num}/{len(self.char_list)})")
        QtWidgets.QApplication.processEvents()

        for idx, item in enumerate(self.char_list):
            str_idx = str(idx + 1).zfill(2)
            if is_debug:
                try:
                    my_loader = myloader(f'./sources/{str_idx}.padata', item)
                    my_loader.signals.result.connect(self.finished_single_audio_file)
                    self.threadpool.start(my_loader)
                except Exception as e:
                    print(e)

                # self.char_sounds[item] = AudioSegment.from_mp3(f'{self.root_dir}\\data\\sources\\{str_idx}.padata')
                # self.char_sounds_high[item] = f'./sources/high/{str_idx}.padata'
            else:
                my_loader = myloader(f'{self.root_dir}\\data\\sources\\{str_idx}.padata', item)
                my_loader.signals.result.connect(self.finished_single_audio_file)
                self.threadpool.start(my_loader)
                # self.char_sounds[item] = AudioSegment.from_mp3(f'{self.root_dir}\\data\\sources\\{str_idx}.padata')

    def finished_single_audio_file(self, sound, char):
        self.char_sounds[char] = sound

        self.loaded_audio_num += 1
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(len(self.char_list))
        self.progress_bar.value = self.loaded_audio_num
        print( self.loaded_audio_num)
        self.progress_label.setText(f"데이터 파일을 불러오고 있어요. 검은색 창이 나와도 놀라지 마세요! ({self.loaded_audio_num}/{len(self.char_list)})")
        QtWidgets.QApplication.processEvents()

        if len(self.char_sounds) == len(self.char_list):
            print('완료')
            self.loading_audio_files = False
            self.progress_label.setText("로드 완료")
            QtWidgets.QApplication.processEvents()

    def convert_to_animalese(self):
        if self.is_processing:
            return

        if self.loading_audio_files:
            return

        self.source_string = self.source_text.text()
        self.result_sound = None
        # print(self.source_string)
        self.is_processing = True
        self.progress_label.setText("변환중...")
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(len(self.source_string))
        QtWidgets.QApplication.processEvents()

        completed_char_num = 0
        skipped_char_num = 0
        for ch in self.source_string:
            jamo_ch = j2hcj(h2j(ch))
            # print(jamo_ch)
            if jamo_ch[0] not in self.char_list:
                skipped_char_num += 1
            else:
                char_sound = self.char_sounds[jamo_ch[0]]

                octaves = 2 * random.uniform(0.96, 1.15)
                new_sample_rate = int(char_sound.frame_rate * (2.0 ** octaves))

                pitch_char_sound = char_sound._spawn(char_sound.raw_data, overrides={'frame_rate': new_sample_rate})
                self.result_sound = pitch_char_sound if self.result_sound is None else self.result_sound + pitch_char_sound

            completed_char_num += 1
            self.progress_bar.setValue(completed_char_num)

        self.is_processing = False
        self.progress_label.setText("변환완료")
        QtWidgets.QApplication.processEvents()

        self.play_sound()

    def play_sound(self):
        if self.result_sound is None:
            return

        my_player = myplayer(self.result_sound)
        self.threadpool.start(my_player)

    def save_sound(self, filename):
        if self.result_sound is None:
            return

        try:
            os.makedirs('result', exist_ok=True)
            self.result_sound.export(f'{self.root_dir}\\result\\{self.source_string}.mp3', format='mp3')
        except Exception as e:
            traceback.print_exc()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.initialize_audio_files()
    sys.exit(app.exec())
