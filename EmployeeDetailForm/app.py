from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
    Eno = db.Column(db.Integer, primary_key=True)
    Ename = db.Column(db.String(20))
    Basic = db.Column(db.Integer)
    Dno = db.Column(db.String(20))

@app.route('/')
def index():
    allEmp = Employee.query.all()
    return render_template('index.html', allEmp=allEmp)

@app.route('/addemp')
def addemp():
    return render_template("addemp.html")
    
@app.route('/SaveEmp', methods=['GET', 'POST'])
def SaveEmp():
    if request.method == "POST":
        eno = request.form['Eno']
        ename = request.form['Ename']
        basic = request.form['Basic']
        dno = request.form['Dno']
        e1 = Employee(Eno=eno, Ename=ename, Basic=basic, Dno=dno)
        db.session.add(e1)
        db.session.commit()

    # Fetch all employee records from the database
    allEmp = Employee.query.all()

    # Render the add employee page with the updated employee records
    return render_template("addemp.html", allEmp=allEmp)


@app.route('/delete_emp/<int:eno>', methods=['POST'])
def delete_emp(eno):
    emp_to_delete = Employee.query.get_or_404(eno)
    db.session.delete(emp_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/show_all', methods=['GET'])
def show_all():
    allEmp = Employee.query.all()
    return render_template('addemp.html', allEmp=allEmp)

@app.route('/delete_all', methods=['POST'])
def delete_all():
    Employee.query.delete()
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
