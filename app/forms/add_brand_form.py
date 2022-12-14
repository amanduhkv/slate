from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired
# from flask_wtf.file import FileField, FileAllowed

from ..seeds.fonts import fonts

f = []
for font in fonts:
   f.append((font['family'], font['family']))


colors = [
   ("aliceblue", "Aliceblue"),
   ("antiquewhite", "Antiquewhite"),
   ("aqua", "Aqua"),
   ("aquamarine", "Aquamarine"),
   ("azure", "Azure"),
   ("beige", "Beige"),
   ("bisque", "Bisque"),
   ("black", "Black"),
   ("blanchedalmond", "Blanchedalmond"),
   ("blue", "Blue"),
   ("blueviolet", "Blueviolet"),
   ("brown", "Brown"),
   ("burlywood", "Burlywood"),
   ("cadetblue", "Cadetblue"),
   ("chartreuse", "Chartreuse"),
   ("chocolate", "Chocolate"),
   ("coral", "Coral"),
   ("cornflowerblue", "Cornflowerblue"),
   ("cornsilk", "Cornsilk"),
   ("crimson", "Crimson"),
   ("cyan", "Cyan"),
   ("darkblue", "Darkblue"),
   ("darkcyan", "Darkcyan"),
   ("darkgoldenrod", "Darkgoldenrod"),
   ("darkgray", "Darkgray"),
   ("darkgrey", "Darkgrey"),
   ("darkgreen", "Darkgreen"),
   ("darkkhaki", "Darkkhaki"),
   ("darkmagenta", "Darkmagenta"),
   ("darkolivegreen", "Darkolivegreen"),
   ("darkorange", "Darkorange"),
   ("darkorchid", "Darkorchid"),
   ("darkred", "Darkred"),
   ("darksalmon", "Darksalmon"),
   ("darkseagreen", "Darkseagreen"),
   ("darkslateblue", "Darkslateblue"),
   ("darkslategray", "Darkslategray"),
   ("darkslategrey", "Darkslategrey"),
   ("darkturquoise", "Darkturquoise"),
   ("darkviolet", "Darkviolet"),
   ("deeppink", "Deeppink"),
   ("deepskyblue", "Deepskyblue"),
   ("dimgray", "Dimgray"),
   ("dimgrey", "Dimgrey"),
   ("dodgerblue", "Dodgerblue"),
   ("firebrick", "Firebrick"),
   ("floralwhite", "Floralwhite"),
   ("forestgreen", "Forestgreen"),
   ("fuchsia", "Fuchsia"),
   ("gainsboro", "Gainsboro"),
   ("ghostwhite", "Ghostwhite"),
   ("gold", "Gold"),
   ("goldenrod", "Goldenrod"),
   ("gray", "Gray"),
   ("grey", "Grey"),
   ("green", "Green"),
   ("greenyellow", "Greenyellow"),
   ("honeydew", "Honeydew"),
   ("hotpink", "Hotpink"),
   ("indianred", "Indianred"),
   ("indigo", "Indigo"),
   ("ivory", "Ivory"),
   ("khaki", "Khaki"),
   ("lavender", "Lavender"),
   ("lavenderblush", "Lavenderblush"),
   ("lawngreen", "Lawngreen"),
   ("lemonchiffon", "Lemonchiffon"),
   ("lightblue", "Lightblue"),
   ("lightcoral", "Lightcoral"),
   ("lightcyan", "Lightcyan"),
   ("lightgoldenrodyellow", "Lightgoldenrodyellow"),
   ("lightgray", "Lightgray"),
   ("lightgrey", "Lightgrey"),
   ("lightgreen", "Lightgreen"),
   ("lightpink", "Lightpink"),
   ("lightsalmon", "Lightsalmon"),
   ("lightseagreen", "Lightseagreen"),
   ("lightskyblue", "Lightskyblue"),
   ("lightslategray", "Lightslategray"),
   ("lightslategrey", "Lightslategrey"),
   ("lightsteelblue", "Lightsteelblue"),
   ("lightyellow", "Lightyellow"),
   ("lime", "Lime"),
   ("limegreen", "Limegreen"),
   ("linen", "Linen"),
   ("magenta", "Magenta"),
   ("maroon", "Maroon"),
   ("mediumaquamarine", "Mediumaquamarine"),
   ("mediumblue", "Mediumblue"),
   ("mediumorchid", "Mediumorchid"),
   ("mediumpurple", "Mediumpurple"),
   ("mediumseagreen", "Mediumseagreen"),
   ("mediumslateblue", "Mediumslateblue"),
   ("mediumspringgreen", "Mediumspringgreen"),
   ("mediumturquoise", "Mediumturquoise"),
   ("mediumvioletred", "Mediumvioletred"),
   ("midnightblue", "Midnightblue"),
   ("mintcream", "Mintcream"),
   ("mistyrose", "Mistyrose"),
   ("moccasin", "Moccasin"),
   ("navajowhite", "Navajowhite"),
   ("navy", "Navy"),
   ("oldlace", "Oldlace"),
   ("olive", "Olive"),
   ("olivedrab", "Olivedrab"),
   ("orange", "Orange"),
   ("orangered", "Orangered"),
   ("orchid", "Orchid"),
   ("palegoldenrod", "Palegoldenrod"),
   ("palegreen", "Palegreen"),
   ("paleturquoise", "Paleturquoise"),
   ("palevioletred", "Palevioletred"),
   ("papayawhip", "Papayawhip"),
   ("peachpuff", "Peachpuff"),
   ("peru", "Peru"),
   ("pink", "Pink"),
   ("plum", "Plum"),
   ("powderblue", "Powderblue"),
   ("purple", "Purple"),
   ("rebeccapurple", "Rebeccapurple"),
   ("red", "Red"),
   ("rosybrown", "Rosybrown"),
   ("royalblue", "Royalblue"),
   ("saddlebrown", "Saddlebrown"),
   ("salmon", "Salmon"),
   ("sandybrown", "Sandybrown"),
   ("seagreen", "Seagreen"),
   ("seashell", "Seashell"),
   ("sienna", "Sienna"),
   ("silver", "Silver"),
   ("skyblue", "Skyblue"),
   ("slateblue", "Slateblue"),
   ("slategray", "Slategray"),
   ("slategrey", "Slategrey"),
   ("snow", "Snow"),
   ("springgreen", "Springgreen"),
   ("steelblue", "Steelblue"),
   ("tan", "Tan"),
   ("teal", "Teal"),
   ("thistle", "Thistle"),
   ("tomato", "Tomato"),
   ("turquoise", "Turquoise"),
   ("violet", "Violet"),
   ("wheat", "Wheat"),
   ("white", "White"),
   ("whitesmoke", "Whitesmoke"),
   ("yellow", "Yellow"),
   ("yellowgreen", "Yellowgreen"),
]

# SelectMultipleField choices must be list of tuples: (alias, name)
class AddBrandForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  logo = StringField('Brand Logo (optional)')
  fonts = SelectMultipleField('Brand Fonts (select up to 3)', choices=f)
  colors = SelectMultipleField('Brand Colors (select up to 5)', choices=colors)

  submit = SubmitField('Create Brand')
