import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr="aamir.abdine@gmail.com"
toaddr="mannkshv@gmail.com"
msg=MIMEMultipart()
msg['from']=fromaddr
msg['to']=toaddr
msg['subject']="hello it's test for python"
body="how are you bro"
msg.attach(MIMEText(body,'plain'))
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,"abdineasif")
text=msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()
