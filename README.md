# Mailer python module

```python
  from mailer import Mailer
from dotenv import load_dotenv
import os

load_dotenv()

u= os.getenv("username")
p= os.getenv("password")
receiver= "receiver email"
subject= "Backup update"
body= "Hey, how is the backup stuff?"


m= Mailer(u,p)
print(m.status)
m.send(receiver,subject,body)
```


