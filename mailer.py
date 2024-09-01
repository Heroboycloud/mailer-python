import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

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
    def send(self,receiver,subject,body,html=False, attachments=None):
      if self.status:
         msg= MIMEMultipart()
         msg["Subject"]= subject
         msg["From"]= self.username
         msg["To"]= receiver
         if html:
            msg.attach(MIMEText(body, 'html'))
         else:
                msg.attach(MIMEText(body, 'plain'))
         if attachments:
            for attachment in attachments:
                with open(attachment, 'rb') as f:
                     part = MIMEApplication(f.read())
                     part.add_header('Content-Disposition', f'attachment; filename= {attachment}')
                     msg.attach(part)

         self.server.sendmail(self.username,receiver,msg.as_string())
         print("Email sent Successfully")
      else:
         print("Not connected to server")

    def __del__(self):
      if self.status:
         self.server.quit()

