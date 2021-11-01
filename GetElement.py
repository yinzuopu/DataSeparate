# -*- coding:GBK -*-
# ���������ģ��
import os
import configparser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


# ������ȡ������
class GetElement():
	"""
	�������ļ��л�ȡ��λ��Ϣ
	"""
	def __init__(self):
		self.elementIni = os.path.dirname(os.path.abspath(__file__)) + r'\Element.ini'  #�����ļ�·��

	def getelement(self, driver, query_section, query_option):
		try:
			config = configparser.ConfigParser()
			# ��ȡ�����ļ����ڴ���
			config.read(self.elementIni)
			locators = config.get(query_section,query_option).split(':')
			query_box = locators[0]
			query_btn = locators[1]
			element = WebDriverWait(driver, 5).until(lambda x : x.find_element(query_box, query_btn))
		except Exception as e:
			raise e
		else:
			return element


if __name__ == "__main__":
	ele = GetElement()
	print(ele.elementIni)
	driver = webdriver.Firefox()
	driver.get("https://www.cnblogs.com/")
	element = ele.getelement(driver, "cnblogs", "queryBox_id")
	element.send_keys("python")



