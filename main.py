from flask import *
from postmanAPP import sendMesage
from mailjet_rest import Client
from dotenv import load_dotenv
import os
from postmanAPP import *

load_dotenv()

# api_key = os.getenv('API_KEY')
# api_secret = os.getenv('SECRET_KEY')
# mailjet = Client(auth=(api_key, api_secret), version='v3.1')

app = Flask(__name__)

@app.route('/')
def home():
    # message = sendMesage('Blabla', 'Pasha!!!')
    # result = mailjet.send.create(data=message)
    return render_template('index.html')

@app.route('/send-data', methods=['POST'])
def send_data():
    # Extract data from the form
    name = request.form['name']
    email = request.form['email']
    message_content = request.form['message']
    print(email)
    print(name)
    print(message_content)
    # Construct the email content using the extracted data
    message = sendMesage(name, message_content)  # Assuming this sends the message to an email
    result = mailjet.send.create(data=message)
    print(result.json())
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


