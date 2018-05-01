#TO DO
#2. If no saved html exists, save html
#3. Compare current html to saved html
#4. If there are changes, store changes
#5. Parse and format changes for various notification options
#6. Send notifications


### DEPENDENCIES ###

# Functional requirements
import sys #required for exit()
import os #required for dir/file functions
from pathlib import Path #required for open

# Web requirements
import html
import requests

# File manipulation requirements
import re #regex
import difflib
from bs4 import BeautifulSoup

# Messaging requirements
import smtplib

### This script will check for updates to a site's html and parse/send them in a notification ###

# Pull the website html and set up our soup
url = "https://mohawkaustin.com/events"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
siteHtml = response.text

soup = BeautifulSoup(siteHtml, "html.parser")

# If there's no comparison html, generate it now and stop the script from proceeding any further
# If the previous HTML is there, open it and create current HTML file object
pathToPreviousHtml = os.getcwd() + "/data/html/previous/mohawk.html"
if not os.path.exists(pathToPreviousHtml) or (os.stat(pathToPreviousHtml).st_size == 0):
    f = open(pathToPreviousHtml, "w+")
    f.write(siteHtml)
    f.close()
    exit()
else:
    previousHtml = open(pathToPreviousHtml, "U")
    pathToCurrentHtml = os.getcwd() + "/data/html/current/mohawk.html"
    currentHtmlFile = open(pathToCurrentHtml, "w+")
    currentHtmlFile.write(siteHtml)
    currentHtmlFile.close()
    currentHtml = open(pathToCurrentHtml, "U")

# Compare current html to saved html
fromLines = currentHtml.readlines()
toLines = previousHtml.readlines()

diff = difflib.HtmlDiff().make_file(fromLines,toLines,previousHtml,currentHtml)
sys.stdout.writelines(diff)
diffFileDir = os.getcwd() + "/diffFile.html"
diffFile = open(diffFileDir, "w+")
diffFile.write(diff)
diffFile.close()

#4. If there are changes, store changes

#5. Parse and format changes for various notification options

#6. Send notifications