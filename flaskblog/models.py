from flaskblog import db
from datetime import datetime

# login authentication
from flaskblog import login_manager
from flask_login import UserMixin


# load the user with id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    ## one to many relation between the user and the post
    # because a user has many posts
    # posts has only one user
    posts = db.relationship('Post', backref='author', lazy=True)

    # __repr__ is a special method which is used to 
    # represent the classes objects as a string. Its a
    # built-in-function. It also called the official representation
    # of an object and used for debugging.
    def __repr__(self):
        return f'User("{self.username}", "{self.email}", "{self.image_file}")'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    ## its the user id 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Post("{self.title}", "{self.date_posted}")'
