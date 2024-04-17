from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas cluster
client = MongoClient('mongodb+srv://Pasupathikumar:MSpk@819@facedetection.g4nbyn9.mongodb.net/')
database = client['Django_project']
collection = database['Project_database']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        contact_no = request.form['contact_no']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        
        # Insert data into MongoDB
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'contact_no': contact_no,
            'email': email,
            'username': username,
            'password': password
        }
        collection.insert_one(data)
        
        return 'Form submitted successfully!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
