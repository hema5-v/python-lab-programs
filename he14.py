#sending mail using python


import smtplib


s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='sender.com'
receiver='receiver.com'
msg="hii"
s.login(sender,'password')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()