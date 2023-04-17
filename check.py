from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import unittest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.app_context().push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_route(self):
        user = User(name='John')
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(name='John').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'John')

    def test_update_route(self):
        user = User(name='John')
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(name='John').first()
        user.name = 'Jane'
        db.session.commit()
        updated_user = User.query.filter_by(name='Jane').first()
        self.assertIsNotNone(updated_user)
        self.assertEqual(updated_user.name, 'Jane')

    def test_delete_route(self):
        user = User(name='John')
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(name='John').first()
        db.session.delete(user)
        db.session.commit()
        deleted_user = User.query.filter_by(name='John').first()
        self.assertIsNone(deleted_user)


if __name__ == '__main__':
    unittest.main()
