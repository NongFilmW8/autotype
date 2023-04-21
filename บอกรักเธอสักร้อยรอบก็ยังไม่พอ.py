import time
import keyboard

limit = int(input("จำนวนข้อความ: "))
m1 = input("m1: ")

i = 0
while i < limit:
    keyboard.write(m1, delay=0.1)
    keyboard.press_and_release("enter")
    i += 1
