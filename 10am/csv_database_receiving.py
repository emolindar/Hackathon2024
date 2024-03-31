# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 06:31:50 2024

@author: Peter-Emil
"""

from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'fileUpload' not in request.files:
        return "No file part", 400
    file = request.files['fileUpload']
    if file.filename == '':
        return "No selected file", 400
    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        # Process your CSV with pandas here
        print(df.head())  # Example: Print the first few rows
        return "File processed successfully", 200
    else:
        return "Invalid file format", 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
