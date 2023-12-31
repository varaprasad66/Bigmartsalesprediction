from flask import Flask, jsonify, render_template, request,url_for,app
import joblib
import os
import numpy as np   

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    item_weight= float(request.form['item_weight'])
    item_fat_content=float(request.form['item_fat_content'])
    item_visibility= float(request.form['item_visibility'])
    item_type= float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    outlet_identifier=float(request.form['outlet_identifier'])
    outlet_establishment_year= float(request.form['outlet_establishment_year'])
    outlet_size= float(request.form['outlet_size'])
    outlet_location_type= float(request.form['outlet_location_type'])
    outlet_type= float(request.form['outlet_type'])

    X= np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                  outlet_identifier,outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])

    sc=joblib.load('scaling.pkl')

    X_std= sc.transform(X)

    model= joblib.load('regressor.pkl')

    Y_pred=model.predict(X_std)

    return render_template("home.html",prediction_text="The Item_Outlet_Sales prediction is  {}".format(Y_pred))


if __name__ == "__main__":
    app.run(debug=True)