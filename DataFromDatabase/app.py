from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Route to display the data in a tabular format
@app.route('/')
def display_data():
    data = fetch_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
