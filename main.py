from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__,template_folder='template')
  

'''@app.route('/')
def ios():
    return render_template('link.html')'''

@app.route('/',methods = ['POST','GET'])
def jen():
    if request.method == "POST":
        model = pickle.load(open('clustering.pkl','rb'))
        result = model.predict([[request.form['a'],request.form['s']]])
        return render_template('index.html',result = result)
    else:
       return render_template('index.html')



if __name__ =='__main__':
    app.run(debug=True)