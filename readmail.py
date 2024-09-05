import imaplib as imap
import utils
import email,os





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



  def create_label(self,query,label):
    if self.status and query and label:
       self.mail_server.select("inbox")
       status,msgs= self.mail_server.search(None,query)
       email_ids= msgs[0].split()
       for email_id in email_ids:
           self.mail_server.store(email_id,'+X-GM-LABELS',label)
       self.mail_server.expunge()
    else:
       print("Seriously!! You must provide a query!\nDeleting Files is irreversible")


  def create_folder(self,mail_folder,query):
    if self.status and mail_folder and query:
       self.mail_server.create(mail_folder)
       self.mail_server.select("inbox")
       status,msgs= self.mail_server.search(None,query)
       email_ids= msgs[0].split()
       for email_id in email_ids:
           self.mail_server.copy(email_id,mail_folder)
       for email_id in email_ids:
           self.mail_server.store(email_id,'+FLAGS',"\\Deleted")
       self.mail_server.expunge()
    else:
       print("Seriously!! You must provide a query and folder..!\nMoving Files is irreversible")



  def delete_spam(self,query="ALL"):
    if self.status and query:
       self.mail_server.select("[Gmail]/Spam")
       status,msgs= self.mail_server.search(None,query)
       email_ids= msgs[0].split()
       for email_id in email_ids:
           self.mail_server.store(email_id,'+FLAGS',"\\Deleted")
       self.mail_server.expunge()
    else:
       print("Seriously!! You must provide a query!\nDeleting Files is irreversible")


  def delete(self,query):
    if self.status and query:
       self.mail_server.select("inbox")
       status,msgs= self.mail_server.search(None,query)
       email_ids= msgs[0].split()
       for email_id in email_ids:
           self.mail_server.store(email_id,'+FLAGS',"\\Deleted")
       self.mail_server.expunge()
    else:
       print("Seriously!! You must provide a query!\nDeleting Files is irreversible")



  def download(self,query="ALL",dir_name="mails",inbox="inbox",num_mails=5):
    if self.status:
       self.mail_server.select(inbox)
       status,messages= self.mail_server.search(None,query)
       self.mail_ids= messages[0].split()[-num_mails:]
       utils.check_dir(dir_name)
       for mail_id in self.mail_ids:
           status, data = self.mail_server.fetch(mail_id, '(RFC822)')
           email_data = data[0][1]
           from email.parser import BytesParser
           from email.policy import default
           msg = BytesParser(policy=default).parsebytes(email_data)
           subject=utils.clean(msg['subject'])
           file= open(f'{dir_name}/{subject}.html','w')
           file.write(msg.get_body().get_content())
           print(f"saved {subject} in {dir_name}")
           file.close()

    else:
       print("Not connected to server")


  def __del__(self):
    if self.status:
       self.mail_server.close()
       self.mail_server.logout()


