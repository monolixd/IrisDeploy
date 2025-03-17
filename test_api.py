import requests

# URL ของ Flask API
url = "http://127.0.0.1:5000/predict"

# JSON ที่ต้องการส่งไปให้ API
data = {"features": [5.1, 3.5, 1.4, 0.2]}

# ส่ง HTTP POST Request ไปที่ API
response = requests.post(url, json=data)

# แสดงผลลัพธ์ที่ได้จาก API
print("📩 Response Status Code:", response.status_code)
print("📌 Response JSON:", response.json())
