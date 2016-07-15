from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib2
user1 = raw_input("Enter User id of 1st user : ")
user2 = raw_input("Enter User id of 2nd user : ")
print "\n"
print "Comparing " + user1 + " and " + user2
url="http://www.spoj.com/users/"
x1=user1
x2=user2
url1 = url + x1
url2 = url + x2
page1=urllib2.urlopen(url1)
soup1=BeautifulSoup(page1.read())
page2=urllib2.urlopen(url2)
soup2=BeautifulSoup(page2.read())
while soup1.find('div', {'class' :'col-md-3'}, id='user-profile-left')==None or soup2.find('div', {'class' :'col-md-3'}, id='user-profile-left')==None:
	print "Invalid Username(s), Enter a valid username : "
	print "Enter User id of 1st user : "
	url1=raw_input()
	print "Enter User id of 2nd user : "
	url2=raw_input()
	url1 = url + url1
	url2 = url + url2
	page1 = urllib2.urlopen(url1)
	soup1 = BeautifulSoup(page1.read())
	page2 = urllib2.urlopen(url2)
	soup2 = BeautifulSoup(page2.read())
problemss1 = soup1.body.table.find_all('a')
problemss2 = soup2.body.table.find_all('a')
no_of_problems_solved_by_user1 = 0
no_of_problems_solved_by_user2 = 0
problems1 = []
problems2 = []
for i in problemss1:
	problems1.append(i.string)
	no_of_problems_solved_by_user1=no_of_problems_solved_by_user1+1
for i in problemss2:
	problems2.append(i.string)
	no_of_problems_solved_by_user2=no_of_problems_solved_by_user2+1
problems_solved_by_user2_not_by_user1 = []
problems_solved_by_user1_not_by_user2 = []
for i in problems1:
	c=0
	for j in problems2:
		if i==j:
			c=1
	if c==0:
		problems_solved_by_user2_not_by_user1.append(i)

for i in problems2:
	c=0
	for j in problems1:
		if i==j:
			c=1
	if c==0:
		problems_solved_by_user1_not_by_user2.append(i)
print "" 
print "Problems Solved by " + user1 + " not by" + user2
print ""
for i in problems_solved_by_user2_not_by_user1:
	print i
print ""
print "Problems solved by " + user2 + " not by " + user1
print ""
for i in problems_solved_by_user1_not_by_user2:
	print i
