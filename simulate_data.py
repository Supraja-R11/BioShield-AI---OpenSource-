import time
import random
import requests

API_URL = "http://localhost:8000/analyze"

while True:
    data = {
        "location": "Lab A",
        "bacterial_count": random.randint(2000, 3000),  # high risk
        "temperature": round(random.uniform(30, 40), 2),
        "humidity": random.randint(40, 80),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        response = requests.post(API_URL, json=data)
        print("Sent:", data)
        print("Response:", response.json())
    except Exception as e:
        print("Error:", e)

    time.sleep(5)  # 5 seconds-ku oru thadava data send pannum
