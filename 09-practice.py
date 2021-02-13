import smtplib

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("nurkadyrurmatbekovich@gmailcom", "putinbyte98")
server.sendmail ("nurkadyrurmatbekovich@gmailcom","toktoraly707@gmail.com","hello" )