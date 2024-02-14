from flask import Flask, render_template, request, jsonify,redirect,url_for
import pyodbc

app = Flask(__name__)

db_config = 'Driver={SQL Server};Server=DESKTOP-H4N659E\SQLEXPRESS;Database=Employees;Trusted_Connection=yes;'


def insert_data(id, name, age, hiring_date):
    try:
        with pyodbc.connect(db_config) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO employees (id, name, age, hiring_date) VALUES (?, ?, ?, ?)"
            values = (id, name, age, hiring_date)
            cursor.execute(query, values)
            connection.commit()
            return True
    except Exception as e:
        print(f"Error inserting data: {e}")
        return False


@app.route('/get_employees', methods=['GET'])
def get_employees():
    try:
        hiring_date = request.args.get('hiring_date')
        
        with pyodbc.connect(db_config) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM employees WHERE hiring_date = ?"
            cursor.execute(query, (hiring_date,))
            employees = cursor.fetchall()

        # Render the template with the retrieved data
        return render_template('home.html', employees=employees)
    except Exception as e:
        print(f"Error retrieving data: {e}")
        # Render the template with an error message
        return render_template('home.html', error_message=f'Failed to retrieve data. {str(e)}')
    
@app.route('/')
def home_page():
    # Retrieve status and message from query parameters
    status = request.args.get('status')
    message = request.args.get('message')

    return render_template('home.html', status=status, message=message)


@app.route('/insert_data', methods=['POST'])
def insert_data_route():
    id = request.form.get('id')
    name = request.form.get('name')
    age = request.form.get('age')
    hiring_date = request.form.get('hiring_date')

    if all([id, name, age, hiring_date]):
        success = insert_data(id, name, age, hiring_date)
        if success:
            # Use SweetAlert to display success message
            return redirect(url_for('home_page', status='success', message='Data inserted successfully'))
        else:
            # Use SweetAlert to display error message
            return redirect(url_for('home_page', status='error', message='Failed to insert data'))
    else:
        # Use SweetAlert to display invalid data message
        return redirect(url_for('home_page', status='error', message='Invalid data'))