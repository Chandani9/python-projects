import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from']='Chandani Bhogayta'
eamil['to']='chandanibhogayta@gmail.com'
email['subject']='hey!!'

email.set_content('how are you')

with smtplib.SMTP(host='smpt.gmail.com',port=587)as smtp:
	smtp.ehlo()
	smtp.starttls()#connect secury eith server
	smtp.login('user id -email id','password')
	smtp.send_message(email)
	print("all good")
#port : smtp is protocol to communicate two computer or device there for we used port 587 or 465.
