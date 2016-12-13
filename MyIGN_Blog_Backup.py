'''
How to run this program:

Install Python3 on your computer from https://www.python.org/downloads/,

You need BeautifulSoup from here: https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/
And requests from here: https://github.com/kennethreitz/requests/tarball/master

Download them both and extract folders. 

Go to both folders and run the python file by typing in terminal (open terminal in that folder) 'python setup.py'

Run script by going to folder where script is stored, open terminal here and type 'python3 MyIGN_Blog_Backup.py'.

You are done.

'''

import requests
from bs4 import BeautifulSoup

username = input("Enter username: ")
year_low = int(input("Enter the lower bound of year: "))
year_up = int(input("Enter the upper bound of year: "))

for year in range(year_low, year_up+1):
	for month in range(1, 13):
		if month < 10:
			url = 'http://www.ign.com/blogs/' + username + '/' + str(year) + '/' + str(0) + str(month)
		else:
			url = 'http://www.ign.com/blogs/' + username + '/' + str(year) + '/' + str(month)
		r = requests.get(url)
		soup = BeautifulSoup(r.content)
		for div in soup.findAll("div", { "class" : "post type-post" }):
			text_file = open(str(year) + '-' + str(month) + ".txt", "a")
			text_file.write('\n\n\n')
			text_file.write(div.text)
			text_file.close()
		
		


