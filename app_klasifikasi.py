from flask import Flask, request, render_template
import pickle
import pandas as pd 
import numpy as np 

app = Flask(__name__)

model_file = open('ball.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('Temp.html', hasil=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html pp8
    '''
    p1=int(request.form['p1'])
    
    p2=int(request.form['p2'])

    p3=int(request.form['p3'])

    p4=int(request.form['p4'])

    p5=int(request.form['p5'])

    p6=int(request.form['p6'])

    p7=int(request.form['p7'])

    p8=int(request.form['p8'])

    x=np.array([[p1,p2,p3,p4,p5,p6,p7,p8]])

    # kelas="NULL"

 
    
    prediction = model.predict(x)
    output = round(prediction[0],0)
    kelas = output
    if (output==1):
        kelas="1"
    elif(output==2):
        kelas="2"
    elif(output==3):
        kelas="3"
    elif(output==4):
        kelas="4"
    elif(output==5):
        kelas="5"
    elif(output==6):
        kelas="6"
    elif(output==7):
        kelas="7"
    elif(output==8):
        kelas="8"


    return render_template('Temp.html', hasil=kelas, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8)


if __name__ == '__main__':
    app.run(debug=True)