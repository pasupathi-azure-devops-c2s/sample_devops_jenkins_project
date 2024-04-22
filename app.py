from flask import Flask, render_template, request
from pymongo import MongoClient
from urllib.parse import quote_plus
import logging

app = Flask(__name__, template_folder='templates', static_folder='static')

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_mongodb():
    username = 'pasupathikumar819'
    password = 'MSpk@819'  # Your actual password here
    # Encode username and password using quote_plus
    encoded_username = quote_plus(username)
    encoded_password = quote_plus(password)
    # Construct connection string with encoded username and password
    connection_string = f'mongodb+srv://{encoded_username}:{encoded_password}@devops.2yb7ut5.mongodb.net/'
    try:
        client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
        database = client['Django_project']
        collection = database['Project_database']
        return collection
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        raise
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            form_data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'contact_no': request.form['contact_no'],
                'email': request.form['email'],
                'username': request.form['username'],
                'password': request.form['password']
            }
            collection = connect_to_mongodb()
            collection.insert_one(form_data)
            return 'Form submitted successfully!'
        except Exception as e:
            logger.error(f"Failed to insert data into MongoDB: {e}")
            return 'Failed to submit form data. Please try again later.', 500
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
