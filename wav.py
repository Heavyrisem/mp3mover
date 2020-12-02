import os
from pydub import AudioSegment

source_path = "mp3/"
target_path = "wavout/"

for filename in os.listdir(source_path):
    if filename.endswith(".mp3"):
        mp3 = AudioSegment.from_mp3(source_path+filename)
        mp3.export(target_path+filename.replace(".mp3","")+".wav", format="wav")
        print("{}이 {}로 처리됨".format(filename, target_path+filename.replace(".mp3","")+".wav"))