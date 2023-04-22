import time
import keyboard
import os
from colorama import Fore

print(f'''
   {Fore.LIGHTMAGENTA_EX}__    _______     _______  __   __      .___  ___.    ____    __    ____  ___   
  {Fore.LIGHTMAGENTA_EX}|  |  /  _____| _ |   ____|/_ | |  |     |   \/   |    \   \  /  \  /   / / _ \  
  {Fore.LIGHTMAGENTA_EX}|  | |  |  __  (_)|  |__    | | |  |     |  \  /  |     \   \/    \/   / | (_) | 
  {Fore.LIGHTMAGENTA_EX}|  | |  | |_ |    |   __|   | | |  |     |  |\/|  |      \            /   > _ <  
  {Fore.LIGHTMAGENTA_EX}|  | |  |__| |  _ |  |      | | |  `----.|  |  |  |       \    /\    /   | (_) | 
  {Fore.LIGHTMAGENTA_EX}|__|  \______| (_)|__|      |_| |_______||__|  |__|  ______\__/  \__/     \___/  
   {Fore.LIGHTMAGENTA_EX}                                                   |______|                     
  ''' + Fore.RESET)

def main():
    while True:
        try:
            limit = int(input("จำนวนข้อความ: "))
            m1 = input("คำที่ต้องการจะพิมพ์: ")
            break
        except KeyboardInterrupt:
            print("\nโปรแกรมถูกยกเลิก")

    while True:
        try:
            print("จะเริ่มพิมพ์ข้อความใน 3 วินาที")
            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)

            i = 0
            while i < limit:
                keyboard.write(m1, delay=0.1)
                keyboard.press_and_release("enter")
                i += 1

            print("ส่งข้อความเสร็จสิ้น")
            print("")
            
            # รอรับ input ใหม่
            while True:
                try:
                    new_input = input("ต้องการพิมพ์ข้อความอีกหรือไม่? (y/n): ")
                    if new_input.lower() == "y":
                        break
                    elif new_input.lower() == "n":
                        os.system("cls" if os.name == "nt" else "clear") # เคลียร์หน้าจอ
                        main()  # เริ่มโปรแกรมใหม่
                    else:
                        raise ValueError
                except ValueError:
                    print("กรุณาป้อน 'y' หรือ 'n' เท่านั้น")
        except KeyboardInterrupt:
            print("\nโปรแกรมถูกยกเลิก")

if __name__ == "__main__":
    main()
