from flask_wtf import FlaskForm
from wtforms import SubmitField


class DeleteDesignForm(FlaskForm):
    submit = SubmitField('Remove Design')
