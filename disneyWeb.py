# Anthony Peza
# Python Programming
# Disney Web
#
# The purpose of this program is alert me when disney tickets go on sale
#
import json
import time
import smtplib
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Global Variables #
disneyUrl = "https://disneyland.disney.go.com/events-tours/disneyland/after-dark-star-wars-nite/"
isRepeating = True
x = 0

# Functions #
def webCheck():
    global firstCheck
    print("Conducting first check\n")
    # This first reference is opening the connection to the disney website and grabbing the page
    disneyWebsiteClient = uReq(disneyUrl)
    # This second function is reading it
    pageHTML = disneyWebsiteClient.read()
    # This third function is closing the connection when I'm done
    disneyWebsiteClient.close()

    # This is now storing the information from pageHTML into a disneyPageSoup and parsing using the html parser
    disneyPageSoup = soup(pageHTML, "html.parser")

    # disneyPageSoup.find is looking for divs in the html and returning the "id"  for everything in that div
    firstCheck = disneyPageSoup.find("h2")

    print("First check complete\nFirst check saved")

    print(firstCheck)

def updateWebCheck():
    global secondCheck
    print("\nConducting second check\n")
    # This first reference is opening the connection to the disney website and grabbing the page
    disneyWebsiteClientSecondAttempt = uReq(disneyUrl)
    # This second function is reading it
    secondPageHTML = disneyWebsiteClientSecondAttempt.read()
    # This third function is closing the connection when I'm done
    disneyWebsiteClientSecondAttempt.close()

    # This is now storing the information from pageHTML into a disneyPageSoup and parsing using the html parser
    disneyPageSoupSecondCheck = soup(secondPageHTML, "html.parser")

    # disneyPageSoup.find is looking for divs in the html and returning the "id"  for everything in that div
    secondCheck = disneyPageSoupSecondCheck.find("h2")

    print("Second check complete\nSecond check saved\n")

def sendEmail():
    global disneyUrl

    with open("pw.json") as email:
        data = json.load(email)
        email = data['Email']
        key = data['key']

    msg = \
        (
            """
            Subject: Disney automated alert\n\n 
            
            Disney after dark, star wars nite tickets are on sale!
            
            Follow this link: https://disneyland.disney.go.com/events-tours/after-dark/?ef_id=Cj0KCQiAvc_xBRCYARIsAC5QT9mEKZQsw_mSfXcLzKOzoq2-Xp4jr5mRaohcdxEWLer0JEgT512UGWQaAjfqEALw_wcB:G:s&s_kwcid=AL!5054!3!398544259080!e!!g!!disneyland%20after%20dark%20tickets&CMP=KNC-FY20_DLR_ACT_LOC_L365AB_SCP_DLAD_Events_EXACT|G|5202059.DL.AM.01.02|MOK33LW|BR|398544259080&keyword_id=aud-687740961259:kwd-432464433963|dc|disneyland%20after%20dark%20tickets|398544259080|e|5054:3|&gclid=Cj0KCQiAvc_xBRCYARIsAC5QT9mEKZQsw_mSfXcLzKOzoq2-Xp4jr5mRaohcdxEWLer0JEgT512UGWQaAjfqEALw_wcB
            
            """
        )
    fromEmail = email
    toEmail = "axpeza@gmail.com"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromEmail, key)

    server.sendmail(fromEmail, toEmail, msg)
    server.quit


    print("email sent")

def checkCounter():
    global x
    x += 1
    countMessage = "\nTimes checked: " + str(x)
    print(countMessage)

# Main Function #
webCheck()
while isRepeating:
    updateWebCheck()
    print("Checking pages...")
    if firstCheck == secondCheck:
        print("Checking again in 15 minutes")
        checkCounter()
        time.sleep(900)
    else:
        sendEmail()
        isRepeating = False
