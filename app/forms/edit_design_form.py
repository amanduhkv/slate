from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError


class EditDesignForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])

  submit = SubmitField('Submit Changes')
