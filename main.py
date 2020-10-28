import os 
import time
import shutil as sh

save_path = "YEE/" # 어디에 저장될지 입력
check_path = "help/" # 어디에서 불러올지 입력

def getFileNumber():
    namedlist = []
    for filename in os.listdir(save_path):
        if filename.endswith(".mp3"):
            namedlist.append(int(filename.replace(".mp3", "")))
    return max(namedlist)



if __name__ == "__main__":
    file_counter = getFileNumber()

    while True:
        for filename in os.listdir(check_path):
            if filename.endswith(".mp3"):
                time.sleep(0.3) # 읽기가 완료된 후 읽어오기
                file_counter += 1
                sh.move(check_path + filename, save_path + "{}.mp3".format(file_counter))
                print("{} File Moved".format(file_counter))

        time.sleep(0.3) # 체크 딜레이 0.3초 기본값
