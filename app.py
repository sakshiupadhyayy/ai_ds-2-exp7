from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Load the CSV file
    df = pd.read_csv('C:\Users\Administrator\Desktop\aids-Exp7\data.csv')
    
    # Process data
    gender_counts = df['gender'].value_counts().to_dict()
    
    # Convert data to JSON
    gender_data = json.dumps(gender_counts)
    
    return render_template('index.html', gender_data=gender_data)

if __name__ == '__main__':
    app.run(debug=True)
