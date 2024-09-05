import os


def check_dir(dir):
  if os.path.isdir(dir):
     pass
  else:
    os.mkdir(dir)



def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)



