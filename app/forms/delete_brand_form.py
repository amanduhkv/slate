from flask_wtf import FlaskForm
from wtforms import SubmitField


class DeleteBrandForm(FlaskForm):
    submit = SubmitField('Remove Brand')
