from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock database for storing user data
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if username already exists
        if username in users:
            return 'Username already exists! Please choose a different one.'
        # Hash the password before storing it
        hashed_password = generate_password_hash(password)
        users[username] = hashed_password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username exists
        if username in users:
            # Check if the password is correct
            if check_password_hash(users[username], password):
                session['username'] = username
                return redirect(url_for('profile'))
        return 'Invalid username or password'
    return render_template('login.html')

@app.route('/profile')
def profile():
    # Check if user is logged in
    if 'username' in session:
        username = session['username']
        return render_template('profile.html', username=username)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
