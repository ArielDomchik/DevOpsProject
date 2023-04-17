from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///efs/crud.db' # Using SQLite database
db = SQLAlchemy(app)

logging.info('Application Running!')
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename="pythonapp.log")



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

with app.app_context():
    # Create the database tables
    db.create_all()

@app.route('/')
def index():
    users = User.query.all()
    app.logger.warning("user asks for home page")
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    app.logger.warning("user added: name={}, email={}".format(name, email))
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    user_id = request.form['id']
    user = User.query.get(user_id)
    user.name = request.form['name']
    user.email = request.form['email']
    db.session.commit()
    app.logger.warning("user updated: name={}, email={}".format(user.name, user.email))
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    user_id = request.form['id']
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    app.logger.warning("User deleted: id={}".format(user_id))
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
