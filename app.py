from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

# import dataset cleaned before using scaler

# codage de pipeline



#with open('model.pkl', 'wb') as file: 
    #pickle.dump(model, file)

#with open('model.pkl', 'rb') as file: 
    #model = pickle.load(file)

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
        visitor_type = request.form.get('visitor_type')
        weekend = request.form.get('weekend', type=bool)
        features = [
            administrative, administrative_duration, informational,
            informational_duration, product_related, product_related_duration,
            bounce_rates, exit_rates, page_values, special_day,
            month, operating_systems, browser, region, traffic_type,
            visitor_type, weekend
        ]
        #prediction = model.predict([features])
        prediction = [0,0]
        return render_template('result.html', prediction=prediction[0])
if __name__ == '__main__':
    app.run(debug=True)
