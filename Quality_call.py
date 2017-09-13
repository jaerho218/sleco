##--- Eric Hoekstra
##--- Date: 13th Sept 2017
##--- Version: 1.25


import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(19, GPIO.IN,pull_up_down=GPIO.PUD_UP)

from email_handler import Class_eMail

#set the email ID the address to send the email 
To_Email_ID = "slecoplasticsnotify@gmail.com"


while True:
    inputValue = GPIO.input(19)
    time.sleep(.1)
    if (inputValue == False):
#        print("Button press ")
        GPIO.output(16,GPIO.HIGH)
        email = Class_eMail()
        email.send_Text_Mail(To_Email_ID, 'Machine 53', 'Quality Auditor to Machine 53')
        del email
        time.sleep(10)
    GPIO.output(16,GPIO.LOW)
