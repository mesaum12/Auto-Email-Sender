import smtplib
import sys

to=input("Enter the email of the recipient:")
content=input("Enter the content of the mail:\n")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.helo()
    server.starttls()
    server.login("mesaum12@gmail.com","s@11mu22#")
    server.sendmail("mesaum12@gmail.com",to,content)
    server.close()

sendEmail("mesaum12@gmail.com",open("saurabh.txt","r").readlines)