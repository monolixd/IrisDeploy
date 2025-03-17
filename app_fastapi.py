from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# สร้าง FastAPI App
app = FastAPI()

# โหลดโมเดล Machine Learning
model = joblib.load("iris_model.pkl")

# สร้าง Dictionary แมปค่าตัวเลขเป็นชื่อดอกไม้
flower_classes = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

# 📌 สร้าง Pydantic Model เพื่อกำหนด JSON Schema
class FlowerInput(BaseModel):
    features: list  # รับค่าเป็น List เท่านั้น

@app.get("/")
async def home():
    return {"message": "🚀 FastAPI พร้อมใช้งาน!"}

@app.post("/predict")
async def predict(input_data: FlowerInput):  # 📌 ใช้ Pydantic Model เป็นพารามิเตอร์
    try:
        # แปลงข้อมูลจาก JSON เป็น NumPy Array
        features_array = np.array(input_data.features).reshape(1, -1)

        # ทำนายผลลัพธ์
        prediction = model.predict(features_array)

        # แปลงค่าตัวเลขเป็นชื่อดอกไม้
        flower_name = flower_classes[int(prediction[0])]

        return {"prediction": flower_name}

    except Exception as e:
        return {"error": str(e)}

# รันเซิร์ฟเวอร์ FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
