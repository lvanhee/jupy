import time
#import RPi.GPIO as GPIO
from pygame import mixer
import keyboard

# Pins definitions
#btn_pin = 4

# Set up pins
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(btn_pin, GPIO.IN)

# Initialize pygame mixer
mixer.init()

# Remember the current and previous button states
current_state = True
prev_state = True

# Load the sounds

is_stoning = False
last_stone = time.time()
sound = mixer.Sound('bell.wav')

time_sounds = []
time_sounds.append(mixer.Sound("buzzer.wav"))
for i in range(1,11):
    print("loading:" + str(i)+".wav")
    time_sounds.append(mixer.Sound(str(i) + '.wav'))

setup_sound = mixer.Sound('setting_up.wav')
over_sound = mixer.Sound("buzzer.wav")
remaining_stones = 100

####################starting up#############
setup_sound.play()

while mixer.get_busy():
    time.sleep(0.1)

try:
    while(remaining_stones > 0):
        current = time.time()
        time.sleep(0.1)
        if (current > last_stone+1.500):
            remaining_stones = remaining_stones - 1
            print(remaining_stones)
            mixer.stop()
            last_stone = current
            if(remaining_stones > 10):
                sound.play()
            else:
                time_sounds[remaining_stones].play()
    if (remaining_stones <= 0):
        over_sound.play()

    while mixer.get_busy():
        time.sleep(0.1)

# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()

