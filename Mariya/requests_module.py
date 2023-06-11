# -*- coding: utf-8 -*-
import requests
from config_module import current_day, current_time
from errors_logger import ErrorsLogger

class RequestsModule():

	def __init__(self, inn:int) -> None:
		self._inn = inn

	def get_id(self, inn:int)->dict[str, int]:
		'''
		с помощью данной функции будем получать ID  организации
		для обращения к серверу напрямую
		'''
		website = 'https://websbor.gks.ru/webstat/api/gs/organizations'     
		data = {
		'okpo': '',
		'inn': inn,
		'ogrn': '',
		'requestDateTime': f'{current_day} в {current_time}'
		}
		response = requests.post(website, data, verify= False).json()
		id = response[0]
		result_data = {
			'id': id['id'],
			'inn' : inn
			}
		return result_data

	def _get_id(self)->int:
		'''
		с помощью данной функции будем получать ID  организации
		для обращения к серверу напрямую
		'''
		website = 'https://websbor.gks.ru/webstat/api/gs/organizations'     
		data = {
		'okpo': '',
		'inn': self._inn,
		'ogrn': '',
		'requestDateTime': f'{current_day} в {current_time}'
		}
		response = requests.post(website, data, verify= False).json()
		result = response[0]
		id = result['id']
		return id

	def get_organization(self)->list:
		'''
		с помощью данной функции получает list c данными(data) напрямую от сайта
		'''
		try:
			id = self._get_id()
			website = f'https://websbor.gks.ru/webstat/api/gs//organizations/{id}/forms'
			data = {
			'okpo': '',
			'inn': self._inn,
			'ogrn': '',
			'requestDateTime': f'{current_day} в {current_time}'
			}
			response = requests.get(website, data, verify= False).json()					
			for item in response:
				id = item['id']
				name = item['name']
				okud = item['okud']
				form_period = item['form_period']
				formatted_period = item['formatted_period']
				reported_period = item['reported_period']
				period = item['period']
				period_comment = item['period_comment']
				dept_nsi_id = item['dept_nsi_id']
				dept_nsi_code = item['dept_nsi_code']
				type_exam = item['type_exam']
				index = item['index']
				description = item['description']
				act_num = item['act_num']
				act_date = item['act_date']
				end_time = item['end_time']
				comment = item['comment']
				updatingDate = item['updatingDate']
				isValid = item['isValid']
				periodicity =item ['periodicity']
				periodNum = item['periodNum']
				periodYear = item['periodYear']
				yield [self._inn, index, name, form_period, end_time, reported_period, comment, okud]

		except:
			ErrorsLogger(f'{self._inn}').print_error()
