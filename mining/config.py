import os
import json
#config worker

def main():
    while True:
        print("\033[34m*******************************************\033[0m")
        print("กรุณาเลือกเมนูที่ต้องการ")
        print("1. ตั้งค่า API")
        print("2. ตั้งค่า Worker")
        print("3. ออกและเริ่มขุด")
        print("4. ออกจากการตั้งค่า")
        print("\033[34m*******************************************\033[0m")
        
        try:
            menu = int(input("เลือกเมนู: "))
            
            if menu == 1:
                setupApi()
            elif menu == 2:
                editWorker()
            elif menu == 3:
                os.system('cls || clear')
                print("\033[92mกำลังเริ่มขุด...\033[0m")
                os.system('startminer')
                break
            elif menu == 4:
                os.system('cls || clear')
                print("\033[31mออกจากโปรแกรม\033[0m")
                break
            else:
                os.system('cls || clear')
                print("\033[1;37;41m ERROR \033[0m \033[31mกรุณาเลือกเมนูใหม่\033[0m")
        except ValueError:
            os.system('cls || clear')
            print("\033[1;37;41m ERROR \033[0m \033[31mกรุณาป้อนตัวเลขเท่านั้น\033[0m")
            
def setupApi():
    os.system('cls || clear')
    with open('./data/api.json', 'r') as f:
        url_data = json.load(f)
        url = url_data.get('url')
    print("\033[34m*******************************************\033[0m")

    if url is None:
        print("API ของคุณตอนนี้คือ: ยังไม่มี API กรุณาตั้งค่า API ก่อน")
    else:
        print(f"API ของคุณตอนนี้คือ: {url}")
    print("กรุณากรอก API ที่มีข้อมูล pool, wallet, password ")
    print("เช่น https://raw.githubusercontent.com/danunaise/ccminer-verus-autostart/main/data/data.json")
    
    print(f"\033[34m*******************************************\033[0m")
    url = input("กรุณากรอก API ของคุณ: ")
    data = {
        "url": url
    }
    with open('./data/api.json', 'w') as f:
        json.dump(data, f, indent=1)
        os.system('cls || clear')
        print(f"\033[1;37;42m SUCCESS \033[0m\033[32m บันทึกข้อมูล API เรียบร้อยแล้ว\033[0m")

def editWorker():
    os.system('cls || clear')
    with open('./data/worker.json', 'r') as f:
        worker_data = json.load(f)
        worker = worker_data.get('worker')
    print(f"\033[34m*******************************************\033[0m")
    print("worker ของคุณตอนนี้คือ " + worker)
    print("กรุณากรอกข้อมูล worker ของคุณ เช่น miner1")
    print(f"\033[34m*******************************************\033[0m")
    worker = input("ชื่อ worker ของคุณ: ")

    #config cpu_threads
    print(f"\033[34m*******************************************\033[0m")
    print("จำนวน cpu_threads ที่ต้องการใช้ขุด ใส่ค่า 0 - 8")
    print(f"\033[34m*******************************************\033[0m")
    cpu_threads = input("cpu_threads ของคุณ: ")

    #save data
    data = {
        "worker": worker,
        "cpu_threads": cpu_threads
    }

    with open('./data/worker.json', 'w') as f:
        json.dump(data, f, indent=2)
        os.system('cls || clear')
        print(f"\033[1;37;42m SUCCESS \033[0m\033[32m บันทึกข้อมูล Worker เรียบร้อยแล้ว\033[0m")

if __name__ == "__main__":
    main()