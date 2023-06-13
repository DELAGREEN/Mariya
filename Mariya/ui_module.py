# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QWidget)
import asyncio
import time
from factory import main_Function


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(380, 150)
        Dialog.setMinimumSize(QSize(380, 100))
        Dialog.setMaximumSize(QSize(380, 150))
        Dialog.setCursor(QCursor(Qt.ArrowCursor))
        Dialog.setMouseTracking(True)
        Dialog.setTabletTracking(False)
        Dialog.setFocusPolicy(Qt.NoFocus)
        Dialog.setContextMenuPolicy(Qt.NoContextMenu)
        Dialog.setAcceptDrops(False)
        Dialog.setWindowTitle(u"\u041c\u0430\u0440\u0438\u044f(\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430 \u043f\u043e \u0444\u043e\u0440\u043c\u0430\u043c \u0424\u0421\u0413\u0421)")
        icon = QIcon()
        iconThemeName = u"applications-system"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        Dialog.setInputMethodHints(Qt.ImhNone)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(131, 50, 121, 51))
        self.pushButton.clicked.connect(self.button_click)   #Кликабельность кнопки
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 120, 381, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 371, 16))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.retranslateUi(Dialog)
        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi


    def button_click(self):
        self.update_progress(40, 60)
        asyncio.run(main_Function())
        self.update_progress(100)
        return None


    def update_progress(self, value1=0, value2=101):
        for i in range(value1, value2):
            self.progressBar.setValue(i)
            self.progressBar.setGeometry(0, 120, 381, 23)
            self.progressBar.show()
            time.sleep(0.1)


    def retranslateUi(self, Dialog):
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043f\u0443\u0441\u043a \u0441\u043a\u0440\u0438\u043f\u0442\u0430", None))
        self.progressBar.setFormat(QCoreApplication.translate("Dialog", u"%p%", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0438 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430 \u0441 \u0441\u0430\u0439\u0442\u0430 \u0424\u0421\u0413\u0421 (exel)", None))
        pass
    # retranslateUi
