#row players-wrapper
from selenium import webdriver
from bs4 import BeautifulSoup
class Player():
	"""docstring for Player"""
	def __init__(self):
		self.name=""
		self.link=""


		
##create driver to download the html page.
def get_player_list():
	driver = webdriver.PhantomJS(executable_path = r'/Users/sachinjose/Downloads/phantomjs/bin/phantomjs')
	url="http://www.nba.com/players"
	driver.get(url)
	soup=BeautifulSoup(driver.page_source,'lxml')
	div=soup.find('div',class_='row players-wrapper')
	player_list=[]
	for a in div.find_all('a'):
		new_play=Player()
		new_play.name=a.text
		new_play.link=a['href']
		player_list.append(new_play)

	for play in player_list:
		print play.name,play.link

	driver.quit()
	return player_list

get_player_list()