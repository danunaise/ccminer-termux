import os 
import json
import requests
import time

def get_data():
    with open('./data/api.json', 'r') as f:
        data = json.load(f)
        url = data.get('url')
        headers = {'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache', 'Expires': '0'}
        try:
            # Fetch data from GitHub
            res = requests.get(url, headers=headers)
            res.raise_for_status()
            return res.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from GitHub: {e}")
            exit(1)
            os.system('cls || clear')
            os.system('startminer')

with open('./data/data.json', 'w') as f:
    json.dump(get_data(), f, indent=3)

with open('./data/data.json', 'r') as f:
    data = json.load(f)
    
with open('./data/worker.json', 'r') as f:
    worker_data = json.load(f)

merge_data = { **data, **worker_data }

worker = merge_data.get('worker')
pool = merge_data.get('pool')
wallet = merge_data.get('wallet')
password = merge_data.get('password')
cpu_threads = merge_data.get('cpu_threads')

os.system('cls || clear')
print("\033[92mกำลังเริ่มขุด...\033[0m")
time.sleep(2)
os.system('cls || clear')
print("\033[34m====+ ข้อมูล Miner +====")
print(f"\033[1;37;32m Worker \033[0m: {worker}")
print(f"\033[1;37;33m Pool \033[0m: {pool}")
print(f"\033[1;37;34m Wallet \033[0m: {wallet}")
print(f"\033[1;37;35m Password \033[0m: {password}")
print(f"\033[1;37;36m CPU Threads \033[0m: {cpu_threads}")
print("หากต้องการแก้ไขข้อมูล กรุณากด Ctrl + C และใช้คำสั่ง editminer")

time.sleep(5)

os.system(f"cd ccminer && ./ccminer -a verus -o stratum+tcp://{pool} -u {wallet}.{worker} -p {password} -t {cpu_threads}")