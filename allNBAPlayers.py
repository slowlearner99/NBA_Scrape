from selenium import webdriver
from bs4 import BeautifulSoup
class Player():
	def __init__(self):
		self.name = ""
		self.link = ""
		self.Height = ""
		self.Weight = ""
		self.Born = ""
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

def get_detail_for_all_players(player_list):
	driver = webdriver.PhantomJS(executable_path = r'/Users/sachinjose/Downloads/phantomjs/bin/phantomjs')
	for p in player_list[0:2]:
		url = p.link
		driver.get(url)
		soup = BeautifulSoup(driver.page_source, 'lxml')
		Height = ""
		born="BORN "
		b_span=soup.find('span',string="BORN")
		for span in b_span.findNextSiblings():	
			born = born + span.text
		height=""
		h_span=soup.find('section',class_="nba-player-vitals__top-left small-6")
		for span in h_span.find_all('p'):
			height=height+span.text
		weight=""
		w_span=soup.find('section',class_="nba-player-vitals__top-right small-6")
		for a in w_span.find_all('p'):
			weight=weight+span.text
		p.Height = Height
		p.Weight = Weight
		p.Born = Born
	driver.quit()
	return player_list	
player_list = get_detail_for_all_players(get_player_list())
for p in player_list[0:2]:
	print '\n'
	print p.name
	print p.link
	print p.Height
	print p.Weight
	print p.Born
	print '\n'