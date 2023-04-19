# -*- coding: utf-8 -*-
import requests
from config_module import current_day, current_time
#from report_module import writer_a_report_file
from time import sleep
import asyncio


class RequestsModule(object):


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


	def get_organization(self, data:dict)->dict:
		'''
		с помощью данной функции получает dict c данными(data) напрямую от сайта
		'''

		id = data['id']
		inn = data['inn']
		website = f'https://websbor.gks.ru/webstat/api/gs//organizations/{id}/forms'
		data = {
		'okpo': '',
		'inn': inn,
		'ogrn': '',
		'requestDateTime': f'{current_day} в {current_time}'
		}
		response = requests.get(website, data, verify= False).json()
		return response


	def report_generation(self, data:dict, inn:int):
		list1 = []
		for item in data:
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
			yield [inn, index, name, form_period, end_time, reported_period, comment, okud]