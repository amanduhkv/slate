from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

templates = [
  ( 'presentation', 'Presentation (1920 x 1080 px)' ),
  ( 'website', 'Website (1366 x 768 px)' ),
  ( 'resume', 'Resume (8.5 x 11 in)' ),
  ( 'igpost', 'Instagram Post (1080 x 1080 px)' ),
  ( 'igstory', 'Instagram Story (1080 x 1920 px)' ),
  ( 'fbpost', 'Facebook Post (940 x 788 px)' ),
  ( 'invitation', 'Invitation (5 x 7 in)' ),
  ( 'businesscard', 'Business Card (3.5 x 2 in)' ),
  ( 'infograph', 'Infographic (1080 x 1920 px)' )
]

class AddDesignForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  template = SelectField('Design dimensions (select one)', validators=[DataRequired()], choices=templates)

  submit = SubmitField('Enter')
