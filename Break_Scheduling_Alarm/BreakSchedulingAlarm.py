#healthy programmer
from pygame import mixer
from datetime import datetime
from time import time
def music_play(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a =input("Enter for stop = ")
        if a== stopper: 
            mixer.music.stop()
            break

def log_fun(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()} and\n")


if __name__=='__main__':
     # music_play("genda.mp3","stop")
     init_water = time()
     init_eye = time()
     init_exercize = time()
     water_sec = 225
     exer_sec = 50
     eye_sec = 10

while True:
    if (time() - init_water) > water_sec:
        print("water drinking time. Enter drank after drink")
        music_play("genda.mp3","drank")
        init_water = time()
        log_fun("drank water at ")

    if(time() - init_eye) > eye_sec:
        print("eye exercize time. Enter done after doing this")
        music_play("roudy.mp3","done")
        init_eye =time()
        log_fun("eye exercize at ")

    if(time() - init_exercize) > exer_sec:
        print("Exercize time . Enter done after doing this")
        music_play("mute.mp3","done")
        init_exercize = time()
        log_fun("Exercize at ")





