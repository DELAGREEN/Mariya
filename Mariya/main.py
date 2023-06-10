# -*- coding: utf-8 -*-
import sys
import asyncio

from time import sleep
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_module import Ui_Dialog
import time 

from report_module import ReportModule
from requests_module import RequestsModule



class App(QMainWindow):
	def __init__(self):
		super(App, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		#self.ui.progressBar.setValue()


def Start_app():

	app = QApplication(sys.argv)
	window = App()
	window.show()
	sys.exit(app.exec())	


if __name__ == '__main__':
#	start = time.time()

	try:
		report = ReportModule()
		report.checking_existence_files
		Start_app()

	except Exception as ex:
		print(f'Ошибка: {ex}')
	

#	end = time.time()
#	total_time = (end - start)/60
#	print(f'Время выполнения: {total_time} мин.')

