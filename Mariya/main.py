# -*- coding: utf-8 -*-
import sys
import asyncio

from time import sleep
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_module import Ui_Dialog
import time 

from report_module import ReportModule
from requests_module import RequestsModule #get_id, get_organization, report_generation



async def progress_bar(steps: int, max_lenght: int = 50):
	step_size = 50 / steps
	#step_size = 100 / max_lenght
	for i in range(1, steps + 1):
		print(f'\r{int(i * step_size)}%', end='')	#очень интересная тема
		counter = int(i * step_size)
		await asyncio.sleep(0.05)

	return('')										#очень интересная тема ^^^



async def request() -> None:
	request = RequestsModule()
	report = ReportModule()
	list_inn = report.read_exel_inn()
	for inn in list_inn:
		print(inn)
		data = request.report_generation(request.get_organization(request.get_id(inn)), inn)
		print(data)
		for organization in data:
			await report.writer_a_report_file(organization)
		print('Write >> OK')
		await asyncio.sleep(2)
	report.formater_to_exel()
			

async def main_Function():
	#try:
		tasks = [
			progress_bar(100, 100),
	   		request()
		]
		await asyncio.gather(*tasks)
		
	#except Exception as ex:
	#	print(f'Ошибка: {ex}')



class App(QMainWindow):
	def __init__(self):
		super(App, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)


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

