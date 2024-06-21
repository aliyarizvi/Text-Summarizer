from src.pipeline.predict_pipeline import Prediction
from flask import Flask, jsonify,request,render_template, redirect, url_for

app = Flask(__name__)

predictor = Prediction()


@app.route('/')
def index():
    return render_template('index.html',summary=None)

@app.route('/predict', methods=['GET','POST'])
def predict():
    summary = ''
    if request.method == 'POST':
        input_text = request.form['input_text']
        if input_text.strip() != '':
            summary = predictor.predict(text = input_text) 
    return render_template('index.html', summary=summary)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)