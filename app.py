from flask import Flask,request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.predict import PredictPipeline

# jsonify converts python dictionary to JSON response
# flask_cors -> is a package that simplifies cross-origin resource sharing handling
# CORS is a secure feature implemented by web browsers to control how web pages or web application from one origin (domain)
# interact with resources from another origin

#-----------------------------------------------------------------

# os.putenv() - function in python is used to set environment variables. it aallows you to define or modify environment
# variable that affect how the os and its process behave.

#-----------------------------------------------------------------

os.putenv('LANG','en_US.UTF-8')
# sets the LANG environment variable tp 'en_US.UTF-8' the LANG variable specifies the default 
# language and culture setting for user interface
os.putenv("LC_ALL",'en_US.UTF-8')
# LC_ALL variable can be used to override all other local setting and enforce a specific local throught

# THIS ENSURES A CONSISTENT AND STANDARDIZED CHARACTER ENCODING AND LANGUAGE SETTING.

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = 'inputImage.jpg'
        self.classifier = PredictPipeline(self.filename)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train',methods = ['GET','POST'])
@cross_origin()  # ALLOWS YOU TO ENABLE CORS FOR ONLY THOSE ROUTES THAT REQUIRE IT, THIS GIVES FINIR CONTROL OVER WHICH ROUTE CAN ACCEPT CROSS-ORIGIN REQUEST 
def trainRoute():
    # os.system('python main.py')
    os.system('dvc repro')
    return 'training done successfully'

@app.route('/predict',methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image,clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == "__main__":
    clApp = ClientApp() # CUSTOM CLASS DEFINED ELSEWHERE IN THE CODEBASE
    # app.run(host='0.0.0.0',port=8080) # FOR LOCALHOST 
    app.run(host = '0.0.0.0', port = 80)  # FOR AZURE

