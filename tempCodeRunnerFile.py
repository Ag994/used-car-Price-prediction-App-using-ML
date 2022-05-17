import joblib
from flask import Flask, render_template, request
import preprocess
import numpy as np 


app = Flask(__name__)

model = joblib.load('models/model.h5')
scaler = joblib.load('models/scaler.h5')


@app.route('/')
def index() :
    return render_template('index.html')


@app.route('/predict', methods = ['POST', 'GET'])
def get_prediction() :

    if request.method == 'POST' :
        year = request.form['Year']
        gear_box = request.form['Gear Box']
        horse_power = request.form['Horse Power']
        kilometer = request.form['kilometer']
        car_type = request.form['cartype']
        car_model = request.form['model']
        fuel_type = request.form['fuel_Type']

    data = {'year' : year, 'gearbox' : gear_box, 'powerh' : horse_power, 
            'kilometer' : kilometer, 'cartype' : car_type, 'model' : car_model, 'fueltype' : fuel_type}

    final_data = preprocess.get_preprocess(data)

    prediction = int(model.predict(scaler.transform([final_data]))[0])

    return render_template('index.html', prediction_text=' The Price Is :{} $'.format(prediction))




if __name__ == "__main__":
    app.run(debug=True)





