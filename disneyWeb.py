# Anthony Peza
# Python Programming
# Disney Web
#
# The purpose of this program is alert me when disney tickets go on sale
#
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Global Variables #
disneyUrl = "https://disneyland.disney.go.com/events-tours/after-dark/?ef_id=Cj0KCQiAvc_xBRCYARIsAC5QT9mEKZQsw_mSfXcLzKOzoq2-Xp4jr5mRaohcdxEWLer0JEgT512UGWQaAjfqEALw_wcB:G:s&s_kwcid=AL!5054!3!398544259080!e!!g!!disneyland%20after%20dark%20tickets&CMP=KNC-FY20_DLR_ACT_LOC_L365AB_SCP_DLAD_Events_EXACT|G|5202059.DL.AM.01.02|MOK33LW|BR|398544259080&keyword_id=aud-687740961259:kwd-432464433963|dc|disneyland%20after%20dark%20tickets|398544259080|e|5054:3|&gclid=Cj0KCQiAvc_xBRCYARIsAC5QT9mEKZQsw_mSfXcLzKOzoq2-Xp4jr5mRaohcdxEWLer0JEgT512UGWQaAjfqEALw_wcB"


# Main Function #
# This first reference is opening the connection to the disney website and grabbing the page
disneyWebsiteClient = uReq(disneyUrl)
# This second function is reading it
pageHTML = disneyWebsiteClient.read()
# This third function is closing the connection when I'm done
disneyWebsiteClient.close()

# This is now storing the information from pageHTML into a disneyPageSoup and parsing using the html parser
disneyPageSoup = soup(pageHTML, "html.parser")
