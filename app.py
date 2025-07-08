from flask import Flask, render_template, request, redirect, url_for
import joblib
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

model = joblib.load('wine_prediction.pkl')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        try:
            features = [float(x) for x in request.form.values()]
            prediction = model.predict([features])
            output = prediction[0]
            text = 'Damn Good Wine' if output == 1 else 'Not that good Wine'
            return render_template('index.html', prediction_text=text)
        except Exception as e:
            text = f'Error: {str(e)}'
            return render_template('index.html', prediction_text=text)
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)