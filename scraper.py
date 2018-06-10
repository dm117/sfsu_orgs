import bs4 as bs
import urllib.request

#opens the SFSU url and reads the page
myUrl = urllib.request.urlopen('http://www.sfsu.edu/~sicc/organizationdirectory.html').read()

#creates soup object and parses url using lxml
soup = bs.BeautifulSoup(myUrl,'lxml')

#look for the div tag with the id: main
divMain = soup.find('div',{'id':'main'})


# print(type(divMain)) #for debugging

# for i in divMain.find_all('ul')[1]:
#     print(i.text)
#     print("---------------------------------")

myFile = open("orgs.txt","w+")

mylist = divMain.find_all('ul')[1] # gets the second <ul> tag
for li in mylist.find_all('li'):
    myFile.write(li.text+"\n") # writes the contents of every <li> tag inside mylist to a file

# to do list
# error handling if cant create the file for some reason
# turn this file into a function so i can run this from the other file
# upload on git
# run on server
#clean up code


# maybe use this as part of a larger program to get contact info for all greekrogs 
# (have a csv file with greek orgs and info, if no info output orgs that still need contact info)