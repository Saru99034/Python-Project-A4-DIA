from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd
import joblib  
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

# Create a custom transformer to select numerical columns
from sklearn.base import BaseEstimator, TransformerMixin
class NumericalSelector(BaseEstimator, TransformerMixin):
    def __init__(self, pca):
        self.pca = pca

    def transform(self, X):
        X = X.select_dtypes(include=['int64', 'float64']).copy()
        reduced_variables = self.pca.transform(X[['Administrative_Duration', 'Administrative', 'ProductRelated_Duration', 'ProductRelated', 'Informational_Duration', 'Informational']])
        X = X.drop(['Administrative_Duration', 'Administrative', 'ProductRelated_Duration', 'ProductRelated', 'Informational_Duration', 'Informational', 'BounceRates'], axis=1)
        # We add the reduced variable
        X['pca1'] = reduced_variables[:, 0]
        X['pca2'] = reduced_variables[:, 1]
        return X
with open('model.pkl', 'rb') as file: 
    loaded_pipeline  = joblib.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        administrative = request.form.get('administrative', type=float)
        administrative_duration = request.form.get('administrative_duration', type=float)
        informational = request.form.get('informational', type=float)
        informational_duration = request.form.get('informational_duration', type=float)
        product_related = request.form.get('product_related', type=float)
        product_related_duration = request.form.get('product_related_duration', type=float)
        bounce_rates = request.form.get('bounce_rates', type=float)
        exit_rates = request.form.get('exit_rates', type=float)
        page_values = request.form.get('page_values', type=float)
        special_day = request.form.get('special_day', type=float)
        month = request.form.get('month')
        operating_systems = request.form.get('operating_systems', type=int)
        browser = request.form.get('browser', type=int)
        region = request.form.get('region', type=int)
        traffic_type = request.form.get('traffic_type', type=int)
        visitor_type = request.form.get('vistor_type')
        weekend = request.form.get('weekend', type=bool)
        features = pd.DataFrame([[
            administrative, administrative_duration, informational,
            informational_duration, product_related, product_related_duration,
            bounce_rates, exit_rates, page_values, special_day,
            month, operating_systems, browser, region, traffic_type,
            visitor_type, weekend
        ]], columns=[
            'Administrative', 'Administrative_Duration', 'Informational',
            'Informational_Duration', 'ProductRelated',
            'ProductRelated_Duration', 'BounceRates', 'ExitRates',
            'PageValues', 'SpecialDay', 'Month', 'OperatingSystems',
            'Browser', 'Region', 'TrafficType', 'VisitorType', 'Weekend'
        ])  
        prediction = loaded_pipeline.predict(features)
        return render_template('result.html', prediction=prediction[0])
if __name__ == '__main__':
    app.run(debug=True)
