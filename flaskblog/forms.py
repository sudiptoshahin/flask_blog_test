from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_wtf.file import FileAllowed

from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms import TextAreaField

##======== For checking out more validation on ============
# https://wtforms.readthedocs.io/en/2.3.x/fields/
##=========================================

from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import ValidationError

from flask_login import current_user

from flaskblog.models import User

##======== For checking out more validation on ============
# https://wtforms.readthedocs.io/en/2.3.x/validators/
##=========================================


############
# for form.validate_on_submit() all validators are remove from the code

###########

class RegistrationForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', [DataRequired(), Email()])

    password = PasswordField('Password', [DataRequired()])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign up')
    
    ## custom validation
    def validate_user(self, username):
        user = User.query.filter_by(username=username.date).first()
        if(user):
            raise ValidationError('That username is already taken. Please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if(user):
            raise ValidationError('That email is already taken. Please choose another one.')




class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=3, max=20)])

    email = StringField('Email', [DataRequired(), Email()])

    picture = FileField('Update the profile picture')
    submit = SubmitField('Update')
    
    ## custom validation
    def validate_user(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.date).first()
            if(user):
                raise ValidationError('That username is already taken. Please choose another one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if(user):
                raise ValidationError('That email is already taken. Please choose another one.')



class PostForm(FlaskForm):
    title = StringField('Title', [DataRequired()])
    content = TextAreaField('Content', [DataRequired()])

    submit = SubmitField('Post')



