from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

from ..seeds.fonts import fonts

f = []
for font in fonts:
   f.append((font['family'], font['family']))

# SelectMultipleField choices must be list of tuples: (alias, name)
class AddBrandForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  logo = StringField('Brand Logo (optional)')
  fonts = SelectMultipleField('Brand Fonts (select up to 3)', choices=f)
  colors = SelectMultipleField('Brand Colors (select up to 5)', choices=[('red', 'red'), ('blue', 'blue'), ('green', 'green'), ('yellow', 'yellow'), ('pink', 'pink'), ('orange', 'orange'), ('magenta', 'magenta'), ('periwinkle', 'periwinkle')])

  submit = SubmitField('Create Brand')
