# after installing the packages in the command line, I'm going to import those libraries, specifically requests (to get
# info from websites), beautiful soup (to scrape the information) and csv (to put the information into a csv). 
# From OS, we'll bring Slack info for outputting the information.

import requests
from bs4 import BeautifulSoup
import csv
import os
from slack import WebClient
from slack.errors import SlackApiError

url = "https://www.umaryland.edu/police/crime-and-safety-statistics/60-day-crime-and-fire-log/"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
# find_all takes the html tag that it wants, in this case "div," but there's a bunch, so we need to get the divs with
# specific class names associated with it. 
htmlEntries = soup.find_all("div", {"class": "sixty-day-log-entry"})

cases = []
# Looping for each entry from the website
for e in htmlEntries:
    # each entry has a p tag in front of it, so we're using find_all to get each entry
    info = e.find_all('p')
    # grabbing the first line of data, i.e. the date reported.
    # removing some text because it'll mess up the output later on. 
    date_reported = info[0].text.replace(u'\xa0', u' ').replace("Date Reported  ","")
    report_number = info[1].text.replace(u'\xa0', u' ')
    location = info[2].text.replace(u'\xa0', u' ').replace("Location  ", "") 
    occurred_from = info[3].text.replace(u'\xa0', u' ').replace("Occurred from  ", "")
    incident = info[4].text.replace(u'\xa0', u' ').replace("Incident  ", "").lower()
    synopsis = info[5].text.replace(u'\xa0', u' ').replace("Synopsis ", "").lower()
    disposition = info[6].text.replace(u'\xa0', u' ').replace("Disposition  ", "").lower()
    # I wanna change the capitalization of some of the words. I want to lowercase everything in incident, synopsis, and disposition. 

    data = {"date_reported": date_reported, "report_number": report_number, "location": location, "occurred_from": occurred_from, "incident": incident, "synopsis": synopsis, "disposition": disposition}

    # putting a list of all the strings into one. 
    cases.append(data)


# printing the most recent case, which will be our message.
print(cases[0])

# Write the data to a CSV file
with open('crime_umb.csv', 'a', newline='') as csvfile:
    fieldnames = ['date_reported', 'report_number', 'location', 'occurred_from', 'incident', 'synopsis', 'disposition']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # Write header row
    writer.writeheader()
    # Write data rows
    for row in cases:
        writer.writerow(row)

# Read the contents of the CSV file into a list of dictionaries
existing_data = []
with open('crime_umb.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        existing_data.append(row)

# New data that you want to append to the CSV file
new_data = [cases[0]]

# Append new data to existing data (without creating duplicates)
for row in new_data:
    if row not in existing_data:
        existing_data.append(row)

# Write the updated data to the CSV file
# with open('crime_umb.csv', 'a', newline='') as csvfile:
#     #fieldnames = ['date_reported', 'report_number', 'location', 'occurred_from', 'incident', 'synopsis', 'disposition']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     # Write header row
#     writer.writeheader()  
#     # Write data rows
#     for row in existing_data:
#         writer.writerow(row)

#Slack info
slack_token = os.environ.get('SLACK_API_TOKEN')

client = WebClient(token=slack_token)

    #if this no case occurred, don't send it to slack.
if cases[0]['report_number'] == "Report #  N/A":
    msg = f"No crime nor fire took place today. Yay!\n\nBut if you'd like to see all crimes and fires that have previously taken place at the University of Maryland, Baltimore, <https://github.com/NewsAppsUMD/secret_slack_vifatusi/blob/main/crime_umb.csv|click here>." 
else:
    # there's nothing to commit
    msg = f"On {cases[0]['date_reported']}, authorities submitted this incident -- *{cases[0]['incident']}* -- to the UMB 60-Day Crime and Fire Log. It took place at {cases[0]['location']} and occurred from {cases[0]['occurred_from']}.\nSimply put, a {cases[0]['synopsis']} Authorities have a {cases[0]['disposition']}. This is identified as {cases[0]['report_number']}.\nIf you'd like to see all of crimes and fires that have taken place at the University of Maryland, Baltimore, <https://github.com/NewsAppsUMD/secret_slack_vifatusi/blob/main/crime_umb.csv|click here>."

try:
    response = client.chat_postMessage(
        channel="slack-bots",
        text=msg,
        unfurl_links=False, 
        unfurl_media=False
    )
    print("success!")
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")