from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Function to retrieve data from Excel file
def get_data_from_excel():
    df = pd.read_excel(r'C:\Users\Gandhi Uday\OneDrive\Desktop\Uday Works\Sem 4 material\Sem 4 Works\PPFD Lab Manual\PythonSet3\Set3.4\templates\data.xlsx')
    return df.values.tolist(), df.columns.tolist()

# Route for displaying data
@app.route('/')
def display_data():
    # Retrieve data from Excel file
    data, headers = get_data_from_excel()
    
    return render_template('index.html', data=data, headers=headers)

if __name__ == '__main__':
    app.run(debug=True)
