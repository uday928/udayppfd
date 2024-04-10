from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'ino': [101, 102, 103],
        'iname': ['Computers', 'Printers', 'Keyboards'],
        'iqty': [12, 5, 20]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
