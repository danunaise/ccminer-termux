import os
import json
from colored import Fore, Back, Style
#config worker

def main():
    while True:
        print(f"{Fore.blue}*******************************************{Style.reset}")
        print("กรุณาเลือกเมนูที่ต้องการ")
        print("1. ตั้งค่า API")
        print("2. ตั้งค่า Worker")
        print("3. ออกและเริ่มขุด")
        print("4. ออกจากการตั้งค่า")
        print(f"{Fore.blue}*******************************************{Style.reset}")
        
        try:
            menu = int(input("เลือกเมนู: "))
            
            if menu == 1:
                setupApi()
            elif menu == 2:
                editWorker()
            elif menu == 3:
                os.system('cls || clear')
                print(f"{Fore.light_green}กำลังเริ่มขุด...{Style.reset}")
                os.system('python3 main.py')
                break
            elif menu == 4:
                os.system('cls || clear')
                print(f"{Fore.red}ออกจากโปรแกรม{Style.reset}")
                break
            else:
                os.system('cls || clear')
                print(f"{Fore.white}{Back.red} ERROR {Style.reset} {Fore.red}กรุณาเลือกเมนูใหม่{Style.reset}")
        except ValueError:
            os.system('cls || clear')
            print(f"{Fore.white}{Back.red} ERROR {Style.reset} {Fore.red}กรุณาป้อนตัวเลขเท่านั้น{Style.reset}")
            
def setupApi():
    os.system('cls || clear')
    with open('./data/api.json', 'r') as f:
        url_data = json.load(f)
        url = url_data.get('url')
    print(f"{Fore.blue}*******************************************{Style.reset}")

    if url is None:
        print("API ของคุณตอนนี้คือ: ยังไม่มี API กรุณาตั้งค่า API ก่อน")
    else:
        print(f"API ของคุณตอนนี้คือ: {url}")
    print("กรุณากรอก API ที่มีข้อมูล pool, wallet, password ")
    print("เช่น https://raw.githubusercontent.com/danunaise/ccminer-verus-autostart/main/data/data.json")
    
    print(f"{Fore.blue}*******************************************{Style.reset}")
    url = input("กรุณากรอก API ของคุณ: ")
    data = {
        "url": url
    }
    with open('./data/api.json', 'w') as f:
        json.dump(data, f, indent=1)
        os.system('cls || clear')
        print(f"{Fore.white}{Back.green} SUCCESS {Style.reset}{Fore.green} บันทึกข้อมูล API เรียบร้อยแล้ว{Style.reset}")

def editWorker():
    os.system('cls || clear')
    with open('./data/worker.json', 'r') as f:
        worker_data = json.load(f)
        worker = worker_data.get('worker')
    print(f"{Fore.blue}*******************************************{Style.reset}")
    print("worker ของคุณตอนนี้คือ " + worker)
    print("กรุณากรอกข้อมูล worker ของคุณ เช่น miner1")
    print(f"{Fore.blue}*******************************************{Style.reset}")
    worker = input("ชื่อ worker ของคุณ: ")

    #config cpu_threads
    print(f"{Fore.blue}*******************************************{Style.reset}")
    print("จำนวน cpu_threads ที่ต้องการใช้ขุด ใส่ค่า 0 - 8")
    print(f"{Fore.blue}*******************************************{Style.reset}")
    cpu_threads = input("cpu_threads ของคุณ: ")

    #save data
    data = {
        "worker": worker,
        "cpu_threads": cpu_threads
    }

    with open('./data/worker.json', 'w') as f:
        json.dump(data, f, indent=2)
        os.system('cls || clear')
        print(f"{Fore.white}{Back.green} SUCCESS {Style.reset}{Fore.green} บันทึกข้อมูล Worker เรียบร้อยแล้ว{Style.reset}")

if __name__ == "__main__":
    main()