from flask import Flask, render_template, request
from datetime import datetime

<<<<<<< HEAD
=======
def calculate_age(dob):
    today = datetime.today()
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

>>>>>>> e0276c6ec8b5fa360a107268daa8beee15f4573d
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
<<<<<<< HEAD
        welcome_message = f"Welcome, {name}! Your date of birth is {dob}."
=======
        age = calculate_age(dob)
        welcome_message = f"Welcome, {name}! You are {age} years old."
>>>>>>> e0276c6ec8b5fa360a107268daa8beee15f4573d
        return render_template('result.html', message=welcome_message)
    return render_template('index.html')

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
    
=======
    app.run(debug=True)
>>>>>>> e0276c6ec8b5fa360a107268daa8beee15f4573d
