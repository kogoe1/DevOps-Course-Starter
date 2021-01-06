from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField('TODO Title', validators=[DataRequired()])
    description = StringField('Description (Optional)')
    submit = SubmitField('Add')