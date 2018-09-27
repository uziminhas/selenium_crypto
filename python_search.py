import unittest # built-in Python unit testing framework based on Junit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase): # this class inherits from TestCase class

	def setUp(self): # Initialization function that gets called before every test function
		self.driver = webdriver.Chrome('/Users/uziminhas/chromedriver') # Creates instance of WebDriver

	def test_search_in_python_org(self): # Test case method
		driver = self.driver # Create local reference to the driver object created in setUp method
		driver.get("http://www.python.org") # WebDriver will wait until onload event has fired before returning control to test script
		self.assertIn("Python",driver.title)
		elem = driver.find_element_by_name("q")
		elem.clear() # Clear any pre-populated text in input fields
		elem.send_keys("pycon")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	def tearDown(self): # Gets called after every test metjod
		self.driver.close()

if __name__ == "__main__": # Boiler plate code to run the test suite
	unittest.main()

