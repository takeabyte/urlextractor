####Code by takeabyte@2015  ###########################################
####Extracts links from a webpage and saves them as txt file ###

from bs4 import BeautifulSoup
import lxml, requests, urllib2, re

## Specify URL (http://www.yoursite.com/foo.html)
url = raw_input("Enter target URL: ");

## Saves Result in variable data
data = urllib2.urlopen(url).read()

## Analyses the data with lxml parser
page = BeautifulSoup(data,"lxml")


## lists links containing only the searchquery
search = raw_input("Enter link searchquery: ");


## saves extracted links in text file (rootdirectory where py script is stored)
filename = raw_input("Enter Filename: ")+'.txt';
with open(filename, 'w') as text_file:
    for link in page.findAll(href=re.compile(search)):
        l = link.get("href")
        text_file.write(l +'\n')
        print l

## Prints all results to console for quick check
## and shows your filename when done
print ''
print 'File '+filename+' saved'
