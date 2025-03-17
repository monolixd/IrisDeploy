## 📌 **สรุปเนื้อหา Day 4: Model Deployment & MLOps** 🚀  

### 🎯 **หัวข้อที่เรียนวันนี้**
✅ **1. Model Deployment คืออะไร?** → การนำโมเดลที่เทรนแล้วไปใช้งานจริง  
✅ **2. Flask & FastAPI** → สร้าง API ให้โมเดลรับ Input และส่ง Output  
✅ **3. Docker & Kubernetes** → ทำให้โมเดลสามารถรันบน Server ได้ง่ายขึ้น  
✅ **4. MLOps เบื้องต้น** → การจัดการ Workflow ของ Machine Learning  

---

### ✅ **1. คำสั่งที่ใช้ติดตั้ง Environment และไลบรารี**
📌 **ก่อนใช้งาน Flask หรือ FastAPI ต้องติดตั้งไลบรารีที่จำเป็น**  
📌 **ใช้คำสั่งเหล่านี้เพื่อติดตั้งทุกอย่างใน Virtual Environment (`env`)**

```bash
# 1️⃣ สร้าง Virtual Environment (สำหรับแยกโปรเจค)
python -m venv env
```
💡 **ทำไมต้องใช้?**  
- ใช้เพื่อแยก Dependencies ของโปรเจคไม่ให้ปะปนกับระบบ  
- ใช้งานในโปรเจค AI และ Web API ได้ง่ายขึ้น  

```bash
# 2️⃣ เปิดใช้งาน Virtual Environment
# Windows
env\Scripts\activate

# macOS/Linux
source env/bin/activate
```
💡 **ทำไมต้องใช้?**  
- เมื่อ `activate` แล้ว คำสั่ง `pip install` จะติดตั้งไลบรารีใน `env` เท่านั้น  

```bash
# 3️⃣ ติดตั้ง Flask และ FastAPI พร้อมไลบรารีที่จำเป็น
pip install flask fastapi uvicorn joblib numpy pandas scikit-learn
```
💡 **ติดตั้งอะไรบ้าง?**  
✅ **Flask** → ใช้สร้าง Web API  
✅ **FastAPI** → ใช้สร้าง Web API ที่เร็วขึ้น  
✅ **Uvicorn** → ใช้รัน FastAPI  
✅ **Joblib** → ใช้บันทึกและโหลดโมเดล  
✅ **NumPy** → ใช้จัดการข้อมูลตัวเลข  
✅ **Pandas** → ใช้จัดการ DataFrame  
✅ **Scikit-learn** → ใช้โหลดและเทรนโมเดล  

```bash
# 4️⃣ ตรวจสอบว่า Flask และ FastAPI ถูกติดตั้งหรือไม่
python -m pip show flask
python -m pip show fastapi
```
💡 **ถ้าขึ้นข้อมูลเวอร์ชันของ Flask หรือ FastAPI แสดงว่าติดตั้งสำเร็จ!** ✅  

---

### ✅ **2. รัน Flask API**
📌 **หลังจากสร้างไฟล์ `app_flask.py` แล้ว ให้รัน Flask**
```bash
python app_flask.py
```
✅ **API จะรันที่:** [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  

---

### ✅ **3. รัน FastAPI**
📌 **หลังจากสร้างไฟล์ `app_fastapi.py` แล้ว ให้รัน FastAPI**
```bash
uvicorn app_fastapi:app --reload
```
✅ **API จะรันที่:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
✅ **ทดสอบ API ผ่าน Swagger UI ที่:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

---

### ✅ **4. ทดสอบ API ด้วย Python (`requests`)**
📌 **สร้างไฟล์ `test_api.py` แล้วรันคำสั่งนี้**  
```python
import requests

# URL ของ FastAPI
url = "http://127.0.0.1:8000/predict"

# JSON ที่ต้องส่งไปให้ API
data = {"features": [5.1, 3.5, 1.4, 0.2]}

# ส่ง HTTP POST Request ไปที่ API
response = requests.post(url, json=data)

# แสดงผลลัพธ์ที่ได้จาก API
print("📩 Response Status Code:", response.status_code)
print("📌 Response JSON:", response.json())
```
📌 **รันคำสั่งนี้ใน Terminal**
```bash
python test_api.py
```
✅ **ถ้า API ทำงานถูกต้อง จะได้ผลลัพธ์ประมาณนี้:**
```json
{"prediction": "Setosa"}
```
✅ **ตอนนี้ API ส่งชื่อดอกไม้แทนตัวเลขเรียบร้อยแล้ว!** 🎉  

---

## 🎯 **สรุป**
| **ขั้นตอน** | **คำอธิบาย** |
|-------------|----------------|
| **สร้าง Virtual Environment** | ✅ `python -m venv env` |
| **เปิดใช้งาน Virtual Environment** | ✅ `env\Scripts\activate` |
| **ติดตั้ง Flask และ FastAPI** | ✅ `pip install flask fastapi uvicorn joblib numpy pandas scikit-learn` |
| **รัน Flask API** | ✅ `python app_flask.py` |
| **รัน FastAPI** | ✅ `uvicorn app_fastapi:app --reload` |
| **ทดสอบ API ผ่าน Python** | ✅ `python test_api.py` |

📌 **ตอนนี้คุณสามารถนำเนื้อหานี้ไปสร้างไฟล์ Markdown (`README.md`) สำหรับ GitHub ได้แล้ว!** 🚀🔥  
🔥 **มีอะไรที่ต้องการให้ฉันช่วยเพิ่มเติมไหม? 😊**