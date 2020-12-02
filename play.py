import os
from playsound import playsound as ps

source_path = "wavout/"
filelist = sorted([int(fn.replace(".wav", "")) for fn in os.listdir(source_path)])



def toint(a):
    try:
        a = int(a)
    except:
        a = str(a)
    return a

i = 0
while i < len(filelist):
    nexttask = input("다음 작업을 입력하세요 (s재생,q종료,r반복,숫자):")
    nexttask = toint(nexttask)

    if nexttask == 'q': break
    elif isinstance(nexttask, int): print("number"); i = nexttask-1
    elif nexttask == 'r' and i > 0:
        i -= 1

    filename = filelist[i]
    playfile = source_path+str(filename)+".wav"
    print(playfile)
    ps(playfile)
    i += 1