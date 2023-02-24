#coding=1251
from time import sleep
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_Dialog
import time 


start = time.time()


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


class App(QMainWindow):
	def __init__(self):
		super(App, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
	

end = time.time()
total_time = (end - start)/60
print(f'Время выполнения: {total_time} мин.')

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	window = App()
	window.show()

	sys.exit(app.exec())