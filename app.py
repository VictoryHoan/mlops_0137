from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize the Flask application
app = Flask(_name_)

# Load the trained model
model = joblib.load('final_sale_hdb_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the form
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])
    floor_area = float(request.form['floor_area'])
    remaining_lease = float(request.form['remaining_lease'])

    # Create a numpy array from the inputs
    features = np.array([[latitude, longitude, floor_area, remaining_lease]])

    # Make prediction
    prediction = model.predict(features)

    # Return the result as a JSON
    return jsonify({'predicted_price': prediction[0]})

if _name_ == "_main_":
    app.run(debug=True)