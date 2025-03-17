from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("iris_model.pkl")

#ทดสอบ Api
@app.route('/')
def home():
    return "Flask Api Ready to use"

#Routeทำนาย
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    feature = np.array(data['feature']).reshape(1, -1) #แปลงข้อมูลให้อยู่ในรูปแบบ Array
    prediction = model.predict(feature)
    return jsonify({"prediction":int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)