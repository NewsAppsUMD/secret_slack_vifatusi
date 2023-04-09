# UMBCrimeBot - a Scraper for Crime and Fires at the University of Maryland, Baltimore.

## MEMO & Diary of a Bot
When starting this assignment, I first thought about what I would be interested in. A lot of those ideas were unfortunately impossible to do because the data wasn't readily available. Then I thought about what would be easily scrapable and available and you guessed it - crime logs. Someone took crime from UMD, so I decided to go with crime from UMB. As you'll see in the diary below, I used the tutorial to get me through this, a little bit of ChatGPT to extract info from my dictionary into a csv and other students' repositiories to figure out my CSV situation. 

* Storing the data:
    The only way how I would store this data is by putting all new crimes into my ``crime_umb_.csv`` dataset. The website I'm scrapping the data from only shows crimes and fires that happened within 60 days, so it doesn't show anything before that. For historical context and research, the csv could help with that.  However, it's been difficult to figure out. That's the issue I'm still running into and the goal I couldn't accomplish. Rather than appending new info, it duplicates what's already there, rather than adding just the most recent case. 
* Input from users:
    Users would have two options for input: date and report. A user could input a date that a crime or fire took place and the bot would spit back details about that crime/fire. The bot would also bring other crimes/fires that happened on that date if there were any. For report #, if a user knows the number of a report, they can also input that, and the bot would spit back that report. 

    Other options would include location and disposition. They can input a specific address to see all the crimes/fires that took place the address they inputted. They would also be able to put in a disposition, like arrest made or report taken, to see all the crimes/fires that resulted in a disposition. However, it might be too vague for use.
* Best Schedule for Updates:
    I noticed that authorities upload new information to the website everyday between 7pm and 9 pm. So I currently have it set to scrape and update 10pm everyday. 

### March 27th, 2023:
    I started taking the first few steps of grabbing the information from [UMB's 60-Day Crime and Fire Log.](https://www.umaryland.edu/police/crime-and-safety-statistics/60-day-crime-and-fire-log/) The tutorial from class was extremely helpful, as it provided the libraries I'd use to scrape the information. I needed to grab the data from the 'p' tags on the website. I had to put my information into a list and do some minor text parsing. For example, when I printed the crimes and fires I was scraping for from the website, the text had "\xa0" in it. So that needed to be removed. I then put all the data together into my list and wrote it out as a CSV. 

### April 2, 2023:
    I've added more things and have removed some other stuff too! I've created a dictionary of the key/column names, so that Python understands the value attached to each column name/key. It allows for easy calling of specific values of the data. I've also created a ``scrape.yml`` file to make the bot run on it's own. The whole thing is acting a little weird because it won't let me commit my changes. 

### April 3, 2023:
    Because some of my changes/creations were made locally and on Github, this caused the non-committing. So I had to delete the codespaces and start again with what I committed back on April 2nd. 

### April 5th, 2023:
    We're getting somewhere. I have now added in my slack information. I had to look at other students' repositories (specifically Varun's) to figure out how to write out my if else statement for printing a specific message. The beauty of this class is that we can kinda look over other people's shoulder virtually. Anyway, it's doing the printing I need it to do, however, it looks like I'll need to clean up the text. I did this by lower-casing some words so that it doesn't look weird and I removed some spaces. 

### April 8th 2023:
    Looking a lot better! I redid my csv-creation code because it was printing just the column names... not doing that anymore! I also lower-cased some of the text in specific keys/column names such as incident, disposition and synopsis. I also edited the text in the messages for it to look a little prettier. I'd say that I'm pretty confident in submitting this!

### Issues I'm Still Having:
Everytime I run the code, it creates duplicates to the csv. I asked Chat GPT for some help but I'm still running into some roadblocks. I definitely plan on revisiting this issue. 