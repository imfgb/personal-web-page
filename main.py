from flask import Flask, render_template, request
from google.cloud import ndb
from contact_model import Contact

app = Flask(__name__)
client = ndb.Client(project="ulrich-web-app")

@app.route(r'/', methods=['GET'])
def ulrichPersonalWeb():
    return render_template('ulrichPersonalWeb.html')

@app.route(r'/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route(r'/contact', methods=['GET', 'POST'])
def add_contact():
    if request.form:
        with client.context():
            contact = Contact(name=request.form.get('name'),
                              email=request.form.get('email'),
                              phone=request.form.get('phone'),
                              message=request.form.get('message'))

            contact.put()

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
