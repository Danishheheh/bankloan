#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request
import joblib
import numpy as np

#initialize flask app
app=Flask(__name__)
#load trained model
model=joblib.load("fraud_model.pkl")


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=["POST"])
def predict():
    #get dat from form
    try:
        features=[float(request.form[f'feature{i}']) for i in range(1,6)]
    except ValueError:
        return render_template('result.html',prediction='Invalid input. Please enter numeric values.')
    # make prediction
    prediction = model.predict([features])[0]
    # map prediction to class name
    class_names=['Not Fraud', 'Fraud']
    result=class_names[prediction]
    return render_template('result.html',prediction=result)
if __name__=='__main__':
    app.run(debug=True)
