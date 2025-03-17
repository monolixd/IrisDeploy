import requests

# URL ของ FastAPI
url = "http://127.0.0.1:8000/predict"

data = {"features": [5.1, 3.5, 1.4, 0.2]}

# ส่ง HTTP POST Request ไปที่ API
response = requests.post(url, json=data)

# แสดงผลลัพธ์ที่ได้จาก API
print("📩 Response Status Code:", response.status_code)
print("📌 Response JSON:", response.json())
