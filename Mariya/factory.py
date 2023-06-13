# -*- coding: utf-8 -*-
import asyncio
from time import sleep
from report_module import ReportModule
from requests_module import RequestsModule


#async def progress_bar(steps: int, max_lenght: int = 50):
#	step_size = 50 / steps
	#step_size = 100 / max_lenght
#	for i in range(1, steps + 1):
#		print(f'\r{int(i * step_size)}%', end='')	#очень интересная тема
#		counter = int(i * step_size)
#		await asyncio.sleep(0.05)
#		Ui_Dialog.on_progress_change(10)

	#return('')										#очень интересная тема ^^^
#class example(Ui_Dialog):
#	def __init__(self, value) -> None:
#		super().__init__()
#		self.value = value
#		self.progressBar.setValue(self.value)
#		self.progressBar.setGeometry(0, 120, 381, 23)
#		self.progressBar.show()


def request() -> None:
	bufered_data = []
	report = ReportModule()
	for inn in report.read_exel_inn():
		request = RequestsModule(inn).get_organization()
		for data in request:
			bufered_data.append(data)
	return bufered_data


async def write_in_exel() -> None:
	report = ReportModule()
	for data in request():
		report.writer_a_report_file(data)


async def main_Function():
	#try:
		tasks = [
	   		write_in_exel(),
		]
		await asyncio.gather(*tasks)
		
	#except Exception as ex:
	#	print(f'Ошибка: {ex}')