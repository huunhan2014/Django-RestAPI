import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import datetime, os

gmail = smtplib.SMTP('smtp.gmail.com:587')
username = 'nghnhanbrvt@gmail.com'
password = 'pxriedhtjmtrsnrr'
userfrom = 'nghnhanbrvt@gmail.com'
userto = 'ng.h.nhan2014@gmail.com'
usercc = ''
userbcc = ''
subject = 'Noi dung cua mail'
content = '''Xin chao,
        Day la` content cua mail'''
attfile = r"""/media/nhuunhan/Data1/Project Django/Rest/djangorest/rest/test.txt"""

def sendMailNow():
    msg = MIMEMultipart()
    msg['From'] = userfrom
    msg['To'] = userto
    msg['Cc'] = usercc
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'plain'))
    attopen = open(attfile, "rb")
    attpart = MIMEBase('application', 'octet-stream')
    attpart.set_payload((attopen).read())
    encoders.encode_base64(attpart)
    attpart.add_header('Content-Disposition', "attachment; filename= {0}".format(attfile.split("\\")[-1]))
    msg.attach(attpart)
    toaddr = [userto] + usercc.split(',') + userbcc.split(',')

    try:
        gmail.ehlo()
        gmail.starttls()
        gmail.login(username, password)
        gmail.sendmail(userfrom, toaddr, msg.as_string())
        gmail.close()
    except Exception as e:
        raise e

if __name__ == "__main__":
    sendMailNow()