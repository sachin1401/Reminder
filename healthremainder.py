
from pygame import init, mixer
from datetime import datetime
from time import time

def message(msg):
    with open("msg.txt",'a') as f:
        f.write(f'{msg} {datetime.now()} \n')
def musicplay(file,stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a ==stop:
            mixer.music.stop()
            break

if __name__=="__main__":
          
    init_water=time()
    init_eyes=time()
    init_exercise=time()

    water=5 #here we set time in seconds likes 5sec
    eyes=10 #10sec
    exercise=20 #20sec

    while True:
        if time()-init_water>water:
            print("water drinking time, print 'stop' to the the alarm" )
            musicplay("water.mp3.wav","stop") #here you can add music whatever you want
            init_water=time()
            message("drinking water at ")

        if time()-init_eyes>eyes:
            print("eyes exercise time, print 'e' to the the alarm" )
            musicplay("water.mp3.wav","e") #here you can add music whatever you want
            init_eyes=time()
            message("eye exercise at ") 

        if time()-init_exercise>exercise:
            print("activity time, print 'a' to the the alarm" )
            musicplay("water.mp3.wav","a") #here you can add music whatever you want
            init_exercise=time()
            message("execise at ")       