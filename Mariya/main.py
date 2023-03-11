# -*- coding: utf-8 -*-
from time import sleep
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_module import Ui_Dialog
import time 
from report_module import read_exel_inn, writer_a_report_file, append_in_data
from config_module import path_to_data, path_to_final_exel_file
from requests_module import get_id, get_organization, report_generation


def progress_bar(steps: int, max_lenght: int = 50) -> None:
	
	step_size = 50 / steps

	#step_size = 100 / max_lenght


	for i in range(1, steps + 1):
		print(f'\r{int(i * step_size)}%', end='')
		p = i * step_size
		sleep(0.05)
	print('')
	return p 

#progress_bar(100)

def main_Function():
	try:
		data = read_exel_inn(path_to_data)
		for inn in data:
			#append_in_data(report_generation(get_organization(get_id(inn)), inn))
			#writer_a_report_file(report_generation(get_organization(get_id(inn)), inn))
			report_generation(get_organization(get_id(inn)), inn)
			#report_generation(get_organization(get_id(inn)), inn)
			#time.sleep(3)
	except Exception as ex:
		print(f'Ошибка: {ex}')
main_Function()

#def example(inn):
#	writer_a_report_file(report_generation(get_organization(get_id(inn)), inn))
#	return("Example >>> Complite")
#
#data = read_exel_inn(path_to_data)
#for inn in data:
#	example(inn)
#	next(data)



class App(QMainWindow):
	def __init__(self):
		super(App, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
	

if __name__ == '__main__':
	start = time.time()

	app = QApplication(sys.argv)
	window = App()
	window.show()


	end = time.time()
	total_time = (end - start)/60
	print(f'Время выполнения: {total_time} мин.')


	sys.exit(app.exec())	




