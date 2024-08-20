import smtplib
from email.mime.text import MIMEText


class Mailer:
    def __init__(self,username,password):
      self.username= username
      self.password= password
      self.status = False
      self.connect()
    def connect(self):
      try:
        self.server= smtplib.SMTP('smtp.gmail.com',587)
        self.server.starttls()
        self.server.login(self.username,self.password)
        self.status= True
      except Exception as e:
          print(f"Failed to connect: {e}")
    def send(self,receiver,subject,body):
      if self.status:
         msg= MIMEText(body)
         msg["Subject"]= subject
         msg["From"]= self.username
         msg["To"]= receiver
         self.server.sendmail(self.username,receiver,msg.as_string())
         print("Email sent Successfully")
      else:
         print("Not connected to server")

    def __del__(self):
      if self.status:
         self.server.quit()

