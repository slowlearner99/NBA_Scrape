from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests
import time
class Player():
	"""docstring for Player"""
	def __init__(self):
		self.name = ""
		self.link = ""
		self.Height = ""
		self.Weight = ""
		self.Born = ""

def get_player_list():
	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	url = 'http://stats.nba.com/players/?ls=iref:nba:gnav'
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_= 'col-lg-12')
	player_list = []
	for a in div.find_all('a'):
		new_play = Player()
		new_play.name = a.text
		new_play.link = a['href']
		player_list.append(new_play)
	for one_player in player_list:
		print one_player.name
		print one_player.link
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


def get_nba_player_image(player_list):
	driver = webdriver.PhantomJS(executable_path = r'/Users/sachinjose/Downloads/phantomjs/bin/phantomjs')
	if not os.path.exists('nba_player'):
		os.makedirs('nba_player')
	for player in player_list:
		url = player.link
		driver.get(url)
		time.sleep(2)
		soup = BeautifulSoup(driver.page_source, 'lxml')
		sect = soup.find('section', class_ = 'nba-player-header__item nba-player-header__headshot')
		img = sect.find('img')	
		print img['src']		f = open('nba_player\{0}.jpg'.format(player.name),'wb')
	f.write(requests.get(img['src']).content
	f.close()
	driver.quit()

get_nba_player_image( get_player_list() )	