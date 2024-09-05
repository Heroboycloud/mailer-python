from readmail import Readmail

from dotenv import load_dotenv
import os

load_dotenv()

u= os.getenv("username")
p= os.getenv("password")
mt= Readmail(u,p)

mt.download(dir_name="important",inbox="[Gmail]/Important")
mt.download(dir_name="starred",inbox="[Gmail]/Starred")
