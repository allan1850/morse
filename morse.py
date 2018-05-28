import RPi.GPIO as GPIO
import time

constant = .500
pinNum = 16

GPIO.setmode(GPIO.BCM) 
GPIO.setup(pinNum,GPIO.OUT) 
GPIO.setwarnings(False)



str = input("Input string:")
str1 = ""
output = ""


for i in str:
    if i.isalpha():
       str1 = str1 + i 
    if i.isspace():
        str1 = str1 + i
    if i.isdigit():
        str1 = str1 + i
        
str1 = str1.lower()
print(str1)

for i in str1:
    if i == 'a':
        output = output + ".- "
    if i == 'b':
        output = output + "-... "
    if i == 'c':
        output = output + "-.-. "
    if i == 'd':
        output = output + "-.. "
    if i == 'e':
        output = output + ". "
    if i == 'f':
        output = output + "..-. "
    if i == 'g':
        output = output + "--. "
    if i == 'h':
        output = output + ".... "
    if i == 'i':
        output = output + ".. "
    if i == 'j':
        output = output + ".--- "
    if i == 'k':
        output = output + "-.- "
    if i == 'l':
        output = output + ".-.. "
    if i == 'm':
        output = output + "-- "
    if i == 'n':
        output = output + "-. "
    if i == 'o':
        output = output + "--- "
    if i == 'p':
        output = output + ".--. "
    if i == 'q':
        output = output + "--.- "
    if i == 'r':
        output = output + ".-. "
    if i == 's':
        output = output + "... "
    if i == 't':
        output = output + "- "
    if i == 'u':
        output = output + "..- "
    if i == 'v':
        output = output + "...- "
    if i == 'w':
        output = output + ".-- "
    if i == 'x':
        output = output + "-..- "
    if i == 'y':
        output = output + "-.-- "
    if i == 'z':
        output = output + "--.. "
    if i == '0':
        output = output + "----- "
    if i == '1':
        output = output + ".---- "
    if i == '2':
        output = output + "..--- "
    if i == '3':
        output = output + "...-- "
    if i == '4':
        output = output + "....- "
    if i == '5':
        output = output + "..... "
    if i == '6':
        output = output + "-.... "
    if i == '7':
        output = output + "--... "
    if i == '8':
        output = output + "---.. "
    if i == '9':
        output = output + "----. "
    if i == ' ':
        output = output + "|"
   
print(output)

for i in output:
    if i == '.':
        GPIO.output(pinNum,GPIO.HIGH)
        time.sleep(constant)
        GPIO.output(pinNum,GPIO.LOW)
    if i == '-':
        GPIO.output(pinNum,GPIO.HIGH)
        time.sleep(3 * constant)
        GPIO.output(pinNum,GPIO.LOW)
    if i == ' ':
        time.sleep(2 * constant)
    if i == '|':
        time.sleep(6 * constant)
    time.sleep(constant)

