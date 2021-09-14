import requests
import time
import threading
import datetime

exts=["zip", "rar", "mp4", "mp3", "png", "mkv", "txt", "doc", "pdf", "ppt", "jpeg", "eps", "psd", "cdr", "ai", "jpg"]

url=input("URL: ")

name=url.split("/")[-1]

ext=name.split(".")[-1]

if ext not in exts:
    name=input("\nName and Extension of file: ")

print("\nGetting Data")

started=datetime.datetime.now()

r=requests.get(url, stream=True)

r.encoding = "ISO-8859-1"

print("\nReady!\n")

print("\nExporting data into a file ----->\n")

file=open(name, "wb")
file.write(r.content)

end=datetime.datetime.now()

print("Done!")

hour=end.hour - started.hour
if started.minute > end.minute:
    minute=started.minute - end.minute
else:
    minute=end.minute - started.minute
if started.second > end.second:
    second=started.second - end.second
else:
    second=end.second - started.second

try:
    input(f"\n  Download Total Time: {hour}:{minute}:{second}")
except:
    pass
file.close()