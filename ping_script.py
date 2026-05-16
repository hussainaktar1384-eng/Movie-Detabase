import requests
import time

print("Auto-Pinger Start ho gaya hai...")

try:
    with open("links.txt", "r") as file:
        links = file.readlines()
except FileNotFoundError:
    print("links.txt file nahi mili.")
    exit()

for link in links:
    link = link.strip()
    if not link or link.startswith("#"):
        continue 
    
    print(f"Ping kar rahe hain: {link}")
    try:
        response = requests.get(link, stream=True, timeout=20)
        downloaded_mb = 0
        
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                downloaded_mb += 1
            if downloaded_mb >= 5:
                print(f"✅ 5MB pura hua. Next link par ja rahe hain...")
                break
                
        response.close()
        time.sleep(5) 
        
    except Exception as e:
        print(f"❌ Error: {e}")

print("Saare links safe ho gaye!")
