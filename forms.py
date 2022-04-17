from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    """Form for registering users."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=5)])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=5)])


# class UserEditForm(FlaskForm):
#     """Form for editing users."""

#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[Length(min=5)])
