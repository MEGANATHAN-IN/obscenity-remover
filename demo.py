from flask import Flask,request,send_from_directory
import os
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])

def home():
    return " hello mega"

    
    
    
if __name__ == '__main__':
    app.run(debug=True)
