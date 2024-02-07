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

print("Starting ccminer-verus...")
print("Data ")
print(f"Worker: {worker}")
print(f"Pool: {pool}")
print(f"Wallet: {wallet}")
print(f"Password: {password}")
print(f"CPU Threads: {cpu_threads}")

time.sleep(5)

os.system(f"cd ccminer-verus && ./ccminer -a verus -o stratum+tcp://{pool} -u {wallet}.{worker} -p {password} -t {cpu_threads}")