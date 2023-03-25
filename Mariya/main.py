# -*- coding: utf-8 -*-
import sys
import asyncio
import random
from time import sleep
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_module import Ui_Dialog
import time 
from report_module import read_exel_inn, checking_existence_files
from requests_module import get_id, get_organization, report_generation


async def progress_bar(steps: int, max_lenght: int = 50):
	step_size = 50 / steps
	#step_size = 100 / max_lenght
	for i in range(1, steps + 1):
		print(f'\r{int(i * step_size)}%', end='')	#очень интересная тема
		counter = int(i * step_size)
		await asyncio.sleep(0.05)
	print('')							#очень интересная тема ^^^


def request():
	list_inn = read_exel_inn()
	for item in list_inn:
		for inn in item:
			report_generation(get_organization(get_id(inn)), inn)


async def main_Function():
	try:
		request()
	except Exception as ex:
		print(f'Ошибка: {ex}')


class App(QMainWindow):
	def __init__(self):
		super(App, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)


if __name__ == '__main__':
	start = time.time()

	checking_existence_files()

	app = QApplication(sys.argv)
	window = App()
	window.show()


	end = time.time()
	total_time = (end - start)/60
	print(f'Время выполнения: {total_time} мин.')


	sys.exit(app.exec())	