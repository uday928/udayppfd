from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

# To add records
@app.route('/add_student', methods=['POST'])
def add_student():
    rollno = request.form['rollno']
    stdname = request.form['stdname']
    course = request.form['course']
    duration = request.form['duration']

    students.append({'rollno': rollno, 'stdname': stdname, 'course': course, 'duration': duration})
    return redirect(url_for('index'))

# To delete all records
@app.route('/delete_students', methods=['POST'])
def delete_students():
    students.clear()
    return redirect(url_for('index'))


# To delete only one record
@app.route('/delete_student/<rollno>', methods=['POST'])
def delete_student(rollno):
    for student in students:
        if student['rollno'] == rollno:
            students.remove(student)
            break
    return redirect(url_for('index'))

#to edit student record

if __name__ == '__main__':
    app.run(debug=True)
