from src.DimondPricePridiction.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import Flask,request,render_template,jsonify




app= Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")