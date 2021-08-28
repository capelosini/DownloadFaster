import requests
import time
import threading
import datetime

def Anim(animation, delay):
    global anim
    while anim:
        for frame in animation:
            if anim == True:
                print(frame, end="\r")
                time.sleep(delay)
            else:
                exit()


anim=False

url=input("URL: ")

name=url.split("/")[-1]

print(" ")

anim=True
threading._start_new_thread(Anim, (["Getting data -", "Getting data |", "Getting data /", "Getting data -", "Getting data |", "Getting data /"], 0.3))

started=datetime.datetime.now()

r=requests.get(url)

anim=False

r.encoding = "ISO-8859-1"

print("\nReady!\n")

time.sleep(0.3)

anim=True
threading._start_new_thread(Anim, (["Exporting data into a file -", "Exporting data into a file --", "Exporting data into a file ---", "Exporting data into a file ----->", ], 0.2))

file=open(name, "wb")
file.write(r.content)

end=datetime.datetime.now()

anim=False

print("Exporting data into a file ---->\nDone!")

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