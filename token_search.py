from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class TokenScraper():

	def __init__(self):
		self.data_source_url = "https://etherscan.io/txs" #"https://www.tokenanalyst.io/"
		self.driver = webdriver.Chrome('/Users/uziminhas/chromedriver')
		self.driver.get(self.data_source_url)

	def input_search(self):
		driver = self.driver
		# search = driver.find_element_by_class_name('tokendropdown')
		# search.click()
		# search.select_by_visible_test('Ox')
		# search.send_keys(Keys.RETURN)

	def scrape_table(self):
		html = self.driver.page_source # Gets source of current page
		soup = BeautifulSoup(html, 'html.parser')
		for rows in soup.findAll('tr'):
			data = [rows.text for rows in rows.findAll("td")]
			print data
		# tds = soup.findAll('td')
		# print tds
		# for link in soup.find_all('a'):
		#	print(link.get('href'))
		# print self.soup.title

if __name__ == "__main__":
    TokenScraper().input_search()
    TokenScraper().scrape_table()


