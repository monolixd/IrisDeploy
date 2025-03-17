from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# โหลดโมเดล
model = joblib.load("iris_model.pkl")

# สร้าง Dictionary แปลงค่าคลาสเป็นชื่อดอกไม้
flower_classes = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

@app.route("/")
def home():
    return "🚀 Flask API พร้อมใช้งาน!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        print(f"📩 ข้อมูลที่ได้รับ: {data}")  # Log JSON ที่ได้รับ

        # เช็คว่า JSON มี key 'features' หรือไม่
        if not data or "features" not in data:
            return jsonify({"error": "Invalid JSON format"}), 400

        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)
        
        # แปลงค่าตัวเลขเป็นชื่อดอกไม้
        flower_name = flower_classes[int(prediction[0])]

        return jsonify({"prediction": flower_name})

    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")  # Log Error
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
