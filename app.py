import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
# load the model
reg_model = pickle.load(open('regmodel.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])

def predict_api():
    data_point = request.json['data_point']
    print(data_point)
    print(np.array(list(data_point.values())).reshape(1,-1))
    scaled_data_point = scaler.transform(np.array(list(data_point.values())).reshape(1,-1)) 
    output = reg_model.predict(scaled_data_point)
    print(output[0])
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug = True)