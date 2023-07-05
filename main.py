from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
from math import pi
from scipy import signal
import sounddevice as sd
import numpy as np
import random


def get_main_freq(note, slider_tone, slider_subtone):
    return 440 * pow(2, (note + slider_tone + slider_subtone * 0.01) / 12)


def normalize(sound, master):
    return sound * master * 0.01 / abs(max(sound))


def sine_generator(tone, volume):
    return np.sin(2 * pi * tone * np.linspace(0, 1, 44100)) * volume


def triangle_generator(tone, volume):
    return signal.sawtooth(2 * pi * tone * np.linspace(0, 1, 44100), 0.5) * volume


def saw_generator(tone, volume):
    return signal.sawtooth(2 * pi * tone * np.linspace(0, 1, 44100)) * volume


def square_generator(tone, volume):
    return signal.square(2 * np.pi * tone * np.linspace(0, 1, 44100)) * volume


def noise_generator(volume):
    return [random.random() * volume for _ in range(44100)]


tones = {'c0': -9, 'cs0': -8, 'd0': -7, 'ds0': -6, 'e0': -5, 'f0': -4, 'fs0': -3, 'g0': -2, 'gs0': -1, 'a0': 0,
         'as0': 1, 'b0': 2, 'c1': 3, 'cs1': 4, 'd1': 5, 'ds1': 6, 'e1': 7, 'f1': 8, 'fs1': 9, 'g1': 10, 'gs1': 11,
         'a1': 12, 'as1': 13, 'b1': 14}
sample_rate = 44100



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.mw = MainWindow
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CardinalSynth = QtWidgets.QLabel(self.centralwidget)
        self.CardinalSynth.setGeometry(QtCore.QRect(250, 0, 300, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CardinalSynth.setFont(font)
        self.CardinalSynth.setStyleSheet("color: rgb(0, 255, 21);")
        self.CardinalSynth.setAlignment(QtCore.Qt.AlignCenter)
        self.CardinalSynth.setObjectName("CardinalSynth")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(640, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.b1.setObjectName("b1")
        self.f1 = QtWidgets.QPushButton(self.centralwidget)
        self.f1.setGeometry(QtCore.QRect(520, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.f1.setFont(font)
        self.f1.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.f1.setObjectName("f1")
        self.f0 = QtWidgets.QPushButton(self.centralwidget)
        self.f0.setGeometry(QtCore.QRect(240, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.f0.setFont(font)
        self.f0.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.f0.setObjectName("f0")
        self.a1 = QtWidgets.QPushButton(self.centralwidget)
        self.a1.setGeometry(QtCore.QRect(600, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.a1.setFont(font)
        self.a1.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.a1.setObjectName("a1")
        self.g1 = QtWidgets.QPushButton(self.centralwidget)
        self.g1.setGeometry(QtCore.QRect(560, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.g1.setFont(font)
        self.g1.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.g1.setObjectName("g1")
        self.e1 = QtWidgets.QPushButton(self.centralwidget)
        self.e1.setGeometry(QtCore.QRect(480, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.e1.setFont(font)
        self.e1.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.e1.setObjectName("e1")
        self.c1 = QtWidgets.QPushButton(self.centralwidget)
        self.c1.setGeometry(QtCore.QRect(400, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.c1.setFont(font)
        self.c1.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.c1.setObjectName("c1")
        self.fs0 = QtWidgets.QPushButton(self.centralwidget)
        self.fs0.setGeometry(QtCore.QRect(265, 450, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.fs0.setFont(font)
        self.fs0.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 0, 255);")
        self.fs0.setObjectName("fs0")
        self.as1 = QtWidgets.QPushButton(self.centralwidget)
        self.as1.setGeometry(QtCore.QRect(625, 450, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.as1.setFont(font)
        self.as1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 0, 255);")
        self.as1.setObjectName("as1")
        self.a0 = QtWidgets.QPushButton(self.centralwidget)
        self.a0.setGeometry(QtCore.QRect(320, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.a0.setFont(font)
        self.a0.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.a0.setObjectName("a0")
        self.gs0 = QtWidgets.QPushButton(self.centralwidget)
        self.gs0.setGeometry(QtCore.QRect(305, 450, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.gs0.setFont(font)
        self.gs0.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 0, 255);")
        self.gs0.setObjectName("gs0")
        self.e0 = QtWidgets.QPushButton(self.centralwidget)
        self.e0.setGeometry(QtCore.QRect(200, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.e0.setFont(font)
        self.e0.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.e0.setObjectName("e0")
        self.cs1 = QtWidgets.QPushButton(self.centralwidget)
        self.cs1.setGeometry(QtCore.QRect(420, 450, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.cs1.setFont(font)
        self.cs1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 0, 255);")
        self.cs1.setObjectName("cs1")
        self.cs0 = QtWidgets.QPushButton(self.centralwidget)
        self.cs0.setGeometry(QtCore.QRect(145, 450, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.cs0.setFont(font)
        self.cs0.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 0, 255);")
        self.cs0.setObjectName("cs0")
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(360, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.b0.setFont(font)
        self.b0.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.b0.setObjectName("b0")
        self.fs1 = QtWidgets.QPushButton(self.centralwidget)
        self.fs1.setGeometry(QtCore.QRect(545, 450, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.fs1.setFont(font)
        self.fs1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 0, 255);")
        self.fs1.setObjectName("fs1")
        self.as0 = QtWidgets.QPushButton(self.centralwidget)
        self.as0.setGeometry(QtCore.QRect(345, 450, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.as0.setFont(font)
        self.as0.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 0, 255);")
        self.as0.setObjectName("as0")
        self.g0 = QtWidgets.QPushButton(self.centralwidget)
        self.g0.setGeometry(QtCore.QRect(280, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.g0.setFont(font)
        self.g0.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.g0.setObjectName("g0")
        self.d0 = QtWidgets.QPushButton(self.centralwidget)
        self.d0.setGeometry(QtCore.QRect(160, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.d0.setFont(font)
        self.d0.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.d0.setObjectName("d0")
        self.c0 = QtWidgets.QPushButton(self.centralwidget)
        self.c0.setGeometry(QtCore.QRect(120, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.c0.setFont(font)
        self.c0.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.c0.setObjectName("c0")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 130, 741, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(211, 121, 255)")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 6, 1, 1)
        self.SineVolume = QtWidgets.QDial(self.gridLayoutWidget)
        self.SineVolume.setStyleSheet("background-color: rgb(205, 255, 23)")
        self.SineVolume.setMaximum(100)
        self.SineVolume.setPageStep(1)
        self.SineVolume.setValue(100)
        self.SineVolume.setObjectName("SineVolume")
        self.gridLayout.addWidget(self.SineVolume, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(49, 255, 26)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.SquareVolume = QtWidgets.QDial(self.gridLayoutWidget)
        self.SquareVolume.setMaximum(100)
        self.SquareVolume.setPageStep(1)
        self.SquareVolume.setObjectName("SquareVolume")
        self.gridLayout.addWidget(self.SquareVolume, 1, 4, 1, 1)
        self.MasterVolume = QtWidgets.QDial(self.gridLayoutWidget)
        self.MasterVolume.setMaximum(100)
        self.MasterVolume.setPageStep(1)
        self.MasterVolume.setProperty("value", 100)
        self.MasterVolume.setObjectName("MasterVolume")
        self.gridLayout.addWidget(self.MasterVolume, 1, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(49, 255, 26)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.SawVolume = QtWidgets.QDial(self.gridLayoutWidget)
        self.SawVolume.setStyleSheet("background-color: rgb(205, 255, 23)")
        self.SawVolume.setMaximum(100)
        self.SawVolume.setPageStep(1)
        self.SawVolume.setProperty("value", 100)
        self.SawVolume.setObjectName("SawVolume")
        self.gridLayout.addWidget(self.SawVolume, 1, 3, 1, 1)
        self.TriangleVolume = QtWidgets.QDial(self.gridLayoutWidget)
        self.TriangleVolume.setStyleSheet("background-color: rgb(205, 255, 23)")
        self.TriangleVolume.setMaximum(100)
        self.TriangleVolume.setPageStep(1)
        self.TriangleVolume.setObjectName("TriangleVolume")
        self.gridLayout.addWidget(self.TriangleVolume, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(49, 255, 26)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(49, 255, 26)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SineTone = QtWidgets.QSlider(self.gridLayoutWidget)
        self.SineTone.setStyleSheet("")
        self.SineTone.setMinimum(-60)
        self.SineTone.setMaximum(60)
        self.SineTone.setPageStep(1)
        self.SineTone.setOrientation(QtCore.Qt.Vertical)
        self.SineTone.setObjectName("SineTone")
        self.horizontalLayout.addWidget(self.SineTone)
        self.SineToneLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.SineToneLine.setMaxLength(3)
        self.SineToneLine.setReadOnly(True)
        self.SineToneLine.setObjectName("SineToneLine")
        self.horizontalLayout.addWidget(self.SineToneLine)
        self.SineSubToneLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.SineSubToneLine.setMaxLength(3)
        self.SineSubToneLine.setReadOnly(True)
        self.SineSubToneLine.setObjectName("SineSubToneLine")
        self.horizontalLayout.addWidget(self.SineSubToneLine)
        self.SineSubTone = QtWidgets.QSlider(self.gridLayoutWidget)
        self.SineSubTone.setPageStep(1)
        self.SineSubTone.setOrientation(QtCore.Qt.Vertical)
        self.SineSubTone.setObjectName("SineSubTone")
        self.horizontalLayout.addWidget(self.SineSubTone)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TriangleTone = QtWidgets.QSlider(self.gridLayoutWidget)
        self.TriangleTone.setMinimum(-60)
        self.TriangleTone.setMaximum(60)
        self.TriangleTone.setPageStep(1)
        self.TriangleTone.setOrientation(QtCore.Qt.Vertical)
        self.TriangleTone.setObjectName("TriangleTone")
        self.horizontalLayout_2.addWidget(self.TriangleTone)
        self.TriangleToneLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.TriangleToneLine.setMaxLength(3)
        self.TriangleToneLine.setReadOnly(True)
        self.TriangleToneLine.setObjectName("TriangleToneLine")
        self.horizontalLayout_2.addWidget(self.TriangleToneLine)
        self.TriangleSubToneLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.TriangleSubToneLine.setMaxLength(3)
        self.TriangleSubToneLine.setReadOnly(True)
        self.TriangleSubToneLine.setObjectName("TriangleSubToneLine")
        self.horizontalLayout_2.addWidget(self.TriangleSubToneLine)
        self.TriangleSubTone = QtWidgets.QSlider(self.gridLayoutWidget)
        self.TriangleSubTone.setPageStep(1)
        self.TriangleSubTone.setOrientation(QtCore.Qt.Vertical)
        self.TriangleSubTone.setObjectName("TriangleSubTone")
        self.horizontalLayout_2.addWidget(self.TriangleSubTone)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 5, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SawTone = QtWidgets.QSlider(self.gridLayoutWidget)
        self.SawTone.setMinimum(-60)
        self.SawTone.setMaximum(60)
        self.SawTone.setPageStep(1)
        self.SawTone.setOrientation(QtCore.Qt.Vertical)
        self.SawTone.setObjectName("SawTone")
        self.horizontalLayout_3.addWidget(self.SawTone)
        self.SawToneLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.SawToneLine.setMaxLength(3)
        self.SawToneLine.setReadOnly(True)
        self.SawToneLine.setObjectName("SawToneLine")
        self.horizontalLayout_3.addWidget(self.SawToneLine)
        self.SawSubToneLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.SawSubToneLine.setMaxLength(3)
        self.SawSubToneLine.setReadOnly(True)
        self.SawSubToneLine.setObjectName("SawSubToneLine")
        self.horizontalLayout_3.addWidget(self.SawSubToneLine)
        self.SawSubTone = QtWidgets.QSlider(self.gridLayoutWidget)
        self.SawSubTone.setPageStep(1)
        self.SawSubTone.setOrientation(QtCore.Qt.Vertical)
        self.SawSubTone.setObjectName("SawSubTone")
        self.horizontalLayout_3.addWidget(self.SawSubTone)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 3, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 6, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SquareTone = QtWidgets.QSlider(self.gridLayoutWidget)
        self.SquareTone.setMinimum(-60)
        self.SquareTone.setMaximum(60)
        self.SquareTone.setPageStep(1)
        self.SquareTone.setOrientation(QtCore.Qt.Vertical)
        self.SquareTone.setObjectName("SquareTone")
        self.horizontalLayout_4.addWidget(self.SquareTone)
        self.SquareToneLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.SquareToneLine.setMaxLength(3)
        self.SquareToneLine.setReadOnly(True)
        self.SquareToneLine.setObjectName("SquareToneLine")
        self.horizontalLayout_4.addWidget(self.SquareToneLine)
        self.SquareSubToneLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.SquareSubToneLine.setMaxLength(3)
        self.SquareSubToneLine.setReadOnly(True)
        self.SquareSubToneLine.setObjectName("SquareSubToneLine")
        self.horizontalLayout_4.addWidget(self.SquareSubToneLine)
        self.SquareSubTone = QtWidgets.QSlider(self.gridLayoutWidget)
        self.SquareSubTone.setPageStep(1)
        self.SquareSubTone.setOrientation(QtCore.Qt.Vertical)
        self.SquareSubTone.setObjectName("SquareSubTone")
        self.horizontalLayout_4.addWidget(self.SquareSubTone)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(49, 255, 26)")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.NoiseVolume = QtWidgets.QDial(self.gridLayoutWidget)
        self.NoiseVolume.setMaximum(100)
        self.NoiseVolume.setPageStep(1)
        self.NoiseVolume.setObjectName("NoiseVolume")
        self.gridLayout.addWidget(self.NoiseVolume, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.ds1 = QtWidgets.QPushButton(self.centralwidget)
        self.ds1.setGeometry(QtCore.QRect(465, 450, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.ds1.setFont(font)
        self.ds1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 0, 255);")
        self.ds1.setObjectName("ds1")
        self.gs1 = QtWidgets.QPushButton(self.centralwidget)
        self.gs1.setGeometry(QtCore.QRect(585, 450, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.gs1.setFont(font)
        self.gs1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 0, 255);")
        self.gs1.setObjectName("gs1")
        self.ds0 = QtWidgets.QPushButton(self.centralwidget)
        self.ds0.setGeometry(QtCore.QRect(185, 450, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.ds0.setFont(font)
        self.ds0.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 0, 255);")
        self.ds0.setObjectName("ds0")
        self.d1 = QtWidgets.QPushButton(self.centralwidget)
        self.d1.setGeometry(QtCore.QRect(440, 455, 40, 100))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.d1.setFont(font)
        self.d1.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);")
        self.d1.setObjectName("d1")
        self.CardinalSynth.raise_()
        self.b1.raise_()
        self.f1.raise_()
        self.f0.raise_()
        self.a1.raise_()
        self.g1.raise_()
        self.e1.raise_()
        self.c1.raise_()
        self.as1.raise_()
        self.a0.raise_()
        self.e0.raise_()
        self.b0.raise_()
        self.fs1.raise_()
        self.as0.raise_()
        self.g0.raise_()
        self.d0.raise_()
        self.c0.raise_()
        self.gridLayoutWidget.raise_()
        self.gs1.raise_()
        self.ds0.raise_()
        self.d1.raise_()
        self.cs0.raise_()
        self.fs0.raise_()
        self.gs0.raise_()
        self.ds1.raise_()
        self.cs1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Set Init Value
        self.SineToneLine.setStyleSheet("color: rgb(49, 255, 26)")
        self.SineToneLine.setAlignment(QtCore.Qt.AlignCenter)
        self.SineToneLine.setText(str(self.SineTone.value()))
        self.SineSubToneLine.setStyleSheet("color: rgb(49, 255, 26)")
        self.SineSubToneLine.setAlignment(QtCore.Qt.AlignCenter)
        self.SineSubToneLine.setText(str(self.SineSubTone.value()))
        self.TriangleToneLine.setStyleSheet("color: rgb(49, 255, 26)")
        self.TriangleToneLine.setAlignment(QtCore.Qt.AlignCenter)
        self.TriangleToneLine.setText(str(self.TriangleTone.value()))
        self.TriangleSubToneLine.setStyleSheet("color: rgb(49, 255, 26)")
        self.TriangleSubToneLine.setAlignment(QtCore.Qt.AlignCenter)
        self.TriangleSubToneLine.setText(str(self.TriangleSubTone.value()))
        self.SawToneLine.setStyleSheet("color: rgb(49, 255, 26)")
        self.SawToneLine.setAlignment(QtCore.Qt.AlignCenter)
        self.SawToneLine.setText(str(self.SawTone.value()))
        self.SawSubToneLine.setStyleSheet("color: rgb(49, 255, 26)")
        self.SawSubToneLine.setAlignment(QtCore.Qt.AlignCenter)
        self.SawSubToneLine.setText(str(self.SawSubTone.value()))
        self.SquareToneLine.setStyleSheet("color: rgb(49, 255, 26)")
        self.SquareToneLine.setAlignment(QtCore.Qt.AlignCenter)
        self.SquareToneLine.setText(str(self.SquareTone.value()))
        self.SquareSubToneLine.setStyleSheet("color: rgb(49, 255, 26)")
        self.SquareSubToneLine.setAlignment(QtCore.Qt.AlignCenter)
        self.SquareSubToneLine.setText(str(self.SquareSubTone.value()))

        self.SineTone.valueChanged.connect(self.sineValue)
        self.SineSubTone.valueChanged.connect(self.sineSubValue)
        self.TriangleTone.valueChanged.connect(self.triangleValue)
        self.TriangleSubTone.valueChanged.connect(self.triangleSubValue)
        self.SawTone.valueChanged.connect(self.sawValue)
        self.SawSubTone.valueChanged.connect(self.sawSubValue)
        self.SquareTone.valueChanged.connect(self.squareValue)
        self.SquareSubTone.valueChanged.connect(self.squareSubValue)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.th = {}

        self.c0.clicked.connect(self.run_threads)
        self.cs0.clicked.connect(self.run_threads)
        self.d0.clicked.connect(self.run_threads)
        self.ds0.clicked.connect(self.run_threads)
        self.e0.clicked.connect(self.run_threads)
        self.f0.clicked.connect(self.run_threads)
        self.fs0.clicked.connect(self.run_threads)
        self.g0.clicked.connect(self.run_threads)
        self.gs0.clicked.connect(self.run_threads)
        self.a0.clicked.connect(self.run_threads)
        self.as0.clicked.connect(self.run_threads)
        self.b0.clicked.connect(self.run_threads)
        self.c1.clicked.connect(self.run_threads)
        self.cs1.clicked.connect(self.run_threads)
        self.d1.clicked.connect(self.run_threads)
        self.ds1.clicked.connect(self.run_threads)
        self.e1.clicked.connect(self.run_threads)
        self.f1.clicked.connect(self.run_threads)
        self.fs1.clicked.connect(self.run_threads)
        self.g1.clicked.connect(self.run_threads)
        self.gs1.clicked.connect(self.run_threads)
        self.a1.clicked.connect(self.run_threads)
        self.as1.clicked.connect(self.run_threads)
        self.b1.clicked.connect(self.run_threads)

    def sineValue(self):
        self.SineToneLine.setText(str(self.SineTone.value()))

    def sineSubValue(self):
        self.SineSubToneLine.setText(str(self.SineSubTone.value()))

    def triangleValue(self):
        self.TriangleToneLine.setText(str(self.TriangleTone.value()))

    def triangleSubValue(self):
        self.TriangleSubToneLine.setText(str(self.TriangleSubTone.value()))

    def sawValue(self):
        self.SawToneLine.setText(str(self.SawTone.value()))

    def sawSubValue(self):
        self.SawSubToneLine.setText(str(self.SawSubTone.value()))

    def squareValue(self):
        self.SquareToneLine.setText(str(self.SquareTone.value()))

    def squareSubValue(self):
        self.SquareSubToneLine.setText(str(self.SquareSubTone.value()))

    def note_player(self, note):
        global sample_rate
        x = sine_generator(get_main_freq(tones.get(note), ui.SineTone.value(), ui.SineSubTone.value()),
                           ui.SineVolume.value()) + \
            triangle_generator(get_main_freq(tones.get(note), ui.TriangleTone.value(), ui.TriangleSubTone.value()),
                           ui.TriangleVolume.value()) + \
            saw_generator(get_main_freq(tones.get(note), ui.SawTone.value(), ui.SawSubTone.value()),
                           ui.SawVolume.value()) + \
            square_generator(get_main_freq(tones.get(note), ui.SquareTone.value(), ui.SquareSubTone.value()),
                           ui.SquareVolume.value()) + \
            noise_generator(ui.NoiseVolume.value())

        sd.play(normalize(x, ui.MasterVolume.value()), sample_rate)


    def run_threads(self):
        self.th[self.mw.sender().objectName()] = Thread(target=self.note_player, args=(self.mw.sender().objectName(), ))
        self.th[self.mw.sender().objectName()].start()
        self.th[self.mw.sender().objectName()].join()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CardinalSynth.setText(_translate("MainWindow", "Cardinal Synth"))
        self.b1.setText(_translate("MainWindow", "B"))
        self.b1.setShortcut(_translate("MainWindow", "O"))
        self.f1.setText(_translate("MainWindow", "F"))
        self.f1.setShortcut(_translate("MainWindow", "Y"))
        self.f0.setText(_translate("MainWindow", "F"))
        self.f0.setShortcut(_translate("MainWindow", "B"))
        self.a1.setText(_translate("MainWindow", "A"))
        self.a1.setShortcut(_translate("MainWindow", "I"))
        self.g1.setText(_translate("MainWindow", "G"))
        self.g1.setShortcut(_translate("MainWindow", "U"))
        self.e1.setText(_translate("MainWindow", "E"))
        self.e1.setShortcut(_translate("MainWindow", "T"))
        self.c1.setText(_translate("MainWindow", "C"))
        self.c1.setShortcut(_translate("MainWindow", "E"))
        self.fs0.setText(_translate("MainWindow", "F#"))
        self.fs0.setShortcut(_translate("MainWindow", "H"))
        self.as1.setText(_translate("MainWindow", "A#"))
        self.as1.setShortcut(_translate("MainWindow", "9"))
        self.a0.setText(_translate("MainWindow", "A"))
        self.a0.setShortcut(_translate("MainWindow", "M"))
        self.gs0.setText(_translate("MainWindow", "G#"))
        self.gs0.setShortcut(_translate("MainWindow", "J"))
        self.e0.setText(_translate("MainWindow", "E"))
        self.e0.setShortcut(_translate("MainWindow", "V"))
        self.cs1.setText(_translate("MainWindow", "C#"))
        self.cs1.setShortcut(_translate("MainWindow", "4"))
        self.cs0.setText(_translate("MainWindow", "C#"))
        self.cs0.setShortcut(_translate("MainWindow", "D"))
        self.b0.setText(_translate("MainWindow", "B"))
        self.b0.setShortcut(_translate("MainWindow", ","))
        self.fs1.setText(_translate("MainWindow", "F#"))
        self.fs1.setShortcut(_translate("MainWindow", "7"))
        self.as0.setText(_translate("MainWindow", "A#"))
        self.as0.setShortcut(_translate("MainWindow", "K"))
        self.g0.setText(_translate("MainWindow", "G"))
        self.g0.setShortcut(_translate("MainWindow", "N"))
        self.d0.setText(_translate("MainWindow", "D"))
        self.d0.setShortcut(_translate("MainWindow", "C"))
        self.c0.setText(_translate("MainWindow", "C"))
        self.c0.setShortcut(_translate("MainWindow", "X"))
        self.label_6.setText(_translate("MainWindow", "Master"))
        self.label.setText(_translate("MainWindow", "Sine"))
        self.SquareVolume.setStyleSheet(_translate("MainWindow", "background-color: rgb(205, 255, 23)"))
        self.MasterVolume.setStyleSheet(_translate("MainWindow", "background-color: rgb(205, 255, 23)"))
        self.label_2.setText(_translate("MainWindow", "Triangle"))
        self.label_3.setText(_translate("MainWindow", "Saw"))
        self.label_4.setText(_translate("MainWindow", "Square"))
        self.label_8.setText(_translate("MainWindow", "1111111111"))
        self.label_5.setText(_translate("MainWindow", "Noise"))
        self.NoiseVolume.setStyleSheet(_translate("MainWindow", "background-color: rgb(205, 255, 23)"))
        self.label_7.setText(_translate("MainWindow", "1111111111"))
        self.ds1.setText(_translate("MainWindow", "D#"))
        self.ds1.setShortcut(_translate("MainWindow", "5"))
        self.gs1.setText(_translate("MainWindow", "G#"))
        self.gs1.setShortcut(_translate("MainWindow", "8"))
        self.ds0.setText(_translate("MainWindow", "D#"))
        self.ds0.setShortcut(_translate("MainWindow", "F"))
        self.d1.setText(_translate("MainWindow", "D"))
        self.d1.setShortcut(_translate("MainWindow", "R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

