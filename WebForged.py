# this python file is used to scrape the flask localhost app for the sign in page and downloading the html
# it is used as an entry point for the csrf attack method-- it allows to imitate the real website appearance in a real scenario attack vector
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

LOCALHOST_WEBPAGE= 'http://127.0.0.1:5000/login?next=%2Fhome'
CSS_STYLESHEET='http://127.0.0.1:5000/static/main.css'
webpage= requests.get(LOCALHOST_WEBPAGE)
webpage_style= requests.get(CSS_STYLESHEET)
htmlsession= HTMLSession()
html_session= htmlsession.get(LOCALHOST_WEBPAGE)
# web_pretty= webpage.json()
soup= BeautifulSoup(webpage.content, 'html.parser')
regex = r"(\s*<\/head\s*>\s*$)\Z"
print(webpage.content)
head= soup.head
headHRefs= head.contents
# print(htmlsession.get_text)
print("email ",soup.find('email'))
print("password ",soup.find('password'))
with open('userdata.txt', 'a') as userdb:
    email_text= soup.find('input',id='email')
    password_text= soup.find('input', 'password')
    userdb.write(str(email_text['value']+"/n"))
    userdb.write(str(password_text))

#   

    if not email_text:
        print("email "+ " null")
        print(password_text)
    elif not password_text:
        print("password "+ " null")
        print(email_text.get_text())
    else:
        print(email_text.get_text())
        print(password_text.get_text())
    # print(email_text.get_text()+" ")

with open ('signForged.html', 'wb') as signForum:
    signForum.write(webpage.content)
    

with open('signforgedStyle.css', 'wb') as fileStyle:
    fileStyle.write(webpage_style.content)



