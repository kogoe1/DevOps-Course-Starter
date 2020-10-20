from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class TodoForm(FlaskForm):
    title = StringField('TODO Title', validators=[DataRequired()])
    submit = SubmitField('Add')