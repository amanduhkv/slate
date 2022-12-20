from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

templates = [
  ('presentation-original', 'Original Presentation (1920 x 1080 px)'),
  ('presentation-fun', 'Fun Presentation (1920 x 1080 px)'),
  ('presentation-aesthetic', 'Aesthetic Presentation (1920 x 1080 px)'),
  ('presentation-green', 'Green Presentation (1920 x 1080 px)'),
  ('presentation-bw', 'Black & White Presentation (1920 x 1080 px)'),
  ('website-original', 'Original Website (1366 x 768 px)'),
  ('website-fun', 'Fun Website (1366 x 768 px)'),
  ('website-aesthetic', 'Aesthetic Website (1366 x 768 px)'),
  ('website-green', 'Green Website (1366 x 768 px)'),
  ('website-bw', 'Black & White Website (1366 x 768 px)'),
  ('resume-original', 'Original Resume (8.5 x 11 in)'),
  ('resume-fun', 'Fun Resume (8.5 x 11 in)'),
  ('resume-aesthetic', 'Aesthetic Resume (8.5 x 11 in)'),
  ('resume-green', 'Green Resume (8.5 x 11 in)'),
  ('resume-bw', 'Black & White Resume (8.5 x 11 in)'),
  ('igpost-original', 'Original Instagram Post (1080 x 1080 px)'),
  ('igpost-fun', 'Fun Instagram Post (1080 x 1080 px)'),
  ('igpost-aesthetic', 'Aesthetic Instagram Post (1080 x 1080 px)'),
  ('igpost-green', 'Green Instagram Post (1080 x 1080 px)'),
  ('igpost-bw', 'Black & White Instagram Post (1080 x 1080 px)'),
  ('igstory-original', 'Original Instagram Story (1080 x 1920 px)'),
  ('igstory-fun', 'Fun Instagram Story (1080 x 1920 px)'),
  ('igstory-aesthetic', 'Aesthetic Instagram Story (1080 x 1920 px)'),
  ('igstory-green', 'Green Instagram Story (1080 x 1920 px)'),
  ('igstory-pink', 'Pink Instagram Story (1080 x 1920 px)'),
  ('fbpost-original', 'Original Facebook Post (940 x 788 px)'),
  ('fbpost-fun', 'Fun Facebook Post (940 x 788 px)'),
  ('fbpost-aesthetic', 'Aesthetic Facebook Post (940 x 788 px)'),
  ('fbpost-green', 'Green Facebook Post (940 x 788 px)'),
  ('fbpost-bw', 'Black & White Facebook Post (940 x 788 px)'),
  ('invitation-original', 'Original Invitation (5 x 7 in)'),
  ('invitation-fun', 'Fun Invitation (5 x 7 in)'),
  ('invitation-aesthetic', 'Aesthetic Invitation (5 x 7 in)'),
  ('invitation-green', 'Green Invitation (5 x 7 in)'),
  ('invitation-bw', 'Black & White Invitation (5 x 7 in)'),
  ('businesscard-original', 'Original Business Card (3.5 x 2 in)'),
  ('businesscard-fun', 'Fun Business Card (3.5 x 2 in)'),
  ('businesscard-aesthetic', 'Aesthetic Business Card (3.5 x 2 in)'),
  ('businesscard-green', 'Green Business Card (3.5 x 2 in)'),
  ('businesscard-bw', 'Black & White Business Card (3.5 x 2 in)'),
  ('infograph-original', 'Original Infographic (1080 x 1920 px)'),
  ('infograph-fun', 'Fun Infographic (1080 x 1920 px)'),
  ('infograph-aesthetic', 'Aesthetic Infographic (1080 x 1920 px)'),
  ('infograph-green', 'Green Infographic (1080 x 1920 px)'),
  ('infograph-bw', 'Black & White Infographic (1080 x 1920 px)'),
]

class AddDesignForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  template = SelectField('Template', validators=[DataRequired()], choices=templates)
  color = StringField('Color')
  font = StringField('Font')
  text_input_1 = TextAreaField('Input 1')
  text_input_2 = TextAreaField('Input 2')
  text_input_3 = TextAreaField('Input 3')
  text_input_4 = TextAreaField('Input 4')
  text_input_5 = TextAreaField('Input 5')

  submit = SubmitField('Enter')
