from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask('__name__')

model = pickle.load(open('Fuel_efficiency_prediction', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        cylinders = int(request.form['cylinders'])
        displacement = float(request.form['displacement'])
        hp = int(request.form['hp'])
        weight = float(request.form['weight'])
        acceleration = float(request.form['acc'])
        year = int(request.form['year'])

        prediction = model.predict([[cylinders, displacement, hp, weight, acceleration, year]])

        output = prediction[0]

        if output < 0:
            return render_template('index.html', prediction_text = "Something is wrong")
        else:
            return render_template('index.html', prediction_text=f"Predicted miles per gallon is {output}")
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)