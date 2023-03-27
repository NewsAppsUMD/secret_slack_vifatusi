# after installing the packages in the command line, I'm going to import those libraries, specifically requests (to get
# info from websites) and beautiful soup (to scrape the )

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.umaryland.edu/police/crime-and-safety-statistics/60-day-crime-and-fire-log/"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
# find_all takes the html tag that it wants, in this case "div," but there's a bunch, so we need to get the divs with
# specific class names associated with it. 
htmlEntries = soup.find_all("div", {"class": "sixty-day-log-entry"})

# making sure that we are getting the info we need
#print(htmlEntries[0])
# we are

# Creating an empty list for our information go in 
cases = []

# Looping for each entry from the website
for e in htmlEntries:
    # each entry has a p tag in front of it, so we're using find_all to get each entry
    info = e.find_all('p')
    # grabbing the first line of data, i.e. the date reported. 
    date_reported = info[0].text.replace(u'\xa0', u' ')
    #info_on_date = date_reported.split(" ")
    #time = info_on_date[2:]
    #timestamp_str = ' '.join(time) 
    report_number = info[1].text.replace(u'\xa0', u' ')
    location = info[2].text.replace(u'\xa0', u' ') 
    occurred_from = info[3].text.replace(u'\xa0', u' ')
    incident = info[4].text.replace(u'\xa0', u' ')
    synopsis = info[5].text.replace(u'\xa0', u' ')
    disposition = info[6].text.replace(u'\xa0', u' ')

    data = [date_reported, report_number, location, occurred_from, incident, synopsis, disposition]

    # putting a list of all the strings into one. 
    cases.append(data)


for c in cases:
    print(c)

outfile = open("crime_umb.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["date_reported", "report_number", "location", "occurred_from", "incident", "synopsis", "disposition"])
writer.writerows(cases)