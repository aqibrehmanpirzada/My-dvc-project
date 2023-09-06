from flask import Flask, request, render_template
import pandas as pd
import joblib  # Use joblib to load the trained model
import numpy as np

app = Flask(__name__)

# Load your trained model from the saved file
model = joblib.load('/media/aqib/Software/MLOPS Project/Project 1/My-dvc-project/artifacts/Models/trained_model.pkl')

# Define the features (columns) used during training
features = ['Urban_population', 'Population: Labor force participation (%)',
            'Population', 'GDP_zscore', 'Tax revenue (%)',
            'Out of pocket health expenditure', 'Physicians per thousand',
            'Maternal mortality ratio', 'Unemployment rate']

# Create a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        try:
            # Get user input from the form
            user_input = [float(request.form[col]) for col in features]

            # Make a prediction using the loaded model
            prediction = model.predict([user_input])[0]

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction, cols=features)

if __name__ == '__main__':
    app.run(debug=True)
