#to find the dob, height and weight of a player

from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.PhantomJS(executable_path = r'/Users/sachinjose/Downloads/phantomjs/bin/phantomjs')
url="http://www.nba.com/players/alex/abrines/203518"
driver.get(url)
soup=BeautifulSoup(driver.page_source,'lxml')
born="BORN "
b_span=soup.find('span',string="BORN")
for span in b_span.findNextSiblings():	
	born = born + span.text
print born
height=""
h_span=soup.find('section',class_="nba-player-vitals__top-left small-6")
for a in h_span.find_all('p'):
	height=height+a.text
print height
weight=""
w_span=soup.find('section',class_="nba-player-vitals__top-right small-6")
for a in w_span.find_all('p'):
	weight=weight+a.text
print weight