<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Employee Management System - README</title>

</head>

<body>

<h1>Project README</h1>

<h2>Employee System</h2>

<p>This project allows users to insert new employee information into a database and retrieve employee data based on hiring dates.</p>
<p>There are various methods for communication between client and servers as :</p>
<ol>
      <li>Get method:</li>
      <p>It's used to request data from a specified resource, <b> as fetching data of employees from the database according to specific condition.</b></p>
      <li>Post method:</li>
      <p>is used to submit data to be processed to a specified resource <b> as insert data of employee into db </b></p>
</ol>

<h3>Features</h3>

<ul>
  <li><strong>Responsive Web Page:</strong> Utilizes Bootstrap for creating a responsive and visually appealing web page.</li>
  <li><strong>Flask Framework:</strong> Implements the Flask framework for handling server-side logic and RESET_aPI</li>
  <li><strong>Database Interaction:</strong> Connects to a SQL Server database to insert and retrieve employee data.</li>
  <li><strong>JavaScript Alerts:</strong> Utilizes SweetAlert to display user-friendly success or error messages.</li>
</ul>

<h3>Project Structure</h3>

<ul>
  <li><code>app.py:</code> Python script containing the Flask application and database interaction functions.</li>
  <li><code>templates/home.html:</code> HTML template for the main application page, including forms and employee data display.</li>
  <li><code>static/style.css:</code> CSS file for styling the web page.</li>
  <li><code>requirements.txt:</code> Lists the project dependencies.</li>
</ul>


<h3>Usage</h3>

<ol>
  <li>Access the main page to insert new employee data.</li>
  <li>Fill in the required details and submit the form.</li>
  <li>SweetAlert messages will inform you of the success or failure of the data insertion.</li>
  <li>Use the "Retrieve Employee Data" section to search for employees based on hiring date.</li>
</ol>

<h3>Dependencies</h3>

<ul>
  <li>Flask</li>
  <li>PyODBC</li>
  <li>Bootstrap (CDN)</li>
  <li>SweetAlert2 (CDN)</li>
</ul>


<h3>Demo</h3>

https://github.com/noraibraheem/Develop_ResetAPI/assets/62545277/fa008c2f-8eb1-493e-8c72-f7cd95482327

</body>

</html>
