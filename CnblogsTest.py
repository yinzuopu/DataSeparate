import time
import unittest
from selenium import webdriver
from GetElement import GetElement


class Cnblogs(unittest.TestCase):

	def setUp(self):
		self.obj = GetElement()
		self.driver = webdriver.Firefox()
		self.driver.get("https://www.cnblogs.com/")

	def test_cnblogs(self):
		element_query = self.obj.getelement(self.driver, "cnblogs", "queryBox_id")
		element_query.send_keys("python")
		element_btn = self.obj.getelement(self.driver, "cnblogs", "queryBtn_id")
		element_btn.click()
		time.sleep(5)

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity=2)