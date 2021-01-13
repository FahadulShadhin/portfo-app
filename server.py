from flask import Flask
from flask import render_template, url_for, request
import csv

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form(name=None):
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('thankyou.html', name=name)
    else:
        return 'something went wrong!'

if __name__ == '__main__':
    app.debug = True
    app.run()