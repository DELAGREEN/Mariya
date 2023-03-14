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
from PySide6.QtWidgets import (QApplication, QDialog, QProgressBar, QPushButton,
    QSizePolicy, QWidget)



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(380, 100)
        Dialog.setMinimumSize(QSize(380, 100))
        Dialog.setMaximumSize(QSize(380, 100))
        Dialog.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        Dialog.setMouseTracking(True)
        Dialog.setTabletTracking(False)
        Dialog.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        Dialog.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        Dialog.setAcceptDrops(False)
        Dialog.setWindowTitle(u"\u041c\u0430\u0440\u0438\u044f(\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430 \u043f\u043e \u0444\u043e\u0440\u043c\u0430\u043c \u0424\u0421\u0413\u0421)")
        icon = QIcon()
        iconThemeName = u"applications-system"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Dialog.setAutoFillBackground(False)
        Dialog.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(0, 10, 381, 41))
        self.pushButton.clicked.connect(self.button_clicked)   #Кликабельность кнопки
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 70, 381, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(20)                                   # % значения заполнения
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi


    def button_clicked(self):
        from main import main_Function
        from report_module import formater_to_exel
        main_Function()
        formater_to_exel()
        print('Тык1')


    #def button_2_clicked(self):
    #    #final_define_write_a_report_file(path_to_loads_dir, final_exel_file)
    #    print('Тык2')
    ##def progress_bar(self):
    def retranslateUi(self, Dialog):
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0438 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430 \u0441 \u0441\u0430\u0439\u0442\u0430 \u0424\u0421\u0413\u0421 (exel)", None)) # type: ignore 
        self.progressBar.setFormat(QCoreApplication.translate("Dialog", u"%p%", None)) # type: ignore 
        pass
    # retranslateUi
    
    
    