import imaplib as imap
import email

class Readmail:
  def __init__(self,username,password):
      self.username=username
      self.password= password
      self.status= False
      try:
        self.connect()
      except:
         print("Could not connect to Mail server")

  def connect(self):
    self.mail_server= imap.IMAP4_SSL("imap.gmail.com")
    self.mail_server.login(self.username,self.password)
    self.status= True
  def download(self,query,num_mails):
    if self.status:
       self.mail_server.select("inbox")
       status,messages= self.mail_server.search(None,query)
       messages= messages[0].split()
       self.mails=[]
       for msg_id in messages:
         status,msg= self.mail_server.fetch(msg_id,"(RFC822)")
         raw_msg= msg[0][1]
         mail= email.message_from_bytes(raw_msg)
         self.mails.append(mail)
         return self.mails
    else:
       print("Not connected to server")


  def __del__(self):
    if self.status:
       self.mail_server.close()
       self.mail_server.logout()


