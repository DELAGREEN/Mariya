################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from ast import Lambda
from tkinter.ttk import Progressbar
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QWidget)
from driver import auto_page_pass
from data import (path_to_data, list_in_list, read_exel_inn, final_define_write_a_report_file)
from config import (path_to_loads_dir, final_exel_file)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(380, 140)
        Dialog.setMinimumSize(QSize(380, 140))
        Dialog.setMaximumSize(QSize(380, 140))
        Dialog.setCursor(QCursor(Qt.ArrowCursor))
        Dialog.setMouseTracking(True)
        Dialog.setTabletTracking(False)
        Dialog.setFocusPolicy(Qt.NoFocus)
        Dialog.setContextMenuPolicy(Qt.NoContextMenu)
        Dialog.setAcceptDrops(False)
        Dialog.setWindowTitle(u"Мария (Формирование отчета ФСГС)")
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
        self.pushButton.setGeometry(QRect(130, 10, 241, 41))
        self.pushButton.clicked.connect(self.button_clicked)                    #Кликабельность кнопки
        
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(130, 60, 241, 41))
        self.pushButton_2.clicked.connect(self.button_2_clicked)                #Кликабельность кнопки

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 110, 361, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(10)                                           #Колл % на которое заполнен прогрессбар  
        self.progressBar.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 5, 21, 41))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 55, 21, 51))
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def button_clicked(self):
        read_exel_inn(path_to_data, 1)
        print('Тык1')
    def button_2_clicked(self):
        final_define_write_a_report_file(path_to_loads_dir, final_exel_file)
        print('Тык2')
    #def progress_bar(self):
 
        



    # setupUi

    def retranslateUi(self, Dialog):
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Загрузка файлов с сайта ФСГС", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Создание финального отчета", None))
        
        self.progressBar.setFormat(QCoreApplication.translate("Dialog", u"50", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" color:#ff0000;\">1</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" color:#ff0000;\">2</span></p></body></html>", None))
        pass

    # retranslateUi