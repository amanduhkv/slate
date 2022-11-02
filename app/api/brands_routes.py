from flask import Blueprint, jsonify, session, request
from app.models import Design, Brand, User, db
from app.models.brands import Color, Font

from ..forms.add_brand_form import AddBrandForm
from ..forms.delete_brand_form import DeleteBrandForm

from flask_login import current_user, login_user, logout_user, login_required

from sqlalchemy import func

brands_routes = Blueprint('brand', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = {}
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages[field] = error
    return errorMessages


# LOAD ALL BRANDS ----------------------------------------
@brands_routes.route('/')
def all_brands():
  brands = Brand.query.all()
  all_brands = [brand.to_dict() for brand in brands]

  for br in all_brands:
    fonts = [font.to_dict() for font in br['fonts']]
    br['fonts'] = fonts
    colors = [color.to_dict() for color in br['colors']]
    br['colors'] = colors


  return jsonify({ 'Brands': all_brands })


# LOAD SINGLE BRAND --------------------------------------
@brands_routes.route('/<int:brand_id>')
def get_one_brand(brand_id):
  brands = Brand.query.get(brand_id)

  if not brands:
    return jsonify({
      "message": "Brand could not be found.",
      "status_code": 404
    }), 404

  brand = brands.to_dict()

  fonts = [font.to_dict() for font in brand['fonts']]
  brand['fonts'] = fonts
  colors = [color.to_dict() for color in brand['colors']]
  brand['colors'] = colors

  return brand


# LOAD ALL USER'S BRANDS --------------------------------
@brands_routes.route('/current')
@login_required
def get_user_brands():
  user = current_user.to_dict()
  user_id = user['id']
  if not user:
        return 'User must be logged in'

  brands = Brand.query.filter_by(user_id=user_id)
  all_brands = [brand.to_dict() for brand in brands]
  current_brands = []


  if len(all_brands) > 0:
    for brand in all_brands:
      fonts = [font.to_dict() for font in brand['fonts']]
      brand['fonts'] = fonts
      colors = [color.to_dict() for color in brand['colors']]
      brand['colors'] = colors

      current_brands.append(brand)
    return jsonify({
      'Brands': current_brands
    })
  return {'Current user does not have any brands yet.'}



colors = [
  {'alias': "aliceblue" , 'title': "Aliceblue"},
  {'alias': "antiquewhite" , 'title': "Antiquewhite"},
  {'alias': "aqua" , 'title': "Aqua"},
  {'alias': "aquamarine" , 'title': "Aquamarine"},
  {'alias': "azure" , 'title': "Azure"},
  {'alias': "beige" , 'title': "Beige"},
  {'alias': "bisque" , 'title': "Bisque"},
  {'alias': "black" , 'title': "Black"},
  {'alias': "blanchedalmond" , 'title': "Blanchedalmond"},
  {'alias': "blue" , 'title': "Blue"},
  {'alias': "blueviolet" , 'title': "Blueviolet"},
  {'alias': "brown" , 'title': "Brown"},
  {'alias': "burlywood" , 'title': "Burlywood"},
  {'alias': "cadetblue" , 'title': "Cadetblue"},
  {'alias': "chartreuse" , 'title': "Chartreuse"},
  {'alias': "chocolate" , 'title': "Chocolate"},
  {'alias': "coral" , 'title': "Coral"},
  {'alias': "cornflowerblue" , 'title': "Cornflowerblue"},
  {'alias': "cornsilk" , 'title': "Cornsilk"},
  {'alias': "crimson" , 'title': "Crimson"},
  {'alias': "cyan" , 'title': "Cyan"},
  {'alias': "darkblue" , 'title': "Darkblue"},
  {'alias': "darkcyan" , 'title': "Darkcyan"},
  {'alias': "darkgoldenrod" , 'title': "Darkgoldenrod"},
  {'alias': "darkgray" , 'title': "Darkgray"},
  {'alias': "darkgrey" , 'title': "Darkgrey"},
  {'alias': "darkgreen" , 'title': "Darkgreen"},
  {'alias': "darkkhaki" , 'title': "Darkkhaki"},
  {'alias': "darkmagenta" , 'title': "Darkmagenta"},
  {'alias': "darkolivegreen" , 'title': "Darkolivegreen"},
  {'alias': "darkorange" , 'title': "Darkorange"},
  {'alias': "darkorchid" , 'title': "Darkorchid"},
  {'alias': "darkred" , 'title': "Darkred"},
  {'alias': "darksalmon" , 'title': "Darksalmon"},
  {'alias': "darkseagreen" , 'title': "Darkseagreen"},
  {'alias': "darkslateblue" , 'title': "Darkslateblue"},
  {'alias': "darkslategray" , 'title': "Darkslategray"},
  {'alias': "darkslategrey" , 'title': "Darkslategrey"},
  {'alias': "darkturquoise" , 'title': "Darkturquoise"},
  {'alias': "darkviolet" , 'title': "Darkviolet"},
  {'alias': "deeppink" , 'title': "Deeppink"},
  {'alias': "deepskyblue" , 'title': "Deepskyblue"},
  {'alias': "dimgray" , 'title': "Dimgray"},
  {'alias': "dimgrey" , 'title': "Dimgrey"},
  {'alias': "dodgerblue" , 'title': "Dodgerblue"},
  {'alias': "firebrick" , 'title': "Firebrick"},
  {'alias': "floralwhite" , 'title': "Floralwhite"},
  {'alias': "forestgreen" , 'title': "Forestgreen"},
  {'alias': "fuchsia" , 'title': "Fuchsia"},
  {'alias': "gainsboro" , 'title': "Gainsboro"},
  {'alias': "ghostwhite" , 'title': "Ghostwhite"},
  {'alias': "gold" , 'title': "Gold"},
  {'alias': "goldenrod" , 'title': "Goldenrod"},
  {'alias': "gray" , 'title': "Gray"},
  {'alias': "grey" , 'title': "Grey"},
  {'alias': "green" , 'title': "Green"},
  {'alias': "greenyellow" , 'title': "Greenyellow"},
  {'alias': "honeydew" , 'title': "Honeydew"},
  {'alias': "hotpink" , 'title': "Hotpink"},
  {'alias': "indianred" , 'title': "Indianred"},
  {'alias': "indigo" , 'title': "Indigo"},
  {'alias': "ivory" , 'title': "Ivory"},
  {'alias': "khaki" , 'title': "Khaki"},
  {'alias': "lavender" , 'title': "Lavender"},
  {'alias': "lavenderblush" , 'title': "Lavenderblush"},
  {'alias': "lawngreen" , 'title': "Lawngreen"},
  {'alias': "lemonchiffon" , 'title': "Lemonchiffon"},
  {'alias': "lightblue" , 'title': "Lightblue"},
  {'alias': "lightcoral" , 'title': "Lightcoral"},
  {'alias': "lightcyan" , 'title': "Lightcyan"},
  {'alias': "lightgoldenrodyellow" , 'title': "Lightgoldenrodyellow"},
  {'alias': "lightgray" , 'title': "Lightgray"},
  {'alias': "lightgrey" , 'title': "Lightgrey"},
  {'alias': "lightgreen" , 'title': "Lightgreen"},
  {'alias': "lightpink" , 'title': "Lightpink"},
  {'alias': "lightsalmon" , 'title': "Lightsalmon"},
  {'alias': "lightseagreen" , 'title': "Lightseagreen"},
  {'alias': "lightskyblue" , 'title': "Lightskyblue"},
  {'alias': "lightslategray" , 'title': "Lightslategray"},
  {'alias': "lightslategrey" , 'title': "Lightslategrey"},
  {'alias': "lightsteelblue" , 'title': "Lightsteelblue"},
  {'alias': "lightyellow" , 'title': "Lightyellow"},
  {'alias': "lime" , 'title': "Lime"},
  {'alias': "limegreen" , 'title': "Limegreen"},
  {'alias': "linen" , 'title': "Linen"},
  {'alias': "magenta" , 'title': "Magenta"},
  {'alias': "maroon" , 'title': "Maroon"},
  {'alias': "mediumaquamarine" , 'title': "Mediumaquamarine"},
  {'alias': "mediumblue" , 'title': "Mediumblue"},
  {'alias': "mediumorchid" , 'title': "Mediumorchid"},
  {'alias': "mediumpurple" , 'title': "Mediumpurple"},
  {'alias': "mediumseagreen" , 'title': "Mediumseagreen"},
  {'alias': "mediumslateblue" , 'title': "Mediumslateblue"},
  {'alias': "mediumspringgreen" , 'title': "Mediumspringgreen"},
  {'alias': "mediumturquoise" , 'title': "Mediumturquoise"},
  {'alias': "mediumvioletred" , 'title': "Mediumvioletred"},
  {'alias': "midnightblue" , 'title': "Midnightblue"},
  {'alias': "mintcream" , 'title': "Mintcream"},
  {'alias': "mistyrose" , 'title': "Mistyrose"},
  {'alias': "moccasin" , 'title': "Moccasin"},
  {'alias': "navajowhite" , 'title': "Navajowhite"},
  {'alias': "navy" , 'title': "Navy"},
  {'alias': "oldlace" , 'title': "Oldlace"},
  {'alias': "olive" , 'title': "Olive"},
  {'alias': "olivedrab" , 'title': "Olivedrab"},
  {'alias': "orange" , 'title': "Orange"},
  {'alias': "orangered" , 'title': "Orangered"},
  {'alias': "orchid" , 'title': "Orchid"},
  {'alias': "palegoldenrod" , 'title': "Palegoldenrod"},
  {'alias': "palegreen" , 'title': "Palegreen"},
  {'alias': "paleturquoise" , 'title': "Paleturquoise"},
  {'alias': "palevioletred" , 'title': "Palevioletred"},
  {'alias': "papayawhip" , 'title': "Papayawhip"},
  {'alias': "peachpuff" , 'title': "Peachpuff"},
  {'alias': "peru" , 'title': "Peru"},
  {'alias': "pink" , 'title': "Pink"},
  {'alias': "plum" , 'title': "Plum"},
  {'alias': "powderblue" , 'title': "Powderblue"},
  {'alias': "purple" , 'title': "Purple"},
  {'alias': "rebeccapurple" , 'title': "Rebeccapurple"},
  {'alias': "red" , 'title': "Red"},
  {'alias': "rosybrown" , 'title': "Rosybrown"},
  {'alias': "royalblue" , 'title': "Royalblue"},
  {'alias': "saddlebrown" , 'title': "Saddlebrown"},
  {'alias': "salmon" , 'title': "Salmon"},
  {'alias': "sandybrown" , 'title': "Sandybrown"},
  {'alias': "seagreen" , 'title': "Seagreen"},
  {'alias': "seashell" , 'title': "Seashell"},
  {'alias': "sienna" , 'title': "Sienna"},
  {'alias': "silver" , 'title': "Silver"},
  {'alias': "skyblue" , 'title': "Skyblue"},
  {'alias': "slateblue" , 'title': "Slateblue"},
  {'alias': "slategray" , 'title': "Slategray"},
  {'alias': "slategrey" , 'title': "Slategrey"},
  {'alias': "snow" , 'title': "Snow"},
  {'alias': "springgreen" , 'title': "Springgreen"},
  {'alias': "steelblue" , 'title': "Steelblue"},
  {'alias': "tan" , 'title': "Tan"},
  {'alias': "teal" , 'title': "Teal"},
  {'alias': "thistle" , 'title': "Thistle"},
  {'alias': "tomato" , 'title': "Tomato"},
  {'alias': "turquoise" , 'title': "Turquoise"},
  {'alias': "violet" , 'title': "Violet"},
  {'alias': "wheat" , 'title': "Wheat"},
  {'alias': "white" , 'title': "White"},
  {'alias': "whitesmoke" , 'title': "Whitesmoke"},
  {'alias': "yellow" , 'title': "Yellow"},
  {'alias': "yellowgreen" , 'title': "Yellowgreen"},
]
fonts = [
  {
    "family": "ABeeZee",
    "variants": [
    "regular",
    "italic"
    ],
    "subsets": [
    "latin",
    "latin-ext"
    ],
    "version": "v22",
    "lastModified": "2022-09-22",
    "files": {
    "regular": "http://fonts.gstatic.com/s/abeezee/v22/esDR31xSG-6AGleN6tKukbcHCpE.ttf",
    "italic": "http://fonts.gstatic.com/s/abeezee/v22/esDT31xSG-6AGleN2tCklZUCGpG-GQ.ttf"
    },
    "category": "sans-serif",
    "kind": "webfonts#webfont"
  },
  {
    "family": "Abel",
    "variants": [
    "regular"
    ],
    "subsets": [
    "latin"
    ],
    "version": "v18",
    "lastModified": "2022-09-22",
    "files": {
    "regular": "http://fonts.gstatic.com/s/abel/v18/MwQ5bhbm2POE6VhLPJp6qGI.ttf"
    },
    "category": "sans-serif",
    "kind": "webfonts#webfont"
  },
  {
  "family": "Abhaya Libre",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "sinhala"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/abhayalibre/v13/e3t5euGtX-Co5MNzeAOqinEYj2ryqtxI6oYtBA.ttf",
  "600": "http://fonts.gstatic.com/s/abhayalibre/v13/e3t5euGtX-Co5MNzeAOqinEYo23yqtxI6oYtBA.ttf",
  "700": "http://fonts.gstatic.com/s/abhayalibre/v13/e3t5euGtX-Co5MNzeAOqinEYx2zyqtxI6oYtBA.ttf",
  "800": "http://fonts.gstatic.com/s/abhayalibre/v13/e3t5euGtX-Co5MNzeAOqinEY22_yqtxI6oYtBA.ttf",
  "regular": "http://fonts.gstatic.com/s/abhayalibre/v13/e3tmeuGtX-Co5MNzeAOqinEge0PWovdU4w.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Aboreto",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/aboreto/v2/5DCXAKLhwDDQ4N8blKTeA2yuxSY.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Abril Fatface",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/abrilfatface/v19/zOL64pLDlL1D99S8g8PtiKchm-BsjOLhZBY.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Abyssinica SIL",
  "variants": [
  "regular"
  ],
  "subsets": [
  "ethiopic",
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/abyssinicasil/v1/oY1H8ezOqK7iI3rK_45WKoc8J6UZBFOVAXuI.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Aclonica",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/aclonica/v18/K2FyfZJVlfNNSEBXGb7TCI6oBjLz.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Acme",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/acme/v18/RrQfboBx-C5_bx3Lb23lzLk.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Actor",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/actor/v17/wEOzEBbCkc5cO3ekXygtUMIO.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Adamina",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-04-20",
  "files": {
  "regular": "http://fonts.gstatic.com/s/adamina/v21/j8_r6-DH1bjoc-dwu-reETl4Bno.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Advent Pro",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "greek",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/adventpro/v18/V8mCoQfxVT4Dvddr_yOwjVmtLZxcBtItFw.ttf",
  "200": "http://fonts.gstatic.com/s/adventpro/v18/V8mDoQfxVT4Dvddr_yOwjfWMDbZyCts0DqQ.ttf",
  "300": "http://fonts.gstatic.com/s/adventpro/v18/V8mDoQfxVT4Dvddr_yOwjZGPDbZyCts0DqQ.ttf",
  "500": "http://fonts.gstatic.com/s/adventpro/v18/V8mDoQfxVT4Dvddr_yOwjcmODbZyCts0DqQ.ttf",
  "600": "http://fonts.gstatic.com/s/adventpro/v18/V8mDoQfxVT4Dvddr_yOwjeWJDbZyCts0DqQ.ttf",
  "700": "http://fonts.gstatic.com/s/adventpro/v18/V8mDoQfxVT4Dvddr_yOwjYGIDbZyCts0DqQ.ttf",
  "regular": "http://fonts.gstatic.com/s/adventpro/v18/V8mAoQfxVT4Dvddr_yOwtT2nKb5ZFtI.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Aguafina Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/aguafinascript/v16/If2QXTv_ZzSxGIO30LemWEOmt1bHqs4pgicOrg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Akaya Kanadaka",
  "variants": [
  "regular"
  ],
  "subsets": [
  "kannada",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/akayakanadaka/v16/N0bM2S5CPO5oOQqvazoRRb-8-PfRS5VBBSSF.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Akaya Telivigala",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "telugu"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/akayatelivigala/v22/lJwc-oo_iG9wXqU3rCTD395tp0uifdLdsIH0YH8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Akronim",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/akronim/v23/fdN-9sqWtWZZlHRp-gBxkFYN-a8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Akshar",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/akshar/v5/Yq6I-LyHWTfz9rGoqDaUbHvhkAUsSSgFy9CY94XsnPc.ttf",
  "500": "http://fonts.gstatic.com/s/akshar/v5/Yq6I-LyHWTfz9rGoqDaUbHvhkAUsSUQFy9CY94XsnPc.ttf",
  "600": "http://fonts.gstatic.com/s/akshar/v5/Yq6I-LyHWTfz9rGoqDaUbHvhkAUsSagCy9CY94XsnPc.ttf",
  "700": "http://fonts.gstatic.com/s/akshar/v5/Yq6I-LyHWTfz9rGoqDaUbHvhkAUsSZECy9CY94XsnPc.ttf",
  "regular": "http://fonts.gstatic.com/s/akshar/v5/Yq6I-LyHWTfz9rGoqDaUbHvhkAUsSXYFy9CY94XsnPc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Aladin",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/aladin/v18/ZgNSjPJFPrvJV5f16Sf4pGT2Ng.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alata",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alata/v9/PbytFmztEwbIofe6xKcRQEOX.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alatsi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alatsi/v9/TK3iWkUJAxQ2nLNGHjUHte5fKg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Albert Sans",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/albertsans/v1/i7dZIFdwYjGaAMFtZd_QA3xXSKZqhr-TenSHq5L_rI32TxAj1g.ttf",
  "200": "http://fonts.gstatic.com/s/albertsans/v1/i7dZIFdwYjGaAMFtZd_QA3xXSKZqhr-TenSHK5P_rI32TxAj1g.ttf",
  "300": "http://fonts.gstatic.com/s/albertsans/v1/i7dZIFdwYjGaAMFtZd_QA3xXSKZqhr-TenSH9ZP_rI32TxAj1g.ttf",
  "500": "http://fonts.gstatic.com/s/albertsans/v1/i7dZIFdwYjGaAMFtZd_QA3xXSKZqhr-TenSHmZP_rI32TxAj1g.ttf",
  "600": "http://fonts.gstatic.com/s/albertsans/v1/i7dZIFdwYjGaAMFtZd_QA3xXSKZqhr-TenSHdZT_rI32TxAj1g.ttf",
  "700": "http://fonts.gstatic.com/s/albertsans/v1/i7dZIFdwYjGaAMFtZd_QA3xXSKZqhr-TenSHTJT_rI32TxAj1g.ttf",
  "800": "http://fonts.gstatic.com/s/albertsans/v1/i7dZIFdwYjGaAMFtZd_QA3xXSKZqhr-TenSHK5T_rI32TxAj1g.ttf",
  "900": "http://fonts.gstatic.com/s/albertsans/v1/i7dZIFdwYjGaAMFtZd_QA3xXSKZqhr-TenSHApT_rI32TxAj1g.ttf",
  "regular": "http://fonts.gstatic.com/s/albertsans/v1/i7dZIFdwYjGaAMFtZd_QA3xXSKZqhr-TenSHq5P_rI32TxAj1g.ttf",
  "100italic": "http://fonts.gstatic.com/s/albertsans/v1/i7dfIFdwYjGaAMFtZd_QA1Zeelmy79QJ1HOSY9AX7ofybRUz1r5t.ttf",
  "200italic": "http://fonts.gstatic.com/s/albertsans/v1/i7dfIFdwYjGaAMFtZd_QA1Zeelmy79QJ1HOSY9CX74fybRUz1r5t.ttf",
  "300italic": "http://fonts.gstatic.com/s/albertsans/v1/i7dfIFdwYjGaAMFtZd_QA1Zeelmy79QJ1HOSY9BJ74fybRUz1r5t.ttf",
  "italic": "http://fonts.gstatic.com/s/albertsans/v1/i7dfIFdwYjGaAMFtZd_QA1Zeelmy79QJ1HOSY9AX74fybRUz1r5t.ttf",
  "500italic": "http://fonts.gstatic.com/s/albertsans/v1/i7dfIFdwYjGaAMFtZd_QA1Zeelmy79QJ1HOSY9Al74fybRUz1r5t.ttf",
  "600italic": "http://fonts.gstatic.com/s/albertsans/v1/i7dfIFdwYjGaAMFtZd_QA1Zeelmy79QJ1HOSY9DJ6IfybRUz1r5t.ttf",
  "700italic": "http://fonts.gstatic.com/s/albertsans/v1/i7dfIFdwYjGaAMFtZd_QA1Zeelmy79QJ1HOSY9Dw6IfybRUz1r5t.ttf",
  "800italic": "http://fonts.gstatic.com/s/albertsans/v1/i7dfIFdwYjGaAMFtZd_QA1Zeelmy79QJ1HOSY9CX6IfybRUz1r5t.ttf",
  "900italic": "http://fonts.gstatic.com/s/albertsans/v1/i7dfIFdwYjGaAMFtZd_QA1Zeelmy79QJ1HOSY9C-6IfybRUz1r5t.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Aldrich",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/aldrich/v17/MCoTzAn-1s3IGyJMZaAS3pP5H_E.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alef",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "hebrew",
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/alef/v21/FeVQS0NQpLYglo50L5la2bxii28.ttf",
  "regular": "http://fonts.gstatic.com/s/alef/v21/FeVfS0NQpLYgrjJbC5FxxbU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alegreya",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v29",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/alegreya/v29/4UacrEBBsBhlBjvfkQjt71kZfyBzPgNGxBUI_KCisSGVrw.ttf",
  "600": "http://fonts.gstatic.com/s/alegreya/v29/4UacrEBBsBhlBjvfkQjt71kZfyBzPgNGKBII_KCisSGVrw.ttf",
  "700": "http://fonts.gstatic.com/s/alegreya/v29/4UacrEBBsBhlBjvfkQjt71kZfyBzPgNGERII_KCisSGVrw.ttf",
  "800": "http://fonts.gstatic.com/s/alegreya/v29/4UacrEBBsBhlBjvfkQjt71kZfyBzPgNGdhII_KCisSGVrw.ttf",
  "900": "http://fonts.gstatic.com/s/alegreya/v29/4UacrEBBsBhlBjvfkQjt71kZfyBzPgNGXxII_KCisSGVrw.ttf",
  "regular": "http://fonts.gstatic.com/s/alegreya/v29/4UacrEBBsBhlBjvfkQjt71kZfyBzPgNG9hUI_KCisSGVrw.ttf",
  "italic": "http://fonts.gstatic.com/s/alegreya/v29/4UaSrEBBsBhlBjvfkSLk3abBFkvpkARTPlbgv6qmkySFr9V9.ttf",
  "500italic": "http://fonts.gstatic.com/s/alegreya/v29/4UaSrEBBsBhlBjvfkSLk3abBFkvpkARTPlbSv6qmkySFr9V9.ttf",
  "600italic": "http://fonts.gstatic.com/s/alegreya/v29/4UaSrEBBsBhlBjvfkSLk3abBFkvpkARTPlY-uKqmkySFr9V9.ttf",
  "700italic": "http://fonts.gstatic.com/s/alegreya/v29/4UaSrEBBsBhlBjvfkSLk3abBFkvpkARTPlYHuKqmkySFr9V9.ttf",
  "800italic": "http://fonts.gstatic.com/s/alegreya/v29/4UaSrEBBsBhlBjvfkSLk3abBFkvpkARTPlZguKqmkySFr9V9.ttf",
  "900italic": "http://fonts.gstatic.com/s/alegreya/v29/4UaSrEBBsBhlBjvfkSLk3abBFkvpkARTPlZJuKqmkySFr9V9.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alegreya SC",
  "variants": [
  "regular",
  "italic",
  "500",
  "500italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/alegreyasc/v22/taiTGmRtCJ62-O0HhNEa-ZZc-rUxQqu2FXKD.ttf",
  "700": "http://fonts.gstatic.com/s/alegreyasc/v22/taiTGmRtCJ62-O0HhNEa-ZYU_LUxQqu2FXKD.ttf",
  "800": "http://fonts.gstatic.com/s/alegreyasc/v22/taiTGmRtCJ62-O0HhNEa-ZYI_7UxQqu2FXKD.ttf",
  "900": "http://fonts.gstatic.com/s/alegreyasc/v22/taiTGmRtCJ62-O0HhNEa-ZYs_rUxQqu2FXKD.ttf",
  "regular": "http://fonts.gstatic.com/s/alegreyasc/v22/taiOGmRtCJ62-O0HhNEa-a6o05E5abe_.ttf",
  "italic": "http://fonts.gstatic.com/s/alegreyasc/v22/taiMGmRtCJ62-O0HhNEa-Z6q2ZUbbKe_DGs.ttf",
  "500italic": "http://fonts.gstatic.com/s/alegreyasc/v22/taiRGmRtCJ62-O0HhNEa-Z6q4WEySK-UEGKDBz4.ttf",
  "700italic": "http://fonts.gstatic.com/s/alegreyasc/v22/taiRGmRtCJ62-O0HhNEa-Z6q4Sk0SK-UEGKDBz4.ttf",
  "800italic": "http://fonts.gstatic.com/s/alegreyasc/v22/taiRGmRtCJ62-O0HhNEa-Z6q4TU3SK-UEGKDBz4.ttf",
  "900italic": "http://fonts.gstatic.com/s/alegreyasc/v22/taiRGmRtCJ62-O0HhNEa-Z6q4RE2SK-UEGKDBz4.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alegreya Sans",
  "variants": [
  "100",
  "100italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUt9_-1phKLFgshYDvh6Vwt5TltuGdShm5bsg.ttf",
  "300": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUu9_-1phKLFgshYDvh6Vwt5fFPmE18imdCqxI.ttf",
  "500": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUu9_-1phKLFgshYDvh6Vwt5alOmE18imdCqxI.ttf",
  "700": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUu9_-1phKLFgshYDvh6Vwt5eFImE18imdCqxI.ttf",
  "800": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUu9_-1phKLFgshYDvh6Vwt5f1LmE18imdCqxI.ttf",
  "900": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUu9_-1phKLFgshYDvh6Vwt5dlKmE18imdCqxI.ttf",
  "100italic": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUv9_-1phKLFgshYDvh6Vwt7V9V3G1WpGtLsgu7.ttf",
  "300italic": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUo9_-1phKLFgshYDvh6Vwt7V9VFE92jkVHuxKiBA.ttf",
  "regular": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUz9_-1phKLFgshYDvh6Vwt3V1nvEVXlm4.ttf",
  "italic": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUt9_-1phKLFgshYDvh6Vwt7V9tuGdShm5bsg.ttf",
  "500italic": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUo9_-1phKLFgshYDvh6Vwt7V9VTE52jkVHuxKiBA.ttf",
  "700italic": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUo9_-1phKLFgshYDvh6Vwt7V9VBEh2jkVHuxKiBA.ttf",
  "800italic": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUo9_-1phKLFgshYDvh6Vwt7V9VGEt2jkVHuxKiBA.ttf",
  "900italic": "http://fonts.gstatic.com/s/alegreyasans/v21/5aUo9_-1phKLFgshYDvh6Vwt7V9VPEp2jkVHuxKiBA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alegreya Sans SC",
  "variants": [
  "100",
  "100italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGn4-RGJqfMvt7P8FUr0Q1j-Hf1Dipl8g5FPYtmMg.ttf",
  "300": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGm4-RGJqfMvt7P8FUr0Q1j-Hf1DuJH0iRrMYJ_K-4.ttf",
  "500": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGm4-RGJqfMvt7P8FUr0Q1j-Hf1DrpG0iRrMYJ_K-4.ttf",
  "700": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGm4-RGJqfMvt7P8FUr0Q1j-Hf1DvJA0iRrMYJ_K-4.ttf",
  "800": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGm4-RGJqfMvt7P8FUr0Q1j-Hf1Du5D0iRrMYJ_K-4.ttf",
  "900": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGm4-RGJqfMvt7P8FUr0Q1j-Hf1DspC0iRrMYJ_K-4.ttf",
  "100italic": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGl4-RGJqfMvt7P8FUr0Q1j-Hf1BkxdlgRBH452Mvds.ttf",
  "300italic": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGk4-RGJqfMvt7P8FUr0Q1j-Hf1BkxdXiZhNaB6O-51OA.ttf",
  "regular": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGh4-RGJqfMvt7P8FUr0Q1j-Hf1Nk5v9ixALYs.ttf",
  "italic": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGn4-RGJqfMvt7P8FUr0Q1j-Hf1Bkxl8g5FPYtmMg.ttf",
  "500italic": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGk4-RGJqfMvt7P8FUr0Q1j-Hf1BkxdBidhNaB6O-51OA.ttf",
  "700italic": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGk4-RGJqfMvt7P8FUr0Q1j-Hf1BkxdTiFhNaB6O-51OA.ttf",
  "800italic": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGk4-RGJqfMvt7P8FUr0Q1j-Hf1BkxdUiJhNaB6O-51OA.ttf",
  "900italic": "http://fonts.gstatic.com/s/alegreyasanssc/v20/mtGk4-RGJqfMvt7P8FUr0Q1j-Hf1BkxddiNhNaB6O-51OA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Aleo",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/aleo/v11/c4mg1nF8G8_syKbr9DVDno985KM.ttf",
  "700": "http://fonts.gstatic.com/s/aleo/v11/c4mg1nF8G8_syLbs9DVDno985KM.ttf",
  "300italic": "http://fonts.gstatic.com/s/aleo/v11/c4mi1nF8G8_swAjxeDdJmq159KOnWA.ttf",
  "regular": "http://fonts.gstatic.com/s/aleo/v11/c4mv1nF8G8_s8ArD0D1ogoY.ttf",
  "italic": "http://fonts.gstatic.com/s/aleo/v11/c4mh1nF8G8_swAjJ1B9tkoZl_Q.ttf",
  "700italic": "http://fonts.gstatic.com/s/aleo/v11/c4mi1nF8G8_swAjxaDBJmq159KOnWA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alex Brush",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alexbrush/v20/SZc83FzrJKuqFbwMKk6EtUL57DtOmCc.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alfa Slab One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alfaslabone/v17/6NUQ8FmMKwSEKjnm5-4v-4Jh6dVretWvYmE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alice",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alice/v20/OpNCnoEEmtHa6FcJpA_chzJ0.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alike",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-04-20",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alike/v20/HI_EiYEYI6BIoEjBSZXAQ4-d.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alike Angular",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-04-20",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alikeangular/v20/3qTrojWunjGQtEBlIcwMbSoI3kM6bB7FKjE.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alkalami",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alkalami/v1/zOL_4pfDmqRL95WXi5eLw8BMuvhH.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Allan",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/allan/v20/ea8aadU7WuTxEu5KEPCN2WpNgEKU.ttf",
  "regular": "http://fonts.gstatic.com/s/allan/v20/ea8XadU7WuTxEtb2P9SF8nZE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Allerta",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/allerta/v18/TwMO-IAHRlkbx940UnEdSQqO5uY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Allerta Stencil",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/allertastencil/v18/HTx0L209KT-LmIE9N7OR6eiycOeF-zz313DuvQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Allison",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/allison/v9/X7nl4b88AP2nkbvZOCaQ4MTgAgk.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Allura",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/allura/v18/9oRPNYsQpS4zjuAPjAIXPtrrGA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Almarai",
  "variants": [
  "300",
  "regular",
  "700",
  "800"
  ],
  "subsets": [
  "arabic"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/almarai/v12/tssoApxBaigK_hnnS_anhnicoq72sXg.ttf",
  "700": "http://fonts.gstatic.com/s/almarai/v12/tssoApxBaigK_hnnS-aghnicoq72sXg.ttf",
  "800": "http://fonts.gstatic.com/s/almarai/v12/tssoApxBaigK_hnnS_qjhnicoq72sXg.ttf",
  "regular": "http://fonts.gstatic.com/s/almarai/v12/tsstApxBaigK_hnnc1qPonC3vqc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Almendra",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/almendra/v22/H4cjBXKAlMnTn0Cskx6G7Zu4qKK-aihq.ttf",
  "regular": "http://fonts.gstatic.com/s/almendra/v22/H4ckBXKAlMnTn0CskyY6wr-wg763.ttf",
  "italic": "http://fonts.gstatic.com/s/almendra/v22/H4ciBXKAlMnTn0CskxY4yLuShq63czE.ttf",
  "700italic": "http://fonts.gstatic.com/s/almendra/v22/H4chBXKAlMnTn0CskxY48Ae9oqacbzhqDtg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Almendra Display",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v25",
  "lastModified": "2022-04-20",
  "files": {
  "regular": "http://fonts.gstatic.com/s/almendradisplay/v25/0FlPVOGWl1Sb4O3tETtADHRRlZhzXS_eTyer338.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Almendra SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/almendrasc/v25/Iure6Yx284eebowr7hbyTZZJprVA4XQ0.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alumni Sans",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/alumnisans/v12/nwpHtKqkOwdO2aOIwhWudEWpx_zq_Xna-Xd9OO5QqFsJ3C8qng.ttf",
  "200": "http://fonts.gstatic.com/s/alumnisans/v12/nwpHtKqkOwdO2aOIwhWudEWpx_zq_Xna-Xd9uO9QqFsJ3C8qng.ttf",
  "300": "http://fonts.gstatic.com/s/alumnisans/v12/nwpHtKqkOwdO2aOIwhWudEWpx_zq_Xna-Xd9Zu9QqFsJ3C8qng.ttf",
  "500": "http://fonts.gstatic.com/s/alumnisans/v12/nwpHtKqkOwdO2aOIwhWudEWpx_zq_Xna-Xd9Cu9QqFsJ3C8qng.ttf",
  "600": "http://fonts.gstatic.com/s/alumnisans/v12/nwpHtKqkOwdO2aOIwhWudEWpx_zq_Xna-Xd95uhQqFsJ3C8qng.ttf",
  "700": "http://fonts.gstatic.com/s/alumnisans/v12/nwpHtKqkOwdO2aOIwhWudEWpx_zq_Xna-Xd93-hQqFsJ3C8qng.ttf",
  "800": "http://fonts.gstatic.com/s/alumnisans/v12/nwpHtKqkOwdO2aOIwhWudEWpx_zq_Xna-Xd9uOhQqFsJ3C8qng.ttf",
  "900": "http://fonts.gstatic.com/s/alumnisans/v12/nwpHtKqkOwdO2aOIwhWudEWpx_zq_Xna-Xd9kehQqFsJ3C8qng.ttf",
  "regular": "http://fonts.gstatic.com/s/alumnisans/v12/nwpHtKqkOwdO2aOIwhWudEWpx_zq_Xna-Xd9OO9QqFsJ3C8qng.ttf",
  "100italic": "http://fonts.gstatic.com/s/alumnisans/v12/nwpBtKqkOwdO2aOIwhWudG-g9QMylBJAV3Bo8Ky46lEN_io6npfB.ttf",
  "200italic": "http://fonts.gstatic.com/s/alumnisans/v12/nwpBtKqkOwdO2aOIwhWudG-g9QMylBJAV3Bo8Kw461EN_io6npfB.ttf",
  "300italic": "http://fonts.gstatic.com/s/alumnisans/v12/nwpBtKqkOwdO2aOIwhWudG-g9QMylBJAV3Bo8Kzm61EN_io6npfB.ttf",
  "italic": "http://fonts.gstatic.com/s/alumnisans/v12/nwpBtKqkOwdO2aOIwhWudG-g9QMylBJAV3Bo8Ky461EN_io6npfB.ttf",
  "500italic": "http://fonts.gstatic.com/s/alumnisans/v12/nwpBtKqkOwdO2aOIwhWudG-g9QMylBJAV3Bo8KyK61EN_io6npfB.ttf",
  "600italic": "http://fonts.gstatic.com/s/alumnisans/v12/nwpBtKqkOwdO2aOIwhWudG-g9QMylBJAV3Bo8Kxm7FEN_io6npfB.ttf",
  "700italic": "http://fonts.gstatic.com/s/alumnisans/v12/nwpBtKqkOwdO2aOIwhWudG-g9QMylBJAV3Bo8Kxf7FEN_io6npfB.ttf",
  "800italic": "http://fonts.gstatic.com/s/alumnisans/v12/nwpBtKqkOwdO2aOIwhWudG-g9QMylBJAV3Bo8Kw47FEN_io6npfB.ttf",
  "900italic": "http://fonts.gstatic.com/s/alumnisans/v12/nwpBtKqkOwdO2aOIwhWudG-g9QMylBJAV3Bo8KwR7FEN_io6npfB.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alumni Sans Collegiate One",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alumnisanscollegiateone/v2/MQpB-XChK8G5CtmK_AuGxQrdNvPSXkn0RM-XqjWWhjdayDiPw2ta.ttf",
  "italic": "http://fonts.gstatic.com/s/alumnisanscollegiateone/v2/MQpD-XChK8G5CtmK_AuGxQrdNvPSXkn0RM-XqjWWhgdYwjytxntaDFU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alumni Sans Inline One",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alumnisansinlineone/v2/RrQBbpJx9zZ3IXTBOASKp5gJAetBdaihcjbpD3AZcr7xbYw.ttf",
  "italic": "http://fonts.gstatic.com/s/alumnisansinlineone/v2/RrQDbpJx9zZ3IXTBOASKp5gJAetBdaihcjbpP3ITdpz0fYxcrQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Alumni Sans Pinstripe",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/alumnisanspinstripe/v1/ZgNNjOFFPq_AUJD1umyS30W-Xub8zD1ObhezYrVIpcDA5w.ttf",
  "italic": "http://fonts.gstatic.com/s/alumnisanspinstripe/v1/ZgNDjOFFPq_AUJD1umyS30W-Xub8zD1ObheDYL9Mh8XQ5_cY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Amarante",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/amarante/v22/xMQXuF1KTa6EvGx9bq-3C3rAmD-b.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Amaranth",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/amaranth/v18/KtkpALODe433f0j1zMF-OPWi6WDfFpuc.ttf",
  "regular": "http://fonts.gstatic.com/s/amaranth/v18/KtkuALODe433f0j1zPnCF9GqwnzW.ttf",
  "italic": "http://fonts.gstatic.com/s/amaranth/v18/KtkoALODe433f0j1zMnAHdWIx2zWD4I.ttf",
  "700italic": "http://fonts.gstatic.com/s/amaranth/v18/KtkrALODe433f0j1zMnAJWmn42T9E4ucRY8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Amatic SC",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "hebrew",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/amaticsc/v24/TUZ3zwprpvBS1izr_vOMscG6eb8D3WTy-A.ttf",
  "regular": "http://fonts.gstatic.com/s/amaticsc/v24/TUZyzwprpvBS1izr_vO0De6ecZQf1A.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Amethysta",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-04-20",
  "files": {
  "regular": "http://fonts.gstatic.com/s/amethysta/v16/rP2Fp2K15kgb_F3ibfWIGDWCBl0O8Q.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Amiko",
  "variants": [
  "regular",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "600": "http://fonts.gstatic.com/s/amiko/v12/WwkdxPq1DFK04uJ9XXrEGoQAUco5.ttf",
  "700": "http://fonts.gstatic.com/s/amiko/v12/WwkdxPq1DFK04uIZXHrEGoQAUco5.ttf",
  "regular": "http://fonts.gstatic.com/s/amiko/v12/WwkQxPq1DFK04tqlc17MMZgJ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Amiri",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/amiri/v24/J7acnpd8CGxBHp2VkZY4xJ9CGyAa.ttf",
  "regular": "http://fonts.gstatic.com/s/amiri/v24/J7aRnpd8CGxBHqUpvrIw74NL.ttf",
  "italic": "http://fonts.gstatic.com/s/amiri/v24/J7afnpd8CGxBHpUrtLYS6pNLAjk.ttf",
  "700italic": "http://fonts.gstatic.com/s/amiri/v24/J7aanpd8CGxBHpUrjAo9zptgHjAavCA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Amiri Quran",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin"
  ],
  "version": "v7",
  "lastModified": "2022-09-14",
  "files": {
  "regular": "http://fonts.gstatic.com/s/amiriquran/v7/_Xmo-Hk0rD6DbUL4_vH8Zq5t7Cycsu-2.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Amita",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/amita/v16/HhyXU5si9Om7PTHTLtCCOopCTKkI.ttf",
  "regular": "http://fonts.gstatic.com/s/amita/v16/HhyaU5si9Om7PQlvAfSKEZZL.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anaheim",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/anaheim/v14/8vII7w042Wp87g4G0UTUEE5eK_w.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Andada Pro",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/andadapro/v12/HhyEU5Qi9-SuOEhPe4LtKoVCuWGURPcg3DP7BY8cFLzvIt2S.ttf",
  "600": "http://fonts.gstatic.com/s/andadapro/v12/HhyEU5Qi9-SuOEhPe4LtKoVCuWGURPcg3DMXAo8cFLzvIt2S.ttf",
  "700": "http://fonts.gstatic.com/s/andadapro/v12/HhyEU5Qi9-SuOEhPe4LtKoVCuWGURPcg3DMuAo8cFLzvIt2S.ttf",
  "800": "http://fonts.gstatic.com/s/andadapro/v12/HhyEU5Qi9-SuOEhPe4LtKoVCuWGURPcg3DNJAo8cFLzvIt2S.ttf",
  "regular": "http://fonts.gstatic.com/s/andadapro/v12/HhyEU5Qi9-SuOEhPe4LtKoVCuWGURPcg3DPJBY8cFLzvIt2S.ttf",
  "italic": "http://fonts.gstatic.com/s/andadapro/v12/HhyGU5Qi9-SuOEhPe4LtAIxwRrn9L22O2yYBRmdfHrjNJ82Stjw.ttf",
  "500italic": "http://fonts.gstatic.com/s/andadapro/v12/HhyGU5Qi9-SuOEhPe4LtAIxwRrn9L22O2yYBRlVfHrjNJ82Stjw.ttf",
  "600italic": "http://fonts.gstatic.com/s/andadapro/v12/HhyGU5Qi9-SuOEhPe4LtAIxwRrn9L22O2yYBRrlYHrjNJ82Stjw.ttf",
  "700italic": "http://fonts.gstatic.com/s/andadapro/v12/HhyGU5Qi9-SuOEhPe4LtAIxwRrn9L22O2yYBRoBYHrjNJ82Stjw.ttf",
  "800italic": "http://fonts.gstatic.com/s/andadapro/v12/HhyGU5Qi9-SuOEhPe4LtAIxwRrn9L22O2yYBRudYHrjNJ82Stjw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Andika",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/andika/v22/mem8Ya6iyW-Lwqg40ZM1UpcaXcl0Aw.ttf",
  "regular": "http://fonts.gstatic.com/s/andika/v22/mem_Ya6iyW-LwqgAbbwRWrwGVA.ttf",
  "italic": "http://fonts.gstatic.com/s/andika/v22/mem9Ya6iyW-Lwqgwb7YVeLkWVNBt.ttf",
  "700italic": "http://fonts.gstatic.com/s/andika/v22/mem6Ya6iyW-Lwqgwb46pV50ef8xkA76a.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anek Bangla",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "bengali",
  "latin",
  "latin-ext"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/anekbangla/v4/_gPW1R38qTExHg-17BhM6n66QhabMYB0fBKONtHhRSIUIre5mq3Ofm9YIocg56yyvt0.ttf",
  "200": "http://fonts.gstatic.com/s/anekbangla/v4/_gPW1R38qTExHg-17BhM6n66QhabMYB0fBKONtHhRSIUIre5mq3Ofu9ZIocg56yyvt0.ttf",
  "300": "http://fonts.gstatic.com/s/anekbangla/v4/_gPW1R38qTExHg-17BhM6n66QhabMYB0fBKONtHhRSIUIre5mq3OfjFZIocg56yyvt0.ttf",
  "500": "http://fonts.gstatic.com/s/anekbangla/v4/_gPW1R38qTExHg-17BhM6n66QhabMYB0fBKONtHhRSIUIre5mq3Ofl1ZIocg56yyvt0.ttf",
  "600": "http://fonts.gstatic.com/s/anekbangla/v4/_gPW1R38qTExHg-17BhM6n66QhabMYB0fBKONtHhRSIUIre5mq3OfrFeIocg56yyvt0.ttf",
  "700": "http://fonts.gstatic.com/s/anekbangla/v4/_gPW1R38qTExHg-17BhM6n66QhabMYB0fBKONtHhRSIUIre5mq3OfoheIocg56yyvt0.ttf",
  "800": "http://fonts.gstatic.com/s/anekbangla/v4/_gPW1R38qTExHg-17BhM6n66QhabMYB0fBKONtHhRSIUIre5mq3Ofu9eIocg56yyvt0.ttf",
  "regular": "http://fonts.gstatic.com/s/anekbangla/v4/_gPW1R38qTExHg-17BhM6n66QhabMYB0fBKONtHhRSIUIre5mq3Ofm9ZIocg56yyvt0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anek Devanagari",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/anekdevanagari/v4/jVyo7nP0CGrUsxB-QiRgw0NlLaVt_QUAkYxLRoCL23mlh20ZVHOMAWbgHLDtk-9nFk0LjZ7E.ttf",
  "200": "http://fonts.gstatic.com/s/anekdevanagari/v4/jVyo7nP0CGrUsxB-QiRgw0NlLaVt_QUAkYxLRoCL23mlh20ZVHOMAWbgHLBtku9nFk0LjZ7E.ttf",
  "300": "http://fonts.gstatic.com/s/anekdevanagari/v4/jVyo7nP0CGrUsxB-QiRgw0NlLaVt_QUAkYxLRoCL23mlh20ZVHOMAWbgHLCzku9nFk0LjZ7E.ttf",
  "500": "http://fonts.gstatic.com/s/anekdevanagari/v4/jVyo7nP0CGrUsxB-QiRgw0NlLaVt_QUAkYxLRoCL23mlh20ZVHOMAWbgHLDfku9nFk0LjZ7E.ttf",
  "600": "http://fonts.gstatic.com/s/anekdevanagari/v4/jVyo7nP0CGrUsxB-QiRgw0NlLaVt_QUAkYxLRoCL23mlh20ZVHOMAWbgHLAzle9nFk0LjZ7E.ttf",
  "700": "http://fonts.gstatic.com/s/anekdevanagari/v4/jVyo7nP0CGrUsxB-QiRgw0NlLaVt_QUAkYxLRoCL23mlh20ZVHOMAWbgHLAKle9nFk0LjZ7E.ttf",
  "800": "http://fonts.gstatic.com/s/anekdevanagari/v4/jVyo7nP0CGrUsxB-QiRgw0NlLaVt_QUAkYxLRoCL23mlh20ZVHOMAWbgHLBtle9nFk0LjZ7E.ttf",
  "regular": "http://fonts.gstatic.com/s/anekdevanagari/v4/jVyo7nP0CGrUsxB-QiRgw0NlLaVt_QUAkYxLRoCL23mlh20ZVHOMAWbgHLDtku9nFk0LjZ7E.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anek Gujarati",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/anekgujarati/v4/l7g_bj5oysqknvkCo2T_8FuiIRBA7lncQUmbIBEtPKiYYQhRwyBxCD-0F5G7w0KgB7Lm7g.ttf",
  "200": "http://fonts.gstatic.com/s/anekgujarati/v4/l7g_bj5oysqknvkCo2T_8FuiIRBA7lncQUmbIBEtPKiYYQhRwyBxCD-0l5C7w0KgB7Lm7g.ttf",
  "300": "http://fonts.gstatic.com/s/anekgujarati/v4/l7g_bj5oysqknvkCo2T_8FuiIRBA7lncQUmbIBEtPKiYYQhRwyBxCD-0SZC7w0KgB7Lm7g.ttf",
  "500": "http://fonts.gstatic.com/s/anekgujarati/v4/l7g_bj5oysqknvkCo2T_8FuiIRBA7lncQUmbIBEtPKiYYQhRwyBxCD-0JZC7w0KgB7Lm7g.ttf",
  "600": "http://fonts.gstatic.com/s/anekgujarati/v4/l7g_bj5oysqknvkCo2T_8FuiIRBA7lncQUmbIBEtPKiYYQhRwyBxCD-0yZe7w0KgB7Lm7g.ttf",
  "700": "http://fonts.gstatic.com/s/anekgujarati/v4/l7g_bj5oysqknvkCo2T_8FuiIRBA7lncQUmbIBEtPKiYYQhRwyBxCD-08Je7w0KgB7Lm7g.ttf",
  "800": "http://fonts.gstatic.com/s/anekgujarati/v4/l7g_bj5oysqknvkCo2T_8FuiIRBA7lncQUmbIBEtPKiYYQhRwyBxCD-0l5e7w0KgB7Lm7g.ttf",
  "regular": "http://fonts.gstatic.com/s/anekgujarati/v4/l7g_bj5oysqknvkCo2T_8FuiIRBA7lncQUmbIBEtPKiYYQhRwyBxCD-0F5C7w0KgB7Lm7g.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anek Gurmukhi",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "gurmukhi",
  "latin",
  "latin-ext"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/anekgurmukhi/v4/0QIAMXRO_YSkA0quVLY79JnHybfeEOrXCa9Dmd9Ql6a6R_vEMc5TaLkbd5ppXK41H6DjbA.ttf",
  "200": "http://fonts.gstatic.com/s/anekgurmukhi/v4/0QIAMXRO_YSkA0quVLY79JnHybfeEOrXCa9Dmd9Ql6a6R_vEMc5TaLkb95tpXK41H6DjbA.ttf",
  "300": "http://fonts.gstatic.com/s/anekgurmukhi/v4/0QIAMXRO_YSkA0quVLY79JnHybfeEOrXCa9Dmd9Ql6a6R_vEMc5TaLkbKZtpXK41H6DjbA.ttf",
  "500": "http://fonts.gstatic.com/s/anekgurmukhi/v4/0QIAMXRO_YSkA0quVLY79JnHybfeEOrXCa9Dmd9Ql6a6R_vEMc5TaLkbRZtpXK41H6DjbA.ttf",
  "600": "http://fonts.gstatic.com/s/anekgurmukhi/v4/0QIAMXRO_YSkA0quVLY79JnHybfeEOrXCa9Dmd9Ql6a6R_vEMc5TaLkbqZxpXK41H6DjbA.ttf",
  "700": "http://fonts.gstatic.com/s/anekgurmukhi/v4/0QIAMXRO_YSkA0quVLY79JnHybfeEOrXCa9Dmd9Ql6a6R_vEMc5TaLkbkJxpXK41H6DjbA.ttf",
  "800": "http://fonts.gstatic.com/s/anekgurmukhi/v4/0QIAMXRO_YSkA0quVLY79JnHybfeEOrXCa9Dmd9Ql6a6R_vEMc5TaLkb95xpXK41H6DjbA.ttf",
  "regular": "http://fonts.gstatic.com/s/anekgurmukhi/v4/0QIAMXRO_YSkA0quVLY79JnHybfeEOrXCa9Dmd9Ql6a6R_vEMc5TaLkbd5tpXK41H6DjbA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anek Kannada",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "kannada",
  "latin",
  "latin-ext"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/anekkannada/v4/raxcHiCNvNMKe1CKFsINYFlgkEIwGa8nL6ruWJg1j--h8pvBKSiw4dFDEAukVReA1oef.ttf",
  "200": "http://fonts.gstatic.com/s/anekkannada/v4/raxcHiCNvNMKe1CKFsINYFlgkEIwGa8nL6ruWJg1j--h8pvBKSiw4dHDEQukVReA1oef.ttf",
  "300": "http://fonts.gstatic.com/s/anekkannada/v4/raxcHiCNvNMKe1CKFsINYFlgkEIwGa8nL6ruWJg1j--h8pvBKSiw4dEdEQukVReA1oef.ttf",
  "500": "http://fonts.gstatic.com/s/anekkannada/v4/raxcHiCNvNMKe1CKFsINYFlgkEIwGa8nL6ruWJg1j--h8pvBKSiw4dFxEQukVReA1oef.ttf",
  "600": "http://fonts.gstatic.com/s/anekkannada/v4/raxcHiCNvNMKe1CKFsINYFlgkEIwGa8nL6ruWJg1j--h8pvBKSiw4dGdFgukVReA1oef.ttf",
  "700": "http://fonts.gstatic.com/s/anekkannada/v4/raxcHiCNvNMKe1CKFsINYFlgkEIwGa8nL6ruWJg1j--h8pvBKSiw4dGkFgukVReA1oef.ttf",
  "800": "http://fonts.gstatic.com/s/anekkannada/v4/raxcHiCNvNMKe1CKFsINYFlgkEIwGa8nL6ruWJg1j--h8pvBKSiw4dHDFgukVReA1oef.ttf",
  "regular": "http://fonts.gstatic.com/s/anekkannada/v4/raxcHiCNvNMKe1CKFsINYFlgkEIwGa8nL6ruWJg1j--h8pvBKSiw4dFDEQukVReA1oef.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anek Latin",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/aneklatin/v4/co3pmWZulTRoU4a8dqrWiajBS5ByUkvdrluH-xWG5uJTY4x-L3PuR7EZKdClWL3kgw.ttf",
  "200": "http://fonts.gstatic.com/s/aneklatin/v4/co3pmWZulTRoU4a8dqrWiajBS5ByUkvdrluH-xWG5uJTY4x-L3Pux7AZKdClWL3kgw.ttf",
  "300": "http://fonts.gstatic.com/s/aneklatin/v4/co3pmWZulTRoU4a8dqrWiajBS5ByUkvdrluH-xWG5uJTY4x-L3PuGbAZKdClWL3kgw.ttf",
  "500": "http://fonts.gstatic.com/s/aneklatin/v4/co3pmWZulTRoU4a8dqrWiajBS5ByUkvdrluH-xWG5uJTY4x-L3PudbAZKdClWL3kgw.ttf",
  "600": "http://fonts.gstatic.com/s/aneklatin/v4/co3pmWZulTRoU4a8dqrWiajBS5ByUkvdrluH-xWG5uJTY4x-L3PumbcZKdClWL3kgw.ttf",
  "700": "http://fonts.gstatic.com/s/aneklatin/v4/co3pmWZulTRoU4a8dqrWiajBS5ByUkvdrluH-xWG5uJTY4x-L3PuoLcZKdClWL3kgw.ttf",
  "800": "http://fonts.gstatic.com/s/aneklatin/v4/co3pmWZulTRoU4a8dqrWiajBS5ByUkvdrluH-xWG5uJTY4x-L3Pux7cZKdClWL3kgw.ttf",
  "regular": "http://fonts.gstatic.com/s/aneklatin/v4/co3pmWZulTRoU4a8dqrWiajBS5ByUkvdrluH-xWG5uJTY4x-L3PuR7AZKdClWL3kgw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anek Malayalam",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "malayalam"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/anekmalayalam/v4/6qLjKZActRTs_mZAJUZWWkhke0nYa_vC8_Azq3-gP1SReZeOtqQuDVUTUZu_HMr5PDO71Qs.ttf",
  "200": "http://fonts.gstatic.com/s/anekmalayalam/v4/6qLjKZActRTs_mZAJUZWWkhke0nYa_vC8_Azq3-gP1SReZeOtqQuDVUTURu-HMr5PDO71Qs.ttf",
  "300": "http://fonts.gstatic.com/s/anekmalayalam/v4/6qLjKZActRTs_mZAJUZWWkhke0nYa_vC8_Azq3-gP1SReZeOtqQuDVUTUcW-HMr5PDO71Qs.ttf",
  "500": "http://fonts.gstatic.com/s/anekmalayalam/v4/6qLjKZActRTs_mZAJUZWWkhke0nYa_vC8_Azq3-gP1SReZeOtqQuDVUTUam-HMr5PDO71Qs.ttf",
  "600": "http://fonts.gstatic.com/s/anekmalayalam/v4/6qLjKZActRTs_mZAJUZWWkhke0nYa_vC8_Azq3-gP1SReZeOtqQuDVUTUUW5HMr5PDO71Qs.ttf",
  "700": "http://fonts.gstatic.com/s/anekmalayalam/v4/6qLjKZActRTs_mZAJUZWWkhke0nYa_vC8_Azq3-gP1SReZeOtqQuDVUTUXy5HMr5PDO71Qs.ttf",
  "800": "http://fonts.gstatic.com/s/anekmalayalam/v4/6qLjKZActRTs_mZAJUZWWkhke0nYa_vC8_Azq3-gP1SReZeOtqQuDVUTURu5HMr5PDO71Qs.ttf",
  "regular": "http://fonts.gstatic.com/s/anekmalayalam/v4/6qLjKZActRTs_mZAJUZWWkhke0nYa_vC8_Azq3-gP1SReZeOtqQuDVUTUZu-HMr5PDO71Qs.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anek Odia",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "oriya"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/anekodia/v4/TK3PWkoJARApz5UCd345tuevwwQX0CwsoYkAWgWYevAauivBUnmZf63mXZAtm_es.ttf",
  "200": "http://fonts.gstatic.com/s/anekodia/v4/TK3PWkoJARApz5UCd345tuevwwQX0CwsoYkAWgWYevAauivBUnkZfq3mXZAtm_es.ttf",
  "300": "http://fonts.gstatic.com/s/anekodia/v4/TK3PWkoJARApz5UCd345tuevwwQX0CwsoYkAWgWYevAauivBUnnHfq3mXZAtm_es.ttf",
  "500": "http://fonts.gstatic.com/s/anekodia/v4/TK3PWkoJARApz5UCd345tuevwwQX0CwsoYkAWgWYevAauivBUnmrfq3mXZAtm_es.ttf",
  "600": "http://fonts.gstatic.com/s/anekodia/v4/TK3PWkoJARApz5UCd345tuevwwQX0CwsoYkAWgWYevAauivBUnlHea3mXZAtm_es.ttf",
  "700": "http://fonts.gstatic.com/s/anekodia/v4/TK3PWkoJARApz5UCd345tuevwwQX0CwsoYkAWgWYevAauivBUnl-ea3mXZAtm_es.ttf",
  "800": "http://fonts.gstatic.com/s/anekodia/v4/TK3PWkoJARApz5UCd345tuevwwQX0CwsoYkAWgWYevAauivBUnkZea3mXZAtm_es.ttf",
  "regular": "http://fonts.gstatic.com/s/anekodia/v4/TK3PWkoJARApz5UCd345tuevwwQX0CwsoYkAWgWYevAauivBUnmZfq3mXZAtm_es.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anek Tamil",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/anektamil/v4/XLYJIZH2bYJHGYtPGSbUB8JKTp-_9n55SsLHW0WZez6TjtkDu3uNQiZ6q4v4oegjOQ.ttf",
  "200": "http://fonts.gstatic.com/s/anektamil/v4/XLYJIZH2bYJHGYtPGSbUB8JKTp-_9n55SsLHW0WZez6TjtkDu3uNwid6q4v4oegjOQ.ttf",
  "300": "http://fonts.gstatic.com/s/anektamil/v4/XLYJIZH2bYJHGYtPGSbUB8JKTp-_9n55SsLHW0WZez6TjtkDu3uNHCd6q4v4oegjOQ.ttf",
  "500": "http://fonts.gstatic.com/s/anektamil/v4/XLYJIZH2bYJHGYtPGSbUB8JKTp-_9n55SsLHW0WZez6TjtkDu3uNcCd6q4v4oegjOQ.ttf",
  "600": "http://fonts.gstatic.com/s/anektamil/v4/XLYJIZH2bYJHGYtPGSbUB8JKTp-_9n55SsLHW0WZez6TjtkDu3uNnCB6q4v4oegjOQ.ttf",
  "700": "http://fonts.gstatic.com/s/anektamil/v4/XLYJIZH2bYJHGYtPGSbUB8JKTp-_9n55SsLHW0WZez6TjtkDu3uNpSB6q4v4oegjOQ.ttf",
  "800": "http://fonts.gstatic.com/s/anektamil/v4/XLYJIZH2bYJHGYtPGSbUB8JKTp-_9n55SsLHW0WZez6TjtkDu3uNwiB6q4v4oegjOQ.ttf",
  "regular": "http://fonts.gstatic.com/s/anektamil/v4/XLYJIZH2bYJHGYtPGSbUB8JKTp-_9n55SsLHW0WZez6TjtkDu3uNQid6q4v4oegjOQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anek Telugu",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "telugu"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/anektelugu/v4/LhWLMVrUNvsddMtYGCx4FcVWOjlwE1WgXdoJ-5XHMl2DkooGK7i13y-_oE2G2ep10_8.ttf",
  "200": "http://fonts.gstatic.com/s/anektelugu/v4/LhWLMVrUNvsddMtYGCx4FcVWOjlwE1WgXdoJ-5XHMl2DkooGK7i136--oE2G2ep10_8.ttf",
  "300": "http://fonts.gstatic.com/s/anektelugu/v4/LhWLMVrUNvsddMtYGCx4FcVWOjlwE1WgXdoJ-5XHMl2DkooGK7i133G-oE2G2ep10_8.ttf",
  "500": "http://fonts.gstatic.com/s/anektelugu/v4/LhWLMVrUNvsddMtYGCx4FcVWOjlwE1WgXdoJ-5XHMl2DkooGK7i13x2-oE2G2ep10_8.ttf",
  "600": "http://fonts.gstatic.com/s/anektelugu/v4/LhWLMVrUNvsddMtYGCx4FcVWOjlwE1WgXdoJ-5XHMl2DkooGK7i13_G5oE2G2ep10_8.ttf",
  "700": "http://fonts.gstatic.com/s/anektelugu/v4/LhWLMVrUNvsddMtYGCx4FcVWOjlwE1WgXdoJ-5XHMl2DkooGK7i138i5oE2G2ep10_8.ttf",
  "800": "http://fonts.gstatic.com/s/anektelugu/v4/LhWLMVrUNvsddMtYGCx4FcVWOjlwE1WgXdoJ-5XHMl2DkooGK7i136-5oE2G2ep10_8.ttf",
  "regular": "http://fonts.gstatic.com/s/anektelugu/v4/LhWLMVrUNvsddMtYGCx4FcVWOjlwE1WgXdoJ-5XHMl2DkooGK7i13y--oE2G2ep10_8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Angkor",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v28",
  "lastModified": "2022-04-20",
  "files": {
  "regular": "http://fonts.gstatic.com/s/angkor/v28/H4cmBXyAlsPdnlb-8iw-4Lqggw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Annie Use Your Telescope",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/annieuseyourtelescope/v18/daaLSS4tI2qYYl3Jq9s_Hu74xwktnlKxH6osGVGjlDfB3UUVZA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anonymous Pro",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "greek",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/anonymouspro/v21/rP2cp2a15UIB7Un-bOeISG3pFuAT0CnW7KOywKo.ttf",
  "regular": "http://fonts.gstatic.com/s/anonymouspro/v21/rP2Bp2a15UIB7Un-bOeISG3pLlw89CH98Ko.ttf",
  "italic": "http://fonts.gstatic.com/s/anonymouspro/v21/rP2fp2a15UIB7Un-bOeISG3pHl428AP44Kqr2Q.ttf",
  "700italic": "http://fonts.gstatic.com/s/anonymouspro/v21/rP2ap2a15UIB7Un-bOeISG3pHl4OTCzc6IG30KqB9Q.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Antic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/antic/v19/TuGfUVB8XY5DRaZLodgzydtk.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Antic Didone",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/anticdidone/v16/RWmPoKKX6u8sp8fIWdnDKqDiqYsGBGBzCw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Antic Slab",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/anticslab/v16/bWt97fPFfRzkCa9Jlp6IWcJWXW5p5Qo.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anton",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/anton/v23/1Ptgg87LROyAm0K08i4gS7lu.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Antonio",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/antonio/v11/gNMbW3NwSYq_9WD34ngK5F8vR8T0PVxx8BtIY2DwSXlM.ttf",
  "200": "http://fonts.gstatic.com/s/antonio/v11/gNMbW3NwSYq_9WD34ngK5F8vR8T0PVzx8RtIY2DwSXlM.ttf",
  "300": "http://fonts.gstatic.com/s/antonio/v11/gNMbW3NwSYq_9WD34ngK5F8vR8T0PVwv8RtIY2DwSXlM.ttf",
  "500": "http://fonts.gstatic.com/s/antonio/v11/gNMbW3NwSYq_9WD34ngK5F8vR8T0PVxD8RtIY2DwSXlM.ttf",
  "600": "http://fonts.gstatic.com/s/antonio/v11/gNMbW3NwSYq_9WD34ngK5F8vR8T0PVyv9htIY2DwSXlM.ttf",
  "700": "http://fonts.gstatic.com/s/antonio/v11/gNMbW3NwSYq_9WD34ngK5F8vR8T0PVyW9htIY2DwSXlM.ttf",
  "regular": "http://fonts.gstatic.com/s/antonio/v11/gNMbW3NwSYq_9WD34ngK5F8vR8T0PVxx8RtIY2DwSXlM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Anybody",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/anybody/v4/VuJbdNvK2Ib2ppdWYq311GH32hxIv0sd5grncSUi2F_Wim4J12HPrsXD_nBPpQ.ttf",
  "200": "http://fonts.gstatic.com/s/anybody/v4/VuJbdNvK2Ib2ppdWYq311GH32hxIv0sd5grncSUi2F_Wim4JV2DPrsXD_nBPpQ.ttf",
  "300": "http://fonts.gstatic.com/s/anybody/v4/VuJbdNvK2Ib2ppdWYq311GH32hxIv0sd5grncSUi2F_Wim4JiWDPrsXD_nBPpQ.ttf",
  "500": "http://fonts.gstatic.com/s/anybody/v4/VuJbdNvK2Ib2ppdWYq311GH32hxIv0sd5grncSUi2F_Wim4J5WDPrsXD_nBPpQ.ttf",
  "600": "http://fonts.gstatic.com/s/anybody/v4/VuJbdNvK2Ib2ppdWYq311GH32hxIv0sd5grncSUi2F_Wim4JCWfPrsXD_nBPpQ.ttf",
  "700": "http://fonts.gstatic.com/s/anybody/v4/VuJbdNvK2Ib2ppdWYq311GH32hxIv0sd5grncSUi2F_Wim4JMGfPrsXD_nBPpQ.ttf",
  "800": "http://fonts.gstatic.com/s/anybody/v4/VuJbdNvK2Ib2ppdWYq311GH32hxIv0sd5grncSUi2F_Wim4JV2fPrsXD_nBPpQ.ttf",
  "900": "http://fonts.gstatic.com/s/anybody/v4/VuJbdNvK2Ib2ppdWYq311GH32hxIv0sd5grncSUi2F_Wim4JfmfPrsXD_nBPpQ.ttf",
  "regular": "http://fonts.gstatic.com/s/anybody/v4/VuJbdNvK2Ib2ppdWYq311GH32hxIv0sd5grncSUi2F_Wim4J12DPrsXD_nBPpQ.ttf",
  "100italic": "http://fonts.gstatic.com/s/anybody/v4/VuJddNvK2Ib2ppdWSKTHN4GOiYrmuF7VpPiuQ9r6sTRMJGkcHyMn7M_H3HVfpcHY.ttf",
  "200italic": "http://fonts.gstatic.com/s/anybody/v4/VuJddNvK2Ib2ppdWSKTHN4GOiYrmuF7VpPiuQ9r6sTRMJGkcHyOn7c_H3HVfpcHY.ttf",
  "300italic": "http://fonts.gstatic.com/s/anybody/v4/VuJddNvK2Ib2ppdWSKTHN4GOiYrmuF7VpPiuQ9r6sTRMJGkcHyN57c_H3HVfpcHY.ttf",
  "italic": "http://fonts.gstatic.com/s/anybody/v4/VuJddNvK2Ib2ppdWSKTHN4GOiYrmuF7VpPiuQ9r6sTRMJGkcHyMn7c_H3HVfpcHY.ttf",
  "500italic": "http://fonts.gstatic.com/s/anybody/v4/VuJddNvK2Ib2ppdWSKTHN4GOiYrmuF7VpPiuQ9r6sTRMJGkcHyMV7c_H3HVfpcHY.ttf",
  "600italic": "http://fonts.gstatic.com/s/anybody/v4/VuJddNvK2Ib2ppdWSKTHN4GOiYrmuF7VpPiuQ9r6sTRMJGkcHyP56s_H3HVfpcHY.ttf",
  "700italic": "http://fonts.gstatic.com/s/anybody/v4/VuJddNvK2Ib2ppdWSKTHN4GOiYrmuF7VpPiuQ9r6sTRMJGkcHyPA6s_H3HVfpcHY.ttf",
  "800italic": "http://fonts.gstatic.com/s/anybody/v4/VuJddNvK2Ib2ppdWSKTHN4GOiYrmuF7VpPiuQ9r6sTRMJGkcHyOn6s_H3HVfpcHY.ttf",
  "900italic": "http://fonts.gstatic.com/s/anybody/v4/VuJddNvK2Ib2ppdWSKTHN4GOiYrmuF7VpPiuQ9r6sTRMJGkcHyOO6s_H3HVfpcHY.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Arapey",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/arapey/v16/-W__XJn-UDDA2RC6Z9AcZkIzeg.ttf",
  "italic": "http://fonts.gstatic.com/s/arapey/v16/-W_9XJn-UDDA2RCKZdoYREcjeo0k.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Arbutus",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/arbutus/v24/NaPYcZ7dG_5J3poob9JtryO8fMU.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Arbutus Slab",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/arbutusslab/v16/oY1Z8e7OuLXkJGbXtr5ba7ZVa68dJlaFAQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Architects Daughter",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/architectsdaughter/v18/KtkxAKiDZI_td1Lkx62xHZHDtgO_Y-bvfY5q4szgE-Q.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Archivo",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/archivo/v18/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTTNDJp8B1oJ0vyVQ.ttf",
  "200": "http://fonts.gstatic.com/s/archivo/v18/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTTtDNp8B1oJ0vyVQ.ttf",
  "300": "http://fonts.gstatic.com/s/archivo/v18/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTTajNp8B1oJ0vyVQ.ttf",
  "500": "http://fonts.gstatic.com/s/archivo/v18/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTTBjNp8B1oJ0vyVQ.ttf",
  "600": "http://fonts.gstatic.com/s/archivo/v18/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTT6jRp8B1oJ0vyVQ.ttf",
  "700": "http://fonts.gstatic.com/s/archivo/v18/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTT0zRp8B1oJ0vyVQ.ttf",
  "800": "http://fonts.gstatic.com/s/archivo/v18/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTTtDRp8B1oJ0vyVQ.ttf",
  "900": "http://fonts.gstatic.com/s/archivo/v18/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTTnTRp8B1oJ0vyVQ.ttf",
  "regular": "http://fonts.gstatic.com/s/archivo/v18/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTTNDNp8B1oJ0vyVQ.ttf",
  "100italic": "http://fonts.gstatic.com/s/archivo/v18/k3k8o8UDI-1M0wlSfdzyIEkpwTM29hr-8mTYIRyOSVz60_PG_HCBshdsBU7iVdxQ.ttf",
  "200italic": "http://fonts.gstatic.com/s/archivo/v18/k3k8o8UDI-1M0wlSfdzyIEkpwTM29hr-8mTYIRyOSVz60_PG_HABsxdsBU7iVdxQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/archivo/v18/k3k8o8UDI-1M0wlSfdzyIEkpwTM29hr-8mTYIRyOSVz60_PG_HDfsxdsBU7iVdxQ.ttf",
  "italic": "http://fonts.gstatic.com/s/archivo/v18/k3k8o8UDI-1M0wlSfdzyIEkpwTM29hr-8mTYIRyOSVz60_PG_HCBsxdsBU7iVdxQ.ttf",
  "500italic": "http://fonts.gstatic.com/s/archivo/v18/k3k8o8UDI-1M0wlSfdzyIEkpwTM29hr-8mTYIRyOSVz60_PG_HCzsxdsBU7iVdxQ.ttf",
  "600italic": "http://fonts.gstatic.com/s/archivo/v18/k3k8o8UDI-1M0wlSfdzyIEkpwTM29hr-8mTYIRyOSVz60_PG_HBftBdsBU7iVdxQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/archivo/v18/k3k8o8UDI-1M0wlSfdzyIEkpwTM29hr-8mTYIRyOSVz60_PG_HBmtBdsBU7iVdxQ.ttf",
  "800italic": "http://fonts.gstatic.com/s/archivo/v18/k3k8o8UDI-1M0wlSfdzyIEkpwTM29hr-8mTYIRyOSVz60_PG_HABtBdsBU7iVdxQ.ttf",
  "900italic": "http://fonts.gstatic.com/s/archivo/v18/k3k8o8UDI-1M0wlSfdzyIEkpwTM29hr-8mTYIRyOSVz60_PG_HAotBdsBU7iVdxQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Archivo Black",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/archivoblack/v17/HTxqL289NzCGg4MzN6KJ7eW6OYuP_x7yx3A.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Archivo Narrow",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/archivonarrow/v24/tss5ApVBdCYD5Q7hcxTE1ArZ0Zz8oY2KRmwvKhhvHlGKpHOtFCQ76Q.ttf",
  "600": "http://fonts.gstatic.com/s/archivonarrow/v24/tss5ApVBdCYD5Q7hcxTE1ArZ0Zz8oY2KRmwvKhhv8laKpHOtFCQ76Q.ttf",
  "700": "http://fonts.gstatic.com/s/archivonarrow/v24/tss5ApVBdCYD5Q7hcxTE1ArZ0Zz8oY2KRmwvKhhvy1aKpHOtFCQ76Q.ttf",
  "regular": "http://fonts.gstatic.com/s/archivonarrow/v24/tss5ApVBdCYD5Q7hcxTE1ArZ0Zz8oY2KRmwvKhhvLFGKpHOtFCQ76Q.ttf",
  "italic": "http://fonts.gstatic.com/s/archivonarrow/v24/tss7ApVBdCYD5Q7hcxTE1ArZ0bb1k3JSLwe1hB965BJi53mpNiEr6T6Y.ttf",
  "500italic": "http://fonts.gstatic.com/s/archivonarrow/v24/tss7ApVBdCYD5Q7hcxTE1ArZ0bb1k3JSLwe1hB965BJQ53mpNiEr6T6Y.ttf",
  "600italic": "http://fonts.gstatic.com/s/archivonarrow/v24/tss7ApVBdCYD5Q7hcxTE1ArZ0bb1k3JSLwe1hB965BK84HmpNiEr6T6Y.ttf",
  "700italic": "http://fonts.gstatic.com/s/archivonarrow/v24/tss7ApVBdCYD5Q7hcxTE1ArZ0bb1k3JSLwe1hB965BKF4HmpNiEr6T6Y.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Are You Serious",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/areyouserious/v10/ll8kK2GVSSr-PtjQ5nONVcNn4306hT9nCGRayg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Aref Ruqaa",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/arefruqaa/v23/WwkYxPW1E165rajQKDulKDwNcNIS2N_7Bdk.ttf",
  "regular": "http://fonts.gstatic.com/s/arefruqaa/v23/WwkbxPW1E165rajQKDulEIAiVNo5xNY.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Aref Ruqaa Ink",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v5",
  "lastModified": "2022-09-14",
  "files": {
  "700": "http://fonts.gstatic.com/s/arefruqaaink/v5/1q2cY5WOGUFlt84GTOkP6Kdx71xde6WhqWBCyxWn.ttf",
  "regular": "http://fonts.gstatic.com/s/arefruqaaink/v5/1q2fY5WOGUFlt84GTOkP6Kdx72ThVIGpgnxL.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Arima",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "malayalam",
  "tamil",
  "vietnamese"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/arima/v1/neIWzCqmt4Aup_qE1nFWqxI1RZX1YTE-pQGOyYw2fw.ttf",
  "200": "http://fonts.gstatic.com/s/arima/v1/neIWzCqmt4Aup_qE1nFWqxI1RZX14TA-pQGOyYw2fw.ttf",
  "300": "http://fonts.gstatic.com/s/arima/v1/neIWzCqmt4Aup_qE1nFWqxI1RZX1PzA-pQGOyYw2fw.ttf",
  "500": "http://fonts.gstatic.com/s/arima/v1/neIWzCqmt4Aup_qE1nFWqxI1RZX1UzA-pQGOyYw2fw.ttf",
  "600": "http://fonts.gstatic.com/s/arima/v1/neIWzCqmt4Aup_qE1nFWqxI1RZX1vzc-pQGOyYw2fw.ttf",
  "700": "http://fonts.gstatic.com/s/arima/v1/neIWzCqmt4Aup_qE1nFWqxI1RZX1hjc-pQGOyYw2fw.ttf",
  "regular": "http://fonts.gstatic.com/s/arima/v1/neIWzCqmt4Aup_qE1nFWqxI1RZX1YTA-pQGOyYw2fw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Arima Madurai",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/arimamadurai/v14/t5t4IRoeKYORG0WNMgnC3seB1V3PqrGCch4Drg.ttf",
  "200": "http://fonts.gstatic.com/s/arimamadurai/v14/t5t7IRoeKYORG0WNMgnC3seB1fHuipusfhcat2c.ttf",
  "300": "http://fonts.gstatic.com/s/arimamadurai/v14/t5t7IRoeKYORG0WNMgnC3seB1ZXtipusfhcat2c.ttf",
  "500": "http://fonts.gstatic.com/s/arimamadurai/v14/t5t7IRoeKYORG0WNMgnC3seB1c3sipusfhcat2c.ttf",
  "700": "http://fonts.gstatic.com/s/arimamadurai/v14/t5t7IRoeKYORG0WNMgnC3seB1YXqipusfhcat2c.ttf",
  "800": "http://fonts.gstatic.com/s/arimamadurai/v14/t5t7IRoeKYORG0WNMgnC3seB1Znpipusfhcat2c.ttf",
  "900": "http://fonts.gstatic.com/s/arimamadurai/v14/t5t7IRoeKYORG0WNMgnC3seB1b3oipusfhcat2c.ttf",
  "regular": "http://fonts.gstatic.com/s/arimamadurai/v14/t5tmIRoeKYORG0WNMgnC3seB7TnFrpOHYh4.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Arimo",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "hebrew",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v27",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/arimo/v27/P5sfzZCDf9_T_3cV7NCUECyoxNk338xsBxDAVQI4aA.ttf",
  "600": "http://fonts.gstatic.com/s/arimo/v27/P5sfzZCDf9_T_3cV7NCUECyoxNk3M8tsBxDAVQI4aA.ttf",
  "700": "http://fonts.gstatic.com/s/arimo/v27/P5sfzZCDf9_T_3cV7NCUECyoxNk3CstsBxDAVQI4aA.ttf",
  "regular": "http://fonts.gstatic.com/s/arimo/v27/P5sfzZCDf9_T_3cV7NCUECyoxNk37cxsBxDAVQI4aA.ttf",
  "italic": "http://fonts.gstatic.com/s/arimo/v27/P5sdzZCDf9_T_10c3i9MeUcyat4iJY-ERBrEdwcoaKww.ttf",
  "500italic": "http://fonts.gstatic.com/s/arimo/v27/P5sdzZCDf9_T_10c3i9MeUcyat4iJY-2RBrEdwcoaKww.ttf",
  "600italic": "http://fonts.gstatic.com/s/arimo/v27/P5sdzZCDf9_T_10c3i9MeUcyat4iJY9aQxrEdwcoaKww.ttf",
  "700italic": "http://fonts.gstatic.com/s/arimo/v27/P5sdzZCDf9_T_10c3i9MeUcyat4iJY9jQxrEdwcoaKww.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Arizonia",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/arizonia/v19/neIIzCemt4A5qa7mv6WGHK06UY30.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Armata",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/armata/v19/gokvH63_HV5jQ-E9lD53Q2u_mQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Arsenal",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/arsenal/v12/wXKuE3kQtZQ4pF3D7-P5JeQAmX8yrdk.ttf",
  "regular": "http://fonts.gstatic.com/s/arsenal/v12/wXKrE3kQtZQ4pF3D11_WAewrhXY.ttf",
  "italic": "http://fonts.gstatic.com/s/arsenal/v12/wXKpE3kQtZQ4pF3D513cBc4ulXYrtA.ttf",
  "700italic": "http://fonts.gstatic.com/s/arsenal/v12/wXKsE3kQtZQ4pF3D513kueEKnV03vdnKjw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Artifika",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/artifika/v20/VEMyRoxzronptCuxu6Wt5jDtreOL.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Arvo",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/arvo/v20/tDbM2oWUg0MKoZw1yLTA8vL7lAE.ttf",
  "regular": "http://fonts.gstatic.com/s/arvo/v20/tDbD2oWUg0MKmSAa7Lzr7vs.ttf",
  "italic": "http://fonts.gstatic.com/s/arvo/v20/tDbN2oWUg0MKqSIQ6J7u_vvijQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/arvo/v20/tDbO2oWUg0MKqSIoVLHK9tD-hAHkGg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Arya",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/arya/v19/ga6NawNG-HJdzfra3b-BaFg3dRE.ttf",
  "regular": "http://fonts.gstatic.com/s/arya/v19/ga6CawNG-HJd9Ub1-beqdFE.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Asap",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/asap/v24/KFO9CniXp96a4Tc2EZzSuDAoKsEI1qhOUX-8AEEe.ttf",
  "600": "http://fonts.gstatic.com/s/asap/v24/KFO9CniXp96a4Tc2EZzSuDAoKsHk0ahOUX-8AEEe.ttf",
  "700": "http://fonts.gstatic.com/s/asap/v24/KFO9CniXp96a4Tc2EZzSuDAoKsHd0ahOUX-8AEEe.ttf",
  "regular": "http://fonts.gstatic.com/s/asap/v24/KFO9CniXp96a4Tc2EZzSuDAoKsE61qhOUX-8AEEe.ttf",
  "italic": "http://fonts.gstatic.com/s/asap/v24/KFO7CniXp96ayz4E7kS706qGLdTylUANW3ueBVEeezU.ttf",
  "500italic": "http://fonts.gstatic.com/s/asap/v24/KFO7CniXp96ayz4E7kS706qGLdTylXINW3ueBVEeezU.ttf",
  "600italic": "http://fonts.gstatic.com/s/asap/v24/KFO7CniXp96ayz4E7kS706qGLdTylZ4KW3ueBVEeezU.ttf",
  "700italic": "http://fonts.gstatic.com/s/asap/v24/KFO7CniXp96ayz4E7kS706qGLdTylacKW3ueBVEeezU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Asap Condensed",
  "variants": [
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/asapcondensed/v15/pxieypY1o9NHyXh3WvSbGSggdO9_S2lEgGqgp-pO.ttf",
  "600": "http://fonts.gstatic.com/s/asapcondensed/v15/pxieypY1o9NHyXh3WvSbGSggdO9TTGlEgGqgp-pO.ttf",
  "700": "http://fonts.gstatic.com/s/asapcondensed/v15/pxieypY1o9NHyXh3WvSbGSggdO83TWlEgGqgp-pO.ttf",
  "regular": "http://fonts.gstatic.com/s/asapcondensed/v15/pxidypY1o9NHyXh3WvSbGSggdNeLYk1Mq3ap.ttf",
  "italic": "http://fonts.gstatic.com/s/asapcondensed/v15/pxifypY1o9NHyXh3WvSbGSggdOeJaElurmapvvM.ttf",
  "500italic": "http://fonts.gstatic.com/s/asapcondensed/v15/pxiYypY1o9NHyXh3WvSbGSggdOeJUL1Him6CovpOkXA.ttf",
  "600italic": "http://fonts.gstatic.com/s/asapcondensed/v15/pxiYypY1o9NHyXh3WvSbGSggdOeJUJFAim6CovpOkXA.ttf",
  "700italic": "http://fonts.gstatic.com/s/asapcondensed/v15/pxiYypY1o9NHyXh3WvSbGSggdOeJUPVBim6CovpOkXA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Asar",
  "variants": [
  "regular"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/asar/v22/sZlLdRyI6TBIXkYQDLlTW6E.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Asset",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/asset/v24/SLXGc1na-mM4cWImRJqExst1.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Assistant",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/assistant/v18/2sDPZGJYnIjSi6H75xkZZE1I0yCmYzzQtmZnEGGf3qGuvM4.ttf",
  "300": "http://fonts.gstatic.com/s/assistant/v18/2sDPZGJYnIjSi6H75xkZZE1I0yCmYzzQtrhnEGGf3qGuvM4.ttf",
  "500": "http://fonts.gstatic.com/s/assistant/v18/2sDPZGJYnIjSi6H75xkZZE1I0yCmYzzQttRnEGGf3qGuvM4.ttf",
  "600": "http://fonts.gstatic.com/s/assistant/v18/2sDPZGJYnIjSi6H75xkZZE1I0yCmYzzQtjhgEGGf3qGuvM4.ttf",
  "700": "http://fonts.gstatic.com/s/assistant/v18/2sDPZGJYnIjSi6H75xkZZE1I0yCmYzzQtgFgEGGf3qGuvM4.ttf",
  "800": "http://fonts.gstatic.com/s/assistant/v18/2sDPZGJYnIjSi6H75xkZZE1I0yCmYzzQtmZgEGGf3qGuvM4.ttf",
  "regular": "http://fonts.gstatic.com/s/assistant/v18/2sDPZGJYnIjSi6H75xkZZE1I0yCmYzzQtuZnEGGf3qGuvM4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Astloch",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-04-20",
  "files": {
  "700": "http://fonts.gstatic.com/s/astloch/v26/TuGUUVJ8QI5GSeUjk2A-6MNPA10xLMQ.ttf",
  "regular": "http://fonts.gstatic.com/s/astloch/v26/TuGRUVJ8QI5GSeUjq9wRzMtkH1Q.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Asul",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/asul/v19/VuJxdNjKxYr40U8qeKbXOIFneRo.ttf",
  "regular": "http://fonts.gstatic.com/s/asul/v19/VuJ-dNjKxYr46fMFXK78JIg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Athiti",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/athiti/v12/pe0sMISdLIZIv1wAxDNyAv2-C99ycg.ttf",
  "300": "http://fonts.gstatic.com/s/athiti/v12/pe0sMISdLIZIv1wAoDByAv2-C99ycg.ttf",
  "500": "http://fonts.gstatic.com/s/athiti/v12/pe0sMISdLIZIv1wA-DFyAv2-C99ycg.ttf",
  "600": "http://fonts.gstatic.com/s/athiti/v12/pe0sMISdLIZIv1wA1DZyAv2-C99ycg.ttf",
  "700": "http://fonts.gstatic.com/s/athiti/v12/pe0sMISdLIZIv1wAsDdyAv2-C99ycg.ttf",
  "regular": "http://fonts.gstatic.com/s/athiti/v12/pe0vMISdLIZIv1w4DBhWCtaiAg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Atkinson Hyperlegible",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/atkinsonhyperlegible/v10/9Bt73C1KxNDXMspQ1lPyU89-1h6ONRlW45G8WbcNcy-OZFy-FA.ttf",
  "regular": "http://fonts.gstatic.com/s/atkinsonhyperlegible/v10/9Bt23C1KxNDXMspQ1lPyU89-1h6ONRlW45GE5ZgpewSSbQ.ttf",
  "italic": "http://fonts.gstatic.com/s/atkinsonhyperlegible/v10/9Bt43C1KxNDXMspQ1lPyU89-1h6ONRlW45G055ItWQGCbUWn.ttf",
  "700italic": "http://fonts.gstatic.com/s/atkinsonhyperlegible/v10/9Bt93C1KxNDXMspQ1lPyU89-1h6ONRlW45G056qRdiWKRlmuFH24.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Atma",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "bengali",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/atma/v15/uK_z4rqWc-Eoo8JzKjc9PvedRkM.ttf",
  "500": "http://fonts.gstatic.com/s/atma/v15/uK_z4rqWc-Eoo5pyKjc9PvedRkM.ttf",
  "600": "http://fonts.gstatic.com/s/atma/v15/uK_z4rqWc-Eoo7Z1Kjc9PvedRkM.ttf",
  "700": "http://fonts.gstatic.com/s/atma/v15/uK_z4rqWc-Eoo9J0Kjc9PvedRkM.ttf",
  "regular": "http://fonts.gstatic.com/s/atma/v15/uK_84rqWc-Eom25bDj8WIv4.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Atomic Age",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v27",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/atomicage/v27/f0Xz0eug6sdmRFkYZZGL58Ht9a8GYeA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Aubrey",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v28",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/aubrey/v28/q5uGsou7NPBw-p7vugNsCxVEgA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Audiowide",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/audiowide/v16/l7gdbjpo0cum0ckerWCtkQXPExpQBw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Autour One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/autourone/v24/UqyVK80cP25l3fJgbdfbk5lWVscxdKE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Average",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/average/v16/fC1hPYBHe23MxA7rIeJwVWytTyk.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Average Sans",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/averagesans/v16/1Ptpg8fLXP2dlAXR-HlJJNJPBdqazVoK4A.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Averia Gruesa Libre",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/averiagruesalibre/v22/NGSov4nEGEktOaDRKsY-1dhh8eEtIx3ZUmmJw0SLRA8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Averia Libre",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/averialibre/v16/2V0FKIcMGZEnV6xygz7eNjEarovtb07t-pQgTw.ttf",
  "700": "http://fonts.gstatic.com/s/averialibre/v16/2V0FKIcMGZEnV6xygz7eNjEavoztb07t-pQgTw.ttf",
  "300italic": "http://fonts.gstatic.com/s/averialibre/v16/2V0HKIcMGZEnV6xygz7eNjESAJFhbUTp2JEwT4Sk.ttf",
  "regular": "http://fonts.gstatic.com/s/averialibre/v16/2V0aKIcMGZEnV6xygz7eNjEiAqPJZ2Xx8w.ttf",
  "italic": "http://fonts.gstatic.com/s/averialibre/v16/2V0EKIcMGZEnV6xygz7eNjESAKnNRWDh8405.ttf",
  "700italic": "http://fonts.gstatic.com/s/averialibre/v16/2V0HKIcMGZEnV6xygz7eNjESAJFxakTp2JEwT4Sk.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Averia Sans Libre",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/averiasanslibre/v17/ga6SaxZG_G5OvCf_rt7FH3B6BHLMEd3lMKcQJZP1LmD9.ttf",
  "700": "http://fonts.gstatic.com/s/averiasanslibre/v17/ga6SaxZG_G5OvCf_rt7FH3B6BHLMEd31N6cQJZP1LmD9.ttf",
  "300italic": "http://fonts.gstatic.com/s/averiasanslibre/v17/ga6caxZG_G5OvCf_rt7FH3B6BHLMEdVLKisSL5fXK3D9qtg.ttf",
  "regular": "http://fonts.gstatic.com/s/averiasanslibre/v17/ga6XaxZG_G5OvCf_rt7FH3B6BHLMEeVJGIMYDo_8.ttf",
  "italic": "http://fonts.gstatic.com/s/averiasanslibre/v17/ga6RaxZG_G5OvCf_rt7FH3B6BHLMEdVLEoc6C5_8N3k.ttf",
  "700italic": "http://fonts.gstatic.com/s/averiasanslibre/v17/ga6caxZG_G5OvCf_rt7FH3B6BHLMEdVLKjsVL5fXK3D9qtg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Averia Serif Libre",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/averiaseriflibre/v16/neIVzD2ms4wxr6GvjeD0X88SHPyX2xYGCSmqwacqdrKvbQ.ttf",
  "700": "http://fonts.gstatic.com/s/averiaseriflibre/v16/neIVzD2ms4wxr6GvjeD0X88SHPyX2xYGGS6qwacqdrKvbQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/averiaseriflibre/v16/neIbzD2ms4wxr6GvjeD0X88SHPyX2xYOpzMmw60uVLe_bXHq.ttf",
  "regular": "http://fonts.gstatic.com/s/averiaseriflibre/v16/neIWzD2ms4wxr6GvjeD0X88SHPyX2xY-pQGOyYw2fw.ttf",
  "italic": "http://fonts.gstatic.com/s/averiaseriflibre/v16/neIUzD2ms4wxr6GvjeD0X88SHPyX2xYOpwuK64kmf6u2.ttf",
  "700italic": "http://fonts.gstatic.com/s/averiaseriflibre/v16/neIbzD2ms4wxr6GvjeD0X88SHPyX2xYOpzM2xK0uVLe_bXHq.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Azeret Mono",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/azeretmono/v11/3XF5ErsiyJsY9O_Gepph-FvtTQgMQUdNekSfnPRh0raa-5s3AA.ttf",
  "200": "http://fonts.gstatic.com/s/azeretmono/v11/3XF5ErsiyJsY9O_Gepph-FvtTQgMQUdNekSfHPVh0raa-5s3AA.ttf",
  "300": "http://fonts.gstatic.com/s/azeretmono/v11/3XF5ErsiyJsY9O_Gepph-FvtTQgMQUdNekSfwvVh0raa-5s3AA.ttf",
  "500": "http://fonts.gstatic.com/s/azeretmono/v11/3XF5ErsiyJsY9O_Gepph-FvtTQgMQUdNekSfrvVh0raa-5s3AA.ttf",
  "600": "http://fonts.gstatic.com/s/azeretmono/v11/3XF5ErsiyJsY9O_Gepph-FvtTQgMQUdNekSfQvJh0raa-5s3AA.ttf",
  "700": "http://fonts.gstatic.com/s/azeretmono/v11/3XF5ErsiyJsY9O_Gepph-FvtTQgMQUdNekSfe_Jh0raa-5s3AA.ttf",
  "800": "http://fonts.gstatic.com/s/azeretmono/v11/3XF5ErsiyJsY9O_Gepph-FvtTQgMQUdNekSfHPJh0raa-5s3AA.ttf",
  "900": "http://fonts.gstatic.com/s/azeretmono/v11/3XF5ErsiyJsY9O_Gepph-FvtTQgMQUdNekSfNfJh0raa-5s3AA.ttf",
  "regular": "http://fonts.gstatic.com/s/azeretmono/v11/3XF5ErsiyJsY9O_Gepph-FvtTQgMQUdNekSfnPVh0raa-5s3AA.ttf",
  "100italic": "http://fonts.gstatic.com/s/azeretmono/v11/3XF_ErsiyJsY9O_Gepph-HHkf_fUKCzX1EOKVLaJkLye2Z4nAN7J.ttf",
  "200italic": "http://fonts.gstatic.com/s/azeretmono/v11/3XF_ErsiyJsY9O_Gepph-HHkf_fUKCzX1EOKVLYJkbye2Z4nAN7J.ttf",
  "300italic": "http://fonts.gstatic.com/s/azeretmono/v11/3XF_ErsiyJsY9O_Gepph-HHkf_fUKCzX1EOKVLbXkbye2Z4nAN7J.ttf",
  "italic": "http://fonts.gstatic.com/s/azeretmono/v11/3XF_ErsiyJsY9O_Gepph-HHkf_fUKCzX1EOKVLaJkbye2Z4nAN7J.ttf",
  "500italic": "http://fonts.gstatic.com/s/azeretmono/v11/3XF_ErsiyJsY9O_Gepph-HHkf_fUKCzX1EOKVLa7kbye2Z4nAN7J.ttf",
  "600italic": "http://fonts.gstatic.com/s/azeretmono/v11/3XF_ErsiyJsY9O_Gepph-HHkf_fUKCzX1EOKVLZXlrye2Z4nAN7J.ttf",
  "700italic": "http://fonts.gstatic.com/s/azeretmono/v11/3XF_ErsiyJsY9O_Gepph-HHkf_fUKCzX1EOKVLZulrye2Z4nAN7J.ttf",
  "800italic": "http://fonts.gstatic.com/s/azeretmono/v11/3XF_ErsiyJsY9O_Gepph-HHkf_fUKCzX1EOKVLYJlrye2Z4nAN7J.ttf",
  "900italic": "http://fonts.gstatic.com/s/azeretmono/v11/3XF_ErsiyJsY9O_Gepph-HHkf_fUKCzX1EOKVLYglrye2Z4nAN7J.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "B612",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/b612/v12/3Jn9SDDxiSz34oWXPDCLTXUETuE.ttf",
  "regular": "http://fonts.gstatic.com/s/b612/v12/3JnySDDxiSz32jm4GDigUXw.ttf",
  "italic": "http://fonts.gstatic.com/s/b612/v12/3Jn8SDDxiSz36juyHBqlQXwdVw.ttf",
  "700italic": "http://fonts.gstatic.com/s/b612/v12/3Jn_SDDxiSz36juKoDWBSVcBXuFb0Q.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "B612 Mono",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/b612mono/v12/kmK6Zq85QVWbN1eW6lJdayv4os9Pv7JGSg.ttf",
  "regular": "http://fonts.gstatic.com/s/b612mono/v12/kmK_Zq85QVWbN1eW6lJl1wTcquRTtg.ttf",
  "italic": "http://fonts.gstatic.com/s/b612mono/v12/kmK5Zq85QVWbN1eW6lJV1Q7YiOFDtqtf.ttf",
  "700italic": "http://fonts.gstatic.com/s/b612mono/v12/kmKkZq85QVWbN1eW6lJV1TZkp8VLnbdWSg4x.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "BIZ UDGothic",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "greek-ext",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v6",
  "lastModified": "2022-09-27",
  "files": {
  "700": "http://fonts.gstatic.com/s/bizudgothic/v6/daaASTouBF7RUjnbt8p3LuKVCSxZ-xTQZMhbaA.ttf",
  "regular": "http://fonts.gstatic.com/s/bizudgothic/v6/daafSTouBF7RUjnbt8p3LuKttQN98z_MbQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "BIZ UDMincho",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "greek-ext",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v6",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bizudmincho/v6/EJRRQgI6eOxFjBdKs38yhtW1dwT7rcpY8Q.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "BIZ UDPGothic",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "greek-ext",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v6",
  "lastModified": "2022-09-27",
  "files": {
  "700": "http://fonts.gstatic.com/s/bizudpgothic/v6/hESq6X5pHAIBjmS84VL0Bue85skjZWEnTABCSQo.ttf",
  "regular": "http://fonts.gstatic.com/s/bizudpgothic/v6/hES36X5pHAIBjmS84VL0Bue83nUMQWkMUAk.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "BIZ UDPMincho",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "greek-ext",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v6",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bizudpmincho/v6/ypvfbXOBrmYppy7oWWTg1_58nhhYtUb0gZk.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Babylonica",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/babylonica/v2/5aUw9_i2qxWVCAE2aHjTqDJ0-VVMoEw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bad Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-04-20",
  "files": {
  "regular": "http://fonts.gstatic.com/s/badscript/v16/6NUT8F6PJgbFWQn47_x7lOwuzd1AZtw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bahiana",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bahiana/v19/uU9PCBUV4YenPWJU7xPb3vyHmlI.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bahianita",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bahianita/v17/yYLr0hTb3vuqqsBUgxWtxTvV2NJPcA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bai Jamjuree",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIqapSCOBt_aeQQ7ftydoa0kePuk5A1-yiSgA.ttf",
  "300": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIqapSCOBt_aeQQ7ftydoa09eDuk5A1-yiSgA.ttf",
  "500": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIqapSCOBt_aeQQ7ftydoa0reHuk5A1-yiSgA.ttf",
  "600": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIqapSCOBt_aeQQ7ftydoa0gebuk5A1-yiSgA.ttf",
  "700": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIqapSCOBt_aeQQ7ftydoa05efuk5A1-yiSgA.ttf",
  "200italic": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIoapSCOBt_aeQQ7ftydoa8W_oGkpox2S2CgOva.ttf",
  "300italic": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIoapSCOBt_aeQQ7ftydoa8W_pikZox2S2CgOva.ttf",
  "regular": "http://fonts.gstatic.com/s/baijamjuree/v11/LDI1apSCOBt_aeQQ7ftydoaMWcjKm7sp8g.ttf",
  "italic": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIrapSCOBt_aeQQ7ftydoa8W8LOub458jGL.ttf",
  "500italic": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIoapSCOBt_aeQQ7ftydoa8W_o6kJox2S2CgOva.ttf",
  "600italic": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIoapSCOBt_aeQQ7ftydoa8W_oWl5ox2S2CgOva.ttf",
  "700italic": "http://fonts.gstatic.com/s/baijamjuree/v11/LDIoapSCOBt_aeQQ7ftydoa8W_pylpox2S2CgOva.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bakbak One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v6",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bakbakone/v6/zOL54pXAl6RI-p_ardnuycRuv-hHkOs.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ballet",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ballet/v21/QGYyz_MYZA-HM4NjuGOVnUEXme1I4Xi3C4G-EiAou6Y.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baloo 2",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/baloo2/v14/wXK0E3kTposypRydzVT08TS3JnAmtdgozapv9Fat7WcN.ttf",
  "600": "http://fonts.gstatic.com/s/baloo2/v14/wXK0E3kTposypRydzVT08TS3JnAmtdjEyqpv9Fat7WcN.ttf",
  "700": "http://fonts.gstatic.com/s/baloo2/v14/wXK0E3kTposypRydzVT08TS3JnAmtdj9yqpv9Fat7WcN.ttf",
  "800": "http://fonts.gstatic.com/s/baloo2/v14/wXK0E3kTposypRydzVT08TS3JnAmtdiayqpv9Fat7WcN.ttf",
  "regular": "http://fonts.gstatic.com/s/baloo2/v14/wXK0E3kTposypRydzVT08TS3JnAmtdgazapv9Fat7WcN.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baloo Bhai 2",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/baloobhai2/v19/sZlWdRSL-z1VEWZ4YNA7Y5ItevYWUOHDE8FvNhohMXeCo-jsZzo.ttf",
  "600": "http://fonts.gstatic.com/s/baloobhai2/v19/sZlWdRSL-z1VEWZ4YNA7Y5ItevYWUOHDE8FvNvYmMXeCo-jsZzo.ttf",
  "700": "http://fonts.gstatic.com/s/baloobhai2/v19/sZlWdRSL-z1VEWZ4YNA7Y5ItevYWUOHDE8FvNs8mMXeCo-jsZzo.ttf",
  "800": "http://fonts.gstatic.com/s/baloobhai2/v19/sZlWdRSL-z1VEWZ4YNA7Y5ItevYWUOHDE8FvNqgmMXeCo-jsZzo.ttf",
  "regular": "http://fonts.gstatic.com/s/baloobhai2/v19/sZlWdRSL-z1VEWZ4YNA7Y5ItevYWUOHDE8FvNighMXeCo-jsZzo.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baloo Bhaijaan 2",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-28",
  "files": {
  "500": "http://fonts.gstatic.com/s/baloobhaijaan2/v12/zYXwKUwuEqdVGqM8tPDdAA_Y-_bMKo1EhQd2tWxo8TyjSqP4L4ppfcyC.ttf",
  "600": "http://fonts.gstatic.com/s/baloobhaijaan2/v12/zYXwKUwuEqdVGqM8tPDdAA_Y-_bMKo1EhQd2tWxo8TxPTaP4L4ppfcyC.ttf",
  "700": "http://fonts.gstatic.com/s/baloobhaijaan2/v12/zYXwKUwuEqdVGqM8tPDdAA_Y-_bMKo1EhQd2tWxo8Tx2TaP4L4ppfcyC.ttf",
  "800": "http://fonts.gstatic.com/s/baloobhaijaan2/v12/zYXwKUwuEqdVGqM8tPDdAA_Y-_bMKo1EhQd2tWxo8TwRTaP4L4ppfcyC.ttf",
  "regular": "http://fonts.gstatic.com/s/baloobhaijaan2/v12/zYXwKUwuEqdVGqM8tPDdAA_Y-_bMKo1EhQd2tWxo8TyRSqP4L4ppfcyC.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baloo Bhaina 2",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "oriya",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/baloobhaina2/v20/qWc-B6yyq4P9Adr3RtoX1q6ySgbwusXwJjkOS-XEgMPvRfRLYWmZSA.ttf",
  "600": "http://fonts.gstatic.com/s/baloobhaina2/v20/qWc-B6yyq4P9Adr3RtoX1q6ySgbwusXwJjkOS-XEbMTvRfRLYWmZSA.ttf",
  "700": "http://fonts.gstatic.com/s/baloobhaina2/v20/qWc-B6yyq4P9Adr3RtoX1q6ySgbwusXwJjkOS-XEVcTvRfRLYWmZSA.ttf",
  "800": "http://fonts.gstatic.com/s/baloobhaina2/v20/qWc-B6yyq4P9Adr3RtoX1q6ySgbwusXwJjkOS-XEMsTvRfRLYWmZSA.ttf",
  "regular": "http://fonts.gstatic.com/s/baloobhaina2/v20/qWc-B6yyq4P9Adr3RtoX1q6ySgbwusXwJjkOS-XEssPvRfRLYWmZSA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baloo Chettan 2",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "malayalam",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/baloochettan2/v14/vm8hdRbmXEva26PK-NtuX4ynWEzF69-L4gqgkIL5CdCTO1oeH9xI2gc.ttf",
  "600": "http://fonts.gstatic.com/s/baloochettan2/v14/vm8hdRbmXEva26PK-NtuX4ynWEzF69-L4gqgkIL5CTyUO1oeH9xI2gc.ttf",
  "700": "http://fonts.gstatic.com/s/baloochettan2/v14/vm8hdRbmXEva26PK-NtuX4ynWEzF69-L4gqgkIL5CQWUO1oeH9xI2gc.ttf",
  "800": "http://fonts.gstatic.com/s/baloochettan2/v14/vm8hdRbmXEva26PK-NtuX4ynWEzF69-L4gqgkIL5CWKUO1oeH9xI2gc.ttf",
  "regular": "http://fonts.gstatic.com/s/baloochettan2/v14/vm8hdRbmXEva26PK-NtuX4ynWEzF69-L4gqgkIL5CeKTO1oeH9xI2gc.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baloo Da 2",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "bengali",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/balooda2/v14/2-c39J9j0IaUMQZwAJyJaOX1UUnf3GLnYjA5sTNe55aRa7UE.ttf",
  "600": "http://fonts.gstatic.com/s/balooda2/v14/2-c39J9j0IaUMQZwAJyJaOX1UUnf3GLnYjDVtjNe55aRa7UE.ttf",
  "700": "http://fonts.gstatic.com/s/balooda2/v14/2-c39J9j0IaUMQZwAJyJaOX1UUnf3GLnYjDstjNe55aRa7UE.ttf",
  "800": "http://fonts.gstatic.com/s/balooda2/v14/2-c39J9j0IaUMQZwAJyJaOX1UUnf3GLnYjCLtjNe55aRa7UE.ttf",
  "regular": "http://fonts.gstatic.com/s/balooda2/v14/2-c39J9j0IaUMQZwAJyJaOX1UUnf3GLnYjALsTNe55aRa7UE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baloo Paaji 2",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "gurmukhi",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/baloopaaji2/v20/i7dfIFFzbz-QHZUdV9_UGWZuelmy79QJ1HOSY9Al74fybRUz1r5t.ttf",
  "600": "http://fonts.gstatic.com/s/baloopaaji2/v20/i7dfIFFzbz-QHZUdV9_UGWZuelmy79QJ1HOSY9DJ6IfybRUz1r5t.ttf",
  "700": "http://fonts.gstatic.com/s/baloopaaji2/v20/i7dfIFFzbz-QHZUdV9_UGWZuelmy79QJ1HOSY9Dw6IfybRUz1r5t.ttf",
  "800": "http://fonts.gstatic.com/s/baloopaaji2/v20/i7dfIFFzbz-QHZUdV9_UGWZuelmy79QJ1HOSY9CX6IfybRUz1r5t.ttf",
  "regular": "http://fonts.gstatic.com/s/baloopaaji2/v20/i7dfIFFzbz-QHZUdV9_UGWZuelmy79QJ1HOSY9AX74fybRUz1r5t.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baloo Tamma 2",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "kannada",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/balootamma2/v13/vEFE2_hCAgcR46PaajtrYlBbVUMUJgIC5LHTrMsuPp-0IF71SGC5.ttf",
  "600": "http://fonts.gstatic.com/s/balootamma2/v13/vEFE2_hCAgcR46PaajtrYlBbVUMUJgIC5LHTrMvCOZ-0IF71SGC5.ttf",
  "700": "http://fonts.gstatic.com/s/balootamma2/v13/vEFE2_hCAgcR46PaajtrYlBbVUMUJgIC5LHTrMv7OZ-0IF71SGC5.ttf",
  "800": "http://fonts.gstatic.com/s/balootamma2/v13/vEFE2_hCAgcR46PaajtrYlBbVUMUJgIC5LHTrMucOZ-0IF71SGC5.ttf",
  "regular": "http://fonts.gstatic.com/s/balootamma2/v13/vEFE2_hCAgcR46PaajtrYlBbVUMUJgIC5LHTrMscPp-0IF71SGC5.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baloo Tammudu 2",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "telugu",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/balootammudu2/v20/1Pt5g8TIS_SAmkLguUdFP8UaJcKkzlPmMT00GaE_Jc0e4c6PZSlGmAA.ttf",
  "600": "http://fonts.gstatic.com/s/balootammudu2/v20/1Pt5g8TIS_SAmkLguUdFP8UaJcKkzlPmMT00GaE_JSEZ4c6PZSlGmAA.ttf",
  "700": "http://fonts.gstatic.com/s/balootammudu2/v20/1Pt5g8TIS_SAmkLguUdFP8UaJcKkzlPmMT00GaE_JRgZ4c6PZSlGmAA.ttf",
  "800": "http://fonts.gstatic.com/s/balootammudu2/v20/1Pt5g8TIS_SAmkLguUdFP8UaJcKkzlPmMT00GaE_JX8Z4c6PZSlGmAA.ttf",
  "regular": "http://fonts.gstatic.com/s/balootammudu2/v20/1Pt5g8TIS_SAmkLguUdFP8UaJcKkzlPmMT00GaE_Jf8e4c6PZSlGmAA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baloo Thambi 2",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/baloothambi2/v14/cY9RfjeOW0NHpmOQXranrbDyu5JMJmNp-aDvUBbK_8IzaQRG_n4osQ.ttf",
  "600": "http://fonts.gstatic.com/s/baloothambi2/v14/cY9RfjeOW0NHpmOQXranrbDyu5JMJmNp-aDvUBbKE8UzaQRG_n4osQ.ttf",
  "700": "http://fonts.gstatic.com/s/baloothambi2/v14/cY9RfjeOW0NHpmOQXranrbDyu5JMJmNp-aDvUBbKKsUzaQRG_n4osQ.ttf",
  "800": "http://fonts.gstatic.com/s/baloothambi2/v14/cY9RfjeOW0NHpmOQXranrbDyu5JMJmNp-aDvUBbKTcUzaQRG_n4osQ.ttf",
  "regular": "http://fonts.gstatic.com/s/baloothambi2/v14/cY9RfjeOW0NHpmOQXranrbDyu5JMJmNp-aDvUBbKzcIzaQRG_n4osQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Balsamiq Sans",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/balsamiqsans/v10/P5sZzZiAbNrN8SB3lQQX7PncyWUyBY9mAzLFRQI.ttf",
  "regular": "http://fonts.gstatic.com/s/balsamiqsans/v10/P5sEzZiAbNrN8SB3lQQX7Pnc8dkdIYdNHzs.ttf",
  "italic": "http://fonts.gstatic.com/s/balsamiqsans/v10/P5sazZiAbNrN8SB3lQQX7PncwdsXJaVIDzvcXA.ttf",
  "700italic": "http://fonts.gstatic.com/s/balsamiqsans/v10/P5sfzZiAbNrN8SB3lQQX7PncwdsvmYpsBxDAVQI4aA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Balthazar",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/balthazar/v17/d6lKkaajS8Gm4CVQjFEvyRTo39l8hw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bangers",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bangers/v20/FeVQS0BTqb0h60ACL5la2bxii28.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Barlow",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/barlow/v12/7cHrv4kjgoGqM7E3b8s8yn4hnCci.ttf",
  "200": "http://fonts.gstatic.com/s/barlow/v12/7cHqv4kjgoGqM7E3w-oc4FAtlT47dw.ttf",
  "300": "http://fonts.gstatic.com/s/barlow/v12/7cHqv4kjgoGqM7E3p-kc4FAtlT47dw.ttf",
  "500": "http://fonts.gstatic.com/s/barlow/v12/7cHqv4kjgoGqM7E3_-gc4FAtlT47dw.ttf",
  "600": "http://fonts.gstatic.com/s/barlow/v12/7cHqv4kjgoGqM7E30-8c4FAtlT47dw.ttf",
  "700": "http://fonts.gstatic.com/s/barlow/v12/7cHqv4kjgoGqM7E3t-4c4FAtlT47dw.ttf",
  "800": "http://fonts.gstatic.com/s/barlow/v12/7cHqv4kjgoGqM7E3q-0c4FAtlT47dw.ttf",
  "900": "http://fonts.gstatic.com/s/barlow/v12/7cHqv4kjgoGqM7E3j-wc4FAtlT47dw.ttf",
  "100italic": "http://fonts.gstatic.com/s/barlow/v12/7cHtv4kjgoGqM7E_CfNYwHoDmTcibrA.ttf",
  "200italic": "http://fonts.gstatic.com/s/barlow/v12/7cHsv4kjgoGqM7E_CfP04Voptzsrd6m9.ttf",
  "300italic": "http://fonts.gstatic.com/s/barlow/v12/7cHsv4kjgoGqM7E_CfOQ4loptzsrd6m9.ttf",
  "regular": "http://fonts.gstatic.com/s/barlow/v12/7cHpv4kjgoGqM7EPC8E46HsxnA.ttf",
  "italic": "http://fonts.gstatic.com/s/barlow/v12/7cHrv4kjgoGqM7E_Ccs8yn4hnCci.ttf",
  "500italic": "http://fonts.gstatic.com/s/barlow/v12/7cHsv4kjgoGqM7E_CfPI41optzsrd6m9.ttf",
  "600italic": "http://fonts.gstatic.com/s/barlow/v12/7cHsv4kjgoGqM7E_CfPk5Foptzsrd6m9.ttf",
  "700italic": "http://fonts.gstatic.com/s/barlow/v12/7cHsv4kjgoGqM7E_CfOA5Voptzsrd6m9.ttf",
  "800italic": "http://fonts.gstatic.com/s/barlow/v12/7cHsv4kjgoGqM7E_CfOc5loptzsrd6m9.ttf",
  "900italic": "http://fonts.gstatic.com/s/barlow/v12/7cHsv4kjgoGqM7E_CfO451optzsrd6m9.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Barlow Condensed",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxxL3I-JCGChYJ8VI-L6OO_au7B43LT31vytKgbaw.ttf",
  "200": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxwL3I-JCGChYJ8VI-L6OO_au7B497y_3HcuKECcrs.ttf",
  "300": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxwL3I-JCGChYJ8VI-L6OO_au7B47rx_3HcuKECcrs.ttf",
  "500": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxwL3I-JCGChYJ8VI-L6OO_au7B4-Lw_3HcuKECcrs.ttf",
  "600": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxwL3I-JCGChYJ8VI-L6OO_au7B4873_3HcuKECcrs.ttf",
  "700": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxwL3I-JCGChYJ8VI-L6OO_au7B46r2_3HcuKECcrs.ttf",
  "800": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxwL3I-JCGChYJ8VI-L6OO_au7B47b1_3HcuKECcrs.ttf",
  "900": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxwL3I-JCGChYJ8VI-L6OO_au7B45L0_3HcuKECcrs.ttf",
  "100italic": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxzL3I-JCGChYJ8VI-L6OO_au7B6xTru1H2lq0La6JN.ttf",
  "200italic": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxyL3I-JCGChYJ8VI-L6OO_au7B6xTrF3DWvIMHYrtUxg.ttf",
  "300italic": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxyL3I-JCGChYJ8VI-L6OO_au7B6xTrc3PWvIMHYrtUxg.ttf",
  "regular": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTx3L3I-JCGChYJ8VI-L6OO_au7B2xbZ23n3pKg.ttf",
  "italic": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxxL3I-JCGChYJ8VI-L6OO_au7B6xTT31vytKgbaw.ttf",
  "500italic": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxyL3I-JCGChYJ8VI-L6OO_au7B6xTrK3LWvIMHYrtUxg.ttf",
  "600italic": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxyL3I-JCGChYJ8VI-L6OO_au7B6xTrB3XWvIMHYrtUxg.ttf",
  "700italic": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxyL3I-JCGChYJ8VI-L6OO_au7B6xTrY3TWvIMHYrtUxg.ttf",
  "800italic": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxyL3I-JCGChYJ8VI-L6OO_au7B6xTrf3fWvIMHYrtUxg.ttf",
  "900italic": "http://fonts.gstatic.com/s/barlowcondensed/v12/HTxyL3I-JCGChYJ8VI-L6OO_au7B6xTrW3bWvIMHYrtUxg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Barlow Semi Condensed",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlphgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRfG4qvKk8ogoSP.ttf",
  "200": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRft6uPAGEki52WfA.ttf",
  "300": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRf06iPAGEki52WfA.ttf",
  "500": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRfi6mPAGEki52WfA.ttf",
  "600": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRfp66PAGEki52WfA.ttf",
  "700": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRfw6-PAGEki52WfA.ttf",
  "800": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRf36yPAGEki52WfA.ttf",
  "900": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRf-62PAGEki52WfA.ttf",
  "100italic": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpjgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRXfbLLIEsKh5SPZWs.ttf",
  "200italic": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpkgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRXfbJnAWsgqZiGfHK5.ttf",
  "300italic": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpkgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRXfbIDAmsgqZiGfHK5.ttf",
  "regular": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpvgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRnf4CrCEo4gg.ttf",
  "italic": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlphgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRXfYqvKk8ogoSP.ttf",
  "500italic": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpkgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRXfbJbA2sgqZiGfHK5.ttf",
  "600italic": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpkgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRXfbJ3BGsgqZiGfHK5.ttf",
  "700italic": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpkgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRXfbITBWsgqZiGfHK5.ttf",
  "800italic": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpkgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRXfbIPBmsgqZiGfHK5.ttf",
  "900italic": "http://fonts.gstatic.com/s/barlowsemicondensed/v14/wlpkgxjLBV1hqnzfr-F8sEYMB0Yybp0mudRXfbIrB2sgqZiGfHK5.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Barriecito",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/barriecito/v17/WWXXlj-CbBOSLY2QTuY_KdUiYwTO0MU.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Barrio",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/barrio/v19/wEO8EBXBk8hBIDiEdQYhWdsX1Q.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Basic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/basic/v17/xfu_0WLxV2_XKQN34lDVyR7D.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baskervville",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/baskervville/v13/YA9Ur0yU4l_XOrogbkun3kQgt5OohvbJ9A.ttf",
  "italic": "http://fonts.gstatic.com/s/baskervville/v13/YA9Kr0yU4l_XOrogbkun3kQQtZmspPPZ9Mlt.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Battambang",
  "variants": [
  "100",
  "300",
  "regular",
  "700",
  "900"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-04-20",
  "files": {
  "100": "http://fonts.gstatic.com/s/battambang/v24/uk-kEGe7raEw-HjkzZabNhGp5w50_o9T7Q.ttf",
  "300": "http://fonts.gstatic.com/s/battambang/v24/uk-lEGe7raEw-HjkzZabNtmLxyRa8oZK9I0.ttf",
  "700": "http://fonts.gstatic.com/s/battambang/v24/uk-lEGe7raEw-HjkzZabNsmMxyRa8oZK9I0.ttf",
  "900": "http://fonts.gstatic.com/s/battambang/v24/uk-lEGe7raEw-HjkzZabNvGOxyRa8oZK9I0.ttf",
  "regular": "http://fonts.gstatic.com/s/battambang/v24/uk-mEGe7raEw-HjkzZabDnWj4yxx7o8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Baumans",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-04-20",
  "files": {
  "regular": "http://fonts.gstatic.com/s/baumans/v17/-W_-XJj9QyTd3QfpR_oyaksqY5Q.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bayon",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v29",
  "lastModified": "2022-04-20",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bayon/v29/9XUrlJNmn0LPFl-pOhYEd2NJ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Be Vietnam Pro",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVNSTAyLFyeg_IDWvOJmVES_HRUBX8YYbAiah8.ttf",
  "200": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVMSTAyLFyeg_IDWvOJmVES_HT4JF8yT7wrcwap.ttf",
  "300": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVMSTAyLFyeg_IDWvOJmVES_HScJ18yT7wrcwap.ttf",
  "500": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVMSTAyLFyeg_IDWvOJmVES_HTEJl8yT7wrcwap.ttf",
  "600": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVMSTAyLFyeg_IDWvOJmVES_HToIV8yT7wrcwap.ttf",
  "700": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVMSTAyLFyeg_IDWvOJmVES_HSMIF8yT7wrcwap.ttf",
  "800": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVMSTAyLFyeg_IDWvOJmVES_HSQI18yT7wrcwap.ttf",
  "900": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVMSTAyLFyeg_IDWvOJmVES_HS0Il8yT7wrcwap.ttf",
  "100italic": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVLSTAyLFyeg_IDWvOJmVES_HwyPRsSZZIneh-waA.ttf",
  "200italic": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVKSTAyLFyeg_IDWvOJmVES_HwyPbczRbgJdhapcUU.ttf",
  "300italic": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVKSTAyLFyeg_IDWvOJmVES_HwyPdMwRbgJdhapcUU.ttf",
  "regular": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVPSTAyLFyeg_IDWvOJmVES_EwwD3s6ZKAi.ttf",
  "italic": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVNSTAyLFyeg_IDWvOJmVES_HwyBX8YYbAiah8.ttf",
  "500italic": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVKSTAyLFyeg_IDWvOJmVES_HwyPYsxRbgJdhapcUU.ttf",
  "600italic": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVKSTAyLFyeg_IDWvOJmVES_HwyPac2RbgJdhapcUU.ttf",
  "700italic": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVKSTAyLFyeg_IDWvOJmVES_HwyPcM3RbgJdhapcUU.ttf",
  "800italic": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVKSTAyLFyeg_IDWvOJmVES_HwyPd80RbgJdhapcUU.ttf",
  "900italic": "http://fonts.gstatic.com/s/bevietnampro/v10/QdVKSTAyLFyeg_IDWvOJmVES_HwyPfs1RbgJdhapcUU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Beau Rivage",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/beaurivage/v2/UcCi3FIgIG2bH4mMNWJUlmg3NZp8K2sL.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bebas Neue",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bebasneue/v9/JTUSjIg69CK48gW7PXooxW5rygbi49c.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Belgrano",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/belgrano/v18/55xvey5tM9rwKWrJZcMFirl08KDJ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bellefair",
  "variants": [
  "regular"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bellefair/v14/kJExBuYY6AAuhiXUxG19__A2pOdvDA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Belleza",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/belleza/v17/0nkoC9_pNeMfhX4BtcbyawzruP8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bellota",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/bellota/v16/MwQzbhXl3_qEpiwAID55kGMViblPtXs.ttf",
  "700": "http://fonts.gstatic.com/s/bellota/v16/MwQzbhXl3_qEpiwAIC5-kGMViblPtXs.ttf",
  "300italic": "http://fonts.gstatic.com/s/bellota/v16/MwQxbhXl3_qEpiwAKJBjHGEfjZtKpXulTQ.ttf",
  "regular": "http://fonts.gstatic.com/s/bellota/v16/MwQ2bhXl3_qEpiwAGJJRtGs-lbA.ttf",
  "italic": "http://fonts.gstatic.com/s/bellota/v16/MwQ0bhXl3_qEpiwAKJBbsEk7hbBWrA.ttf",
  "700italic": "http://fonts.gstatic.com/s/bellota/v16/MwQxbhXl3_qEpiwAKJBjDGYfjZtKpXulTQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bellota Text",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/bellotatext/v16/0FlMVP2VnlWS4f3-UE9hHXM5VfsqfQXwQy6yxg.ttf",
  "700": "http://fonts.gstatic.com/s/bellotatext/v16/0FlMVP2VnlWS4f3-UE9hHXM5RfwqfQXwQy6yxg.ttf",
  "300italic": "http://fonts.gstatic.com/s/bellotatext/v16/0FlOVP2VnlWS4f3-UE9hHXMx--Gmfw_0YSuixmYK.ttf",
  "regular": "http://fonts.gstatic.com/s/bellotatext/v16/0FlTVP2VnlWS4f3-UE9hHXMB-dMOdS7sSg.ttf",
  "italic": "http://fonts.gstatic.com/s/bellotatext/v16/0FlNVP2VnlWS4f3-UE9hHXMx-9kKVyv8Sjer.ttf",
  "700italic": "http://fonts.gstatic.com/s/bellotatext/v16/0FlOVP2VnlWS4f3-UE9hHXMx--G2eA_0YSuixmYK.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "BenchNine",
  "variants": [
  "300",
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/benchnine/v16/ahcev8612zF4jxrwMosT--tRhWa8q0v8ag.ttf",
  "700": "http://fonts.gstatic.com/s/benchnine/v16/ahcev8612zF4jxrwMosT6-xRhWa8q0v8ag.ttf",
  "regular": "http://fonts.gstatic.com/s/benchnine/v16/ahcbv8612zF4jxrwMosrV8N1jU2gog.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Benne",
  "variants": [
  "regular"
  ],
  "subsets": [
  "kannada",
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/benne/v22/L0xzDFAhn18E6Vjxlt6qTDBN.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bentham",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bentham/v18/VdGeAZQPEpYfmHglKWw7CJaK_y4.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Berkshire Swash",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/berkshireswash/v16/ptRRTi-cavZOGqCvnNJDl5m5XmNPrcQybX4pQA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Besley",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/besley/v12/PlIhFlO1MaNwaNGWUC92IOH_mtG4fYTBSdRoFPOl8-E.ttf",
  "600": "http://fonts.gstatic.com/s/besley/v12/PlIhFlO1MaNwaNGWUC92IOH_mtG4fWjGSdRoFPOl8-E.ttf",
  "700": "http://fonts.gstatic.com/s/besley/v12/PlIhFlO1MaNwaNGWUC92IOH_mtG4fVHGSdRoFPOl8-E.ttf",
  "800": "http://fonts.gstatic.com/s/besley/v12/PlIhFlO1MaNwaNGWUC92IOH_mtG4fTbGSdRoFPOl8-E.ttf",
  "900": "http://fonts.gstatic.com/s/besley/v12/PlIhFlO1MaNwaNGWUC92IOH_mtG4fR_GSdRoFPOl8-E.ttf",
  "regular": "http://fonts.gstatic.com/s/besley/v12/PlIhFlO1MaNwaNGWUC92IOH_mtG4fbbBSdRoFPOl8-E.ttf",
  "italic": "http://fonts.gstatic.com/s/besley/v12/PlIjFlO1MaNwaNG8WR2J-IiUAH-_aH6CoZdiENGg4-E04A.ttf",
  "500italic": "http://fonts.gstatic.com/s/besley/v12/PlIjFlO1MaNwaNG8WR2J-IiUAH-_aH6Ck5diENGg4-E04A.ttf",
  "600italic": "http://fonts.gstatic.com/s/besley/v12/PlIjFlO1MaNwaNG8WR2J-IiUAH-_aH6Cf5BiENGg4-E04A.ttf",
  "700italic": "http://fonts.gstatic.com/s/besley/v12/PlIjFlO1MaNwaNG8WR2J-IiUAH-_aH6CRpBiENGg4-E04A.ttf",
  "800italic": "http://fonts.gstatic.com/s/besley/v12/PlIjFlO1MaNwaNG8WR2J-IiUAH-_aH6CIZBiENGg4-E04A.ttf",
  "900italic": "http://fonts.gstatic.com/s/besley/v12/PlIjFlO1MaNwaNG8WR2J-IiUAH-_aH6CCJBiENGg4-E04A.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Beth Ellen",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-04-20",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bethellen/v17/WwkbxPW2BE-3rb_JNT-qEIAiVNo5xNY.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bevan",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bevan/v20/4iCj6KZ0a9NXjF8aUir7tlSJ.ttf",
  "italic": "http://fonts.gstatic.com/s/bevan/v20/4iCt6KZ0a9NXjG8YWC7Zs0SJD4U.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "BhuTuka Expanded One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "gurmukhi",
  "latin",
  "latin-ext"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bhutukaexpandedone/v2/SLXXc0jZ4WUJcClHTtv0t7IaDRsBsWRiJCyX8pg_RVH1.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Big Shoulders Display",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/bigshouldersdisplay/v15/fC1MPZJEZG-e9gHhdI4-NBbfd2ys3SjJCx12wPgf9g-_3F0YdY86JF46SRP4yZQ.ttf",
  "200": "http://fonts.gstatic.com/s/bigshouldersdisplay/v15/fC1MPZJEZG-e9gHhdI4-NBbfd2ys3SjJCx12wPgf9g-_3F0YdQ87JF46SRP4yZQ.ttf",
  "300": "http://fonts.gstatic.com/s/bigshouldersdisplay/v15/fC1MPZJEZG-e9gHhdI4-NBbfd2ys3SjJCx12wPgf9g-_3F0YddE7JF46SRP4yZQ.ttf",
  "500": "http://fonts.gstatic.com/s/bigshouldersdisplay/v15/fC1MPZJEZG-e9gHhdI4-NBbfd2ys3SjJCx12wPgf9g-_3F0Ydb07JF46SRP4yZQ.ttf",
  "600": "http://fonts.gstatic.com/s/bigshouldersdisplay/v15/fC1MPZJEZG-e9gHhdI4-NBbfd2ys3SjJCx12wPgf9g-_3F0YdVE8JF46SRP4yZQ.ttf",
  "700": "http://fonts.gstatic.com/s/bigshouldersdisplay/v15/fC1MPZJEZG-e9gHhdI4-NBbfd2ys3SjJCx12wPgf9g-_3F0YdWg8JF46SRP4yZQ.ttf",
  "800": "http://fonts.gstatic.com/s/bigshouldersdisplay/v15/fC1MPZJEZG-e9gHhdI4-NBbfd2ys3SjJCx12wPgf9g-_3F0YdQ88JF46SRP4yZQ.ttf",
  "900": "http://fonts.gstatic.com/s/bigshouldersdisplay/v15/fC1MPZJEZG-e9gHhdI4-NBbfd2ys3SjJCx12wPgf9g-_3F0YdSY8JF46SRP4yZQ.ttf",
  "regular": "http://fonts.gstatic.com/s/bigshouldersdisplay/v15/fC1MPZJEZG-e9gHhdI4-NBbfd2ys3SjJCx12wPgf9g-_3F0YdY87JF46SRP4yZQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Big Shoulders Inline Display",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/bigshouldersinlinedisplay/v21/_LOumyfF4eSU_SCrJc9OI24U7siGvBGcZqmqV9-ZZ85CGNOFeNLxoYMPJ0nBEnR5yPc2Huux.ttf",
  "200": "http://fonts.gstatic.com/s/bigshouldersinlinedisplay/v21/_LOumyfF4eSU_SCrJc9OI24U7siGvBGcZqmqV9-ZZ85CGNOFeNLxoYMPJ0lBE3R5yPc2Huux.ttf",
  "300": "http://fonts.gstatic.com/s/bigshouldersinlinedisplay/v21/_LOumyfF4eSU_SCrJc9OI24U7siGvBGcZqmqV9-ZZ85CGNOFeNLxoYMPJ0mfE3R5yPc2Huux.ttf",
  "500": "http://fonts.gstatic.com/s/bigshouldersinlinedisplay/v21/_LOumyfF4eSU_SCrJc9OI24U7siGvBGcZqmqV9-ZZ85CGNOFeNLxoYMPJ0nzE3R5yPc2Huux.ttf",
  "600": "http://fonts.gstatic.com/s/bigshouldersinlinedisplay/v21/_LOumyfF4eSU_SCrJc9OI24U7siGvBGcZqmqV9-ZZ85CGNOFeNLxoYMPJ0kfFHR5yPc2Huux.ttf",
  "700": "http://fonts.gstatic.com/s/bigshouldersinlinedisplay/v21/_LOumyfF4eSU_SCrJc9OI24U7siGvBGcZqmqV9-ZZ85CGNOFeNLxoYMPJ0kmFHR5yPc2Huux.ttf",
  "800": "http://fonts.gstatic.com/s/bigshouldersinlinedisplay/v21/_LOumyfF4eSU_SCrJc9OI24U7siGvBGcZqmqV9-ZZ85CGNOFeNLxoYMPJ0lBFHR5yPc2Huux.ttf",
  "900": "http://fonts.gstatic.com/s/bigshouldersinlinedisplay/v21/_LOumyfF4eSU_SCrJc9OI24U7siGvBGcZqmqV9-ZZ85CGNOFeNLxoYMPJ0loFHR5yPc2Huux.ttf",
  "regular": "http://fonts.gstatic.com/s/bigshouldersinlinedisplay/v21/_LOumyfF4eSU_SCrJc9OI24U7siGvBGcZqmqV9-ZZ85CGNOFeNLxoYMPJ0nBE3R5yPc2Huux.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Big Shoulders Inline Text",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/bigshouldersinlinetext/v21/vm8XdQDmVECV5-vm5dJ-Tp-6WDeRjL4RV7dP8u-NMyHY74qpoNNcwga0yqGN7Y6Jsc8c.ttf",
  "200": "http://fonts.gstatic.com/s/bigshouldersinlinetext/v21/vm8XdQDmVECV5-vm5dJ-Tp-6WDeRjL4RV7dP8u-NMyHY74qpoNNcwgY0y6GN7Y6Jsc8c.ttf",
  "300": "http://fonts.gstatic.com/s/bigshouldersinlinetext/v21/vm8XdQDmVECV5-vm5dJ-Tp-6WDeRjL4RV7dP8u-NMyHY74qpoNNcwgbqy6GN7Y6Jsc8c.ttf",
  "500": "http://fonts.gstatic.com/s/bigshouldersinlinetext/v21/vm8XdQDmVECV5-vm5dJ-Tp-6WDeRjL4RV7dP8u-NMyHY74qpoNNcwgaGy6GN7Y6Jsc8c.ttf",
  "600": "http://fonts.gstatic.com/s/bigshouldersinlinetext/v21/vm8XdQDmVECV5-vm5dJ-Tp-6WDeRjL4RV7dP8u-NMyHY74qpoNNcwgZqzKGN7Y6Jsc8c.ttf",
  "700": "http://fonts.gstatic.com/s/bigshouldersinlinetext/v21/vm8XdQDmVECV5-vm5dJ-Tp-6WDeRjL4RV7dP8u-NMyHY74qpoNNcwgZTzKGN7Y6Jsc8c.ttf",
  "800": "http://fonts.gstatic.com/s/bigshouldersinlinetext/v21/vm8XdQDmVECV5-vm5dJ-Tp-6WDeRjL4RV7dP8u-NMyHY74qpoNNcwgY0zKGN7Y6Jsc8c.ttf",
  "900": "http://fonts.gstatic.com/s/bigshouldersinlinetext/v21/vm8XdQDmVECV5-vm5dJ-Tp-6WDeRjL4RV7dP8u-NMyHY74qpoNNcwgYdzKGN7Y6Jsc8c.ttf",
  "regular": "http://fonts.gstatic.com/s/bigshouldersinlinetext/v21/vm8XdQDmVECV5-vm5dJ-Tp-6WDeRjL4RV7dP8u-NMyHY74qpoNNcwga0y6GN7Y6Jsc8c.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Big Shoulders Stencil Display",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/bigshouldersstencildisplay/v21/6aeZ4LS6U6pR_bp5b_t2ugOhHWFcxSGP9ttD96KCb8xPytKb-oPRU-vkuLm_O0nPKHznJucP9w.ttf",
  "200": "http://fonts.gstatic.com/s/bigshouldersstencildisplay/v21/6aeZ4LS6U6pR_bp5b_t2ugOhHWFcxSGP9ttD96KCb8xPytKb-oPRU-vkuLm_u0jPKHznJucP9w.ttf",
  "300": "http://fonts.gstatic.com/s/bigshouldersstencildisplay/v21/6aeZ4LS6U6pR_bp5b_t2ugOhHWFcxSGP9ttD96KCb8xPytKb-oPRU-vkuLm_ZUjPKHznJucP9w.ttf",
  "500": "http://fonts.gstatic.com/s/bigshouldersstencildisplay/v21/6aeZ4LS6U6pR_bp5b_t2ugOhHWFcxSGP9ttD96KCb8xPytKb-oPRU-vkuLm_CUjPKHznJucP9w.ttf",
  "600": "http://fonts.gstatic.com/s/bigshouldersstencildisplay/v21/6aeZ4LS6U6pR_bp5b_t2ugOhHWFcxSGP9ttD96KCb8xPytKb-oPRU-vkuLm_5U_PKHznJucP9w.ttf",
  "700": "http://fonts.gstatic.com/s/bigshouldersstencildisplay/v21/6aeZ4LS6U6pR_bp5b_t2ugOhHWFcxSGP9ttD96KCb8xPytKb-oPRU-vkuLm_3E_PKHznJucP9w.ttf",
  "800": "http://fonts.gstatic.com/s/bigshouldersstencildisplay/v21/6aeZ4LS6U6pR_bp5b_t2ugOhHWFcxSGP9ttD96KCb8xPytKb-oPRU-vkuLm_u0_PKHznJucP9w.ttf",
  "900": "http://fonts.gstatic.com/s/bigshouldersstencildisplay/v21/6aeZ4LS6U6pR_bp5b_t2ugOhHWFcxSGP9ttD96KCb8xPytKb-oPRU-vkuLm_kk_PKHznJucP9w.ttf",
  "regular": "http://fonts.gstatic.com/s/bigshouldersstencildisplay/v21/6aeZ4LS6U6pR_bp5b_t2ugOhHWFcxSGP9ttD96KCb8xPytKb-oPRU-vkuLm_O0jPKHznJucP9w.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Big Shoulders Stencil Text",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/bigshouldersstenciltext/v21/5aUV9-i2oxDMNwY3dHfW7UAt3Q453SM15wNj53bCcab2SJYLLUtk1OGR04XIGS_Py_AWbQ.ttf",
  "200": "http://fonts.gstatic.com/s/bigshouldersstenciltext/v21/5aUV9-i2oxDMNwY3dHfW7UAt3Q453SM15wNj53bCcab2SJYLLUtk1OGRU4TIGS_Py_AWbQ.ttf",
  "300": "http://fonts.gstatic.com/s/bigshouldersstenciltext/v21/5aUV9-i2oxDMNwY3dHfW7UAt3Q453SM15wNj53bCcab2SJYLLUtk1OGRjYTIGS_Py_AWbQ.ttf",
  "500": "http://fonts.gstatic.com/s/bigshouldersstenciltext/v21/5aUV9-i2oxDMNwY3dHfW7UAt3Q453SM15wNj53bCcab2SJYLLUtk1OGR4YTIGS_Py_AWbQ.ttf",
  "600": "http://fonts.gstatic.com/s/bigshouldersstenciltext/v21/5aUV9-i2oxDMNwY3dHfW7UAt3Q453SM15wNj53bCcab2SJYLLUtk1OGRDYPIGS_Py_AWbQ.ttf",
  "700": "http://fonts.gstatic.com/s/bigshouldersstenciltext/v21/5aUV9-i2oxDMNwY3dHfW7UAt3Q453SM15wNj53bCcab2SJYLLUtk1OGRNIPIGS_Py_AWbQ.ttf",
  "800": "http://fonts.gstatic.com/s/bigshouldersstenciltext/v21/5aUV9-i2oxDMNwY3dHfW7UAt3Q453SM15wNj53bCcab2SJYLLUtk1OGRU4PIGS_Py_AWbQ.ttf",
  "900": "http://fonts.gstatic.com/s/bigshouldersstenciltext/v21/5aUV9-i2oxDMNwY3dHfW7UAt3Q453SM15wNj53bCcab2SJYLLUtk1OGReoPIGS_Py_AWbQ.ttf",
  "regular": "http://fonts.gstatic.com/s/bigshouldersstenciltext/v21/5aUV9-i2oxDMNwY3dHfW7UAt3Q453SM15wNj53bCcab2SJYLLUtk1OGR04TIGS_Py_AWbQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Big Shoulders Text",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/bigshoulderstext/v17/55xEezRtP9G3CGPIf49hxc8P0eytUxB2l66LmF6xc3kA3Y-r3TIPNl6P2pc.ttf",
  "200": "http://fonts.gstatic.com/s/bigshoulderstext/v17/55xEezRtP9G3CGPIf49hxc8P0eytUxB2l66LmF6xc3kA3Q-q3TIPNl6P2pc.ttf",
  "300": "http://fonts.gstatic.com/s/bigshoulderstext/v17/55xEezRtP9G3CGPIf49hxc8P0eytUxB2l66LmF6xc3kA3dGq3TIPNl6P2pc.ttf",
  "500": "http://fonts.gstatic.com/s/bigshoulderstext/v17/55xEezRtP9G3CGPIf49hxc8P0eytUxB2l66LmF6xc3kA3b2q3TIPNl6P2pc.ttf",
  "600": "http://fonts.gstatic.com/s/bigshoulderstext/v17/55xEezRtP9G3CGPIf49hxc8P0eytUxB2l66LmF6xc3kA3VGt3TIPNl6P2pc.ttf",
  "700": "http://fonts.gstatic.com/s/bigshoulderstext/v17/55xEezRtP9G3CGPIf49hxc8P0eytUxB2l66LmF6xc3kA3Wit3TIPNl6P2pc.ttf",
  "800": "http://fonts.gstatic.com/s/bigshoulderstext/v17/55xEezRtP9G3CGPIf49hxc8P0eytUxB2l66LmF6xc3kA3Q-t3TIPNl6P2pc.ttf",
  "900": "http://fonts.gstatic.com/s/bigshoulderstext/v17/55xEezRtP9G3CGPIf49hxc8P0eytUxB2l66LmF6xc3kA3Sat3TIPNl6P2pc.ttf",
  "regular": "http://fonts.gstatic.com/s/bigshoulderstext/v17/55xEezRtP9G3CGPIf49hxc8P0eytUxB2l66LmF6xc3kA3Y-q3TIPNl6P2pc.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bigelow Rules",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bigelowrules/v23/RrQWboly8iR_I3KWSzeRuN0zT4cCH8WAJVk.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bigshot One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bigshotone/v25/u-470qukhRkkO6BD_7cM_gxuUQJBXv_-.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bilbo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bilbo/v20/o-0EIpgpwWwZ210hpIRz4wxE.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bilbo Swash Caps",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bilboswashcaps/v22/zrf-0GXbz-H3Wb4XBsGrTgq2PVmdqAPopiRfKp8.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "BioRhyme",
  "variants": [
  "200",
  "300",
  "regular",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/biorhyme/v12/1cX3aULHBpDMsHYW_ESOjnGAq8Sk1PoH.ttf",
  "300": "http://fonts.gstatic.com/s/biorhyme/v12/1cX3aULHBpDMsHYW_ETqjXGAq8Sk1PoH.ttf",
  "700": "http://fonts.gstatic.com/s/biorhyme/v12/1cX3aULHBpDMsHYW_ET6inGAq8Sk1PoH.ttf",
  "800": "http://fonts.gstatic.com/s/biorhyme/v12/1cX3aULHBpDMsHYW_ETmiXGAq8Sk1PoH.ttf",
  "regular": "http://fonts.gstatic.com/s/biorhyme/v12/1cXwaULHBpDMsHYW_HxGpVWIgNit.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "BioRhyme Expanded",
  "variants": [
  "200",
  "300",
  "regular",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/biorhymeexpanded/v19/i7dVIE1zZzytGswgU577CDY9LjbffxxcblSHSdTXrb_z.ttf",
  "300": "http://fonts.gstatic.com/s/biorhymeexpanded/v19/i7dVIE1zZzytGswgU577CDY9Ljbffxw4bVSHSdTXrb_z.ttf",
  "700": "http://fonts.gstatic.com/s/biorhymeexpanded/v19/i7dVIE1zZzytGswgU577CDY9LjbffxwoalSHSdTXrb_z.ttf",
  "800": "http://fonts.gstatic.com/s/biorhymeexpanded/v19/i7dVIE1zZzytGswgU577CDY9Ljbffxw0aVSHSdTXrb_z.ttf",
  "regular": "http://fonts.gstatic.com/s/biorhymeexpanded/v19/i7dQIE1zZzytGswgU577CDY9LjbffySURXCPYsje.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Birthstone",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/birthstone/v10/8AtsGs2xO4yLRhy87sv_HLn5jRfZHzM.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Birthstone Bounce",
  "variants": [
  "regular",
  "500"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/birthstonebounce/v9/ga6SaxZF43lIvTWrktHOTBJZGH7dEd29MacQJZP1LmD9.ttf",
  "regular": "http://fonts.gstatic.com/s/birthstonebounce/v9/ga6XaxZF43lIvTWrktHOTBJZGH7dEeVJGIMYDo_8.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Biryani",
  "variants": [
  "200",
  "300",
  "regular",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/biryani/v13/hv-TlzNxIFoO84YddYQyGTBSU-J-RxQ.ttf",
  "300": "http://fonts.gstatic.com/s/biryani/v13/hv-TlzNxIFoO84YddeAxGTBSU-J-RxQ.ttf",
  "600": "http://fonts.gstatic.com/s/biryani/v13/hv-TlzNxIFoO84YddZQ3GTBSU-J-RxQ.ttf",
  "700": "http://fonts.gstatic.com/s/biryani/v13/hv-TlzNxIFoO84YddfA2GTBSU-J-RxQ.ttf",
  "800": "http://fonts.gstatic.com/s/biryani/v13/hv-TlzNxIFoO84Yddew1GTBSU-J-RxQ.ttf",
  "900": "http://fonts.gstatic.com/s/biryani/v13/hv-TlzNxIFoO84Yddcg0GTBSU-J-RxQ.ttf",
  "regular": "http://fonts.gstatic.com/s/biryani/v13/hv-WlzNxIFoO84YdTUwZPTh5T-s.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bitter",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v28",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/bitter/v28/raxhHiqOu8IVPmnRc6SY1KXhnF_Y8fbeCL_EXFh2reU.ttf",
  "200": "http://fonts.gstatic.com/s/bitter/v28/raxhHiqOu8IVPmnRc6SY1KXhnF_Y8XbfCL_EXFh2reU.ttf",
  "300": "http://fonts.gstatic.com/s/bitter/v28/raxhHiqOu8IVPmnRc6SY1KXhnF_Y8ajfCL_EXFh2reU.ttf",
  "500": "http://fonts.gstatic.com/s/bitter/v28/raxhHiqOu8IVPmnRc6SY1KXhnF_Y8cTfCL_EXFh2reU.ttf",
  "600": "http://fonts.gstatic.com/s/bitter/v28/raxhHiqOu8IVPmnRc6SY1KXhnF_Y8SjYCL_EXFh2reU.ttf",
  "700": "http://fonts.gstatic.com/s/bitter/v28/raxhHiqOu8IVPmnRc6SY1KXhnF_Y8RHYCL_EXFh2reU.ttf",
  "800": "http://fonts.gstatic.com/s/bitter/v28/raxhHiqOu8IVPmnRc6SY1KXhnF_Y8XbYCL_EXFh2reU.ttf",
  "900": "http://fonts.gstatic.com/s/bitter/v28/raxhHiqOu8IVPmnRc6SY1KXhnF_Y8V_YCL_EXFh2reU.ttf",
  "regular": "http://fonts.gstatic.com/s/bitter/v28/raxhHiqOu8IVPmnRc6SY1KXhnF_Y8fbfCL_EXFh2reU.ttf",
  "100italic": "http://fonts.gstatic.com/s/bitter/v28/raxjHiqOu8IVPmn7epZnDMyKBvHf5D6c4P3OWHpzveWxBw.ttf",
  "200italic": "http://fonts.gstatic.com/s/bitter/v28/raxjHiqOu8IVPmn7epZnDMyKBvHf5D6cYPzOWHpzveWxBw.ttf",
  "300italic": "http://fonts.gstatic.com/s/bitter/v28/raxjHiqOu8IVPmn7epZnDMyKBvHf5D6cvvzOWHpzveWxBw.ttf",
  "italic": "http://fonts.gstatic.com/s/bitter/v28/raxjHiqOu8IVPmn7epZnDMyKBvHf5D6c4PzOWHpzveWxBw.ttf",
  "500italic": "http://fonts.gstatic.com/s/bitter/v28/raxjHiqOu8IVPmn7epZnDMyKBvHf5D6c0vzOWHpzveWxBw.ttf",
  "600italic": "http://fonts.gstatic.com/s/bitter/v28/raxjHiqOu8IVPmn7epZnDMyKBvHf5D6cPvvOWHpzveWxBw.ttf",
  "700italic": "http://fonts.gstatic.com/s/bitter/v28/raxjHiqOu8IVPmn7epZnDMyKBvHf5D6cB_vOWHpzveWxBw.ttf",
  "800italic": "http://fonts.gstatic.com/s/bitter/v28/raxjHiqOu8IVPmn7epZnDMyKBvHf5D6cYPvOWHpzveWxBw.ttf",
  "900italic": "http://fonts.gstatic.com/s/bitter/v28/raxjHiqOu8IVPmn7epZnDMyKBvHf5D6cSfvOWHpzveWxBw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Black And White Picture",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/blackandwhitepicture/v22/TwMe-JAERlQd3ooUHBUXGmrmioKjjnRSFO-NqI5HbcMi-yWY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Black Han Sans",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/blackhansans/v15/ea8Aad44WunzF9a-dL6toA8r8nqVIXSkH-Hc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Black Ops One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/blackopsone/v20/qWcsB6-ypo7xBdr6Xshe96H3WDzRtjkho4M.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Blaka",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/blaka/v3/8vIG7w8722p_6kdr20D2FV5e.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Blaka Hollow",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/blakahollow/v3/MCoUzAL91sjRE2FsKsxUtezYB9oFyW_-oA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Blaka Ink",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v5",
  "lastModified": "2022-09-14",
  "files": {
  "regular": "http://fonts.gstatic.com/s/blakaink/v5/AlZy_zVVtpj22Znag2chdXf4XB0Tow.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Blinker",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/blinker/v12/cIf_MaFatEE-VTaP_E2hZEsCkIt9QQ.ttf",
  "200": "http://fonts.gstatic.com/s/blinker/v12/cIf4MaFatEE-VTaP_OGARGEsnIJkWL4.ttf",
  "300": "http://fonts.gstatic.com/s/blinker/v12/cIf4MaFatEE-VTaP_IWDRGEsnIJkWL4.ttf",
  "600": "http://fonts.gstatic.com/s/blinker/v12/cIf4MaFatEE-VTaP_PGFRGEsnIJkWL4.ttf",
  "700": "http://fonts.gstatic.com/s/blinker/v12/cIf4MaFatEE-VTaP_JWERGEsnIJkWL4.ttf",
  "800": "http://fonts.gstatic.com/s/blinker/v12/cIf4MaFatEE-VTaP_ImHRGEsnIJkWL4.ttf",
  "900": "http://fonts.gstatic.com/s/blinker/v12/cIf4MaFatEE-VTaP_K2GRGEsnIJkWL4.ttf",
  "regular": "http://fonts.gstatic.com/s/blinker/v12/cIf9MaFatEE-VTaPxCmrYGkHgIs.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bodoni Moda",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT67PxzY382XsXX63LUYL6GYFcan6NJrKp-VPjfJMShrpsGFUt8oXzawIBytVjMYwE.ttf",
  "600": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT67PxzY382XsXX63LUYL6GYFcan6NJrKp-VPjfJMShrpsGFUt8oZDdwIBytVjMYwE.ttf",
  "700": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT67PxzY382XsXX63LUYL6GYFcan6NJrKp-VPjfJMShrpsGFUt8oandwIBytVjMYwE.ttf",
  "800": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT67PxzY382XsXX63LUYL6GYFcan6NJrKp-VPjfJMShrpsGFUt8oc7dwIBytVjMYwE.ttf",
  "900": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT67PxzY382XsXX63LUYL6GYFcan6NJrKp-VPjfJMShrpsGFUt8oefdwIBytVjMYwE.ttf",
  "regular": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT67PxzY382XsXX63LUYL6GYFcan6NJrKp-VPjfJMShrpsGFUt8oU7awIBytVjMYwE.ttf",
  "italic": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT07PxzY382XsXX63LUYJSPUqb0pL6OQqxrZLnVbvZedvJtj-V7tIaZKMN4sXrJcwHqoQ.ttf",
  "500italic": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT07PxzY382XsXX63LUYJSPUqb0pL6OQqxrZLnVbvZedvJtj-V7tIaZGsN4sXrJcwHqoQ.ttf",
  "600italic": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT07PxzY382XsXX63LUYJSPUqb0pL6OQqxrZLnVbvZedvJtj-V7tIaZ9sR4sXrJcwHqoQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT07PxzY382XsXX63LUYJSPUqb0pL6OQqxrZLnVbvZedvJtj-V7tIaZz8R4sXrJcwHqoQ.ttf",
  "800italic": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT07PxzY382XsXX63LUYJSPUqb0pL6OQqxrZLnVbvZedvJtj-V7tIaZqMR4sXrJcwHqoQ.ttf",
  "900italic": "http://fonts.gstatic.com/s/bodonimoda/v19/aFT07PxzY382XsXX63LUYJSPUqb0pL6OQqxrZLnVbvZedvJtj-V7tIaZgcR4sXrJcwHqoQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bokor",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v30",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bokor/v30/m8JcjfpeeaqTiR2WdInbcaxE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bona Nova",
  "variants": [
  "regular",
  "italic",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "hebrew",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/bonanova/v10/B50IF7ZCpX7fcHfvIUBxN4dOFISeJY8GgQ.ttf",
  "regular": "http://fonts.gstatic.com/s/bonanova/v10/B50NF7ZCpX7fcHfvIUBJi6hqHK-CLA.ttf",
  "italic": "http://fonts.gstatic.com/s/bonanova/v10/B50LF7ZCpX7fcHfvIUB5iaJuPqqSLJYf.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bonbon",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bonbon/v26/0FlVVPeVlFec4ee_cDEAbQY5-A.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bonheur Royale",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bonheurroyale/v9/c4m51nt_GMTrtX-b9GcG4-YRmYK_c0f1N5Ij.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Boogaloo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/boogaloo/v19/kmK-Zq45GAvOdnaW6x1F_SrQo_1K.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bowlby One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bowlbyone/v19/taiPGmVuC4y96PFeqp8smo6C_Z0wcK4.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bowlby One SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bowlbyonesc/v19/DtVlJxerQqQm37tzN3wMug9Pzgj8owhNjuE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Brawler",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/brawler/v19/xn7lYHE3xXewAscGiryUb932eNaPfk8.ttf",
  "regular": "http://fonts.gstatic.com/s/brawler/v19/xn7gYHE3xXewAscGsgC7S9XdZN8.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bree Serif",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/breeserif/v17/4UaHrEJCrhhnVA3DgluAx63j5pN1MwI.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Brygada 1918",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/brygada1918/v21/pe08MI6eKpdGqlF5LANrM--ACNaeo8mTUIR_y12f-V8Wu5O3gbo.ttf",
  "600": "http://fonts.gstatic.com/s/brygada1918/v21/pe08MI6eKpdGqlF5LANrM--ACNaeo8mTUIR_y7GY-V8Wu5O3gbo.ttf",
  "700": "http://fonts.gstatic.com/s/brygada1918/v21/pe08MI6eKpdGqlF5LANrM--ACNaeo8mTUIR_y4iY-V8Wu5O3gbo.ttf",
  "regular": "http://fonts.gstatic.com/s/brygada1918/v21/pe08MI6eKpdGqlF5LANrM--ACNaeo8mTUIR_y2-f-V8Wu5O3gbo.ttf",
  "italic": "http://fonts.gstatic.com/s/brygada1918/v21/pe06MI6eKpdGqlF5LANrM--qAeRhe6D4yip43qfcERwcv7GykboaLg.ttf",
  "500italic": "http://fonts.gstatic.com/s/brygada1918/v21/pe06MI6eKpdGqlF5LANrM--qAeRhe6D4yip43qfcIxwcv7GykboaLg.ttf",
  "600italic": "http://fonts.gstatic.com/s/brygada1918/v21/pe06MI6eKpdGqlF5LANrM--qAeRhe6D4yip43qfczxscv7GykboaLg.ttf",
  "700italic": "http://fonts.gstatic.com/s/brygada1918/v21/pe06MI6eKpdGqlF5LANrM--qAeRhe6D4yip43qfc9hscv7GykboaLg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bubblegum Sans",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bubblegumsans/v16/AYCSpXb_Z9EORv1M5QTjEzMEtdaHzoPPb7R4.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bubbler One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bubblerone/v20/f0Xy0eqj68ppQV9KBLmAouHH26MPePkt.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Buda",
  "variants": [
  "300"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/buda/v25/GFDqWAN8mnyIJSSrG7UBr7pZKA0.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Buenard",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/buenard/v17/OD5GuM6Cyma8FnnsB4vSjGCWALepwss.ttf",
  "regular": "http://fonts.gstatic.com/s/buenard/v17/OD5DuM6Cyma8FnnsPzf9qGi9HL4.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bungee",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bungee/v11/N0bU2SZBIuF2PU_ECn50Kd_PmA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bungee Hairline",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bungeehairline/v18/snfys0G548t04270a_ljTLUVrv-7YB2dQ5ZPqQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bungee Inline",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bungeeinline/v11/Gg8zN58UcgnlCweMrih332VuDGJ1-FEglsc.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bungee Outline",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bungeeoutline/v18/_6_mEDvmVP24UvU2MyiGDslL3Qg3YhJqPXxo.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bungee Shade",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bungeeshade/v11/DtVkJxarWL0t2KdzK3oI_jks7iLSrwFUlw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Bungee Spice",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v8",
  "lastModified": "2022-09-14",
  "files": {
  "regular": "http://fonts.gstatic.com/s/bungeespice/v8/nwpTtK2nIhxE0q-IwgSpZBqCzyI-aMPF7Q.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Butcherman",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/butcherman/v24/2EbiL-thF0loflXUBOdb1zWzq_5uT84.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Butterfly Kids",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/butterflykids/v21/ll8lK2CWTjuqAsXDqlnIbMNs5S4arxFrAX1D.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cabin",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v26",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/cabin/v26/u-4X0qWljRw-PfU81xCKCpdpbgZJl6XFpfEd7eA9BIxxkW-EL7Gvxm7rE_s.ttf",
  "600": "http://fonts.gstatic.com/s/cabin/v26/u-4X0qWljRw-PfU81xCKCpdpbgZJl6XFpfEd7eA9BIxxkYODL7Gvxm7rE_s.ttf",
  "700": "http://fonts.gstatic.com/s/cabin/v26/u-4X0qWljRw-PfU81xCKCpdpbgZJl6XFpfEd7eA9BIxxkbqDL7Gvxm7rE_s.ttf",
  "regular": "http://fonts.gstatic.com/s/cabin/v26/u-4X0qWljRw-PfU81xCKCpdpbgZJl6XFpfEd7eA9BIxxkV2EL7Gvxm7rE_s.ttf",
  "italic": "http://fonts.gstatic.com/s/cabin/v26/u-4V0qWljRw-Pd815fNqc8T_wAFcX-c37MPiNYlWniJ2hJXHx_KlwkzuA_u1Bg.ttf",
  "500italic": "http://fonts.gstatic.com/s/cabin/v26/u-4V0qWljRw-Pd815fNqc8T_wAFcX-c37MPiNYlWniJ2hJXH9fKlwkzuA_u1Bg.ttf",
  "600italic": "http://fonts.gstatic.com/s/cabin/v26/u-4V0qWljRw-Pd815fNqc8T_wAFcX-c37MPiNYlWniJ2hJXHGfWlwkzuA_u1Bg.ttf",
  "700italic": "http://fonts.gstatic.com/s/cabin/v26/u-4V0qWljRw-Pd815fNqc8T_wAFcX-c37MPiNYlWniJ2hJXHIPWlwkzuA_u1Bg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cabin Condensed",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/cabincondensed/v19/nwpJtK6mNhBK2err_hqkYhHRqmwilMH97F15-K1oqQ.ttf",
  "600": "http://fonts.gstatic.com/s/cabincondensed/v19/nwpJtK6mNhBK2err_hqkYhHRqmwiuMb97F15-K1oqQ.ttf",
  "700": "http://fonts.gstatic.com/s/cabincondensed/v19/nwpJtK6mNhBK2err_hqkYhHRqmwi3Mf97F15-K1oqQ.ttf",
  "regular": "http://fonts.gstatic.com/s/cabincondensed/v19/nwpMtK6mNhBK2err_hqkYhHRqmwaYOjZ5HZl8Q.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cabin Sketch",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/cabinsketch/v19/QGY2z_kZZAGCONcK2A4bGOj0I_1o4dLyI4CMFw.ttf",
  "regular": "http://fonts.gstatic.com/s/cabinsketch/v19/QGYpz_kZZAGCONcK2A4bGOjMn9JM6fnuKg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Caesar Dressing",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/caesardressing/v21/yYLx0hLa3vawqtwdswbotmK4vrR3cbb6LZttyg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cagliostro",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cagliostro/v21/ZgNWjP5HM73BV5amnX-TjGXEM4COoE4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cairo",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/cairo/v20/SLXVc1nY6HkvangtZmpcWmhzfH5l2WgsQSaT0J0vRQ.ttf",
  "300": "http://fonts.gstatic.com/s/cairo/v20/SLXVc1nY6HkvangtZmpcWmhzfH5lB2gsQSaT0J0vRQ.ttf",
  "500": "http://fonts.gstatic.com/s/cairo/v20/SLXVc1nY6HkvangtZmpcWmhzfH5la2gsQSaT0J0vRQ.ttf",
  "600": "http://fonts.gstatic.com/s/cairo/v20/SLXVc1nY6HkvangtZmpcWmhzfH5lh28sQSaT0J0vRQ.ttf",
  "700": "http://fonts.gstatic.com/s/cairo/v20/SLXVc1nY6HkvangtZmpcWmhzfH5lvm8sQSaT0J0vRQ.ttf",
  "800": "http://fonts.gstatic.com/s/cairo/v20/SLXVc1nY6HkvangtZmpcWmhzfH5l2W8sQSaT0J0vRQ.ttf",
  "900": "http://fonts.gstatic.com/s/cairo/v20/SLXVc1nY6HkvangtZmpcWmhzfH5l8G8sQSaT0J0vRQ.ttf",
  "regular": "http://fonts.gstatic.com/s/cairo/v20/SLXVc1nY6HkvangtZmpcWmhzfH5lWWgsQSaT0J0vRQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cairo Play",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v5",
  "lastModified": "2022-09-14",
  "files": {
  "200": "http://fonts.gstatic.com/s/cairoplay/v5/wXKEE3QSpo4vpRz_mz6FP-8iaauCLt_Hjopv3miu5IvcJo49mOo1EnYq9yXa8GvzaA.ttf",
  "300": "http://fonts.gstatic.com/s/cairoplay/v5/wXKEE3QSpo4vpRz_mz6FP-8iaauCLt_Hjopv3miu5IvcJo49mOo1zHYq9yXa8GvzaA.ttf",
  "500": "http://fonts.gstatic.com/s/cairoplay/v5/wXKEE3QSpo4vpRz_mz6FP-8iaauCLt_Hjopv3miu5IvcJo49mOo1oHYq9yXa8GvzaA.ttf",
  "600": "http://fonts.gstatic.com/s/cairoplay/v5/wXKEE3QSpo4vpRz_mz6FP-8iaauCLt_Hjopv3miu5IvcJo49mOo1THEq9yXa8GvzaA.ttf",
  "700": "http://fonts.gstatic.com/s/cairoplay/v5/wXKEE3QSpo4vpRz_mz6FP-8iaauCLt_Hjopv3miu5IvcJo49mOo1dXEq9yXa8GvzaA.ttf",
  "800": "http://fonts.gstatic.com/s/cairoplay/v5/wXKEE3QSpo4vpRz_mz6FP-8iaauCLt_Hjopv3miu5IvcJo49mOo1EnEq9yXa8GvzaA.ttf",
  "900": "http://fonts.gstatic.com/s/cairoplay/v5/wXKEE3QSpo4vpRz_mz6FP-8iaauCLt_Hjopv3miu5IvcJo49mOo1O3Eq9yXa8GvzaA.ttf",
  "regular": "http://fonts.gstatic.com/s/cairoplay/v5/wXKEE3QSpo4vpRz_mz6FP-8iaauCLt_Hjopv3miu5IvcJo49mOo1knYq9yXa8GvzaA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Caladea",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/caladea/v7/kJE2BugZ7AAjhybUtaNY39oYqO52FZ0.ttf",
  "regular": "http://fonts.gstatic.com/s/caladea/v7/kJEzBugZ7AAjhybUjR93-9IztOc.ttf",
  "italic": "http://fonts.gstatic.com/s/caladea/v7/kJExBugZ7AAjhybUvR19__A2pOdvDA.ttf",
  "700italic": "http://fonts.gstatic.com/s/caladea/v7/kJE0BugZ7AAjhybUvR1FQ98SrMxzBZ2lDA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Calistoga",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/calistoga/v10/6NUU8F2OJg6MeR7l4e0vtMYAwdRZfw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Calligraffitti",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/calligraffitti/v19/46k2lbT3XjDVqJw3DCmCFjE0vnFZM5ZBpYN-.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cambay",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/cambay/v12/SLXKc1rY6H0_ZDs-0pusx_lwYX99kA.ttf",
  "regular": "http://fonts.gstatic.com/s/cambay/v12/SLXJc1rY6H0_ZDsGbrSIz9JsaA.ttf",
  "italic": "http://fonts.gstatic.com/s/cambay/v12/SLXLc1rY6H0_ZDs2bL6M7dd8aGZk.ttf",
  "700italic": "http://fonts.gstatic.com/s/cambay/v12/SLXMc1rY6H0_ZDs2bIYwwvN0Q3ptkDMN.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cambo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cambo/v14/IFSqHeNEk8FJk416ok7xkPm8.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Candal",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/candal/v15/XoHn2YH6T7-t_8cNAR4Jt9Yxlw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cantarell",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/cantarell/v15/B50IF7ZDq37KMUvlO01xN4dOFISeJY8GgQ.ttf",
  "regular": "http://fonts.gstatic.com/s/cantarell/v15/B50NF7ZDq37KMUvlO01Ji6hqHK-CLA.ttf",
  "italic": "http://fonts.gstatic.com/s/cantarell/v15/B50LF7ZDq37KMUvlO015iaJuPqqSLJYf.ttf",
  "700italic": "http://fonts.gstatic.com/s/cantarell/v15/B50WF7ZDq37KMUvlO015iZrSEY6aB4oWgWHB.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cantata One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cantataone/v15/PlI5Fl60Nb5obNzNe2jslVxEt8CwfGaD.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cantora One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cantoraone/v17/gyB4hws1JdgnKy56GB_JX6zdZ4vZVbgZ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Capriola",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/capriola/v13/wXKoE3YSppcvo1PDln_8L-AinG8y.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Caramel",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/caramel/v7/P5sCzZKBbMTf_ShyxCRuiZ-uydg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Carattere",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/carattere/v7/4iCv6Kp1b9dXlgt_CkvTt2aMH4V_gg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cardo",
  "variants": [
  "regular",
  "italic",
  "700"
  ],
  "subsets": [
  "greek",
  "greek-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/cardo/v19/wlpygwjKBV1pqhND-aQR82JHaTBX.ttf",
  "regular": "http://fonts.gstatic.com/s/cardo/v19/wlp_gwjKBV1pqiv_1oAZ2H5O.ttf",
  "italic": "http://fonts.gstatic.com/s/cardo/v19/wlpxgwjKBV1pqhv93IQ73W5OcCk.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Carme",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/carme/v16/ptRHTiWdbvZIDOjGxLNrxfbZ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Carrois Gothic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/carroisgothic/v16/Z9XPDmFATg-N1PLtLOOxvIHl9ZmD3i7ajcJ-.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Carrois Gothic SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/carroisgothicsc/v15/ZgNJjOVHM6jfUZCmyUqT2A2HVKjc-28nNHabY4dN.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Carter One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/carterone/v17/q5uCsoe5IOB2-pXv9UcNIxR2hYxREMs.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Castoro",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/castoro/v18/1q2GY5yMCld3-O4cHYhEzOYenEU.ttf",
  "italic": "http://fonts.gstatic.com/s/castoro/v18/1q2EY5yMCld3-O4cLYpOyMQbjEX5fw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Catamaran",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/catamaran/v17/o-0bIpQoyXQa2RxT7-5B6Ryxs2E_6n1iPHjc1anXuluiLyw.ttf",
  "200": "http://fonts.gstatic.com/s/catamaran/v17/o-0bIpQoyXQa2RxT7-5B6Ryxs2E_6n1iPPjd1anXuluiLyw.ttf",
  "300": "http://fonts.gstatic.com/s/catamaran/v17/o-0bIpQoyXQa2RxT7-5B6Ryxs2E_6n1iPCbd1anXuluiLyw.ttf",
  "500": "http://fonts.gstatic.com/s/catamaran/v17/o-0bIpQoyXQa2RxT7-5B6Ryxs2E_6n1iPErd1anXuluiLyw.ttf",
  "600": "http://fonts.gstatic.com/s/catamaran/v17/o-0bIpQoyXQa2RxT7-5B6Ryxs2E_6n1iPKba1anXuluiLyw.ttf",
  "700": "http://fonts.gstatic.com/s/catamaran/v17/o-0bIpQoyXQa2RxT7-5B6Ryxs2E_6n1iPJ_a1anXuluiLyw.ttf",
  "800": "http://fonts.gstatic.com/s/catamaran/v17/o-0bIpQoyXQa2RxT7-5B6Ryxs2E_6n1iPPja1anXuluiLyw.ttf",
  "900": "http://fonts.gstatic.com/s/catamaran/v17/o-0bIpQoyXQa2RxT7-5B6Ryxs2E_6n1iPNHa1anXuluiLyw.ttf",
  "regular": "http://fonts.gstatic.com/s/catamaran/v17/o-0bIpQoyXQa2RxT7-5B6Ryxs2E_6n1iPHjd1anXuluiLyw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Caudex",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "greek",
  "greek-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/caudex/v15/esDT311QOP6BJUrwdteklZUCGpG-GQ.ttf",
  "regular": "http://fonts.gstatic.com/s/caudex/v15/esDQ311QOP6BJUrIyviAnb4eEw.ttf",
  "italic": "http://fonts.gstatic.com/s/caudex/v15/esDS311QOP6BJUr4yPKEv7sOE4in.ttf",
  "700italic": "http://fonts.gstatic.com/s/caudex/v15/esDV311QOP6BJUr4yMo4kJ8GOJSuGdLB.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Caveat",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/caveat/v17/WnznHAc5bAfYB2QRah7pcpNvOx-pjcB9SIKjYBxPigs.ttf",
  "600": "http://fonts.gstatic.com/s/caveat/v17/WnznHAc5bAfYB2QRah7pcpNvOx-pjSx6SIKjYBxPigs.ttf",
  "700": "http://fonts.gstatic.com/s/caveat/v17/WnznHAc5bAfYB2QRah7pcpNvOx-pjRV6SIKjYBxPigs.ttf",
  "regular": "http://fonts.gstatic.com/s/caveat/v17/WnznHAc5bAfYB2QRah7pcpNvOx-pjfJ9SIKjYBxPigs.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Caveat Brush",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/caveatbrush/v11/EYq0maZfwr9S9-ETZc3fKXtMW7mT03pdQw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cedarville Cursive",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cedarvillecursive/v17/yYL00g_a2veiudhUmxjo5VKkoqA-B_neJbBxw8BeTg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ceviche One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cevicheone/v16/gyB4hws1IcA6JzR-GB_JX6zdZ4vZVbgZ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chakra Petch",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/chakrapetch/v9/cIflMapbsEk7TDLdtEz1BwkeNIhFQJXE3AY00g.ttf",
  "500": "http://fonts.gstatic.com/s/chakrapetch/v9/cIflMapbsEk7TDLdtEz1BwkebIlFQJXE3AY00g.ttf",
  "600": "http://fonts.gstatic.com/s/chakrapetch/v9/cIflMapbsEk7TDLdtEz1BwkeQI5FQJXE3AY00g.ttf",
  "700": "http://fonts.gstatic.com/s/chakrapetch/v9/cIflMapbsEk7TDLdtEz1BwkeJI9FQJXE3AY00g.ttf",
  "300italic": "http://fonts.gstatic.com/s/chakrapetch/v9/cIfnMapbsEk7TDLdtEz1BwkWmpLJQp_A_gMk0izH.ttf",
  "regular": "http://fonts.gstatic.com/s/chakrapetch/v9/cIf6MapbsEk7TDLdtEz1BwkmmKBhSL7Y1Q.ttf",
  "italic": "http://fonts.gstatic.com/s/chakrapetch/v9/cIfkMapbsEk7TDLdtEz1BwkWmqplarvI1R8t.ttf",
  "500italic": "http://fonts.gstatic.com/s/chakrapetch/v9/cIfnMapbsEk7TDLdtEz1BwkWmpKRQ5_A_gMk0izH.ttf",
  "600italic": "http://fonts.gstatic.com/s/chakrapetch/v9/cIfnMapbsEk7TDLdtEz1BwkWmpK9RJ_A_gMk0izH.ttf",
  "700italic": "http://fonts.gstatic.com/s/chakrapetch/v9/cIfnMapbsEk7TDLdtEz1BwkWmpLZRZ_A_gMk0izH.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Changa",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/changa/v20/2-c79JNi2YuVOUcOarRPgnNGooxCZy2xQjDp9htf1ZM.ttf",
  "300": "http://fonts.gstatic.com/s/changa/v20/2-c79JNi2YuVOUcOarRPgnNGooxCZ_OxQjDp9htf1ZM.ttf",
  "500": "http://fonts.gstatic.com/s/changa/v20/2-c79JNi2YuVOUcOarRPgnNGooxCZ5-xQjDp9htf1ZM.ttf",
  "600": "http://fonts.gstatic.com/s/changa/v20/2-c79JNi2YuVOUcOarRPgnNGooxCZ3O2QjDp9htf1ZM.ttf",
  "700": "http://fonts.gstatic.com/s/changa/v20/2-c79JNi2YuVOUcOarRPgnNGooxCZ0q2QjDp9htf1ZM.ttf",
  "800": "http://fonts.gstatic.com/s/changa/v20/2-c79JNi2YuVOUcOarRPgnNGooxCZy22QjDp9htf1ZM.ttf",
  "regular": "http://fonts.gstatic.com/s/changa/v20/2-c79JNi2YuVOUcOarRPgnNGooxCZ62xQjDp9htf1ZM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Changa One",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/changaone/v18/xfu00W3wXn3QLUJXhzq46AbouLfbK64.ttf",
  "italic": "http://fonts.gstatic.com/s/changaone/v18/xfu20W3wXn3QLUJXhzq42ATivJXeO67ISw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chango",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/chango/v21/2V0cKI0OB5U7WaJyz324TFUaAw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Charis SIL",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/charissil/v1/oPWJ_kV3l-s-Q8govXvKlEbJRj5dQnSX1ko.ttf",
  "regular": "http://fonts.gstatic.com/s/charissil/v1/oPWK_kV3l-s-Q8govXvKrPrmYjZ2Xn0.ttf",
  "italic": "http://fonts.gstatic.com/s/charissil/v1/oPWI_kV3l-s-Q8govXvKnPjsZhRzTn2Ozw.ttf",
  "700italic": "http://fonts.gstatic.com/s/charissil/v1/oPWX_kV3l-s-Q8govXvKnPjU2jtXRlaSxkrMCQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Charm",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/charm/v10/7cHrv4oii5K0Md6TDss8yn4hnCci.ttf",
  "regular": "http://fonts.gstatic.com/s/charm/v10/7cHmv4oii5K0MeYvIe804WIo.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Charmonman",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/charmonman/v18/MjQAmiR3vP_nuxDv47jiYC2HmL9K9OhmGnY.ttf",
  "regular": "http://fonts.gstatic.com/s/charmonman/v18/MjQDmiR3vP_nuxDv47jiWJGovLdh6OE.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chathura",
  "variants": [
  "100",
  "300",
  "regular",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v20",
  "lastModified": "2022-04-21",
  "files": {
  "100": "http://fonts.gstatic.com/s/chathura/v20/_gP91R7-rzUuVjim42dEq0SbTvZyuDo.ttf",
  "300": "http://fonts.gstatic.com/s/chathura/v20/_gP81R7-rzUuVjim42eMiWSxYPp7oSNy.ttf",
  "700": "http://fonts.gstatic.com/s/chathura/v20/_gP81R7-rzUuVjim42ecjmSxYPp7oSNy.ttf",
  "800": "http://fonts.gstatic.com/s/chathura/v20/_gP81R7-rzUuVjim42eAjWSxYPp7oSNy.ttf",
  "regular": "http://fonts.gstatic.com/s/chathura/v20/_gP71R7-rzUuVjim418goUC5S-Zy.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chau Philomene One",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/chauphilomeneone/v15/55xxezRsPtfie1vPY49qzdgSlJiHRQFsnIx7QMISdQ.ttf",
  "italic": "http://fonts.gstatic.com/s/chauphilomeneone/v15/55xzezRsPtfie1vPY49qzdgSlJiHRQFcnoZ_YscCdXQB.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chela One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/chelaone/v21/6ae-4KC7Uqgdz_JZdPIy31vWNTMwoQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chelsea Market",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/chelseamarket/v13/BCawqZsHqfr89WNP_IApC8tzKBhlLA4uKkWk.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chenla",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/chenla/v25/SZc43FDpIKu8WZ9eXxfonUPL6Q.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cherish",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cherish/v7/ll88K2mXUyqsDsTN5iDCI6IJjg8.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cherry Cream Soda",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cherrycreamsoda/v21/UMBIrOxBrW6w2FFyi9paG0fdVdRciTd6Cd47DJ7G.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cherry Swash",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-04-21",
  "files": {
  "700": "http://fonts.gstatic.com/s/cherryswash/v18/i7dSIFByZjaNAMxtZcnfAy5E_FeaGy6QZ3WfYg.ttf",
  "regular": "http://fonts.gstatic.com/s/cherryswash/v18/i7dNIFByZjaNAMxtZcnfAy58QHi-EwWMbg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chewy",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/chewy/v18/uK_94ruUb-k-wk5xIDMfO-ed.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chicle",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/chicle/v21/lJwG-pw9i2dqU-BDyWKuobYSxw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chilanka",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "malayalam"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/chilanka/v18/WWXRlj2DZQiMJYaYRrJQI9EAZhTO.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chivo",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/chivo/v17/va9F4kzIxd1KFrjDY8Z_uqzGQC_-.ttf",
  "700": "http://fonts.gstatic.com/s/chivo/v17/va9F4kzIxd1KFrjTZMZ_uqzGQC_-.ttf",
  "900": "http://fonts.gstatic.com/s/chivo/v17/va9F4kzIxd1KFrjrZsZ_uqzGQC_-.ttf",
  "300italic": "http://fonts.gstatic.com/s/chivo/v17/va9D4kzIxd1KFrBteUp9sKjkRT_-bF0.ttf",
  "regular": "http://fonts.gstatic.com/s/chivo/v17/va9I4kzIxd1KFoBvS-J3kbDP.ttf",
  "italic": "http://fonts.gstatic.com/s/chivo/v17/va9G4kzIxd1KFrBtQeZVlKDPWTY.ttf",
  "700italic": "http://fonts.gstatic.com/s/chivo/v17/va9D4kzIxd1KFrBteVp6sKjkRT_-bF0.ttf",
  "900italic": "http://fonts.gstatic.com/s/chivo/v17/va9D4kzIxd1KFrBteWJ4sKjkRT_-bF0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Chonburi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/chonburi/v10/8AtqGs-wOpGRTBq66IWaFr3biAfZ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cinzel",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/cinzel/v19/8vIU7ww63mVu7gtR-kwKxNvkNOjw-uTnTYrvDE5ZdqU.ttf",
  "600": "http://fonts.gstatic.com/s/cinzel/v19/8vIU7ww63mVu7gtR-kwKxNvkNOjw-gjgTYrvDE5ZdqU.ttf",
  "700": "http://fonts.gstatic.com/s/cinzel/v19/8vIU7ww63mVu7gtR-kwKxNvkNOjw-jHgTYrvDE5ZdqU.ttf",
  "800": "http://fonts.gstatic.com/s/cinzel/v19/8vIU7ww63mVu7gtR-kwKxNvkNOjw-lbgTYrvDE5ZdqU.ttf",
  "900": "http://fonts.gstatic.com/s/cinzel/v19/8vIU7ww63mVu7gtR-kwKxNvkNOjw-n_gTYrvDE5ZdqU.ttf",
  "regular": "http://fonts.gstatic.com/s/cinzel/v19/8vIU7ww63mVu7gtR-kwKxNvkNOjw-tbnTYrvDE5ZdqU.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cinzel Decorative",
  "variants": [
  "regular",
  "700",
  "900"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/cinzeldecorative/v14/daaHSScvJGqLYhG8nNt8KPPswUAPniZoaelDQzCLlQXE.ttf",
  "900": "http://fonts.gstatic.com/s/cinzeldecorative/v14/daaHSScvJGqLYhG8nNt8KPPswUAPniZQa-lDQzCLlQXE.ttf",
  "regular": "http://fonts.gstatic.com/s/cinzeldecorative/v14/daaCSScvJGqLYhG8nNt8KPPswUAPnh7URs1LaCyC.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Clicker Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/clickerscript/v13/raxkHiKPvt8CMH6ZWP8PdlEq72rY2zqUKafv.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Coda",
  "variants": [
  "regular",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "800": "http://fonts.gstatic.com/s/coda/v21/SLXIc1jY5nQ8HeIgTp6mw9t1cX8.ttf",
  "regular": "http://fonts.gstatic.com/s/coda/v21/SLXHc1jY5nQ8JUIMapaN39I.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Coda Caption",
  "variants": [
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "800": "http://fonts.gstatic.com/s/codacaption/v19/ieVm2YRII2GMY7SyXSoDRiQGqcx6x_-fACIgaw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Codystar",
  "variants": [
  "300",
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/codystar/v15/FwZf7-Q1xVk-40qxOuYsyuyrj0e29bfC.ttf",
  "regular": "http://fonts.gstatic.com/s/codystar/v15/FwZY7-Q1xVk-40qxOt6A4sijpFu_.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Coiny",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/coiny/v16/gyByhwU1K989PXwbElSvO5Tc.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Combo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/combo/v21/BXRlvF3Jh_fIhg0iBu9y8Hf0.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Comfortaa",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v40",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/comfortaa/v40/1Pt_g8LJRfWJmhDAuUsSQamb1W0lwk4S4TbMPrQVIT9c2c8.ttf",
  "500": "http://fonts.gstatic.com/s/comfortaa/v40/1Pt_g8LJRfWJmhDAuUsSQamb1W0lwk4S4VrMPrQVIT9c2c8.ttf",
  "600": "http://fonts.gstatic.com/s/comfortaa/v40/1Pt_g8LJRfWJmhDAuUsSQamb1W0lwk4S4bbLPrQVIT9c2c8.ttf",
  "700": "http://fonts.gstatic.com/s/comfortaa/v40/1Pt_g8LJRfWJmhDAuUsSQamb1W0lwk4S4Y_LPrQVIT9c2c8.ttf",
  "regular": "http://fonts.gstatic.com/s/comfortaa/v40/1Pt_g8LJRfWJmhDAuUsSQamb1W0lwk4S4WjMPrQVIT9c2c8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Comforter",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/comforter/v5/H4clBXOCl8nQnlaql3Qa6JG8iqeuag.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Comforter Brush",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/comforterbrush/v5/Y4GTYa1xVSggrfzZI5WMjxRaOz0jwLL9Th8YYA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Comic Neue",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/comicneue/v8/4UaErEJDsxBrF37olUeD_wHLwpteLwtHJlc.ttf",
  "700": "http://fonts.gstatic.com/s/comicneue/v8/4UaErEJDsxBrF37olUeD_xHMwpteLwtHJlc.ttf",
  "300italic": "http://fonts.gstatic.com/s/comicneue/v8/4UaarEJDsxBrF37olUeD96_RTplUKylCNlcw_Q.ttf",
  "regular": "http://fonts.gstatic.com/s/comicneue/v8/4UaHrEJDsxBrF37olUeDx63j5pN1MwI.ttf",
  "italic": "http://fonts.gstatic.com/s/comicneue/v8/4UaFrEJDsxBrF37olUeD96_p4rFwIwJePw.ttf",
  "700italic": "http://fonts.gstatic.com/s/comicneue/v8/4UaarEJDsxBrF37olUeD96_RXp5UKylCNlcw_Q.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Coming Soon",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/comingsoon/v19/qWcuB6mzpYL7AJ2VfdQR1u-SUjjzsykh.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Commissioner",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/commissioner/v13/tDbe2o2WnlgI0FNDgduEk4jAhwgIy5k8SlfU5Ni-IO9pOXuRoaY.ttf",
  "200": "http://fonts.gstatic.com/s/commissioner/v13/tDbe2o2WnlgI0FNDgduEk4jAhwgIy5k8SlfU5Fi_IO9pOXuRoaY.ttf",
  "300": "http://fonts.gstatic.com/s/commissioner/v13/tDbe2o2WnlgI0FNDgduEk4jAhwgIy5k8SlfU5Ia_IO9pOXuRoaY.ttf",
  "500": "http://fonts.gstatic.com/s/commissioner/v13/tDbe2o2WnlgI0FNDgduEk4jAhwgIy5k8SlfU5Oq_IO9pOXuRoaY.ttf",
  "600": "http://fonts.gstatic.com/s/commissioner/v13/tDbe2o2WnlgI0FNDgduEk4jAhwgIy5k8SlfU5Aa4IO9pOXuRoaY.ttf",
  "700": "http://fonts.gstatic.com/s/commissioner/v13/tDbe2o2WnlgI0FNDgduEk4jAhwgIy5k8SlfU5D-4IO9pOXuRoaY.ttf",
  "800": "http://fonts.gstatic.com/s/commissioner/v13/tDbe2o2WnlgI0FNDgduEk4jAhwgIy5k8SlfU5Fi4IO9pOXuRoaY.ttf",
  "900": "http://fonts.gstatic.com/s/commissioner/v13/tDbe2o2WnlgI0FNDgduEk4jAhwgIy5k8SlfU5HG4IO9pOXuRoaY.ttf",
  "regular": "http://fonts.gstatic.com/s/commissioner/v13/tDbe2o2WnlgI0FNDgduEk4jAhwgIy5k8SlfU5Ni_IO9pOXuRoaY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Concert One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/concertone/v17/VEM1Ro9xs5PjtzCu-srDqRTlhv-CuVAQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Condiment",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/condiment/v20/pONk1hggFNmwvXALyH6Sq4n4o1vyCQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Content",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "khmer"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/content/v24/zrfg0HLayePhU_AwaRzdBirfWCHvkAI.ttf",
  "regular": "http://fonts.gstatic.com/s/content/v24/zrfl0HLayePhU_AwUaDyIiL0RCg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Contrail One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/contrailone/v15/eLGbP-j_JA-kG0_Zo51noafdZUvt_c092w.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Convergence",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/convergence/v15/rax5HiePvdgXPmmMHcIPYRhasU7Q8Cad.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cookie",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cookie/v17/syky-y18lb0tSbfNlQCT9tPdpw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Copse",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/copse/v15/11hPGpDKz1rGb0djHkihUb-A.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Corben",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/corben/v19/LYjAdGzzklQtCMpFHCZgrXArXN7HWQ.ttf",
  "regular": "http://fonts.gstatic.com/s/corben/v19/LYjDdGzzklQtCMp9oAlEpVs3VQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Corinthia",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/corinthia/v9/wEO6EBrAnchaJyPMHE097d8v1GAbgbLXQA.ttf",
  "regular": "http://fonts.gstatic.com/s/corinthia/v9/wEO_EBrAnchaJyPMHE0FUfAL3EsHiA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cormorant",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/cormorant/v18/H4c2BXOCl9bbnla_nHIA47NMUjsNbCVrFk9TQ7Rg7A2uwYs.ttf",
  "500": "http://fonts.gstatic.com/s/cormorant/v18/H4c2BXOCl9bbnla_nHIA47NMUjsNbCVrFiNTQ7Rg7A2uwYs.ttf",
  "600": "http://fonts.gstatic.com/s/cormorant/v18/H4c2BXOCl9bbnla_nHIA47NMUjsNbCVrFs9UQ7Rg7A2uwYs.ttf",
  "700": "http://fonts.gstatic.com/s/cormorant/v18/H4c2BXOCl9bbnla_nHIA47NMUjsNbCVrFvZUQ7Rg7A2uwYs.ttf",
  "regular": "http://fonts.gstatic.com/s/cormorant/v18/H4c2BXOCl9bbnla_nHIA47NMUjsNbCVrFhFTQ7Rg7A2uwYs.ttf",
  "300italic": "http://fonts.gstatic.com/s/cormorant/v18/H4c0BXOCl9bbnla_nHIq6oGzilJm9otsA9kQ9fdq6C-r0YvxdA.ttf",
  "italic": "http://fonts.gstatic.com/s/cormorant/v18/H4c0BXOCl9bbnla_nHIq6oGzilJm9otsA9kQq_dq6C-r0YvxdA.ttf",
  "500italic": "http://fonts.gstatic.com/s/cormorant/v18/H4c0BXOCl9bbnla_nHIq6oGzilJm9otsA9kQmfdq6C-r0YvxdA.ttf",
  "600italic": "http://fonts.gstatic.com/s/cormorant/v18/H4c0BXOCl9bbnla_nHIq6oGzilJm9otsA9kQdfBq6C-r0YvxdA.ttf",
  "700italic": "http://fonts.gstatic.com/s/cormorant/v18/H4c0BXOCl9bbnla_nHIq6oGzilJm9otsA9kQTPBq6C-r0YvxdA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cormorant Garamond",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/cormorantgaramond/v16/co3YmX5slCNuHLi8bLeY9MK7whWMhyjQAllvuQWJ5heb_w.ttf",
  "500": "http://fonts.gstatic.com/s/cormorantgaramond/v16/co3YmX5slCNuHLi8bLeY9MK7whWMhyjQWlhvuQWJ5heb_w.ttf",
  "600": "http://fonts.gstatic.com/s/cormorantgaramond/v16/co3YmX5slCNuHLi8bLeY9MK7whWMhyjQdl9vuQWJ5heb_w.ttf",
  "700": "http://fonts.gstatic.com/s/cormorantgaramond/v16/co3YmX5slCNuHLi8bLeY9MK7whWMhyjQEl5vuQWJ5heb_w.ttf",
  "300italic": "http://fonts.gstatic.com/s/cormorantgaramond/v16/co3WmX5slCNuHLi8bLeY9MK7whWMhyjYrEPjuw-NxBKL_y94.ttf",
  "regular": "http://fonts.gstatic.com/s/cormorantgaramond/v16/co3bmX5slCNuHLi8bLeY9MK7whWMhyjornFLsS6V7w.ttf",
  "italic": "http://fonts.gstatic.com/s/cormorantgaramond/v16/co3ZmX5slCNuHLi8bLeY9MK7whWMhyjYrHtPkyuF7w6C.ttf",
  "500italic": "http://fonts.gstatic.com/s/cormorantgaramond/v16/co3WmX5slCNuHLi8bLeY9MK7whWMhyjYrEO7ug-NxBKL_y94.ttf",
  "600italic": "http://fonts.gstatic.com/s/cormorantgaramond/v16/co3WmX5slCNuHLi8bLeY9MK7whWMhyjYrEOXvQ-NxBKL_y94.ttf",
  "700italic": "http://fonts.gstatic.com/s/cormorantgaramond/v16/co3WmX5slCNuHLi8bLeY9MK7whWMhyjYrEPzvA-NxBKL_y94.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cormorant Infant",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/cormorantinfant/v17/HhyIU44g9vKiM1sORYSiWeAsLN9951w3_DMrQqcdJrk.ttf",
  "500": "http://fonts.gstatic.com/s/cormorantinfant/v17/HhyIU44g9vKiM1sORYSiWeAsLN995wQ2_DMrQqcdJrk.ttf",
  "600": "http://fonts.gstatic.com/s/cormorantinfant/v17/HhyIU44g9vKiM1sORYSiWeAsLN995ygx_DMrQqcdJrk.ttf",
  "700": "http://fonts.gstatic.com/s/cormorantinfant/v17/HhyIU44g9vKiM1sORYSiWeAsLN9950ww_DMrQqcdJrk.ttf",
  "300italic": "http://fonts.gstatic.com/s/cormorantinfant/v17/HhyKU44g9vKiM1sORYSiWeAsLN997_ItcDEhRoUYNrn_Ig.ttf",
  "regular": "http://fonts.gstatic.com/s/cormorantinfant/v17/HhyPU44g9vKiM1sORYSiWeAsLN993_Af2DsAXq4.ttf",
  "italic": "http://fonts.gstatic.com/s/cormorantinfant/v17/HhyJU44g9vKiM1sORYSiWeAsLN997_IV3BkFTq4EPw.ttf",
  "500italic": "http://fonts.gstatic.com/s/cormorantinfant/v17/HhyKU44g9vKiM1sORYSiWeAsLN997_ItKDAhRoUYNrn_Ig.ttf",
  "600italic": "http://fonts.gstatic.com/s/cormorantinfant/v17/HhyKU44g9vKiM1sORYSiWeAsLN997_ItBDchRoUYNrn_Ig.ttf",
  "700italic": "http://fonts.gstatic.com/s/cormorantinfant/v17/HhyKU44g9vKiM1sORYSiWeAsLN997_ItYDYhRoUYNrn_Ig.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cormorant SC",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/cormorantsc/v17/0ybmGD4kxqXBmOVLG30OGwsmABIU_R3y8DOWGA.ttf",
  "500": "http://fonts.gstatic.com/s/cormorantsc/v17/0ybmGD4kxqXBmOVLG30OGwsmWBMU_R3y8DOWGA.ttf",
  "600": "http://fonts.gstatic.com/s/cormorantsc/v17/0ybmGD4kxqXBmOVLG30OGwsmdBQU_R3y8DOWGA.ttf",
  "700": "http://fonts.gstatic.com/s/cormorantsc/v17/0ybmGD4kxqXBmOVLG30OGwsmEBUU_R3y8DOWGA.ttf",
  "regular": "http://fonts.gstatic.com/s/cormorantsc/v17/0yb5GD4kxqXBmOVLG30OGwserDow9Tbu-Q.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cormorant Unicase",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/cormorantunicase/v24/HI_ViZUaILtOqhqgDeXoF_n1_fTGX9N_tucv7Gy0DRzS.ttf",
  "500": "http://fonts.gstatic.com/s/cormorantunicase/v24/HI_ViZUaILtOqhqgDeXoF_n1_fTGX9Mnt-cv7Gy0DRzS.ttf",
  "600": "http://fonts.gstatic.com/s/cormorantunicase/v24/HI_ViZUaILtOqhqgDeXoF_n1_fTGX9MLsOcv7Gy0DRzS.ttf",
  "700": "http://fonts.gstatic.com/s/cormorantunicase/v24/HI_ViZUaILtOqhqgDeXoF_n1_fTGX9Nvsecv7Gy0DRzS.ttf",
  "regular": "http://fonts.gstatic.com/s/cormorantunicase/v24/HI_QiZUaILtOqhqgDeXoF_n1_fTGX-vTnsMnx3C9.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cormorant Upright",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/cormorantupright/v18/VuJudM3I2Y35poFONtLdafkUCHw1y1N5phDsU9X6RPzQ.ttf",
  "500": "http://fonts.gstatic.com/s/cormorantupright/v18/VuJudM3I2Y35poFONtLdafkUCHw1y1MhpxDsU9X6RPzQ.ttf",
  "600": "http://fonts.gstatic.com/s/cormorantupright/v18/VuJudM3I2Y35poFONtLdafkUCHw1y1MNoBDsU9X6RPzQ.ttf",
  "700": "http://fonts.gstatic.com/s/cormorantupright/v18/VuJudM3I2Y35poFONtLdafkUCHw1y1NpoRDsU9X6RPzQ.ttf",
  "regular": "http://fonts.gstatic.com/s/cormorantupright/v18/VuJrdM3I2Y35poFONtLdafkUCHw1y2vVjjTkeMnz.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Courgette",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/courgette/v13/wEO_EBrAnc9BLjLQAUkFUfAL3EsHiA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Courier Prime",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/courierprime/v7/u-4k0q2lgwslOqpF_6gQ8kELY7pMf-fVqvHoJXw.ttf",
  "regular": "http://fonts.gstatic.com/s/courierprime/v7/u-450q2lgwslOqpF_6gQ8kELWwZjW-_-tvg.ttf",
  "italic": "http://fonts.gstatic.com/s/courierprime/v7/u-4n0q2lgwslOqpF_6gQ8kELawRpX837pvjxPA.ttf",
  "700italic": "http://fonts.gstatic.com/s/courierprime/v7/u-4i0q2lgwslOqpF_6gQ8kELawRR4-LfrtPtNXyeAg.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cousine",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "hebrew",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/cousine/v25/d6lNkaiiRdih4SpP9Z8K6T7G09BlnmQ.ttf",
  "regular": "http://fonts.gstatic.com/s/cousine/v25/d6lIkaiiRdih4SpPzSMlzTbtz9k.ttf",
  "italic": "http://fonts.gstatic.com/s/cousine/v25/d6lKkaiiRdih4SpP_SEvyRTo39l8hw.ttf",
  "700italic": "http://fonts.gstatic.com/s/cousine/v25/d6lPkaiiRdih4SpP_SEXdTvM1_JgjmRpOA.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Coustard",
  "variants": [
  "regular",
  "900"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "900": "http://fonts.gstatic.com/s/coustard/v16/3XFuErgg3YsZ5fqUU-2LkEHmb_jU3eRL.ttf",
  "regular": "http://fonts.gstatic.com/s/coustard/v16/3XFpErgg3YsZ5fqUU9UPvWXuROTd.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Covered By Your Grace",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/coveredbyyourgrace/v15/QGYwz-AZahWOJJI9kykWW9mD6opopoqXSOS0FgItq6bFIg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Crafty Girls",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/craftygirls/v16/va9B4kXI39VaDdlPJo8N_NvuQR37fF3Wlg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Creepster",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/creepster/v13/AlZy_zVUqJz4yMrniH4hdXf4XB0Tow.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Crete Round",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/creteround/v14/55xoey1sJNPjPiv1ZZZrxJ1827zAKnxN.ttf",
  "italic": "http://fonts.gstatic.com/s/creteround/v14/55xqey1sJNPjPiv1ZZZrxK1-0bjiL2xNhKc.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Crimson Pro",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uUsoa5M_tv7IihmnkabC5XiXCAlXGks1WZTm18OJE_VNWoyQ.ttf",
  "300": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uUsoa5M_tv7IihmnkabC5XiXCAlXGks1WZkG18OJE_VNWoyQ.ttf",
  "500": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uUsoa5M_tv7IihmnkabC5XiXCAlXGks1WZ_G18OJE_VNWoyQ.ttf",
  "600": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uUsoa5M_tv7IihmnkabC5XiXCAlXGks1WZEGp8OJE_VNWoyQ.ttf",
  "700": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uUsoa5M_tv7IihmnkabC5XiXCAlXGks1WZKWp8OJE_VNWoyQ.ttf",
  "800": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uUsoa5M_tv7IihmnkabC5XiXCAlXGks1WZTmp8OJE_VNWoyQ.ttf",
  "900": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uUsoa5M_tv7IihmnkabC5XiXCAlXGks1WZZ2p8OJE_VNWoyQ.ttf",
  "regular": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uUsoa5M_tv7IihmnkabC5XiXCAlXGks1WZzm18OJE_VNWoyQ.ttf",
  "200italic": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uSsoa5M_tv7IihmnkabAReu49Y_Bo-HVKMBi4Ue5s7dtC4yZNE.ttf",
  "300italic": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uSsoa5M_tv7IihmnkabAReu49Y_Bo-HVKMBi7Ke5s7dtC4yZNE.ttf",
  "italic": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uSsoa5M_tv7IihmnkabAReu49Y_Bo-HVKMBi6Ue5s7dtC4yZNE.ttf",
  "500italic": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uSsoa5M_tv7IihmnkabAReu49Y_Bo-HVKMBi6me5s7dtC4yZNE.ttf",
  "600italic": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uSsoa5M_tv7IihmnkabAReu49Y_Bo-HVKMBi5KfJs7dtC4yZNE.ttf",
  "700italic": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uSsoa5M_tv7IihmnkabAReu49Y_Bo-HVKMBi5zfJs7dtC4yZNE.ttf",
  "800italic": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uSsoa5M_tv7IihmnkabAReu49Y_Bo-HVKMBi4UfJs7dtC4yZNE.ttf",
  "900italic": "http://fonts.gstatic.com/s/crimsonpro/v23/q5uSsoa5M_tv7IihmnkabAReu49Y_Bo-HVKMBi49fJs7dtC4yZNE.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Crimson Text",
  "variants": [
  "regular",
  "italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "600": "http://fonts.gstatic.com/s/crimsontext/v19/wlppgwHKFkZgtmSR3NB0oRJXsCx2C9lR1LFffg.ttf",
  "700": "http://fonts.gstatic.com/s/crimsontext/v19/wlppgwHKFkZgtmSR3NB0oRJX1C12C9lR1LFffg.ttf",
  "regular": "http://fonts.gstatic.com/s/crimsontext/v19/wlp2gwHKFkZgtmSR3NB0oRJvaAJSA_JN3Q.ttf",
  "italic": "http://fonts.gstatic.com/s/crimsontext/v19/wlpogwHKFkZgtmSR3NB0oRJfaghWIfdd3ahG.ttf",
  "600italic": "http://fonts.gstatic.com/s/crimsontext/v19/wlprgwHKFkZgtmSR3NB0oRJfajCOD9NV9rRPfrKu.ttf",
  "700italic": "http://fonts.gstatic.com/s/crimsontext/v19/wlprgwHKFkZgtmSR3NB0oRJfajDqDtNV9rRPfrKu.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Croissant One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/croissantone/v20/3y9n6bU9bTPg4m8NDy3Kq24UM3pqn5cdJ-4.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Crushed",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/crushed/v25/U9Mc6dym6WXImTlFT1kfuIqyLzA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cuprum",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/cuprum/v20/dg45_pLmvrkcOkBnKsOzXyGWTBcmg9f6ZjzSJjQjgnU.ttf",
  "600": "http://fonts.gstatic.com/s/cuprum/v20/dg45_pLmvrkcOkBnKsOzXyGWTBcmgzv9ZjzSJjQjgnU.ttf",
  "700": "http://fonts.gstatic.com/s/cuprum/v20/dg45_pLmvrkcOkBnKsOzXyGWTBcmgwL9ZjzSJjQjgnU.ttf",
  "regular": "http://fonts.gstatic.com/s/cuprum/v20/dg45_pLmvrkcOkBnKsOzXyGWTBcmg-X6ZjzSJjQjgnU.ttf",
  "italic": "http://fonts.gstatic.com/s/cuprum/v20/dg47_pLmvrkcOkBNI_FMh0j91rkhli25jn_YIhYmknUPEA.ttf",
  "500italic": "http://fonts.gstatic.com/s/cuprum/v20/dg47_pLmvrkcOkBNI_FMh0j91rkhli25vH_YIhYmknUPEA.ttf",
  "600italic": "http://fonts.gstatic.com/s/cuprum/v20/dg47_pLmvrkcOkBNI_FMh0j91rkhli25UHjYIhYmknUPEA.ttf",
  "700italic": "http://fonts.gstatic.com/s/cuprum/v20/dg47_pLmvrkcOkBNI_FMh0j91rkhli25aXjYIhYmknUPEA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cute Font",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cutefont/v20/Noaw6Uny2oWPbSHMrY6vmJNVNC9hkw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cutive",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cutive/v17/NaPZcZ_fHOhV3Ip7T_hDoyqlZQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Cutive Mono",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/cutivemono/v14/m8JWjfRfY7WVjVi2E-K9H5RFRG-K3Mud.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "DM Mono",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/dmmono/v10/aFTR7PB1QTsUX8KYvrGyIYSnbKX9Rlk.ttf",
  "500": "http://fonts.gstatic.com/s/dmmono/v10/aFTR7PB1QTsUX8KYvumzIYSnbKX9Rlk.ttf",
  "300italic": "http://fonts.gstatic.com/s/dmmono/v10/aFTT7PB1QTsUX8KYth-orYataIf4VllXuA.ttf",
  "regular": "http://fonts.gstatic.com/s/dmmono/v10/aFTU7PB1QTsUX8KYhh2aBYyMcKw.ttf",
  "italic": "http://fonts.gstatic.com/s/dmmono/v10/aFTW7PB1QTsUX8KYth-QAa6JYKzkXw.ttf",
  "500italic": "http://fonts.gstatic.com/s/dmmono/v10/aFTT7PB1QTsUX8KYth-o9YetaIf4VllXuA.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "DM Sans",
  "variants": [
  "regular",
  "italic",
  "500",
  "500italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/dmsans/v11/rP2Cp2ywxg089UriAWCrOB-sClQX6Cg.ttf",
  "700": "http://fonts.gstatic.com/s/dmsans/v11/rP2Cp2ywxg089UriASitOB-sClQX6Cg.ttf",
  "regular": "http://fonts.gstatic.com/s/dmsans/v11/rP2Hp2ywxg089UriOZSCHBeHFl0.ttf",
  "italic": "http://fonts.gstatic.com/s/dmsans/v11/rP2Fp2ywxg089UriCZaIGDWCBl0O8Q.ttf",
  "500italic": "http://fonts.gstatic.com/s/dmsans/v11/rP2Ap2ywxg089UriCZaw7BymDnYS-Cjk6Q.ttf",
  "700italic": "http://fonts.gstatic.com/s/dmsans/v11/rP2Ap2ywxg089UriCZawpBqmDnYS-Cjk6Q.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "DM Serif Display",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dmserifdisplay/v10/-nFnOHM81r4j6k0gjAW3mujVU2B2K_d709jy92k.ttf",
  "italic": "http://fonts.gstatic.com/s/dmserifdisplay/v10/-nFhOHM81r4j6k0gjAW3mujVU2B2G_Vx1_r352np3Q.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "DM Serif Text",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dmseriftext/v10/rnCu-xZa_krGokauCeNq1wWyafOPXHIJErY.ttf",
  "italic": "http://fonts.gstatic.com/s/dmseriftext/v10/rnCw-xZa_krGokauCeNq1wWyWfGFWFAMArZKqQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Damion",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/damion/v14/hv-XlzJ3KEUe_YZUbWY3MTFgVg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dancing Script",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/dancingscript/v24/If2cXTr6YS-zF4S-kcSWSVi_sxjsohD9F50Ruu7BAyoHTeB9ptDqpw.ttf",
  "600": "http://fonts.gstatic.com/s/dancingscript/v24/If2cXTr6YS-zF4S-kcSWSVi_sxjsohD9F50Ruu7B7y0HTeB9ptDqpw.ttf",
  "700": "http://fonts.gstatic.com/s/dancingscript/v24/If2cXTr6YS-zF4S-kcSWSVi_sxjsohD9F50Ruu7B1i0HTeB9ptDqpw.ttf",
  "regular": "http://fonts.gstatic.com/s/dancingscript/v24/If2cXTr6YS-zF4S-kcSWSVi_sxjsohD9F50Ruu7BMSoHTeB9ptDqpw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dangrek",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dangrek/v26/LYjCdG30nEgoH8E2gCNqqVIuTN4.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Darker Grotesque",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/darkergrotesque/v7/U9MA6cuh-mLQlC4BKCtayOfARkSVoxr2AW8hTOsXsX0.ttf",
  "500": "http://fonts.gstatic.com/s/darkergrotesque/v7/U9MA6cuh-mLQlC4BKCtayOfARkSVo0L3AW8hTOsXsX0.ttf",
  "600": "http://fonts.gstatic.com/s/darkergrotesque/v7/U9MA6cuh-mLQlC4BKCtayOfARkSVo27wAW8hTOsXsX0.ttf",
  "700": "http://fonts.gstatic.com/s/darkergrotesque/v7/U9MA6cuh-mLQlC4BKCtayOfARkSVowrxAW8hTOsXsX0.ttf",
  "800": "http://fonts.gstatic.com/s/darkergrotesque/v7/U9MA6cuh-mLQlC4BKCtayOfARkSVoxbyAW8hTOsXsX0.ttf",
  "900": "http://fonts.gstatic.com/s/darkergrotesque/v7/U9MA6cuh-mLQlC4BKCtayOfARkSVozLzAW8hTOsXsX0.ttf",
  "regular": "http://fonts.gstatic.com/s/darkergrotesque/v7/U9MH6cuh-mLQlC4BKCtayOfARkSVm7beJWcKUOI.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "David Libre",
  "variants": [
  "regular",
  "500",
  "700"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/davidlibre/v12/snfzs0W_99N64iuYSvp4W8GIw7qbSjORSo9W.ttf",
  "700": "http://fonts.gstatic.com/s/davidlibre/v12/snfzs0W_99N64iuYSvp4W8HAxbqbSjORSo9W.ttf",
  "regular": "http://fonts.gstatic.com/s/davidlibre/v12/snfus0W_99N64iuYSvp4W_l86p6TYS-Y.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dawning of a New Day",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dawningofanewday/v16/t5t_IQMbOp2SEwuncwLRjMfIg1yYit_nAz8bhWJGNoBE.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Days One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/daysone/v14/mem9YaCnxnKRiYZOCLYVeLkWVNBt.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dekko",
  "variants": [
  "regular"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dekko/v19/46khlb_wWjfSrttFR0vsfl1B.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dela Gothic One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "greek",
  "japanese",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/delagothicone/v10/~ChEKD0RlbGEgR290aGljIE9uZSAAKgQIARgB.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Delius",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/delius/v15/PN_xRfK0pW_9e1rtYcI-jT3L_w.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Delius Swash Caps",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/deliusswashcaps/v19/oY1E8fPLr7v4JWCExZpWebxVKORpXXedKmeBvEYs.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Delius Unicase",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/deliusunicase/v26/845CNMEwEIOVT8BmgfSzIr_6mlp7WMr_BmmlS5aw.ttf",
  "regular": "http://fonts.gstatic.com/s/deliusunicase/v26/845BNMEwEIOVT8BmgfSzIr_6mmLHd-73LXWs.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Della Respira",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dellarespira/v18/RLp5K5v44KaueWI6iEJQBiGPRfkSu6EuTHo.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Denk One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/denkone/v15/dg4m_pzhrqcFb2IzROtHpbglShon.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Devonshire",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/devonshire/v21/46kqlbDwWirWr4gtBD2BX0Vq01lYAZM.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dhurjati",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v20",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dhurjati/v20/_6_8ED3gSeatXfFiFX3ySKQtuTA2.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Didact Gothic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/didactgothic/v19/ahcfv8qz1zt6hCC5G4F_P4ASpUySp0LlcyQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Diplomata",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/diplomata/v24/Cn-0JtiMXwhNwp-wKxyfYGxYrdM9Sg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Diplomata SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/diplomatasc/v21/buExpoi3ecvs3kidKgBJo2kf-P5Oaiw4cw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Do Hyeon",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dohyeon/v16/TwMN-I8CRRU2zM86HFE3ZwaH__-C.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dokdo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dokdo/v15/esDf315XNuCBLxLo4NaMlKcH.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Domine",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/domine/v19/L0xhDFMnlVwD4h3Lt9JWnbX3jG-2X0DAI10VErGuW8Q.ttf",
  "600": "http://fonts.gstatic.com/s/domine/v19/L0xhDFMnlVwD4h3Lt9JWnbX3jG-2X6zHI10VErGuW8Q.ttf",
  "700": "http://fonts.gstatic.com/s/domine/v19/L0xhDFMnlVwD4h3Lt9JWnbX3jG-2X5XHI10VErGuW8Q.ttf",
  "regular": "http://fonts.gstatic.com/s/domine/v19/L0xhDFMnlVwD4h3Lt9JWnbX3jG-2X3LAI10VErGuW8Q.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Donegal One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/donegalone/v20/m8JWjfRYea-ZnFz6fsK9FZRFRG-K3Mud.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dongle",
  "variants": [
  "300",
  "regular",
  "700"
  ],
  "subsets": [
  "korean",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v8",
  "lastModified": "2022-09-27",
  "files": {
  "300": "http://fonts.gstatic.com/s/dongle/v8/sJoG3Ltdjt6VPkqeEcxrYjWNzXvVPA.ttf",
  "700": "http://fonts.gstatic.com/s/dongle/v8/sJoG3Ltdjt6VPkqeActrYjWNzXvVPA.ttf",
  "regular": "http://fonts.gstatic.com/s/dongle/v8/sJoF3Ltdjt6VPkqmveRPah6RxA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Doppio One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/doppioone/v13/Gg8wN5gSaBfyBw2MqCh-lgshKGpe5Fg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dorsa",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dorsa/v23/yYLn0hjd0OGwqo493XCFxAnQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dosis",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v27",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/dosis/v27/HhyJU5sn9vOmLxNkIwRSjTVNWLEJt7MV3BkFTq4EPw.ttf",
  "300": "http://fonts.gstatic.com/s/dosis/v27/HhyJU5sn9vOmLxNkIwRSjTVNWLEJabMV3BkFTq4EPw.ttf",
  "500": "http://fonts.gstatic.com/s/dosis/v27/HhyJU5sn9vOmLxNkIwRSjTVNWLEJBbMV3BkFTq4EPw.ttf",
  "600": "http://fonts.gstatic.com/s/dosis/v27/HhyJU5sn9vOmLxNkIwRSjTVNWLEJ6bQV3BkFTq4EPw.ttf",
  "700": "http://fonts.gstatic.com/s/dosis/v27/HhyJU5sn9vOmLxNkIwRSjTVNWLEJ0LQV3BkFTq4EPw.ttf",
  "800": "http://fonts.gstatic.com/s/dosis/v27/HhyJU5sn9vOmLxNkIwRSjTVNWLEJt7QV3BkFTq4EPw.ttf",
  "regular": "http://fonts.gstatic.com/s/dosis/v27/HhyJU5sn9vOmLxNkIwRSjTVNWLEJN7MV3BkFTq4EPw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "DotGothic16",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dotgothic16/v15/v6-QGYjBJFKgyw5nSoDAGE7L435YPFrT.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dr Sugiyama",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/drsugiyama/v22/HTxoL2k4N3O9n5I1boGI7abRM4-t-g7y.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Duru Sans",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/durusans/v19/xn7iYH8xwmSyTvEV_HOxT_fYdN-WZw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "DynaPuff",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/dynapuff/v1/z7N5dRvsZDIVHbYPMhZJ3HQ83UaSu4uhr7-ZFeoYkgAr1x8RSyQu6YjrSRs4wn8.ttf",
  "600": "http://fonts.gstatic.com/s/dynapuff/v1/z7N5dRvsZDIVHbYPMhZJ3HQ83UaSu4uhr7-ZFeoYkgAr1x8RS8gp6YjrSRs4wn8.ttf",
  "700": "http://fonts.gstatic.com/s/dynapuff/v1/z7N5dRvsZDIVHbYPMhZJ3HQ83UaSu4uhr7-ZFeoYkgAr1x8RS_Ep6YjrSRs4wn8.ttf",
  "regular": "http://fonts.gstatic.com/s/dynapuff/v1/z7N5dRvsZDIVHbYPMhZJ3HQ83UaSu4uhr7-ZFeoYkgAr1x8RSxYu6YjrSRs4wn8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Dynalight",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/dynalight/v18/1Ptsg8LOU_aOmQvTsF4ISotrDfGGxA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "EB Garamond",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v26",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/ebgaramond/v26/SlGDmQSNjdsmc35JDF1K5E55YMjF_7DPuGi-2fRUA4V-e6yHgQ.ttf",
  "600": "http://fonts.gstatic.com/s/ebgaramond/v26/SlGDmQSNjdsmc35JDF1K5E55YMjF_7DPuGi-NfNUA4V-e6yHgQ.ttf",
  "700": "http://fonts.gstatic.com/s/ebgaramond/v26/SlGDmQSNjdsmc35JDF1K5E55YMjF_7DPuGi-DPNUA4V-e6yHgQ.ttf",
  "800": "http://fonts.gstatic.com/s/ebgaramond/v26/SlGDmQSNjdsmc35JDF1K5E55YMjF_7DPuGi-a_NUA4V-e6yHgQ.ttf",
  "regular": "http://fonts.gstatic.com/s/ebgaramond/v26/SlGDmQSNjdsmc35JDF1K5E55YMjF_7DPuGi-6_RUA4V-e6yHgQ.ttf",
  "italic": "http://fonts.gstatic.com/s/ebgaramond/v26/SlGFmQSNjdsmc35JDF1K5GRwUjcdlttVFm-rI7e8QI96WamXgXFI.ttf",
  "500italic": "http://fonts.gstatic.com/s/ebgaramond/v26/SlGFmQSNjdsmc35JDF1K5GRwUjcdlttVFm-rI7eOQI96WamXgXFI.ttf",
  "600italic": "http://fonts.gstatic.com/s/ebgaramond/v26/SlGFmQSNjdsmc35JDF1K5GRwUjcdlttVFm-rI7diR496WamXgXFI.ttf",
  "700italic": "http://fonts.gstatic.com/s/ebgaramond/v26/SlGFmQSNjdsmc35JDF1K5GRwUjcdlttVFm-rI7dbR496WamXgXFI.ttf",
  "800italic": "http://fonts.gstatic.com/s/ebgaramond/v26/SlGFmQSNjdsmc35JDF1K5GRwUjcdlttVFm-rI7c8R496WamXgXFI.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Eagle Lake",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/eaglelake/v20/ptRMTiqbbuNJDOiKj9wG5O7yKQNute8.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "East Sea Dokdo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/eastseadokdo/v20/xfuo0Wn2V2_KanASqXSZp22m05_aGavYS18y.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Eater",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/eater/v21/mtG04_FCK7bOvpu2u3FwsXsR.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Economica",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/economica/v13/Qw3aZQZaHCLgIWa29ZBTjeckCnZ5dHw8iw.ttf",
  "regular": "http://fonts.gstatic.com/s/economica/v13/Qw3fZQZaHCLgIWa29ZBrMcgAAl1lfQ.ttf",
  "italic": "http://fonts.gstatic.com/s/economica/v13/Qw3ZZQZaHCLgIWa29ZBbM8IEIFh1fWUl.ttf",
  "700italic": "http://fonts.gstatic.com/s/economica/v13/Qw3EZQZaHCLgIWa29ZBbM_q4D3x9Vnksi4M7.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Eczar",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "devanagari",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/eczar/v17/BXR2vF3Pi-DLmxcpJB-qbNTyTMDXL96WqTIVKWJKWg.ttf",
  "600": "http://fonts.gstatic.com/s/eczar/v17/BXR2vF3Pi-DLmxcpJB-qbNTyTMDXw9mWqTIVKWJKWg.ttf",
  "700": "http://fonts.gstatic.com/s/eczar/v17/BXR2vF3Pi-DLmxcpJB-qbNTyTMDX-tmWqTIVKWJKWg.ttf",
  "800": "http://fonts.gstatic.com/s/eczar/v17/BXR2vF3Pi-DLmxcpJB-qbNTyTMDXndmWqTIVKWJKWg.ttf",
  "regular": "http://fonts.gstatic.com/s/eczar/v17/BXR2vF3Pi-DLmxcpJB-qbNTyTMDXHd6WqTIVKWJKWg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Edu NSW ACT Foundation",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/edunswactfoundation/v1/raxRHjqJtsNBFUi8WO0vUBgc9D-2lV_oQdCAYlt_QTQ0vUxJki9fovGLeC-sfguJ.ttf",
  "600": "http://fonts.gstatic.com/s/edunswactfoundation/v1/raxRHjqJtsNBFUi8WO0vUBgc9D-2lV_oQdCAYlt_QTQ0vUxJki-zpfGLeC-sfguJ.ttf",
  "700": "http://fonts.gstatic.com/s/edunswactfoundation/v1/raxRHjqJtsNBFUi8WO0vUBgc9D-2lV_oQdCAYlt_QTQ0vUxJki-KpfGLeC-sfguJ.ttf",
  "regular": "http://fonts.gstatic.com/s/edunswactfoundation/v1/raxRHjqJtsNBFUi8WO0vUBgc9D-2lV_oQdCAYlt_QTQ0vUxJki9tovGLeC-sfguJ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Edu QLD Beginner",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/eduqldbeginner/v1/AMOHz5iUuHLEMNXyohhc_Y56PR3A8dNLF_w3Ka4HKE423oebi6vyVWCN.ttf",
  "600": "http://fonts.gstatic.com/s/eduqldbeginner/v1/AMOHz5iUuHLEMNXyohhc_Y56PR3A8dNLF_w3Ka4HKE7a2Yebi6vyVWCN.ttf",
  "700": "http://fonts.gstatic.com/s/eduqldbeginner/v1/AMOHz5iUuHLEMNXyohhc_Y56PR3A8dNLF_w3Ka4HKE7j2Yebi6vyVWCN.ttf",
  "regular": "http://fonts.gstatic.com/s/eduqldbeginner/v1/AMOHz5iUuHLEMNXyohhc_Y56PR3A8dNLF_w3Ka4HKE4E3oebi6vyVWCN.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Edu SA Beginner",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/edusabeginner/v1/rnC_-xRb1x-1lHXnLaZZ2xOoLIGfU3L82irpr_3C9-09fo1yBydUEDs.ttf",
  "600": "http://fonts.gstatic.com/s/edusabeginner/v1/rnC_-xRb1x-1lHXnLaZZ2xOoLIGfU3L82irpr_3C9wE6fo1yBydUEDs.ttf",
  "700": "http://fonts.gstatic.com/s/edusabeginner/v1/rnC_-xRb1x-1lHXnLaZZ2xOoLIGfU3L82irpr_3C9zg6fo1yBydUEDs.ttf",
  "regular": "http://fonts.gstatic.com/s/edusabeginner/v1/rnC_-xRb1x-1lHXnLaZZ2xOoLIGfU3L82irpr_3C9989fo1yBydUEDs.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Edu TAS Beginner",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/edutasbeginner/v1/ZXuwe04WubHfGVY-1TcNg7AFUmshg8jIUTzK3r34f_HCemkrBWRhvk02.ttf",
  "600": "http://fonts.gstatic.com/s/edutasbeginner/v1/ZXuwe04WubHfGVY-1TcNg7AFUmshg8jIUTzK3r34f_EufWkrBWRhvk02.ttf",
  "700": "http://fonts.gstatic.com/s/edutasbeginner/v1/ZXuwe04WubHfGVY-1TcNg7AFUmshg8jIUTzK3r34f_EXfWkrBWRhvk02.ttf",
  "regular": "http://fonts.gstatic.com/s/edutasbeginner/v1/ZXuwe04WubHfGVY-1TcNg7AFUmshg8jIUTzK3r34f_HwemkrBWRhvk02.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Edu VIC WA NT Beginner",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/eduvicwantbeginner/v1/jiz2RF1BuW9OwcnNPxLl4KfZCHd9nFtd5Tu7stCpElYpvPfZZ-OllPmFXwnpkeGR.ttf",
  "600": "http://fonts.gstatic.com/s/eduvicwantbeginner/v1/jiz2RF1BuW9OwcnNPxLl4KfZCHd9nFtd5Tu7stCpElYpvPfZZ-NJk_mFXwnpkeGR.ttf",
  "700": "http://fonts.gstatic.com/s/eduvicwantbeginner/v1/jiz2RF1BuW9OwcnNPxLl4KfZCHd9nFtd5Tu7stCpElYpvPfZZ-Nwk_mFXwnpkeGR.ttf",
  "regular": "http://fonts.gstatic.com/s/eduvicwantbeginner/v1/jiz2RF1BuW9OwcnNPxLl4KfZCHd9nFtd5Tu7stCpElYpvPfZZ-OXlPmFXwnpkeGR.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "El Messiri",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "arabic",
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/elmessiri/v16/K2FhfZBRmr9vQ1pHEey6GIGo8_pv3myYjuXCe65ghj3OoapG.ttf",
  "600": "http://fonts.gstatic.com/s/elmessiri/v16/K2FhfZBRmr9vQ1pHEey6GIGo8_pv3myYjuUufK5ghj3OoapG.ttf",
  "700": "http://fonts.gstatic.com/s/elmessiri/v16/K2FhfZBRmr9vQ1pHEey6GIGo8_pv3myYjuUXfK5ghj3OoapG.ttf",
  "regular": "http://fonts.gstatic.com/s/elmessiri/v16/K2FhfZBRmr9vQ1pHEey6GIGo8_pv3myYjuXwe65ghj3OoapG.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Electrolize",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/electrolize/v14/cIf5Ma1dtE0zSiGSiED7AUEGso5tQafB.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Elsie",
  "variants": [
  "regular",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "900": "http://fonts.gstatic.com/s/elsie/v12/BCaqqZABrez54x6q2-1IU6QeXSBk.ttf",
  "regular": "http://fonts.gstatic.com/s/elsie/v12/BCanqZABrez54yYu9slAeLgX.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Elsie Swash Caps",
  "variants": [
  "regular",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "900": "http://fonts.gstatic.com/s/elsieswashcaps/v21/845ENN8xGZyVX5MVo_upKf7KnjK0RW74DG2HToawrdU.ttf",
  "regular": "http://fonts.gstatic.com/s/elsieswashcaps/v21/845DNN8xGZyVX5MVo_upKf7KnjK0ferVKGWsUo8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Emblema One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/emblemaone/v21/nKKT-GQ0F5dSY8vzG0rOEIRBHl57G_f_.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Emilys Candy",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/emilyscandy/v13/2EbgL-1mD1Rnb0OGKudbk0y5r9xrX84JjA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Encode Sans",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/encodesans/v15/LDIcapOFNxEwR-Bd1O9uYNmnUQomAgE25imKSbHhROjLsZBWTSrQGGHiZtWP7FJCt2c.ttf",
  "200": "http://fonts.gstatic.com/s/encodesans/v15/LDIcapOFNxEwR-Bd1O9uYNmnUQomAgE25imKSbHhROjLsZBWTSrQGOHjZtWP7FJCt2c.ttf",
  "300": "http://fonts.gstatic.com/s/encodesans/v15/LDIcapOFNxEwR-Bd1O9uYNmnUQomAgE25imKSbHhROjLsZBWTSrQGD_jZtWP7FJCt2c.ttf",
  "500": "http://fonts.gstatic.com/s/encodesans/v15/LDIcapOFNxEwR-Bd1O9uYNmnUQomAgE25imKSbHhROjLsZBWTSrQGFPjZtWP7FJCt2c.ttf",
  "600": "http://fonts.gstatic.com/s/encodesans/v15/LDIcapOFNxEwR-Bd1O9uYNmnUQomAgE25imKSbHhROjLsZBWTSrQGL_kZtWP7FJCt2c.ttf",
  "700": "http://fonts.gstatic.com/s/encodesans/v15/LDIcapOFNxEwR-Bd1O9uYNmnUQomAgE25imKSbHhROjLsZBWTSrQGIbkZtWP7FJCt2c.ttf",
  "800": "http://fonts.gstatic.com/s/encodesans/v15/LDIcapOFNxEwR-Bd1O9uYNmnUQomAgE25imKSbHhROjLsZBWTSrQGOHkZtWP7FJCt2c.ttf",
  "900": "http://fonts.gstatic.com/s/encodesans/v15/LDIcapOFNxEwR-Bd1O9uYNmnUQomAgE25imKSbHhROjLsZBWTSrQGMjkZtWP7FJCt2c.ttf",
  "regular": "http://fonts.gstatic.com/s/encodesans/v15/LDIcapOFNxEwR-Bd1O9uYNmnUQomAgE25imKSbHhROjLsZBWTSrQGGHjZtWP7FJCt2c.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Encode Sans Condensed",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/encodesanscondensed/v10/j8_76_LD37rqfuwxyIuaZhE6cRXOLtm2gfT-5a-JLQoFI2KR.ttf",
  "200": "http://fonts.gstatic.com/s/encodesanscondensed/v10/j8_46_LD37rqfuwxyIuaZhE6cRXOLtm2gfT-SY6pByQJKnuIFA.ttf",
  "300": "http://fonts.gstatic.com/s/encodesanscondensed/v10/j8_46_LD37rqfuwxyIuaZhE6cRXOLtm2gfT-LY2pByQJKnuIFA.ttf",
  "500": "http://fonts.gstatic.com/s/encodesanscondensed/v10/j8_46_LD37rqfuwxyIuaZhE6cRXOLtm2gfT-dYypByQJKnuIFA.ttf",
  "600": "http://fonts.gstatic.com/s/encodesanscondensed/v10/j8_46_LD37rqfuwxyIuaZhE6cRXOLtm2gfT-WYupByQJKnuIFA.ttf",
  "700": "http://fonts.gstatic.com/s/encodesanscondensed/v10/j8_46_LD37rqfuwxyIuaZhE6cRXOLtm2gfT-PYqpByQJKnuIFA.ttf",
  "800": "http://fonts.gstatic.com/s/encodesanscondensed/v10/j8_46_LD37rqfuwxyIuaZhE6cRXOLtm2gfT-IYmpByQJKnuIFA.ttf",
  "900": "http://fonts.gstatic.com/s/encodesanscondensed/v10/j8_46_LD37rqfuwxyIuaZhE6cRXOLtm2gfT-BYipByQJKnuIFA.ttf",
  "regular": "http://fonts.gstatic.com/s/encodesanscondensed/v10/j8_16_LD37rqfuwxyIuaZhE6cRXOLtm2gfTGgaWNDw8VIw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Encode Sans Expanded",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/encodesansexpanded/v10/c4mx1mF4GcnstG_Jh1QH6ac4hNLeNyeYUpJGKQNicoAbJlw.ttf",
  "200": "http://fonts.gstatic.com/s/encodesansexpanded/v10/c4mw1mF4GcnstG_Jh1QH6ac4hNLeNyeYUpLqCCNIXIwSP0XD.ttf",
  "300": "http://fonts.gstatic.com/s/encodesansexpanded/v10/c4mw1mF4GcnstG_Jh1QH6ac4hNLeNyeYUpKOCyNIXIwSP0XD.ttf",
  "500": "http://fonts.gstatic.com/s/encodesansexpanded/v10/c4mw1mF4GcnstG_Jh1QH6ac4hNLeNyeYUpLWCiNIXIwSP0XD.ttf",
  "600": "http://fonts.gstatic.com/s/encodesansexpanded/v10/c4mw1mF4GcnstG_Jh1QH6ac4hNLeNyeYUpL6DSNIXIwSP0XD.ttf",
  "700": "http://fonts.gstatic.com/s/encodesansexpanded/v10/c4mw1mF4GcnstG_Jh1QH6ac4hNLeNyeYUpKeDCNIXIwSP0XD.ttf",
  "800": "http://fonts.gstatic.com/s/encodesansexpanded/v10/c4mw1mF4GcnstG_Jh1QH6ac4hNLeNyeYUpKCDyNIXIwSP0XD.ttf",
  "900": "http://fonts.gstatic.com/s/encodesansexpanded/v10/c4mw1mF4GcnstG_Jh1QH6ac4hNLeNyeYUpKmDiNIXIwSP0XD.ttf",
  "regular": "http://fonts.gstatic.com/s/encodesansexpanded/v10/c4m_1mF4GcnstG_Jh1QH6ac4hNLeNyeYUqoiIwdAd5Ab.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Encode Sans SC",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/encodesanssc/v8/jVyp7nLwCGzQ9zE7ZyRg0QRXHPZc_uUA6Kb3VJWLE_Pdtm7lcD6qvXT1HHhn8c9NOEEClIc.ttf",
  "200": "http://fonts.gstatic.com/s/encodesanssc/v8/jVyp7nLwCGzQ9zE7ZyRg0QRXHPZc_uUA6Kb3VJWLE_Pdtm7lcD6qvXT1HPhm8c9NOEEClIc.ttf",
  "300": "http://fonts.gstatic.com/s/encodesanssc/v8/jVyp7nLwCGzQ9zE7ZyRg0QRXHPZc_uUA6Kb3VJWLE_Pdtm7lcD6qvXT1HCZm8c9NOEEClIc.ttf",
  "500": "http://fonts.gstatic.com/s/encodesanssc/v8/jVyp7nLwCGzQ9zE7ZyRg0QRXHPZc_uUA6Kb3VJWLE_Pdtm7lcD6qvXT1HEpm8c9NOEEClIc.ttf",
  "600": "http://fonts.gstatic.com/s/encodesanssc/v8/jVyp7nLwCGzQ9zE7ZyRg0QRXHPZc_uUA6Kb3VJWLE_Pdtm7lcD6qvXT1HKZh8c9NOEEClIc.ttf",
  "700": "http://fonts.gstatic.com/s/encodesanssc/v8/jVyp7nLwCGzQ9zE7ZyRg0QRXHPZc_uUA6Kb3VJWLE_Pdtm7lcD6qvXT1HJ9h8c9NOEEClIc.ttf",
  "800": "http://fonts.gstatic.com/s/encodesanssc/v8/jVyp7nLwCGzQ9zE7ZyRg0QRXHPZc_uUA6Kb3VJWLE_Pdtm7lcD6qvXT1HPhh8c9NOEEClIc.ttf",
  "900": "http://fonts.gstatic.com/s/encodesanssc/v8/jVyp7nLwCGzQ9zE7ZyRg0QRXHPZc_uUA6Kb3VJWLE_Pdtm7lcD6qvXT1HNFh8c9NOEEClIc.ttf",
  "regular": "http://fonts.gstatic.com/s/encodesanssc/v8/jVyp7nLwCGzQ9zE7ZyRg0QRXHPZc_uUA6Kb3VJWLE_Pdtm7lcD6qvXT1HHhm8c9NOEEClIc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Encode Sans Semi Condensed",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/encodesanssemicondensed/v10/3qT6oiKqnDuUtQUEHMoXcmspmy55SFWrXFRp9FTOG1T19MFtQ9jpVUA.ttf",
  "200": "http://fonts.gstatic.com/s/encodesanssemicondensed/v10/3qT7oiKqnDuUtQUEHMoXcmspmy55SFWrXFRp9FTOG1RZ1eFHbdTgTFmr.ttf",
  "300": "http://fonts.gstatic.com/s/encodesanssemicondensed/v10/3qT7oiKqnDuUtQUEHMoXcmspmy55SFWrXFRp9FTOG1Q91uFHbdTgTFmr.ttf",
  "500": "http://fonts.gstatic.com/s/encodesanssemicondensed/v10/3qT7oiKqnDuUtQUEHMoXcmspmy55SFWrXFRp9FTOG1Rl1-FHbdTgTFmr.ttf",
  "600": "http://fonts.gstatic.com/s/encodesanssemicondensed/v10/3qT7oiKqnDuUtQUEHMoXcmspmy55SFWrXFRp9FTOG1RJ0OFHbdTgTFmr.ttf",
  "700": "http://fonts.gstatic.com/s/encodesanssemicondensed/v10/3qT7oiKqnDuUtQUEHMoXcmspmy55SFWrXFRp9FTOG1Qt0eFHbdTgTFmr.ttf",
  "800": "http://fonts.gstatic.com/s/encodesanssemicondensed/v10/3qT7oiKqnDuUtQUEHMoXcmspmy55SFWrXFRp9FTOG1Qx0uFHbdTgTFmr.ttf",
  "900": "http://fonts.gstatic.com/s/encodesanssemicondensed/v10/3qT7oiKqnDuUtQUEHMoXcmspmy55SFWrXFRp9FTOG1QV0-FHbdTgTFmr.ttf",
  "regular": "http://fonts.gstatic.com/s/encodesanssemicondensed/v10/3qT4oiKqnDuUtQUEHMoXcmspmy55SFWrXFRp9FTOG2yR_sVPRsjp.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Encode Sans Semi Expanded",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/encodesanssemiexpanded/v18/ke8xOhAPMEZs-BDuzwftTNJ85JvwMOzE9d9Cca5TM-41KwrlKXeOEA.ttf",
  "200": "http://fonts.gstatic.com/s/encodesanssemiexpanded/v18/ke8yOhAPMEZs-BDuzwftTNJ85JvwMOzE9d9Cca5TM0IUCyDLJX6XCWU.ttf",
  "300": "http://fonts.gstatic.com/s/encodesanssemiexpanded/v18/ke8yOhAPMEZs-BDuzwftTNJ85JvwMOzE9d9Cca5TMyYXCyDLJX6XCWU.ttf",
  "500": "http://fonts.gstatic.com/s/encodesanssemiexpanded/v18/ke8yOhAPMEZs-BDuzwftTNJ85JvwMOzE9d9Cca5TM34WCyDLJX6XCWU.ttf",
  "600": "http://fonts.gstatic.com/s/encodesanssemiexpanded/v18/ke8yOhAPMEZs-BDuzwftTNJ85JvwMOzE9d9Cca5TM1IRCyDLJX6XCWU.ttf",
  "700": "http://fonts.gstatic.com/s/encodesanssemiexpanded/v18/ke8yOhAPMEZs-BDuzwftTNJ85JvwMOzE9d9Cca5TMzYQCyDLJX6XCWU.ttf",
  "800": "http://fonts.gstatic.com/s/encodesanssemiexpanded/v18/ke8yOhAPMEZs-BDuzwftTNJ85JvwMOzE9d9Cca5TMyoTCyDLJX6XCWU.ttf",
  "900": "http://fonts.gstatic.com/s/encodesanssemiexpanded/v18/ke8yOhAPMEZs-BDuzwftTNJ85JvwMOzE9d9Cca5TMw4SCyDLJX6XCWU.ttf",
  "regular": "http://fonts.gstatic.com/s/encodesanssemiexpanded/v18/ke83OhAPMEZs-BDuzwftTNJ85JvwMOzE9d9Cca5TC4o_LyjgOXc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Engagement",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/engagement/v22/x3dlckLDZbqa7RUs9MFVXNossybsHQI.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Englebert",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/englebert/v17/xn7iYH8w2XGrC8AR4HSxT_fYdN-WZw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Enriqueta",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/enriqueta/v15/gokpH6L7AUFrRvV44HVrv2mHmNZEq6TTFw.ttf",
  "600": "http://fonts.gstatic.com/s/enriqueta/v15/gokpH6L7AUFrRvV44HVrk26HmNZEq6TTFw.ttf",
  "700": "http://fonts.gstatic.com/s/enriqueta/v15/gokpH6L7AUFrRvV44HVr92-HmNZEq6TTFw.ttf",
  "regular": "http://fonts.gstatic.com/s/enriqueta/v15/goksH6L7AUFrRvV44HVTS0CjkP1Yog.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ephesis",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ephesis/v7/uU9PCBUS8IerL2VG7xPb3vyHmlI.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Epilogue",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/epilogue/v13/O4ZMFGj5hxF0EhjimngomvnCCtqb30OXMDLiDJXVigHPVA.ttf",
  "200": "http://fonts.gstatic.com/s/epilogue/v13/O4ZMFGj5hxF0EhjimngomvnCCtqb30OXsDPiDJXVigHPVA.ttf",
  "300": "http://fonts.gstatic.com/s/epilogue/v13/O4ZMFGj5hxF0EhjimngomvnCCtqb30OXbjPiDJXVigHPVA.ttf",
  "500": "http://fonts.gstatic.com/s/epilogue/v13/O4ZMFGj5hxF0EhjimngomvnCCtqb30OXAjPiDJXVigHPVA.ttf",
  "600": "http://fonts.gstatic.com/s/epilogue/v13/O4ZMFGj5hxF0EhjimngomvnCCtqb30OX7jTiDJXVigHPVA.ttf",
  "700": "http://fonts.gstatic.com/s/epilogue/v13/O4ZMFGj5hxF0EhjimngomvnCCtqb30OX1zTiDJXVigHPVA.ttf",
  "800": "http://fonts.gstatic.com/s/epilogue/v13/O4ZMFGj5hxF0EhjimngomvnCCtqb30OXsDTiDJXVigHPVA.ttf",
  "900": "http://fonts.gstatic.com/s/epilogue/v13/O4ZMFGj5hxF0EhjimngomvnCCtqb30OXmTTiDJXVigHPVA.ttf",
  "regular": "http://fonts.gstatic.com/s/epilogue/v13/O4ZMFGj5hxF0EhjimngomvnCCtqb30OXMDPiDJXVigHPVA.ttf",
  "100italic": "http://fonts.gstatic.com/s/epilogue/v13/O4ZCFGj5hxF0EhjimlIhqAYaY7EBcUSC-HAKTp_RqATfVHNU.ttf",
  "200italic": "http://fonts.gstatic.com/s/epilogue/v13/O4ZCFGj5hxF0EhjimlIhqAYaY7EBcUSC-HCKT5_RqATfVHNU.ttf",
  "300italic": "http://fonts.gstatic.com/s/epilogue/v13/O4ZCFGj5hxF0EhjimlIhqAYaY7EBcUSC-HBUT5_RqATfVHNU.ttf",
  "italic": "http://fonts.gstatic.com/s/epilogue/v13/O4ZCFGj5hxF0EhjimlIhqAYaY7EBcUSC-HAKT5_RqATfVHNU.ttf",
  "500italic": "http://fonts.gstatic.com/s/epilogue/v13/O4ZCFGj5hxF0EhjimlIhqAYaY7EBcUSC-HA4T5_RqATfVHNU.ttf",
  "600italic": "http://fonts.gstatic.com/s/epilogue/v13/O4ZCFGj5hxF0EhjimlIhqAYaY7EBcUSC-HDUSJ_RqATfVHNU.ttf",
  "700italic": "http://fonts.gstatic.com/s/epilogue/v13/O4ZCFGj5hxF0EhjimlIhqAYaY7EBcUSC-HDtSJ_RqATfVHNU.ttf",
  "800italic": "http://fonts.gstatic.com/s/epilogue/v13/O4ZCFGj5hxF0EhjimlIhqAYaY7EBcUSC-HCKSJ_RqATfVHNU.ttf",
  "900italic": "http://fonts.gstatic.com/s/epilogue/v13/O4ZCFGj5hxF0EhjimlIhqAYaY7EBcUSC-HCjSJ_RqATfVHNU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Erica One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ericaone/v23/WBLnrEXccV9VGrOKmGD1W0_MJMGxiQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Esteban",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/esteban/v14/r05bGLZE-bdGdN-GdOuD5jokU8E.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Estonia",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/estonia/v9/7Au_p_4ijSecA1yHCCL8zkwMIFg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Euphoria Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/euphoriascript/v16/mFTpWb0X2bLb_cx6To2B8GpKoD5ak_ZT1D8x7Q.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ewert",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ewert/v21/va9I4kzO2tFODYBvS-J3kbDP.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Exo",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/exo/v20/4UaZrEtFpBI4f1ZSIK9d4LjJ4lM2CwNsOl4p5Is.ttf",
  "200": "http://fonts.gstatic.com/s/exo/v20/4UaZrEtFpBI4f1ZSIK9d4LjJ4tM3CwNsOl4p5Is.ttf",
  "300": "http://fonts.gstatic.com/s/exo/v20/4UaZrEtFpBI4f1ZSIK9d4LjJ4g03CwNsOl4p5Is.ttf",
  "500": "http://fonts.gstatic.com/s/exo/v20/4UaZrEtFpBI4f1ZSIK9d4LjJ4mE3CwNsOl4p5Is.ttf",
  "600": "http://fonts.gstatic.com/s/exo/v20/4UaZrEtFpBI4f1ZSIK9d4LjJ4o0wCwNsOl4p5Is.ttf",
  "700": "http://fonts.gstatic.com/s/exo/v20/4UaZrEtFpBI4f1ZSIK9d4LjJ4rQwCwNsOl4p5Is.ttf",
  "800": "http://fonts.gstatic.com/s/exo/v20/4UaZrEtFpBI4f1ZSIK9d4LjJ4tMwCwNsOl4p5Is.ttf",
  "900": "http://fonts.gstatic.com/s/exo/v20/4UaZrEtFpBI4f1ZSIK9d4LjJ4vowCwNsOl4p5Is.ttf",
  "regular": "http://fonts.gstatic.com/s/exo/v20/4UaZrEtFpBI4f1ZSIK9d4LjJ4lM3CwNsOl4p5Is.ttf",
  "100italic": "http://fonts.gstatic.com/s/exo/v20/4UafrEtFpBISdmSt-MY2ehbO95t040FmPnws9Iu-uA.ttf",
  "200italic": "http://fonts.gstatic.com/s/exo/v20/4UafrEtFpBISdmSt-MY2ehbO95t0Y0BmPnws9Iu-uA.ttf",
  "300italic": "http://fonts.gstatic.com/s/exo/v20/4UafrEtFpBISdmSt-MY2ehbO95t0vUBmPnws9Iu-uA.ttf",
  "italic": "http://fonts.gstatic.com/s/exo/v20/4UafrEtFpBISdmSt-MY2ehbO95t040BmPnws9Iu-uA.ttf",
  "500italic": "http://fonts.gstatic.com/s/exo/v20/4UafrEtFpBISdmSt-MY2ehbO95t00UBmPnws9Iu-uA.ttf",
  "600italic": "http://fonts.gstatic.com/s/exo/v20/4UafrEtFpBISdmSt-MY2ehbO95t0PUdmPnws9Iu-uA.ttf",
  "700italic": "http://fonts.gstatic.com/s/exo/v20/4UafrEtFpBISdmSt-MY2ehbO95t0BEdmPnws9Iu-uA.ttf",
  "800italic": "http://fonts.gstatic.com/s/exo/v20/4UafrEtFpBISdmSt-MY2ehbO95t0Y0dmPnws9Iu-uA.ttf",
  "900italic": "http://fonts.gstatic.com/s/exo/v20/4UafrEtFpBISdmSt-MY2ehbO95t0SkdmPnws9Iu-uA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Exo 2",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/exo2/v20/7cH1v4okm5zmbvwkAx_sfcEuiD8jvvOcPtq-rpvLpQ.ttf",
  "200": "http://fonts.gstatic.com/s/exo2/v20/7cH1v4okm5zmbvwkAx_sfcEuiD8jPvKcPtq-rpvLpQ.ttf",
  "300": "http://fonts.gstatic.com/s/exo2/v20/7cH1v4okm5zmbvwkAx_sfcEuiD8j4PKcPtq-rpvLpQ.ttf",
  "500": "http://fonts.gstatic.com/s/exo2/v20/7cH1v4okm5zmbvwkAx_sfcEuiD8jjPKcPtq-rpvLpQ.ttf",
  "600": "http://fonts.gstatic.com/s/exo2/v20/7cH1v4okm5zmbvwkAx_sfcEuiD8jYPWcPtq-rpvLpQ.ttf",
  "700": "http://fonts.gstatic.com/s/exo2/v20/7cH1v4okm5zmbvwkAx_sfcEuiD8jWfWcPtq-rpvLpQ.ttf",
  "800": "http://fonts.gstatic.com/s/exo2/v20/7cH1v4okm5zmbvwkAx_sfcEuiD8jPvWcPtq-rpvLpQ.ttf",
  "900": "http://fonts.gstatic.com/s/exo2/v20/7cH1v4okm5zmbvwkAx_sfcEuiD8jF_WcPtq-rpvLpQ.ttf",
  "regular": "http://fonts.gstatic.com/s/exo2/v20/7cH1v4okm5zmbvwkAx_sfcEuiD8jvvKcPtq-rpvLpQ.ttf",
  "100italic": "http://fonts.gstatic.com/s/exo2/v20/7cH3v4okm5zmbtYtMeA0FKq0Jjg2drF0fNC6jJ7bpQBL.ttf",
  "200italic": "http://fonts.gstatic.com/s/exo2/v20/7cH3v4okm5zmbtYtMeA0FKq0Jjg2drH0fdC6jJ7bpQBL.ttf",
  "300italic": "http://fonts.gstatic.com/s/exo2/v20/7cH3v4okm5zmbtYtMeA0FKq0Jjg2drEqfdC6jJ7bpQBL.ttf",
  "italic": "http://fonts.gstatic.com/s/exo2/v20/7cH3v4okm5zmbtYtMeA0FKq0Jjg2drF0fdC6jJ7bpQBL.ttf",
  "500italic": "http://fonts.gstatic.com/s/exo2/v20/7cH3v4okm5zmbtYtMeA0FKq0Jjg2drFGfdC6jJ7bpQBL.ttf",
  "600italic": "http://fonts.gstatic.com/s/exo2/v20/7cH3v4okm5zmbtYtMeA0FKq0Jjg2drGqetC6jJ7bpQBL.ttf",
  "700italic": "http://fonts.gstatic.com/s/exo2/v20/7cH3v4okm5zmbtYtMeA0FKq0Jjg2drGTetC6jJ7bpQBL.ttf",
  "800italic": "http://fonts.gstatic.com/s/exo2/v20/7cH3v4okm5zmbtYtMeA0FKq0Jjg2drH0etC6jJ7bpQBL.ttf",
  "900italic": "http://fonts.gstatic.com/s/exo2/v20/7cH3v4okm5zmbtYtMeA0FKq0Jjg2drHdetC6jJ7bpQBL.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Expletus Sans",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/expletussans/v24/RLpqK5v5_bqufTYdnhFzDj2dX_IwS3my73zcDaSq2s1oFQTcXfMm.ttf",
  "600": "http://fonts.gstatic.com/s/expletussans/v24/RLpqK5v5_bqufTYdnhFzDj2dX_IwS3my73zcDaRG3c1oFQTcXfMm.ttf",
  "700": "http://fonts.gstatic.com/s/expletussans/v24/RLpqK5v5_bqufTYdnhFzDj2dX_IwS3my73zcDaR_3c1oFQTcXfMm.ttf",
  "regular": "http://fonts.gstatic.com/s/expletussans/v24/RLpqK5v5_bqufTYdnhFzDj2dX_IwS3my73zcDaSY2s1oFQTcXfMm.ttf",
  "italic": "http://fonts.gstatic.com/s/expletussans/v24/RLpoK5v5_bqufTYdnhFzDj2ddfsCtKHbhOZyCrFQmSUrHwD-WOMmKKY.ttf",
  "500italic": "http://fonts.gstatic.com/s/expletussans/v24/RLpoK5v5_bqufTYdnhFzDj2ddfsCtKHbhOZyCrFQmRcrHwD-WOMmKKY.ttf",
  "600italic": "http://fonts.gstatic.com/s/expletussans/v24/RLpoK5v5_bqufTYdnhFzDj2ddfsCtKHbhOZyCrFQmfssHwD-WOMmKKY.ttf",
  "700italic": "http://fonts.gstatic.com/s/expletussans/v24/RLpoK5v5_bqufTYdnhFzDj2ddfsCtKHbhOZyCrFQmcIsHwD-WOMmKKY.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Explora",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cherokee",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/explora/v7/tsstApxFfjUH4wrvc1qPonC3vqc.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fahkwang",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/fahkwang/v16/Noa26Uj3zpmBOgbNpOJHmZlRFipxkwjx.ttf",
  "300": "http://fonts.gstatic.com/s/fahkwang/v16/Noa26Uj3zpmBOgbNpOIjmplRFipxkwjx.ttf",
  "500": "http://fonts.gstatic.com/s/fahkwang/v16/Noa26Uj3zpmBOgbNpOJ7m5lRFipxkwjx.ttf",
  "600": "http://fonts.gstatic.com/s/fahkwang/v16/Noa26Uj3zpmBOgbNpOJXnJlRFipxkwjx.ttf",
  "700": "http://fonts.gstatic.com/s/fahkwang/v16/Noa26Uj3zpmBOgbNpOIznZlRFipxkwjx.ttf",
  "200italic": "http://fonts.gstatic.com/s/fahkwang/v16/Noa06Uj3zpmBOgbNpOqNgHFQHC5Tlhjxdw4.ttf",
  "300italic": "http://fonts.gstatic.com/s/fahkwang/v16/Noa06Uj3zpmBOgbNpOqNgBVTHC5Tlhjxdw4.ttf",
  "regular": "http://fonts.gstatic.com/s/fahkwang/v16/Noax6Uj3zpmBOgbNpNqPsr1ZPTZ4.ttf",
  "italic": "http://fonts.gstatic.com/s/fahkwang/v16/Noa36Uj3zpmBOgbNpOqNuLl7OCZ4ihE.ttf",
  "500italic": "http://fonts.gstatic.com/s/fahkwang/v16/Noa06Uj3zpmBOgbNpOqNgE1SHC5Tlhjxdw4.ttf",
  "600italic": "http://fonts.gstatic.com/s/fahkwang/v16/Noa06Uj3zpmBOgbNpOqNgGFVHC5Tlhjxdw4.ttf",
  "700italic": "http://fonts.gstatic.com/s/fahkwang/v16/Noa06Uj3zpmBOgbNpOqNgAVUHC5Tlhjxdw4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Familjen Grotesk",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/familjengrotesk/v4/Qw3LZR9ZHiDnImG6-NEMQ41wby8WRnYsfkunR_eGfMG7aSztc1jcEYq2.ttf",
  "600": "http://fonts.gstatic.com/s/familjengrotesk/v4/Qw3LZR9ZHiDnImG6-NEMQ41wby8WRnYsfkunR_eGfMFXbiztc1jcEYq2.ttf",
  "700": "http://fonts.gstatic.com/s/familjengrotesk/v4/Qw3LZR9ZHiDnImG6-NEMQ41wby8WRnYsfkunR_eGfMFubiztc1jcEYq2.ttf",
  "regular": "http://fonts.gstatic.com/s/familjengrotesk/v4/Qw3LZR9ZHiDnImG6-NEMQ41wby8WRnYsfkunR_eGfMGJaSztc1jcEYq2.ttf",
  "italic": "http://fonts.gstatic.com/s/familjengrotesk/v4/Qw31ZR9ZHiDnImG6-NEMQ41wby8WbH8egZPOLG0oe9RBKsSueVz-FJq2Rv4.ttf",
  "500italic": "http://fonts.gstatic.com/s/familjengrotesk/v4/Qw31ZR9ZHiDnImG6-NEMQ41wby8WbH8egZPOLG0oe9RBKvaueVz-FJq2Rv4.ttf",
  "600italic": "http://fonts.gstatic.com/s/familjengrotesk/v4/Qw31ZR9ZHiDnImG6-NEMQ41wby8WbH8egZPOLG0oe9RBKhqpeVz-FJq2Rv4.ttf",
  "700italic": "http://fonts.gstatic.com/s/familjengrotesk/v4/Qw31ZR9ZHiDnImG6-NEMQ41wby8WbH8egZPOLG0oe9RBKiOpeVz-FJq2Rv4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fanwood Text",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fanwoodtext/v15/3XFtErwl05Ad_vSCF6Fq7xXGRdbY1P1Sbg.ttf",
  "italic": "http://fonts.gstatic.com/s/fanwoodtext/v15/3XFzErwl05Ad_vSCF6Fq7xX2R9zc9vhCblye.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Farro",
  "variants": [
  "300",
  "regular",
  "500",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/farro/v14/i7dJIFl3byGNHa3hNJ6-WkJUQUq7.ttf",
  "500": "http://fonts.gstatic.com/s/farro/v14/i7dJIFl3byGNHa25NZ6-WkJUQUq7.ttf",
  "700": "http://fonts.gstatic.com/s/farro/v14/i7dJIFl3byGNHa3xM56-WkJUQUq7.ttf",
  "regular": "http://fonts.gstatic.com/s/farro/v14/i7dEIFl3byGNHZVNHLq2cV5d.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Farsan",
  "variants": [
  "regular"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/farsan/v18/VEMwRoJ0vY_zsyz62q-pxDX9rQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fascinate",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fascinate/v21/z7NWdRrufC8XJK0IIEli1LbQRPyNrw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fascinate Inline",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fascinateinline/v22/jVyR7mzzB3zc-jp6QCAu60poNqIy1g3CfRXxWZQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Faster One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fasterone/v17/H4ciBXCHmdfClFb-vWhfyLuShq63czE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fasthand",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fasthand/v26/0yb9GDohyKTYn_ZEESkuYkw2rQg1.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fauna One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/faunaone/v13/wlpzgwTPBVpjpCuwkuEx2UxLYClOCg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Faustina",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/faustina/v16/XLY4IZPxYpJfTbZAFXWzNT2SO8wpWHls3IEvGVWWe8tbEg.ttf",
  "500": "http://fonts.gstatic.com/s/faustina/v16/XLY4IZPxYpJfTbZAFXWzNT2SO8wpWHlssIEvGVWWe8tbEg.ttf",
  "600": "http://fonts.gstatic.com/s/faustina/v16/XLY4IZPxYpJfTbZAFXWzNT2SO8wpWHlsXIYvGVWWe8tbEg.ttf",
  "700": "http://fonts.gstatic.com/s/faustina/v16/XLY4IZPxYpJfTbZAFXWzNT2SO8wpWHlsZYYvGVWWe8tbEg.ttf",
  "800": "http://fonts.gstatic.com/s/faustina/v16/XLY4IZPxYpJfTbZAFXWzNT2SO8wpWHlsAoYvGVWWe8tbEg.ttf",
  "regular": "http://fonts.gstatic.com/s/faustina/v16/XLY4IZPxYpJfTbZAFXWzNT2SO8wpWHlsgoEvGVWWe8tbEg.ttf",
  "300italic": "http://fonts.gstatic.com/s/faustina/v16/XLY2IZPxYpJfTbZAFV-6B8JKUqez9n55SsKZWl-SWc5LEnoF.ttf",
  "italic": "http://fonts.gstatic.com/s/faustina/v16/XLY2IZPxYpJfTbZAFV-6B8JKUqez9n55SsLHWl-SWc5LEnoF.ttf",
  "500italic": "http://fonts.gstatic.com/s/faustina/v16/XLY2IZPxYpJfTbZAFV-6B8JKUqez9n55SsL1Wl-SWc5LEnoF.ttf",
  "600italic": "http://fonts.gstatic.com/s/faustina/v16/XLY2IZPxYpJfTbZAFV-6B8JKUqez9n55SsIZXV-SWc5LEnoF.ttf",
  "700italic": "http://fonts.gstatic.com/s/faustina/v16/XLY2IZPxYpJfTbZAFV-6B8JKUqez9n55SsIgXV-SWc5LEnoF.ttf",
  "800italic": "http://fonts.gstatic.com/s/faustina/v16/XLY2IZPxYpJfTbZAFV-6B8JKUqez9n55SsJHXV-SWc5LEnoF.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Federant",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/federant/v25/2sDdZGNfip_eirT0_U0jRUG0AqUc.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Federo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/federo/v19/iJWFBX-cbD_ETsbmjVOe2WTG7Q.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Felipa",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/felipa/v19/FwZa7-owz1Eu4F_wSNSEwM2zpA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fenix",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fenix/v20/XoHo2YL_S7-g5ostKzAFvs8o.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Festive",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/festive/v7/cY9Ffj6KX1xcoDWhFtfgy9HTkak.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Figtree",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/figtree/v1/_Xmz-HUzqDCFdgfMsYiV_F7wfS-Bs_chQF5ewkEU4HTy.ttf",
  "500": "http://fonts.gstatic.com/s/figtree/v1/_Xmz-HUzqDCFdgfMsYiV_F7wfS-Bs_dNQF5ewkEU4HTy.ttf",
  "600": "http://fonts.gstatic.com/s/figtree/v1/_Xmz-HUzqDCFdgfMsYiV_F7wfS-Bs_ehR15ewkEU4HTy.ttf",
  "700": "http://fonts.gstatic.com/s/figtree/v1/_Xmz-HUzqDCFdgfMsYiV_F7wfS-Bs_eYR15ewkEU4HTy.ttf",
  "800": "http://fonts.gstatic.com/s/figtree/v1/_Xmz-HUzqDCFdgfMsYiV_F7wfS-Bs_f_R15ewkEU4HTy.ttf",
  "900": "http://fonts.gstatic.com/s/figtree/v1/_Xmz-HUzqDCFdgfMsYiV_F7wfS-Bs_fWR15ewkEU4HTy.ttf",
  "regular": "http://fonts.gstatic.com/s/figtree/v1/_Xmz-HUzqDCFdgfMsYiV_F7wfS-Bs_d_QF5ewkEU4HTy.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Finger Paint",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fingerpaint/v15/0QInMXVJ-o-oRn_7dron8YWO85bS8ANesw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Finlandica",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/finlandica/v3/-nFsOGk-8vAc7lEtg0aSyZCty9GSsPBE19AJrEjx9i5ss3a3.ttf",
  "600": "http://fonts.gstatic.com/s/finlandica/v3/-nFsOGk-8vAc7lEtg0aSyZCty9GSsPBE19Dlq0jx9i5ss3a3.ttf",
  "700": "http://fonts.gstatic.com/s/finlandica/v3/-nFsOGk-8vAc7lEtg0aSyZCty9GSsPBE19Dcq0jx9i5ss3a3.ttf",
  "regular": "http://fonts.gstatic.com/s/finlandica/v3/-nFsOGk-8vAc7lEtg0aSyZCty9GSsPBE19A7rEjx9i5ss3a3.ttf",
  "italic": "http://fonts.gstatic.com/s/finlandica/v3/-nFuOGk-8vAc7lEtg0aS45mfNAn722rq0MXz76Cy_CpOtma3uNQ.ttf",
  "500italic": "http://fonts.gstatic.com/s/finlandica/v3/-nFuOGk-8vAc7lEtg0aS45mfNAn722rq0MXz75Ky_CpOtma3uNQ.ttf",
  "600italic": "http://fonts.gstatic.com/s/finlandica/v3/-nFuOGk-8vAc7lEtg0aS45mfNAn722rq0MXz7361_CpOtma3uNQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/finlandica/v3/-nFuOGk-8vAc7lEtg0aS45mfNAn722rq0MXz70e1_CpOtma3uNQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fira Code",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/firacode/v21/uU9eCBsR6Z2vfE9aq3bL0fxyUs4tcw4W_GNsFVfxN87gsj0.ttf",
  "500": "http://fonts.gstatic.com/s/firacode/v21/uU9eCBsR6Z2vfE9aq3bL0fxyUs4tcw4W_A9sFVfxN87gsj0.ttf",
  "600": "http://fonts.gstatic.com/s/firacode/v21/uU9eCBsR6Z2vfE9aq3bL0fxyUs4tcw4W_ONrFVfxN87gsj0.ttf",
  "700": "http://fonts.gstatic.com/s/firacode/v21/uU9eCBsR6Z2vfE9aq3bL0fxyUs4tcw4W_NprFVfxN87gsj0.ttf",
  "regular": "http://fonts.gstatic.com/s/firacode/v21/uU9eCBsR6Z2vfE9aq3bL0fxyUs4tcw4W_D1sFVfxN87gsj0.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fira Mono",
  "variants": [
  "regular",
  "500",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/firamono/v14/N0bS2SlFPv1weGeLZDto1d33mf3VaZBRBQ.ttf",
  "700": "http://fonts.gstatic.com/s/firamono/v14/N0bS2SlFPv1weGeLZDtondv3mf3VaZBRBQ.ttf",
  "regular": "http://fonts.gstatic.com/s/firamono/v14/N0bX2SlFPv1weGeLZDtQIfTTkdbJYA.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fira Sans",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/firasans/v16/va9C4kDNxMZdWfMOD5Vn9IjOazP3dUTP.ttf",
  "200": "http://fonts.gstatic.com/s/firasans/v16/va9B4kDNxMZdWfMOD5VnWKnuQR37fF3Wlg.ttf",
  "300": "http://fonts.gstatic.com/s/firasans/v16/va9B4kDNxMZdWfMOD5VnPKruQR37fF3Wlg.ttf",
  "500": "http://fonts.gstatic.com/s/firasans/v16/va9B4kDNxMZdWfMOD5VnZKvuQR37fF3Wlg.ttf",
  "600": "http://fonts.gstatic.com/s/firasans/v16/va9B4kDNxMZdWfMOD5VnSKzuQR37fF3Wlg.ttf",
  "700": "http://fonts.gstatic.com/s/firasans/v16/va9B4kDNxMZdWfMOD5VnLK3uQR37fF3Wlg.ttf",
  "800": "http://fonts.gstatic.com/s/firasans/v16/va9B4kDNxMZdWfMOD5VnMK7uQR37fF3Wlg.ttf",
  "900": "http://fonts.gstatic.com/s/firasans/v16/va9B4kDNxMZdWfMOD5VnFK_uQR37fF3Wlg.ttf",
  "100italic": "http://fonts.gstatic.com/s/firasans/v16/va9A4kDNxMZdWfMOD5VvkrCqYTfVcFTPj0s.ttf",
  "200italic": "http://fonts.gstatic.com/s/firasans/v16/va9f4kDNxMZdWfMOD5VvkrAGQBf_XljGllLX.ttf",
  "300italic": "http://fonts.gstatic.com/s/firasans/v16/va9f4kDNxMZdWfMOD5VvkrBiQxf_XljGllLX.ttf",
  "regular": "http://fonts.gstatic.com/s/firasans/v16/va9E4kDNxMZdWfMOD5VfkILKSTbndQ.ttf",
  "italic": "http://fonts.gstatic.com/s/firasans/v16/va9C4kDNxMZdWfMOD5VvkojOazP3dUTP.ttf",
  "500italic": "http://fonts.gstatic.com/s/firasans/v16/va9f4kDNxMZdWfMOD5VvkrA6Qhf_XljGllLX.ttf",
  "600italic": "http://fonts.gstatic.com/s/firasans/v16/va9f4kDNxMZdWfMOD5VvkrAWRRf_XljGllLX.ttf",
  "700italic": "http://fonts.gstatic.com/s/firasans/v16/va9f4kDNxMZdWfMOD5VvkrByRBf_XljGllLX.ttf",
  "800italic": "http://fonts.gstatic.com/s/firasans/v16/va9f4kDNxMZdWfMOD5VvkrBuRxf_XljGllLX.ttf",
  "900italic": "http://fonts.gstatic.com/s/firasans/v16/va9f4kDNxMZdWfMOD5VvkrBKRhf_XljGllLX.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fira Sans Condensed",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOjEADFm8hSaQTFG18FErVhsC9x-tarWZXtqOlQfx9CjA.ttf",
  "200": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOsEADFm8hSaQTFG18FErVhsC9x-tarWTnMiMN-cxZblY4.ttf",
  "300": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOsEADFm8hSaQTFG18FErVhsC9x-tarWV3PiMN-cxZblY4.ttf",
  "500": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOsEADFm8hSaQTFG18FErVhsC9x-tarWQXOiMN-cxZblY4.ttf",
  "600": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOsEADFm8hSaQTFG18FErVhsC9x-tarWSnJiMN-cxZblY4.ttf",
  "700": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOsEADFm8hSaQTFG18FErVhsC9x-tarWU3IiMN-cxZblY4.ttf",
  "800": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOsEADFm8hSaQTFG18FErVhsC9x-tarWVHLiMN-cxZblY4.ttf",
  "900": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOsEADFm8hSaQTFG18FErVhsC9x-tarWXXKiMN-cxZblY4.ttf",
  "100italic": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOtEADFm8hSaQTFG18FErVhsC9x-tarUfPVzONUXRpSjJcu.ttf",
  "200italic": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOuEADFm8hSaQTFG18FErVhsC9x-tarUfPVYMJ0dzRehY43EA.ttf",
  "300italic": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOuEADFm8hSaQTFG18FErVhsC9x-tarUfPVBMF0dzRehY43EA.ttf",
  "regular": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOhEADFm8hSaQTFG18FErVhsC9x-tarYfHnrMtVbx8.ttf",
  "italic": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOjEADFm8hSaQTFG18FErVhsC9x-tarUfPtqOlQfx9CjA.ttf",
  "500italic": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOuEADFm8hSaQTFG18FErVhsC9x-tarUfPVXMB0dzRehY43EA.ttf",
  "600italic": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOuEADFm8hSaQTFG18FErVhsC9x-tarUfPVcMd0dzRehY43EA.ttf",
  "700italic": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOuEADFm8hSaQTFG18FErVhsC9x-tarUfPVFMZ0dzRehY43EA.ttf",
  "800italic": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOuEADFm8hSaQTFG18FErVhsC9x-tarUfPVCMV0dzRehY43EA.ttf",
  "900italic": "http://fonts.gstatic.com/s/firasanscondensed/v10/wEOuEADFm8hSaQTFG18FErVhsC9x-tarUfPVLMR0dzRehY43EA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fira Sans Extra Condensed",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPMcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda3Zyuv1WarE9ncg.ttf",
  "200": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPPcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda3TCPn3-0oEZ-a2Q.ttf",
  "300": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPPcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda3VSMn3-0oEZ-a2Q.ttf",
  "500": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPPcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda3QyNn3-0oEZ-a2Q.ttf",
  "600": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPPcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda3SCKn3-0oEZ-a2Q.ttf",
  "700": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPPcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda3USLn3-0oEZ-a2Q.ttf",
  "800": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPPcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda3ViIn3-0oEZ-a2Q.ttf",
  "900": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPPcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda3XyJn3-0oEZ-a2Q.ttf",
  "100italic": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPOcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda1fqW21-ejkp3cn22.ttf",
  "200italic": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPxcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda1fqWd36-pGR7e2SvJQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPxcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda1fqWE32-pGR7e2SvJQ.ttf",
  "regular": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPKcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda5fiku3efvE8.ttf",
  "italic": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPMcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda1fquv1WarE9ncg.ttf",
  "500italic": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPxcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda1fqWS3y-pGR7e2SvJQ.ttf",
  "600italic": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPxcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda1fqWZ3u-pGR7e2SvJQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPxcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda1fqWA3q-pGR7e2SvJQ.ttf",
  "800italic": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPxcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda1fqWH3m-pGR7e2SvJQ.ttf",
  "900italic": "http://fonts.gstatic.com/s/firasansextracondensed/v10/NaPxcYDaAO5dirw6IaFn7lPJFqXmS-M9Atn3wgda1fqWO3i-pGR7e2SvJQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fjalla One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fjallaone/v13/Yq6R-LCAWCX3-6Ky7FAFnOZwkxgtUb8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fjord One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fjordone/v21/zOL-4pbEnKBY_9S1jNKr6e5As-FeiQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Flamenco",
  "variants": [
  "300",
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/flamenco/v18/neIPzCehqYguo67ssZ0qNIkyepH9qGsf.ttf",
  "regular": "http://fonts.gstatic.com/s/flamenco/v18/neIIzCehqYguo67ssaWGHK06UY30.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Flavors",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/flavors/v22/FBV2dDrhxqmveJTpbkzlNqkG9UY.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fleur De Leah",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fleurdeleah/v7/AYCNpXX7ftYZWLhv9UmPJTMC5vat4I_Gdq0.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Flow Block",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/flowblock/v7/wlp0gwfPCEB65UmTk-d6-WZlbCBXE_I.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Flow Circular",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/flowcircular/v7/lJwB-pc4j2F-H8YKuyvfxdZ45ifpWdr2rIg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Flow Rounded",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/flowrounded/v7/-zki91mtwsU9qlLiGwD4oQX3oZX-Xup87g.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fondamento",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fondamento/v16/4UaHrEJGsxNmFTPDnkaJx63j5pN1MwI.ttf",
  "italic": "http://fonts.gstatic.com/s/fondamento/v16/4UaFrEJGsxNmFTPDnkaJ96_p4rFwIwJePw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fontdiner Swanky",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fontdinerswanky/v19/ijwOs4XgRNsiaI5-hcVb4hQgMvCD4uEfKiGvxts.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Forum",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/forum/v16/6aey4Ky-Vb8Ew_IWMJMa3mnT.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Francois One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/francoisone/v20/_Xmr-H4zszafZw3A-KPSZutNxgKQu_avAg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Frank Ruhl Libre",
  "variants": [
  "300",
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/frankruhllibre/v12/j8_36_fAw7jrcalD7oKYNX0QfAnPUxvHxJDMhYeIHw8.ttf",
  "500": "http://fonts.gstatic.com/s/frankruhllibre/v12/j8_36_fAw7jrcalD7oKYNX0QfAnPU0PGxJDMhYeIHw8.ttf",
  "700": "http://fonts.gstatic.com/s/frankruhllibre/v12/j8_36_fAw7jrcalD7oKYNX0QfAnPUwvAxJDMhYeIHw8.ttf",
  "900": "http://fonts.gstatic.com/s/frankruhllibre/v12/j8_36_fAw7jrcalD7oKYNX0QfAnPUzPCxJDMhYeIHw8.ttf",
  "regular": "http://fonts.gstatic.com/s/frankruhllibre/v12/j8_w6_fAw7jrcalD7oKYNX0QfAnPa7fv4JjnmY4.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fraunces",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/fraunces/v24/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIctxqjDvTShUtWNg.ttf",
  "200": "http://fonts.gstatic.com/s/fraunces/v24/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIcNxujDvTShUtWNg.ttf",
  "300": "http://fonts.gstatic.com/s/fraunces/v24/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIc6RujDvTShUtWNg.ttf",
  "500": "http://fonts.gstatic.com/s/fraunces/v24/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIchRujDvTShUtWNg.ttf",
  "600": "http://fonts.gstatic.com/s/fraunces/v24/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIcaRyjDvTShUtWNg.ttf",
  "700": "http://fonts.gstatic.com/s/fraunces/v24/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIcUByjDvTShUtWNg.ttf",
  "800": "http://fonts.gstatic.com/s/fraunces/v24/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIcNxyjDvTShUtWNg.ttf",
  "900": "http://fonts.gstatic.com/s/fraunces/v24/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIcHhyjDvTShUtWNg.ttf",
  "regular": "http://fonts.gstatic.com/s/fraunces/v24/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92uemAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIctxujDvTShUtWNg.ttf",
  "100italic": "http://fonts.gstatic.com/s/fraunces/v24/6NVf8FyLNQOQZAnv9ZwNjucMHVn85Ni7emAe9lKqZTnbB-gzTK0K1ChJdt9vIVYX9G37lvd9sPEKsxx664UJf1hLTP7Wp05GNi3k.ttf",
  "200italic": "http://fonts.gstatic.com/s/fraunces/v24/6NVf8FyLNQOQZAnv9ZwNjucMHVn85Ni7emAe9lKqZTnbB-gzTK0K1ChJdt9vIVYX9G37lvd9sPEKsxx664UJf1jLTf7Wp05GNi3k.ttf",
  "300italic": "http://fonts.gstatic.com/s/fraunces/v24/6NVf8FyLNQOQZAnv9ZwNjucMHVn85Ni7emAe9lKqZTnbB-gzTK0K1ChJdt9vIVYX9G37lvd9sPEKsxx664UJf1gVTf7Wp05GNi3k.ttf",
  "italic": "http://fonts.gstatic.com/s/fraunces/v24/6NVf8FyLNQOQZAnv9ZwNjucMHVn85Ni7emAe9lKqZTnbB-gzTK0K1ChJdt9vIVYX9G37lvd9sPEKsxx664UJf1hLTf7Wp05GNi3k.ttf",
  "500italic": "http://fonts.gstatic.com/s/fraunces/v24/6NVf8FyLNQOQZAnv9ZwNjucMHVn85Ni7emAe9lKqZTnbB-gzTK0K1ChJdt9vIVYX9G37lvd9sPEKsxx664UJf1h5Tf7Wp05GNi3k.ttf",
  "600italic": "http://fonts.gstatic.com/s/fraunces/v24/6NVf8FyLNQOQZAnv9ZwNjucMHVn85Ni7emAe9lKqZTnbB-gzTK0K1ChJdt9vIVYX9G37lvd9sPEKsxx664UJf1iVSv7Wp05GNi3k.ttf",
  "700italic": "http://fonts.gstatic.com/s/fraunces/v24/6NVf8FyLNQOQZAnv9ZwNjucMHVn85Ni7emAe9lKqZTnbB-gzTK0K1ChJdt9vIVYX9G37lvd9sPEKsxx664UJf1isSv7Wp05GNi3k.ttf",
  "800italic": "http://fonts.gstatic.com/s/fraunces/v24/6NVf8FyLNQOQZAnv9ZwNjucMHVn85Ni7emAe9lKqZTnbB-gzTK0K1ChJdt9vIVYX9G37lvd9sPEKsxx664UJf1jLSv7Wp05GNi3k.ttf",
  "900italic": "http://fonts.gstatic.com/s/fraunces/v24/6NVf8FyLNQOQZAnv9ZwNjucMHVn85Ni7emAe9lKqZTnbB-gzTK0K1ChJdt9vIVYX9G37lvd9sPEKsxx664UJf1jiSv7Wp05GNi3k.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Freckle Face",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/freckleface/v14/AMOWz4SXrmKHCvXTohxY-YI0U1K2w9lb4g.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fredericka the Great",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/frederickathegreat/v15/9Bt33CxNwt7aOctW2xjbCstzwVKsIBVV-9Skz7Ylch2L.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fredoka",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/fredoka/v9/X7nP4b87HvSqjb_WIi2yDCRwoQ_k7367_B-i2yQag0-mac3OryLMFuOLlNldbw.ttf",
  "500": "http://fonts.gstatic.com/s/fredoka/v9/X7nP4b87HvSqjb_WIi2yDCRwoQ_k7367_B-i2yQag0-mac3OwyLMFuOLlNldbw.ttf",
  "600": "http://fonts.gstatic.com/s/fredoka/v9/X7nP4b87HvSqjb_WIi2yDCRwoQ_k7367_B-i2yQag0-mac3OLyXMFuOLlNldbw.ttf",
  "700": "http://fonts.gstatic.com/s/fredoka/v9/X7nP4b87HvSqjb_WIi2yDCRwoQ_k7367_B-i2yQag0-mac3OFiXMFuOLlNldbw.ttf",
  "regular": "http://fonts.gstatic.com/s/fredoka/v9/X7nP4b87HvSqjb_WIi2yDCRwoQ_k7367_B-i2yQag0-mac3O8SLMFuOLlNldbw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fredoka One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fredokaone/v13/k3kUo8kEI-tA1RRcTZGmTmHBA6aF8Bf_.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Freehand",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v27",
  "lastModified": "2022-04-21",
  "files": {
  "regular": "http://fonts.gstatic.com/s/freehand/v27/cIf-Ma5eqk01VjKTgAmBTmUOmZJk.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fresca",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fresca/v18/6ae94K--SKgCzbM2Gr0W13DKPA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Frijole",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/frijole/v14/uU9PCBUR8oakM2BQ7xPb3vyHmlI.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fruktur",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v26",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fruktur/v26/SZc53FHsOru5QYsMfz3GkUrS8DI.ttf",
  "italic": "http://fonts.gstatic.com/s/fruktur/v26/SZc73FHsOru5QYsMTz_MlWjX4DJXgQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fugaz One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fugazone/v15/rax_HiWKp9EAITukFslMBBJek0vA8A.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fuggles",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/fuggles/v8/k3kQo8UEJOlD1hpOTd7iL0nAMaM.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Fuzzy Bubbles",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/fuzzybubbles/v5/6qLbKZMbrgv9pwtjPEVNV0F2Ds_WQxMAZkM1pn4.ttf",
  "regular": "http://fonts.gstatic.com/s/fuzzybubbles/v5/6qLGKZMbrgv9pwtjPEVNV0F2NnP5Zxsreko.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "GFS Didot",
  "variants": [
  "regular"
  ],
  "subsets": [
  "greek"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gfsdidot/v15/Jqzh5TybZ9vZMWFssvwiF-fGFSCGAA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "GFS Neohellenic",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "greek"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/gfsneohellenic/v25/8QIUdiDOrfiq0b7R8O1Iw9WLcY5rkYdr644fWsRO9w.ttf",
  "regular": "http://fonts.gstatic.com/s/gfsneohellenic/v25/8QIRdiDOrfiq0b7R8O1Iw9WLcY5TLahP46UDUw.ttf",
  "italic": "http://fonts.gstatic.com/s/gfsneohellenic/v25/8QITdiDOrfiq0b7R8O1Iw9WLcY5jL6JLwaATU91X.ttf",
  "700italic": "http://fonts.gstatic.com/s/gfsneohellenic/v25/8QIWdiDOrfiq0b7R8O1Iw9WLcY5jL5r37oQbeMFe985V.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gabriela",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gabriela/v14/qkBWXvsO6sreR8E-b_m-zrpHmRzC.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gaegu",
  "variants": [
  "300",
  "regular",
  "700"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-27",
  "files": {
  "300": "http://fonts.gstatic.com/s/gaegu/v15/TuGSUVB6Up9NU57nifw74sdtBk0x.ttf",
  "700": "http://fonts.gstatic.com/s/gaegu/v15/TuGSUVB6Up9NU573jvw74sdtBk0x.ttf",
  "regular": "http://fonts.gstatic.com/s/gaegu/v15/TuGfUVB6Up9NU6ZLodgzydtk.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gafata",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gafata/v16/XRXV3I6Cn0VJKon4MuyAbsrVcA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Galada",
  "variants": [
  "regular"
  ],
  "subsets": [
  "bengali",
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/galada/v14/H4cmBXyGmcjXlUX-8iw-4Lqggw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Galdeano",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/galdeano/v22/uU9MCBoQ4YOqOW1boDPx8PCOg0uX.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Galindo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/galindo/v20/HI_KiYMeLqVKqwyuQ5HiRp-dhpQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gamja Flower",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gamjaflower/v20/6NUR8FiKJg-Pa0rM6uN40Z4kyf9Fdty2ew.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gantari",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/gantari/v1/jVyV7nvyB2HL8iZyDk4GVvSZ5MtC9g0gOz3wa5GD2qnm.ttf",
  "200": "http://fonts.gstatic.com/s/gantari/v1/jVyV7nvyB2HL8iZyDk4GVvSZ5MtC9g2gOj3wa5GD2qnm.ttf",
  "300": "http://fonts.gstatic.com/s/gantari/v1/jVyV7nvyB2HL8iZyDk4GVvSZ5MtC9g1-Oj3wa5GD2qnm.ttf",
  "500": "http://fonts.gstatic.com/s/gantari/v1/jVyV7nvyB2HL8iZyDk4GVvSZ5MtC9g0SOj3wa5GD2qnm.ttf",
  "600": "http://fonts.gstatic.com/s/gantari/v1/jVyV7nvyB2HL8iZyDk4GVvSZ5MtC9g3-PT3wa5GD2qnm.ttf",
  "700": "http://fonts.gstatic.com/s/gantari/v1/jVyV7nvyB2HL8iZyDk4GVvSZ5MtC9g3HPT3wa5GD2qnm.ttf",
  "800": "http://fonts.gstatic.com/s/gantari/v1/jVyV7nvyB2HL8iZyDk4GVvSZ5MtC9g2gPT3wa5GD2qnm.ttf",
  "900": "http://fonts.gstatic.com/s/gantari/v1/jVyV7nvyB2HL8iZyDk4GVvSZ5MtC9g2JPT3wa5GD2qnm.ttf",
  "regular": "http://fonts.gstatic.com/s/gantari/v1/jVyV7nvyB2HL8iZyDk4GVvSZ5MtC9g0gOj3wa5GD2qnm.ttf",
  "100italic": "http://fonts.gstatic.com/s/gantari/v1/jVyb7nvyB2HL8iZyJEc0qSzwj1Hs8RjoedWyYZWh37nmpWc.ttf",
  "200italic": "http://fonts.gstatic.com/s/gantari/v1/jVyb7nvyB2HL8iZyJEc0qSzwj1Hs8RjoeVWzYZWh37nmpWc.ttf",
  "300italic": "http://fonts.gstatic.com/s/gantari/v1/jVyb7nvyB2HL8iZyJEc0qSzwj1Hs8RjoeYuzYZWh37nmpWc.ttf",
  "italic": "http://fonts.gstatic.com/s/gantari/v1/jVyb7nvyB2HL8iZyJEc0qSzwj1Hs8RjoedWzYZWh37nmpWc.ttf",
  "500italic": "http://fonts.gstatic.com/s/gantari/v1/jVyb7nvyB2HL8iZyJEc0qSzwj1Hs8RjoeeezYZWh37nmpWc.ttf",
  "600italic": "http://fonts.gstatic.com/s/gantari/v1/jVyb7nvyB2HL8iZyJEc0qSzwj1Hs8RjoeQu0YZWh37nmpWc.ttf",
  "700italic": "http://fonts.gstatic.com/s/gantari/v1/jVyb7nvyB2HL8iZyJEc0qSzwj1Hs8RjoeTK0YZWh37nmpWc.ttf",
  "800italic": "http://fonts.gstatic.com/s/gantari/v1/jVyb7nvyB2HL8iZyJEc0qSzwj1Hs8RjoeVW0YZWh37nmpWc.ttf",
  "900italic": "http://fonts.gstatic.com/s/gantari/v1/jVyb7nvyB2HL8iZyJEc0qSzwj1Hs8RjoeXy0YZWh37nmpWc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gayathri",
  "variants": [
  "100",
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "malayalam"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/gayathri/v15/MCoWzAb429DbBilWLLhc-pvSA_gA2W8.ttf",
  "700": "http://fonts.gstatic.com/s/gayathri/v15/MCoXzAb429DbBilWLLiE37v4LfQJwHbn.ttf",
  "regular": "http://fonts.gstatic.com/s/gayathri/v15/MCoQzAb429DbBilWLIA48J_wBugA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gelasio",
  "variants": [
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/gelasio/v10/cIf4MaFfvUQxTTqS_N2CRGEsnIJkWL4.ttf",
  "600": "http://fonts.gstatic.com/s/gelasio/v10/cIf4MaFfvUQxTTqS_PGFRGEsnIJkWL4.ttf",
  "700": "http://fonts.gstatic.com/s/gelasio/v10/cIf4MaFfvUQxTTqS_JWERGEsnIJkWL4.ttf",
  "regular": "http://fonts.gstatic.com/s/gelasio/v10/cIf9MaFfvUQxTTqSxCmrYGkHgIs.ttf",
  "italic": "http://fonts.gstatic.com/s/gelasio/v10/cIf_MaFfvUQxTTqS9CuhZEsCkIt9QQ.ttf",
  "500italic": "http://fonts.gstatic.com/s/gelasio/v10/cIf6MaFfvUQxTTqS9CuZkGImmKBhSL7Y1Q.ttf",
  "600italic": "http://fonts.gstatic.com/s/gelasio/v10/cIf6MaFfvUQxTTqS9CuZvGUmmKBhSL7Y1Q.ttf",
  "700italic": "http://fonts.gstatic.com/s/gelasio/v10/cIf6MaFfvUQxTTqS9CuZ2GQmmKBhSL7Y1Q.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gemunu Libre",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "sinhala"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/gemunulibre/v8/X7n34bQ6Cfy7jKGXVE_YlqnbEQAFP-PIuTCp05iJPvSLeMXPIWA.ttf",
  "300": "http://fonts.gstatic.com/s/gemunulibre/v8/X7n34bQ6Cfy7jKGXVE_YlqnbEQAFP-PIuTCp00aJPvSLeMXPIWA.ttf",
  "500": "http://fonts.gstatic.com/s/gemunulibre/v8/X7n34bQ6Cfy7jKGXVE_YlqnbEQAFP-PIuTCp0yqJPvSLeMXPIWA.ttf",
  "600": "http://fonts.gstatic.com/s/gemunulibre/v8/X7n34bQ6Cfy7jKGXVE_YlqnbEQAFP-PIuTCp08aOPvSLeMXPIWA.ttf",
  "700": "http://fonts.gstatic.com/s/gemunulibre/v8/X7n34bQ6Cfy7jKGXVE_YlqnbEQAFP-PIuTCp0_-OPvSLeMXPIWA.ttf",
  "800": "http://fonts.gstatic.com/s/gemunulibre/v8/X7n34bQ6Cfy7jKGXVE_YlqnbEQAFP-PIuTCp05iOPvSLeMXPIWA.ttf",
  "regular": "http://fonts.gstatic.com/s/gemunulibre/v8/X7n34bQ6Cfy7jKGXVE_YlqnbEQAFP-PIuTCp0xiJPvSLeMXPIWA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Genos",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cherokee",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v6",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/genos/v6/SlGNmQqPqpUOYTYjacb0Hc91fTwVqknorUK6K7ZsAg.ttf",
  "200": "http://fonts.gstatic.com/s/genos/v6/SlGNmQqPqpUOYTYjacb0Hc91fTwVKkjorUK6K7ZsAg.ttf",
  "300": "http://fonts.gstatic.com/s/genos/v6/SlGNmQqPqpUOYTYjacb0Hc91fTwV9EjorUK6K7ZsAg.ttf",
  "500": "http://fonts.gstatic.com/s/genos/v6/SlGNmQqPqpUOYTYjacb0Hc91fTwVmEjorUK6K7ZsAg.ttf",
  "600": "http://fonts.gstatic.com/s/genos/v6/SlGNmQqPqpUOYTYjacb0Hc91fTwVdE_orUK6K7ZsAg.ttf",
  "700": "http://fonts.gstatic.com/s/genos/v6/SlGNmQqPqpUOYTYjacb0Hc91fTwVTU_orUK6K7ZsAg.ttf",
  "800": "http://fonts.gstatic.com/s/genos/v6/SlGNmQqPqpUOYTYjacb0Hc91fTwVKk_orUK6K7ZsAg.ttf",
  "900": "http://fonts.gstatic.com/s/genos/v6/SlGNmQqPqpUOYTYjacb0Hc91fTwVA0_orUK6K7ZsAg.ttf",
  "regular": "http://fonts.gstatic.com/s/genos/v6/SlGNmQqPqpUOYTYjacb0Hc91fTwVqkjorUK6K7ZsAg.ttf",
  "100italic": "http://fonts.gstatic.com/s/genos/v6/SlGPmQqPqpUOYRwqWzksdKTv0zsAYgsA70i-CbN8Ard7.ttf",
  "200italic": "http://fonts.gstatic.com/s/genos/v6/SlGPmQqPqpUOYRwqWzksdKTv0zsAYguA7ki-CbN8Ard7.ttf",
  "300italic": "http://fonts.gstatic.com/s/genos/v6/SlGPmQqPqpUOYRwqWzksdKTv0zsAYgte7ki-CbN8Ard7.ttf",
  "italic": "http://fonts.gstatic.com/s/genos/v6/SlGPmQqPqpUOYRwqWzksdKTv0zsAYgsA7ki-CbN8Ard7.ttf",
  "500italic": "http://fonts.gstatic.com/s/genos/v6/SlGPmQqPqpUOYRwqWzksdKTv0zsAYgsy7ki-CbN8Ard7.ttf",
  "600italic": "http://fonts.gstatic.com/s/genos/v6/SlGPmQqPqpUOYRwqWzksdKTv0zsAYgve6Ui-CbN8Ard7.ttf",
  "700italic": "http://fonts.gstatic.com/s/genos/v6/SlGPmQqPqpUOYRwqWzksdKTv0zsAYgvn6Ui-CbN8Ard7.ttf",
  "800italic": "http://fonts.gstatic.com/s/genos/v6/SlGPmQqPqpUOYRwqWzksdKTv0zsAYguA6Ui-CbN8Ard7.ttf",
  "900italic": "http://fonts.gstatic.com/s/genos/v6/SlGPmQqPqpUOYRwqWzksdKTv0zsAYgup6Ui-CbN8Ard7.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gentium Book Basic",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/gentiumbookbasic/v16/pe0wMJCbPYBVokB1LHA9bbyaQb8ZGjcw65Rfy43Y0V4kvg.ttf",
  "regular": "http://fonts.gstatic.com/s/gentiumbookbasic/v16/pe0zMJCbPYBVokB1LHA9bbyaQb8ZGjcIV7t7w6bE2A.ttf",
  "italic": "http://fonts.gstatic.com/s/gentiumbookbasic/v16/pe0xMJCbPYBVokB1LHA9bbyaQb8ZGjc4VbF_4aPU2Ec9.ttf",
  "700italic": "http://fonts.gstatic.com/s/gentiumbookbasic/v16/pe0-MJCbPYBVokB1LHA9bbyaQb8ZGjc4VYnDzofc81s0voO3.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gentium Book Plus",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/gentiumbookplus/v1/vEFO2-RHBgUK5fbjKxRpbBtJPyRpocojWpbGhs_cfKe1.ttf",
  "regular": "http://fonts.gstatic.com/s/gentiumbookplus/v1/vEFL2-RHBgUK5fbjKxRpbBtJPyRpofKfdbLOrdPV.ttf",
  "italic": "http://fonts.gstatic.com/s/gentiumbookplus/v1/vEFN2-RHBgUK5fbjKxRpbBtJPyRpocKdf7bsqMPVZb4.ttf",
  "700italic": "http://fonts.gstatic.com/s/gentiumbookplus/v1/vEFA2-RHBgUK5fbjKxRpbBtJPyRpocKdRwrDjMv-ebe1Els.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gentium Plus",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/gentiumplus/v1/IurC6Ytw-oSPaZ00r2bNe8VRMLRo4EYx_ofHsw.ttf",
  "regular": "http://fonts.gstatic.com/s/gentiumplus/v1/Iurd6Ytw-oSPaZ00r2bNe8VpjJtM6G0t9w.ttf",
  "italic": "http://fonts.gstatic.com/s/gentiumplus/v1/IurD6Ytw-oSPaZ00r2bNe8VZjpFIymg9957e.ttf",
  "700italic": "http://fonts.gstatic.com/s/gentiumplus/v1/IurA6Ytw-oSPaZ00r2bNe8VZjqn05Uw13ILXs-h6.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Geo",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/geo/v19/CSRz4zRZlufVL3BmQjlCbQ.ttf",
  "italic": "http://fonts.gstatic.com/s/geo/v19/CSRx4zRZluflLXpiYDxSbf8r.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Georama",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/georama/v8/MCo5zAn438bIEyxFf6swMnNpvPcUwW4u4yRcDh-ZjxApn9K5GvktmQsL5_tgbg.ttf",
  "200": "http://fonts.gstatic.com/s/georama/v8/MCo5zAn438bIEyxFf6swMnNpvPcUwW4u4yRcDh-ZjxApn9K5mvgtmQsL5_tgbg.ttf",
  "300": "http://fonts.gstatic.com/s/georama/v8/MCo5zAn438bIEyxFf6swMnNpvPcUwW4u4yRcDh-ZjxApn9K5RPgtmQsL5_tgbg.ttf",
  "500": "http://fonts.gstatic.com/s/georama/v8/MCo5zAn438bIEyxFf6swMnNpvPcUwW4u4yRcDh-ZjxApn9K5KPgtmQsL5_tgbg.ttf",
  "600": "http://fonts.gstatic.com/s/georama/v8/MCo5zAn438bIEyxFf6swMnNpvPcUwW4u4yRcDh-ZjxApn9K5xP8tmQsL5_tgbg.ttf",
  "700": "http://fonts.gstatic.com/s/georama/v8/MCo5zAn438bIEyxFf6swMnNpvPcUwW4u4yRcDh-ZjxApn9K5_f8tmQsL5_tgbg.ttf",
  "800": "http://fonts.gstatic.com/s/georama/v8/MCo5zAn438bIEyxFf6swMnNpvPcUwW4u4yRcDh-ZjxApn9K5mv8tmQsL5_tgbg.ttf",
  "900": "http://fonts.gstatic.com/s/georama/v8/MCo5zAn438bIEyxFf6swMnNpvPcUwW4u4yRcDh-ZjxApn9K5s_8tmQsL5_tgbg.ttf",
  "regular": "http://fonts.gstatic.com/s/georama/v8/MCo5zAn438bIEyxFf6swMnNpvPcUwW4u4yRcDh-ZjxApn9K5GvgtmQsL5_tgbg.ttf",
  "100italic": "http://fonts.gstatic.com/s/georama/v8/MCo_zAn438bIEyxFVaIC0ZMQ72G6xnvmodYVPOBB5nuzMdWs0rvF2wEPxf5wbh3T.ttf",
  "200italic": "http://fonts.gstatic.com/s/georama/v8/MCo_zAn438bIEyxFVaIC0ZMQ72G6xnvmodYVPOBB5nuzMdWs0rtF2gEPxf5wbh3T.ttf",
  "300italic": "http://fonts.gstatic.com/s/georama/v8/MCo_zAn438bIEyxFVaIC0ZMQ72G6xnvmodYVPOBB5nuzMdWs0rub2gEPxf5wbh3T.ttf",
  "italic": "http://fonts.gstatic.com/s/georama/v8/MCo_zAn438bIEyxFVaIC0ZMQ72G6xnvmodYVPOBB5nuzMdWs0rvF2gEPxf5wbh3T.ttf",
  "500italic": "http://fonts.gstatic.com/s/georama/v8/MCo_zAn438bIEyxFVaIC0ZMQ72G6xnvmodYVPOBB5nuzMdWs0rv32gEPxf5wbh3T.ttf",
  "600italic": "http://fonts.gstatic.com/s/georama/v8/MCo_zAn438bIEyxFVaIC0ZMQ72G6xnvmodYVPOBB5nuzMdWs0rsb3QEPxf5wbh3T.ttf",
  "700italic": "http://fonts.gstatic.com/s/georama/v8/MCo_zAn438bIEyxFVaIC0ZMQ72G6xnvmodYVPOBB5nuzMdWs0rsi3QEPxf5wbh3T.ttf",
  "800italic": "http://fonts.gstatic.com/s/georama/v8/MCo_zAn438bIEyxFVaIC0ZMQ72G6xnvmodYVPOBB5nuzMdWs0rtF3QEPxf5wbh3T.ttf",
  "900italic": "http://fonts.gstatic.com/s/georama/v8/MCo_zAn438bIEyxFVaIC0ZMQ72G6xnvmodYVPOBB5nuzMdWs0rts3QEPxf5wbh3T.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Geostar",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/geostar/v22/sykz-yx4n701VLOftSq9-trEvlQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Geostar Fill",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/geostarfill/v22/AMOWz4SWuWiXFfjEohxQ9os0U1K2w9lb4g.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Germania One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/germaniaone/v20/Fh4yPjrqIyv2ucM2qzBjeS3ezAJONau6ew.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gideon Roman",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gideonroman/v7/e3tmeuGrVOys8sxzZgWlmXoge0PWovdU4w.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gidugu",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gidugu/v21/L0x8DFMkk1Uf6w3RvPCmRSlUig.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gilda Display",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gildadisplay/v13/t5tmIRoYMoaYG0WEOh7HwMeR7TnFrpOHYh4.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Girassol",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/girassol/v16/JTUUjIo_-DK48laaNC9Nz2pJzxbi.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Give You Glory",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/giveyouglory/v15/8QIQdiHOgt3vv4LR7ahjw9-XYc1zB4ZD6rwa.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Glass Antiqua",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/glassantiqua/v20/xfu30Wr0Wn3NOQM2piC0uXOjnL_wN6fRUkY.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Glegoo",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/glegoo/v14/_Xmu-HQyrTKWaw2xN4a9CKRpzimMsg.ttf",
  "regular": "http://fonts.gstatic.com/s/glegoo/v14/_Xmt-HQyrTKWaw2Ji6mZAI91xw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gloria Hallelujah",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gloriahallelujah/v17/LYjYdHv3kUk9BMV96EIswT9DIbW-MLSy3TKEvkCF.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Glory",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/glory/v9/q5uasoi9Lf1w5t3Est24nq9blIRQwIiDpn-dDi9EOQ.ttf",
  "200": "http://fonts.gstatic.com/s/glory/v9/q5uasoi9Lf1w5t3Est24nq9blIRQQImDpn-dDi9EOQ.ttf",
  "300": "http://fonts.gstatic.com/s/glory/v9/q5uasoi9Lf1w5t3Est24nq9blIRQnomDpn-dDi9EOQ.ttf",
  "500": "http://fonts.gstatic.com/s/glory/v9/q5uasoi9Lf1w5t3Est24nq9blIRQ8omDpn-dDi9EOQ.ttf",
  "600": "http://fonts.gstatic.com/s/glory/v9/q5uasoi9Lf1w5t3Est24nq9blIRQHo6Dpn-dDi9EOQ.ttf",
  "700": "http://fonts.gstatic.com/s/glory/v9/q5uasoi9Lf1w5t3Est24nq9blIRQJ46Dpn-dDi9EOQ.ttf",
  "800": "http://fonts.gstatic.com/s/glory/v9/q5uasoi9Lf1w5t3Est24nq9blIRQQI6Dpn-dDi9EOQ.ttf",
  "regular": "http://fonts.gstatic.com/s/glory/v9/q5uasoi9Lf1w5t3Est24nq9blIRQwImDpn-dDi9EOQ.ttf",
  "100italic": "http://fonts.gstatic.com/s/glory/v9/q5uYsoi9Lf1w5vfNgCJg98TBOoNFCMpr5HWZLCpUOaM6.ttf",
  "200italic": "http://fonts.gstatic.com/s/glory/v9/q5uYsoi9Lf1w5vfNgCJg98TBOoNFCMrr5XWZLCpUOaM6.ttf",
  "300italic": "http://fonts.gstatic.com/s/glory/v9/q5uYsoi9Lf1w5vfNgCJg98TBOoNFCMo15XWZLCpUOaM6.ttf",
  "italic": "http://fonts.gstatic.com/s/glory/v9/q5uYsoi9Lf1w5vfNgCJg98TBOoNFCMpr5XWZLCpUOaM6.ttf",
  "500italic": "http://fonts.gstatic.com/s/glory/v9/q5uYsoi9Lf1w5vfNgCJg98TBOoNFCMpZ5XWZLCpUOaM6.ttf",
  "600italic": "http://fonts.gstatic.com/s/glory/v9/q5uYsoi9Lf1w5vfNgCJg98TBOoNFCMq14nWZLCpUOaM6.ttf",
  "700italic": "http://fonts.gstatic.com/s/glory/v9/q5uYsoi9Lf1w5vfNgCJg98TBOoNFCMqM4nWZLCpUOaM6.ttf",
  "800italic": "http://fonts.gstatic.com/s/glory/v9/q5uYsoi9Lf1w5vfNgCJg98TBOoNFCMrr4nWZLCpUOaM6.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gluten",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/gluten/v9/Hhy_U5gk9fW7OUdVIPh2zD_RSqQJ__A15jgJsn-Bhb_yI8Vb7B1Luni7ciJh.ttf",
  "200": "http://fonts.gstatic.com/s/gluten/v9/Hhy_U5gk9fW7OUdVIPh2zD_RSqQJ__A15jgJsn-Bhb_yI8Xb7R1Luni7ciJh.ttf",
  "300": "http://fonts.gstatic.com/s/gluten/v9/Hhy_U5gk9fW7OUdVIPh2zD_RSqQJ__A15jgJsn-Bhb_yI8UF7R1Luni7ciJh.ttf",
  "500": "http://fonts.gstatic.com/s/gluten/v9/Hhy_U5gk9fW7OUdVIPh2zD_RSqQJ__A15jgJsn-Bhb_yI8Vp7R1Luni7ciJh.ttf",
  "600": "http://fonts.gstatic.com/s/gluten/v9/Hhy_U5gk9fW7OUdVIPh2zD_RSqQJ__A15jgJsn-Bhb_yI8WF6h1Luni7ciJh.ttf",
  "700": "http://fonts.gstatic.com/s/gluten/v9/Hhy_U5gk9fW7OUdVIPh2zD_RSqQJ__A15jgJsn-Bhb_yI8W86h1Luni7ciJh.ttf",
  "800": "http://fonts.gstatic.com/s/gluten/v9/Hhy_U5gk9fW7OUdVIPh2zD_RSqQJ__A15jgJsn-Bhb_yI8Xb6h1Luni7ciJh.ttf",
  "900": "http://fonts.gstatic.com/s/gluten/v9/Hhy_U5gk9fW7OUdVIPh2zD_RSqQJ__A15jgJsn-Bhb_yI8Xy6h1Luni7ciJh.ttf",
  "regular": "http://fonts.gstatic.com/s/gluten/v9/Hhy_U5gk9fW7OUdVIPh2zD_RSqQJ__A15jgJsn-Bhb_yI8Vb7R1Luni7ciJh.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Goblin One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/goblinone/v22/CSR64z1ZnOqZRjRCBVY_TOcATNt_pOU.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gochi Hand",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gochihand/v16/hES06XlsOjtJsgCkx1PkTo71-n0nXWA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Goldman",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/goldman/v15/pe0rMIWbN4JFplR2FI5XIteQB9Zra1U.ttf",
  "regular": "http://fonts.gstatic.com/s/goldman/v15/pe0uMIWbN4JFplR2LDJ4Bt-7G98.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gorditas",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/gorditas/v20/ll84K2aTVD26DsPEtThUIooIvAoShA1i.ttf",
  "regular": "http://fonts.gstatic.com/s/gorditas/v20/ll8_K2aTVD26DsPEtQDoDa4AlxYb.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gothic A1",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/gothica1/v13/CSR74z5ZnPydRjlCCwlCCMcqYtd2vfwk.ttf",
  "200": "http://fonts.gstatic.com/s/gothica1/v13/CSR44z5ZnPydRjlCCwlCpOYKSPl6tOU9Eg.ttf",
  "300": "http://fonts.gstatic.com/s/gothica1/v13/CSR44z5ZnPydRjlCCwlCwOUKSPl6tOU9Eg.ttf",
  "500": "http://fonts.gstatic.com/s/gothica1/v13/CSR44z5ZnPydRjlCCwlCmOQKSPl6tOU9Eg.ttf",
  "600": "http://fonts.gstatic.com/s/gothica1/v13/CSR44z5ZnPydRjlCCwlCtOMKSPl6tOU9Eg.ttf",
  "700": "http://fonts.gstatic.com/s/gothica1/v13/CSR44z5ZnPydRjlCCwlC0OIKSPl6tOU9Eg.ttf",
  "800": "http://fonts.gstatic.com/s/gothica1/v13/CSR44z5ZnPydRjlCCwlCzOEKSPl6tOU9Eg.ttf",
  "900": "http://fonts.gstatic.com/s/gothica1/v13/CSR44z5ZnPydRjlCCwlC6OAKSPl6tOU9Eg.ttf",
  "regular": "http://fonts.gstatic.com/s/gothica1/v13/CSR94z5ZnPydRjlCCwl6bM0uQNJmvQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gotu",
  "variants": [
  "regular"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gotu/v14/o-0FIpksx3QOlH0Lioh6-hU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Goudy Bookletter 1911",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/goudybookletter1911/v15/sykt-z54laciWfKv-kX8krex0jDiD2HbY6I5tRbXZ4IXAA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gowun Batang",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "korean",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-27",
  "files": {
  "700": "http://fonts.gstatic.com/s/gowunbatang/v7/ijwNs5nhRMIjYsdSgcMa3wRZ4J7awssxJii23w.ttf",
  "regular": "http://fonts.gstatic.com/s/gowunbatang/v7/ijwSs5nhRMIjYsdSgcMa3wRhXLH-yuAtLw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gowun Dodum",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gowundodum/v7/3Jn5SD_00GqwlBnWc1TUJF0FfORL0fNy.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Graduate",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/graduate/v13/C8cg4cs3o2n15t_2YxgR6X2NZAn2.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Grand Hotel",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/grandhotel/v13/7Au7p_IgjDKdCRWuR1azpmQNEl0O0kEx.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Grandstander",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/grandstander/v11/ga6fawtA-GpSsTWrnNHPCSIMZhhKpFjyNZIQD1-_D3jWttFGmQk.ttf",
  "200": "http://fonts.gstatic.com/s/grandstander/v11/ga6fawtA-GpSsTWrnNHPCSIMZhhKpFjyNZIQD9--D3jWttFGmQk.ttf",
  "300": "http://fonts.gstatic.com/s/grandstander/v11/ga6fawtA-GpSsTWrnNHPCSIMZhhKpFjyNZIQDwG-D3jWttFGmQk.ttf",
  "500": "http://fonts.gstatic.com/s/grandstander/v11/ga6fawtA-GpSsTWrnNHPCSIMZhhKpFjyNZIQD22-D3jWttFGmQk.ttf",
  "600": "http://fonts.gstatic.com/s/grandstander/v11/ga6fawtA-GpSsTWrnNHPCSIMZhhKpFjyNZIQD4G5D3jWttFGmQk.ttf",
  "700": "http://fonts.gstatic.com/s/grandstander/v11/ga6fawtA-GpSsTWrnNHPCSIMZhhKpFjyNZIQD7i5D3jWttFGmQk.ttf",
  "800": "http://fonts.gstatic.com/s/grandstander/v11/ga6fawtA-GpSsTWrnNHPCSIMZhhKpFjyNZIQD9-5D3jWttFGmQk.ttf",
  "900": "http://fonts.gstatic.com/s/grandstander/v11/ga6fawtA-GpSsTWrnNHPCSIMZhhKpFjyNZIQD_a5D3jWttFGmQk.ttf",
  "regular": "http://fonts.gstatic.com/s/grandstander/v11/ga6fawtA-GpSsTWrnNHPCSIMZhhKpFjyNZIQD1--D3jWttFGmQk.ttf",
  "100italic": "http://fonts.gstatic.com/s/grandstander/v11/ga6ZawtA-GpSsTWrnNHPCSImbyq1fDGZrzwXGpf95zrcsvNDiQlBYQ.ttf",
  "200italic": "http://fonts.gstatic.com/s/grandstander/v11/ga6ZawtA-GpSsTWrnNHPCSImbyq1fDGZrzwXGpf9ZzvcsvNDiQlBYQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/grandstander/v11/ga6ZawtA-GpSsTWrnNHPCSImbyq1fDGZrzwXGpf9uTvcsvNDiQlBYQ.ttf",
  "italic": "http://fonts.gstatic.com/s/grandstander/v11/ga6ZawtA-GpSsTWrnNHPCSImbyq1fDGZrzwXGpf95zvcsvNDiQlBYQ.ttf",
  "500italic": "http://fonts.gstatic.com/s/grandstander/v11/ga6ZawtA-GpSsTWrnNHPCSImbyq1fDGZrzwXGpf91TvcsvNDiQlBYQ.ttf",
  "600italic": "http://fonts.gstatic.com/s/grandstander/v11/ga6ZawtA-GpSsTWrnNHPCSImbyq1fDGZrzwXGpf9OTzcsvNDiQlBYQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/grandstander/v11/ga6ZawtA-GpSsTWrnNHPCSImbyq1fDGZrzwXGpf9ADzcsvNDiQlBYQ.ttf",
  "800italic": "http://fonts.gstatic.com/s/grandstander/v11/ga6ZawtA-GpSsTWrnNHPCSImbyq1fDGZrzwXGpf9ZzzcsvNDiQlBYQ.ttf",
  "900italic": "http://fonts.gstatic.com/s/grandstander/v11/ga6ZawtA-GpSsTWrnNHPCSImbyq1fDGZrzwXGpf9TjzcsvNDiQlBYQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Grape Nuts",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/grapenuts/v2/syk2-yF4iLM2RfKj4F7k3tLvol2RN1E.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gravitas One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gravitasone/v15/5h1diZ4hJ3cblKy3LWakKQmaDWRNr3DzbQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Great Vibes",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/greatvibes/v14/RWmMoKWR9v4ksMfaWd_JN-XCg6UKDXlq.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Grechen Fuemen",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/grechenfuemen/v7/vEFI2_tHEQ4d5ObgKxBzZh0MAWgc-NaXXq7H.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Grenze",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/grenze/v14/O4ZRFGb7hR12BxqPm2IjuAkalnmd.ttf",
  "200": "http://fonts.gstatic.com/s/grenze/v14/O4ZQFGb7hR12BxqPN0MDkicWn2CEyw.ttf",
  "300": "http://fonts.gstatic.com/s/grenze/v14/O4ZQFGb7hR12BxqPU0ADkicWn2CEyw.ttf",
  "500": "http://fonts.gstatic.com/s/grenze/v14/O4ZQFGb7hR12BxqPC0EDkicWn2CEyw.ttf",
  "600": "http://fonts.gstatic.com/s/grenze/v14/O4ZQFGb7hR12BxqPJ0YDkicWn2CEyw.ttf",
  "700": "http://fonts.gstatic.com/s/grenze/v14/O4ZQFGb7hR12BxqPQ0cDkicWn2CEyw.ttf",
  "800": "http://fonts.gstatic.com/s/grenze/v14/O4ZQFGb7hR12BxqPX0QDkicWn2CEyw.ttf",
  "900": "http://fonts.gstatic.com/s/grenze/v14/O4ZQFGb7hR12BxqPe0UDkicWn2CEyw.ttf",
  "100italic": "http://fonts.gstatic.com/s/grenze/v14/O4ZXFGb7hR12BxqH_VpHsg04k2md0kI.ttf",
  "200italic": "http://fonts.gstatic.com/s/grenze/v14/O4ZWFGb7hR12BxqH_Vrrky0SvWWUy1uW.ttf",
  "300italic": "http://fonts.gstatic.com/s/grenze/v14/O4ZWFGb7hR12BxqH_VqPkC0SvWWUy1uW.ttf",
  "regular": "http://fonts.gstatic.com/s/grenze/v14/O4ZTFGb7hR12Bxq3_2gnmgwKlg.ttf",
  "italic": "http://fonts.gstatic.com/s/grenze/v14/O4ZRFGb7hR12BxqH_WIjuAkalnmd.ttf",
  "500italic": "http://fonts.gstatic.com/s/grenze/v14/O4ZWFGb7hR12BxqH_VrXkS0SvWWUy1uW.ttf",
  "600italic": "http://fonts.gstatic.com/s/grenze/v14/O4ZWFGb7hR12BxqH_Vr7li0SvWWUy1uW.ttf",
  "700italic": "http://fonts.gstatic.com/s/grenze/v14/O4ZWFGb7hR12BxqH_Vqfly0SvWWUy1uW.ttf",
  "800italic": "http://fonts.gstatic.com/s/grenze/v14/O4ZWFGb7hR12BxqH_VqDlC0SvWWUy1uW.ttf",
  "900italic": "http://fonts.gstatic.com/s/grenze/v14/O4ZWFGb7hR12BxqH_VqnlS0SvWWUy1uW.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Grenze Gotisch",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/grenzegotisch/v12/Fh4hPjjqNDz1osh_jX9YfjudpBJBNV5y5wf_k1i5Lz5UcICdYPSd_w.ttf",
  "200": "http://fonts.gstatic.com/s/grenzegotisch/v12/Fh4hPjjqNDz1osh_jX9YfjudpBJBNV5y5wf_k1i5rz9UcICdYPSd_w.ttf",
  "300": "http://fonts.gstatic.com/s/grenzegotisch/v12/Fh4hPjjqNDz1osh_jX9YfjudpBJBNV5y5wf_k1i5cT9UcICdYPSd_w.ttf",
  "500": "http://fonts.gstatic.com/s/grenzegotisch/v12/Fh4hPjjqNDz1osh_jX9YfjudpBJBNV5y5wf_k1i5HT9UcICdYPSd_w.ttf",
  "600": "http://fonts.gstatic.com/s/grenzegotisch/v12/Fh4hPjjqNDz1osh_jX9YfjudpBJBNV5y5wf_k1i58ThUcICdYPSd_w.ttf",
  "700": "http://fonts.gstatic.com/s/grenzegotisch/v12/Fh4hPjjqNDz1osh_jX9YfjudpBJBNV5y5wf_k1i5yDhUcICdYPSd_w.ttf",
  "800": "http://fonts.gstatic.com/s/grenzegotisch/v12/Fh4hPjjqNDz1osh_jX9YfjudpBJBNV5y5wf_k1i5rzhUcICdYPSd_w.ttf",
  "900": "http://fonts.gstatic.com/s/grenzegotisch/v12/Fh4hPjjqNDz1osh_jX9YfjudpBJBNV5y5wf_k1i5hjhUcICdYPSd_w.ttf",
  "regular": "http://fonts.gstatic.com/s/grenzegotisch/v12/Fh4hPjjqNDz1osh_jX9YfjudpBJBNV5y5wf_k1i5Lz9UcICdYPSd_w.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Grey Qo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/greyqo/v7/BXRrvF_Nmv_TyXxNDOtQ9Wf0QcE.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Griffy",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/griffy/v21/FwZa7-ox2FQh9kfwSNSEwM2zpA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gruppo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gruppo/v16/WwkfxPmzE06v_ZWFWXDAOIEQUQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gudea",
  "variants": [
  "regular",
  "italic",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/gudea/v15/neIIzCqgsI0mp9gz26WGHK06UY30.ttf",
  "regular": "http://fonts.gstatic.com/s/gudea/v15/neIFzCqgsI0mp-CP9IGON7Ez.ttf",
  "italic": "http://fonts.gstatic.com/s/gudea/v15/neILzCqgsI0mp9CN_oWsMqEzSJQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gugi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gugi/v13/A2BVn5dXywshVA6A9DEfgqM.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gulzar",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v5",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gulzar/v5/Wnz6HAc9eB3HB2ILYTwZqg_MPQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gupter",
  "variants": [
  "regular",
  "500",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/gupter/v14/2-cl9JNmxJqPO1Qslb-bUsT5rZhaZg.ttf",
  "700": "http://fonts.gstatic.com/s/gupter/v14/2-cl9JNmxJqPO1Qs3bmbUsT5rZhaZg.ttf",
  "regular": "http://fonts.gstatic.com/s/gupter/v14/2-cm9JNmxJqPO1QUYZa_Wu_lpA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gurajada",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/gurajada/v15/FwZY7-Qx308m-l-0Kd6A4sijpFu_.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Gwendolyn",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/gwendolyn/v5/qkBSXvoO_M3CSss-d7emWLtvmC7HONiSFQ.ttf",
  "regular": "http://fonts.gstatic.com/s/gwendolyn/v5/qkBXXvoO_M3CSss-d7ee5JRLkAXbMQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Habibi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/habibi/v21/CSR-4zFWkuqcTTNCShJeZOYySQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hachi Maru Pop",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/hachimarupop/v17/HI_TiYoRLqpLrEiMAuO9Ysfz7rW1EM_btd8u.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hahmlet",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "korean",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/hahmlet/v9/BngXUXpCQ3nKpIo0TfPyfCdXfaeU4RhKOdjobsO-aVxn.ttf",
  "200": "http://fonts.gstatic.com/s/hahmlet/v9/BngXUXpCQ3nKpIo0TfPyfCdXfaeU4RjKONjobsO-aVxn.ttf",
  "300": "http://fonts.gstatic.com/s/hahmlet/v9/BngXUXpCQ3nKpIo0TfPyfCdXfaeU4RgUONjobsO-aVxn.ttf",
  "500": "http://fonts.gstatic.com/s/hahmlet/v9/BngXUXpCQ3nKpIo0TfPyfCdXfaeU4Rh4ONjobsO-aVxn.ttf",
  "600": "http://fonts.gstatic.com/s/hahmlet/v9/BngXUXpCQ3nKpIo0TfPyfCdXfaeU4RiUP9jobsO-aVxn.ttf",
  "700": "http://fonts.gstatic.com/s/hahmlet/v9/BngXUXpCQ3nKpIo0TfPyfCdXfaeU4RitP9jobsO-aVxn.ttf",
  "800": "http://fonts.gstatic.com/s/hahmlet/v9/BngXUXpCQ3nKpIo0TfPyfCdXfaeU4RjKP9jobsO-aVxn.ttf",
  "900": "http://fonts.gstatic.com/s/hahmlet/v9/BngXUXpCQ3nKpIo0TfPyfCdXfaeU4RjjP9jobsO-aVxn.ttf",
  "regular": "http://fonts.gstatic.com/s/hahmlet/v9/BngXUXpCQ3nKpIo0TfPyfCdXfaeU4RhKONjobsO-aVxn.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Halant",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/halant/v13/u-490qaujRI2Pbsvc_pCmwZqcwdRXg.ttf",
  "500": "http://fonts.gstatic.com/s/halant/v13/u-490qaujRI2PbsvK_tCmwZqcwdRXg.ttf",
  "600": "http://fonts.gstatic.com/s/halant/v13/u-490qaujRI2PbsvB_xCmwZqcwdRXg.ttf",
  "700": "http://fonts.gstatic.com/s/halant/v13/u-490qaujRI2PbsvY_1CmwZqcwdRXg.ttf",
  "regular": "http://fonts.gstatic.com/s/halant/v13/u-4-0qaujRI2PbsX39Jmky12eg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hammersmith One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/hammersmithone/v17/qWcyB624q4L_C4jGQ9IK0O_dFlnbshsks4MRXw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hanalei",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/hanalei/v23/E21n_dD8iufIjBRHXzgmVydREus.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hanalei Fill",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/hanaleifill/v21/fC1mPYtObGbfyQznIaQzPQiMVwLBplm9aw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Handlee",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/handlee/v14/-F6xfjBsISg9aMakDmr6oilJ3ik.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hanuman",
  "variants": [
  "100",
  "300",
  "regular",
  "700",
  "900"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-04-21",
  "files": {
  "100": "http://fonts.gstatic.com/s/hanuman/v22/VuJzdNvD15HhpJJBQMLdPKNiaRpFvg.ttf",
  "300": "http://fonts.gstatic.com/s/hanuman/v22/VuJ0dNvD15HhpJJBQAr_HIlMZRNcp0o.ttf",
  "700": "http://fonts.gstatic.com/s/hanuman/v22/VuJ0dNvD15HhpJJBQBr4HIlMZRNcp0o.ttf",
  "900": "http://fonts.gstatic.com/s/hanuman/v22/VuJ0dNvD15HhpJJBQCL6HIlMZRNcp0o.ttf",
  "regular": "http://fonts.gstatic.com/s/hanuman/v22/VuJxdNvD15HhpJJBeKbXOIFneRo.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Happy Monkey",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/happymonkey/v14/K2F2fZZcl-9SXwl5F_C4R_OABwD2bWqVjw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Harmattan",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/harmattan/v15/gokpH6L2DkFvVvRp9Xpr92-HmNZEq6TTFw.ttf",
  "regular": "http://fonts.gstatic.com/s/harmattan/v15/goksH6L2DkFvVvRp9XpTS0CjkP1Yog.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Headland One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/headlandone/v15/yYLu0hHR2vKnp89Tk1TCq3Tx0PlTeZ3mJA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Heebo",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "hebrew",
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/heebo/v21/NGSpv5_NC0k9P_v6ZUCbLRAHxK1EiS2cckOnz02SXQ.ttf",
  "200": "http://fonts.gstatic.com/s/heebo/v21/NGSpv5_NC0k9P_v6ZUCbLRAHxK1ECSycckOnz02SXQ.ttf",
  "300": "http://fonts.gstatic.com/s/heebo/v21/NGSpv5_NC0k9P_v6ZUCbLRAHxK1E1yycckOnz02SXQ.ttf",
  "500": "http://fonts.gstatic.com/s/heebo/v21/NGSpv5_NC0k9P_v6ZUCbLRAHxK1EuyycckOnz02SXQ.ttf",
  "600": "http://fonts.gstatic.com/s/heebo/v21/NGSpv5_NC0k9P_v6ZUCbLRAHxK1EVyucckOnz02SXQ.ttf",
  "700": "http://fonts.gstatic.com/s/heebo/v21/NGSpv5_NC0k9P_v6ZUCbLRAHxK1EbiucckOnz02SXQ.ttf",
  "800": "http://fonts.gstatic.com/s/heebo/v21/NGSpv5_NC0k9P_v6ZUCbLRAHxK1ECSucckOnz02SXQ.ttf",
  "900": "http://fonts.gstatic.com/s/heebo/v21/NGSpv5_NC0k9P_v6ZUCbLRAHxK1EICucckOnz02SXQ.ttf",
  "regular": "http://fonts.gstatic.com/s/heebo/v21/NGSpv5_NC0k9P_v6ZUCbLRAHxK1EiSycckOnz02SXQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Henny Penny",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/hennypenny/v17/wXKvE3UZookzsxz_kjGSfMQqt3M7tMDT.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hepta Slab",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/heptaslab/v17/ea8JadoyU_jkHdalebHvyWVNdYoIsHe5HvkV5jfbY5B0NBkz.ttf",
  "200": "http://fonts.gstatic.com/s/heptaslab/v17/ea8JadoyU_jkHdalebHvyWVNdYoIsHe5HvmV5zfbY5B0NBkz.ttf",
  "300": "http://fonts.gstatic.com/s/heptaslab/v17/ea8JadoyU_jkHdalebHvyWVNdYoIsHe5HvlL5zfbY5B0NBkz.ttf",
  "500": "http://fonts.gstatic.com/s/heptaslab/v17/ea8JadoyU_jkHdalebHvyWVNdYoIsHe5Hvkn5zfbY5B0NBkz.ttf",
  "600": "http://fonts.gstatic.com/s/heptaslab/v17/ea8JadoyU_jkHdalebHvyWVNdYoIsHe5HvnL4DfbY5B0NBkz.ttf",
  "700": "http://fonts.gstatic.com/s/heptaslab/v17/ea8JadoyU_jkHdalebHvyWVNdYoIsHe5Hvny4DfbY5B0NBkz.ttf",
  "800": "http://fonts.gstatic.com/s/heptaslab/v17/ea8JadoyU_jkHdalebHvyWVNdYoIsHe5HvmV4DfbY5B0NBkz.ttf",
  "900": "http://fonts.gstatic.com/s/heptaslab/v17/ea8JadoyU_jkHdalebHvyWVNdYoIsHe5Hvm84DfbY5B0NBkz.ttf",
  "regular": "http://fonts.gstatic.com/s/heptaslab/v17/ea8JadoyU_jkHdalebHvyWVNdYoIsHe5HvkV5zfbY5B0NBkz.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Herr Von Muellerhoff",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/herrvonmuellerhoff/v15/WBL6rFjRZkREW8WqmCWYLgCkQKXb4CAft3c6_qJY3QPQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hi Melody",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/himelody/v13/46ktlbP8Vnz0pJcqCTbEf29E31BBGA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hina Mincho",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v8",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/hinamincho/v8/2sDaZGBRhpXa2Jjz5w5LAGW8KbkVZTHR.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hind",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/hind/v16/5aU19_a8oxmIfMJaIRuYjDpf5Vw.ttf",
  "500": "http://fonts.gstatic.com/s/hind/v16/5aU19_a8oxmIfJpbIRuYjDpf5Vw.ttf",
  "600": "http://fonts.gstatic.com/s/hind/v16/5aU19_a8oxmIfLZcIRuYjDpf5Vw.ttf",
  "700": "http://fonts.gstatic.com/s/hind/v16/5aU19_a8oxmIfNJdIRuYjDpf5Vw.ttf",
  "regular": "http://fonts.gstatic.com/s/hind/v16/5aU69_a8oxmIRG5yBROzkDM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hind Guntur",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "telugu"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/hindguntur/v12/wXKyE3UZrok56nvamSuJd_yGn1czn9zaj5Ju.ttf",
  "500": "http://fonts.gstatic.com/s/hindguntur/v12/wXKyE3UZrok56nvamSuJd_zenlczn9zaj5Ju.ttf",
  "600": "http://fonts.gstatic.com/s/hindguntur/v12/wXKyE3UZrok56nvamSuJd_zymVczn9zaj5Ju.ttf",
  "700": "http://fonts.gstatic.com/s/hindguntur/v12/wXKyE3UZrok56nvamSuJd_yWmFczn9zaj5Ju.ttf",
  "regular": "http://fonts.gstatic.com/s/hindguntur/v12/wXKvE3UZrok56nvamSuJd8Qqt3M7tMDT.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hind Madurai",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/hindmadurai/v11/f0Xu0e2p98ZvDXdZQIOcpqjfXaUnecsoMJ0b_g.ttf",
  "500": "http://fonts.gstatic.com/s/hindmadurai/v11/f0Xu0e2p98ZvDXdZQIOcpqjfBaQnecsoMJ0b_g.ttf",
  "600": "http://fonts.gstatic.com/s/hindmadurai/v11/f0Xu0e2p98ZvDXdZQIOcpqjfKaMnecsoMJ0b_g.ttf",
  "700": "http://fonts.gstatic.com/s/hindmadurai/v11/f0Xu0e2p98ZvDXdZQIOcpqjfTaInecsoMJ0b_g.ttf",
  "regular": "http://fonts.gstatic.com/s/hindmadurai/v11/f0Xx0e2p98ZvDXdZQIOcpqjn8Y0DceA0OQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hind Siliguri",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "bengali",
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/hindsiliguri/v12/ijwOs5juQtsyLLR5jN4cxBEoRDf44uEfKiGvxts.ttf",
  "500": "http://fonts.gstatic.com/s/hindsiliguri/v12/ijwOs5juQtsyLLR5jN4cxBEoRG_54uEfKiGvxts.ttf",
  "600": "http://fonts.gstatic.com/s/hindsiliguri/v12/ijwOs5juQtsyLLR5jN4cxBEoREP-4uEfKiGvxts.ttf",
  "700": "http://fonts.gstatic.com/s/hindsiliguri/v12/ijwOs5juQtsyLLR5jN4cxBEoRCf_4uEfKiGvxts.ttf",
  "regular": "http://fonts.gstatic.com/s/hindsiliguri/v12/ijwTs5juQtsyLLR5jN4cxBEofJvQxuk0Nig.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hind Vadodara",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/hindvadodara/v12/neIQzCKvrIcn5pbuuuriV9tTSDn3iXM0oSOL2Yw.ttf",
  "500": "http://fonts.gstatic.com/s/hindvadodara/v12/neIQzCKvrIcn5pbuuuriV9tTSGH2iXM0oSOL2Yw.ttf",
  "600": "http://fonts.gstatic.com/s/hindvadodara/v12/neIQzCKvrIcn5pbuuuriV9tTSE3xiXM0oSOL2Yw.ttf",
  "700": "http://fonts.gstatic.com/s/hindvadodara/v12/neIQzCKvrIcn5pbuuuriV9tTSCnwiXM0oSOL2Yw.ttf",
  "regular": "http://fonts.gstatic.com/s/hindvadodara/v12/neINzCKvrIcn5pbuuuriV9tTcJXfrXsfvSo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Holtwood One SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/holtwoodonesc/v16/yYLx0hLR0P-3vMFSk1TCq3Txg5B3cbb6LZttyg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Homemade Apple",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/homemadeapple/v18/Qw3EZQFXECDrI2q789EKQZJob3x9Vnksi4M7.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Homenaje",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/homenaje/v16/FwZY7-Q-xVAi_l-6Ld6A4sijpFu_.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hubballi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "kannada",
  "latin",
  "latin-ext"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/hubballi/v4/o-0JIpUj3WIZ1RFN56B7yBBNYuSF.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Hurricane",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/hurricane/v5/pe0sMIuULZxTolZ5YldyAv2-C99ycg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IBM Plex Mono",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6pfjptAgt5VM-kVkqdyU8n3kwq0n1hj-sNFQ.ttf",
  "200": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6qfjptAgt5VM-kVkqdyU8n3uAL8ldPg-IUDNg.ttf",
  "300": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6qfjptAgt5VM-kVkqdyU8n3oQI8ldPg-IUDNg.ttf",
  "500": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6qfjptAgt5VM-kVkqdyU8n3twJ8ldPg-IUDNg.ttf",
  "600": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6qfjptAgt5VM-kVkqdyU8n3vAO8ldPg-IUDNg.ttf",
  "700": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6qfjptAgt5VM-kVkqdyU8n3pQP8ldPg-IUDNg.ttf",
  "100italic": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6rfjptAgt5VM-kVkqdyU8n1ioStndlre4dFcFh.ttf",
  "200italic": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6sfjptAgt5VM-kVkqdyU8n1ioSGlZFh8ARHNh4zg.ttf",
  "300italic": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6sfjptAgt5VM-kVkqdyU8n1ioSflVFh8ARHNh4zg.ttf",
  "regular": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F63fjptAgt5VM-kVkqdyU8n5igg1l9kn-s.ttf",
  "italic": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6pfjptAgt5VM-kVkqdyU8n1ioq0n1hj-sNFQ.ttf",
  "500italic": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6sfjptAgt5VM-kVkqdyU8n1ioSJlRFh8ARHNh4zg.ttf",
  "600italic": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6sfjptAgt5VM-kVkqdyU8n1ioSClNFh8ARHNh4zg.ttf",
  "700italic": "http://fonts.gstatic.com/s/ibmplexmono/v12/-F6sfjptAgt5VM-kVkqdyU8n1ioSblJFh8ARHNh4zg.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IBM Plex Sans",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX-KVElMYYaJe8bpLHnCwDKjbLeEKxIedbzDw.ttf",
  "200": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX9KVElMYYaJe8bpLHnCwDKjR7_MIZmdd_qFmo.ttf",
  "300": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX9KVElMYYaJe8bpLHnCwDKjXr8MIZmdd_qFmo.ttf",
  "500": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX9KVElMYYaJe8bpLHnCwDKjSL9MIZmdd_qFmo.ttf",
  "600": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX9KVElMYYaJe8bpLHnCwDKjQ76MIZmdd_qFmo.ttf",
  "700": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX9KVElMYYaJe8bpLHnCwDKjWr7MIZmdd_qFmo.ttf",
  "100italic": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX8KVElMYYaJe8bpLHnCwDKhdTmdKZMW9PjD3N8.ttf",
  "200italic": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX7KVElMYYaJe8bpLHnCwDKhdTm2Idscf3vBmpl8A.ttf",
  "300italic": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX7KVElMYYaJe8bpLHnCwDKhdTmvIRscf3vBmpl8A.ttf",
  "regular": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYXgKVElMYYaJe8bpLHnCwDKtdbUFI5NadY.ttf",
  "italic": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX-KVElMYYaJe8bpLHnCwDKhdTeEKxIedbzDw.ttf",
  "500italic": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX7KVElMYYaJe8bpLHnCwDKhdTm5IVscf3vBmpl8A.ttf",
  "600italic": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX7KVElMYYaJe8bpLHnCwDKhdTmyIJscf3vBmpl8A.ttf",
  "700italic": "http://fonts.gstatic.com/s/ibmplexsans/v14/zYX7KVElMYYaJe8bpLHnCwDKhdTmrINscf3vBmpl8A.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IBM Plex Sans Arabic",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "arabic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/ibmplexsansarabic/v7/Qw3MZRtWPQCuHme67tEYUIx3Kh0PHR9N6YNe3PC5eMlAMg0.ttf",
  "200": "http://fonts.gstatic.com/s/ibmplexsansarabic/v7/Qw3NZRtWPQCuHme67tEYUIx3Kh0PHR9N6YPy_dCTVsVJKxTs.ttf",
  "300": "http://fonts.gstatic.com/s/ibmplexsansarabic/v7/Qw3NZRtWPQCuHme67tEYUIx3Kh0PHR9N6YOW_tCTVsVJKxTs.ttf",
  "500": "http://fonts.gstatic.com/s/ibmplexsansarabic/v7/Qw3NZRtWPQCuHme67tEYUIx3Kh0PHR9N6YPO_9CTVsVJKxTs.ttf",
  "600": "http://fonts.gstatic.com/s/ibmplexsansarabic/v7/Qw3NZRtWPQCuHme67tEYUIx3Kh0PHR9N6YPi-NCTVsVJKxTs.ttf",
  "700": "http://fonts.gstatic.com/s/ibmplexsansarabic/v7/Qw3NZRtWPQCuHme67tEYUIx3Kh0PHR9N6YOG-dCTVsVJKxTs.ttf",
  "regular": "http://fonts.gstatic.com/s/ibmplexsansarabic/v7/Qw3CZRtWPQCuHme67tEYUIx3Kh0PHR9N6bs61vSbfdlA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IBM Plex Sans Condensed",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8nN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHY7KyKvBgYsMDhM.ttf",
  "200": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8gN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHY5m6Yvrr4cFFwq5.ttf",
  "300": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8gN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHY4C6ovrr4cFFwq5.ttf",
  "500": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8gN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHY5a64vrr4cFFwq5.ttf",
  "600": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8gN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHY527Ivrr4cFFwq5.ttf",
  "700": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8gN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHY4S7Yvrr4cFFwq5.ttf",
  "100italic": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8hN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHYas8M_LhakJHhOgBg.ttf",
  "200italic": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8iN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHYas8GPqpYMnEhq5H1w.ttf",
  "300italic": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8iN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHYas8AfppYMnEhq5H1w.ttf",
  "regular": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8lN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHbauwq_jhJsM.ttf",
  "italic": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8nN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHYasyKvBgYsMDhM.ttf",
  "500italic": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8iN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHYas8F_opYMnEhq5H1w.ttf",
  "600italic": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8iN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHYas8HPvpYMnEhq5H1w.ttf",
  "700italic": "http://fonts.gstatic.com/s/ibmplexsanscondensed/v13/Gg8iN4UfRSqiPg7Jn2ZI12V4DCEwkj1E4LVeHYas8BfupYMnEhq5H1w.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IBM Plex Sans Devanagari",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic-ext",
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/ibmplexsansdevanagari/v7/XRXB3JCMvG4IDoS9SubXB6W-UX5iehIMBFR2-O_HMUjwUcjwCEQq.ttf",
  "200": "http://fonts.gstatic.com/s/ibmplexsansdevanagari/v7/XRXA3JCMvG4IDoS9SubXB6W-UX5iehIMBFR2-O_HnWnQe-b8AV0z0w.ttf",
  "300": "http://fonts.gstatic.com/s/ibmplexsansdevanagari/v7/XRXA3JCMvG4IDoS9SubXB6W-UX5iehIMBFR2-O_H-WrQe-b8AV0z0w.ttf",
  "500": "http://fonts.gstatic.com/s/ibmplexsansdevanagari/v7/XRXA3JCMvG4IDoS9SubXB6W-UX5iehIMBFR2-O_HoWvQe-b8AV0z0w.ttf",
  "600": "http://fonts.gstatic.com/s/ibmplexsansdevanagari/v7/XRXA3JCMvG4IDoS9SubXB6W-UX5iehIMBFR2-O_HjWzQe-b8AV0z0w.ttf",
  "700": "http://fonts.gstatic.com/s/ibmplexsansdevanagari/v7/XRXA3JCMvG4IDoS9SubXB6W-UX5iehIMBFR2-O_H6W3Qe-b8AV0z0w.ttf",
  "regular": "http://fonts.gstatic.com/s/ibmplexsansdevanagari/v7/XRXH3JCMvG4IDoS9SubXB6W-UX5iehIMBFR2-O__VUL0c83gCA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IBM Plex Sans Hebrew",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/ibmplexsanshebrew/v8/BCa4qYENg9Kw1mpLpO0bGM5lfHAAZHhDXEXB-l0VqDaM7C4.ttf",
  "200": "http://fonts.gstatic.com/s/ibmplexsanshebrew/v8/BCa5qYENg9Kw1mpLpO0bGM5lfHAAZHhDXEVt230_hjqF9Tc2.ttf",
  "300": "http://fonts.gstatic.com/s/ibmplexsanshebrew/v8/BCa5qYENg9Kw1mpLpO0bGM5lfHAAZHhDXEUJ2H0_hjqF9Tc2.ttf",
  "500": "http://fonts.gstatic.com/s/ibmplexsanshebrew/v8/BCa5qYENg9Kw1mpLpO0bGM5lfHAAZHhDXEVR2X0_hjqF9Tc2.ttf",
  "600": "http://fonts.gstatic.com/s/ibmplexsanshebrew/v8/BCa5qYENg9Kw1mpLpO0bGM5lfHAAZHhDXEV93n0_hjqF9Tc2.ttf",
  "700": "http://fonts.gstatic.com/s/ibmplexsanshebrew/v8/BCa5qYENg9Kw1mpLpO0bGM5lfHAAZHhDXEUZ330_hjqF9Tc2.ttf",
  "regular": "http://fonts.gstatic.com/s/ibmplexsanshebrew/v8/BCa2qYENg9Kw1mpLpO0bGM5lfHAAZHhDXH2l8Fk3rSaM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IBM Plex Sans KR",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "korean",
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/ibmplexsanskr/v7/vEFM2-VJISZe3O_rc3ZVYh4aTwNOyra_X5zCpMrMfA.ttf",
  "200": "http://fonts.gstatic.com/s/ibmplexsanskr/v7/vEFN2-VJISZe3O_rc3ZVYh4aTwNOyhqef7bsqMPVZb4.ttf",
  "300": "http://fonts.gstatic.com/s/ibmplexsanskr/v7/vEFN2-VJISZe3O_rc3ZVYh4aTwNOyn6df7bsqMPVZb4.ttf",
  "500": "http://fonts.gstatic.com/s/ibmplexsanskr/v7/vEFN2-VJISZe3O_rc3ZVYh4aTwNOyiacf7bsqMPVZb4.ttf",
  "600": "http://fonts.gstatic.com/s/ibmplexsanskr/v7/vEFN2-VJISZe3O_rc3ZVYh4aTwNOygqbf7bsqMPVZb4.ttf",
  "700": "http://fonts.gstatic.com/s/ibmplexsanskr/v7/vEFN2-VJISZe3O_rc3ZVYh4aTwNOym6af7bsqMPVZb4.ttf",
  "regular": "http://fonts.gstatic.com/s/ibmplexsanskr/v7/vEFK2-VJISZe3O_rc3ZVYh4aTwNO8tK1W77HtMo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IBM Plex Sans Thai",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "thai"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/ibmplexsansthai/v7/m8JNje1VVIzcq1HzJq2AEdo2Tj_qvLqEatYlR8ZKUqcX.ttf",
  "200": "http://fonts.gstatic.com/s/ibmplexsansthai/v7/m8JMje1VVIzcq1HzJq2AEdo2Tj_qvLqExvcFbehGW74OXw.ttf",
  "300": "http://fonts.gstatic.com/s/ibmplexsansthai/v7/m8JMje1VVIzcq1HzJq2AEdo2Tj_qvLqEovQFbehGW74OXw.ttf",
  "500": "http://fonts.gstatic.com/s/ibmplexsansthai/v7/m8JMje1VVIzcq1HzJq2AEdo2Tj_qvLqE-vUFbehGW74OXw.ttf",
  "600": "http://fonts.gstatic.com/s/ibmplexsansthai/v7/m8JMje1VVIzcq1HzJq2AEdo2Tj_qvLqE1vIFbehGW74OXw.ttf",
  "700": "http://fonts.gstatic.com/s/ibmplexsansthai/v7/m8JMje1VVIzcq1HzJq2AEdo2Tj_qvLqEsvMFbehGW74OXw.ttf",
  "regular": "http://fonts.gstatic.com/s/ibmplexsansthai/v7/m8JPje1VVIzcq1HzJq2AEdo2Tj_qvLq8DtwhZcNaUg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IBM Plex Sans Thai Looped",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "thai"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/ibmplexsansthailooped/v7/tss5AoJJRAhL3BTrK3r2xxbFhvKfyBB6l7hHT30L_HaKpHOtFCQ76Q.ttf",
  "200": "http://fonts.gstatic.com/s/ibmplexsansthailooped/v7/tss6AoJJRAhL3BTrK3r2xxbFhvKfyBB6l7hHT30L_NqrhFmDGC0i8Cc.ttf",
  "300": "http://fonts.gstatic.com/s/ibmplexsansthailooped/v7/tss6AoJJRAhL3BTrK3r2xxbFhvKfyBB6l7hHT30L_L6ohFmDGC0i8Cc.ttf",
  "500": "http://fonts.gstatic.com/s/ibmplexsansthailooped/v7/tss6AoJJRAhL3BTrK3r2xxbFhvKfyBB6l7hHT30L_OaphFmDGC0i8Cc.ttf",
  "600": "http://fonts.gstatic.com/s/ibmplexsansthailooped/v7/tss6AoJJRAhL3BTrK3r2xxbFhvKfyBB6l7hHT30L_MquhFmDGC0i8Cc.ttf",
  "700": "http://fonts.gstatic.com/s/ibmplexsansthailooped/v7/tss6AoJJRAhL3BTrK3r2xxbFhvKfyBB6l7hHT30L_K6vhFmDGC0i8Cc.ttf",
  "regular": "http://fonts.gstatic.com/s/ibmplexsansthailooped/v7/tss_AoJJRAhL3BTrK3r2xxbFhvKfyBB6l7hHT30LxBKAoFGoBCQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IBM Plex Serif",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizBREVNn1dOx-zrZ2X3pZvkTi182zIZj1bIkNo.ttf",
  "200": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizAREVNn1dOx-zrZ2X3pZvkTi3Q-hIzoVrBicOg.ttf",
  "300": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizAREVNn1dOx-zrZ2X3pZvkTi20-RIzoVrBicOg.ttf",
  "500": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizAREVNn1dOx-zrZ2X3pZvkTi3s-BIzoVrBicOg.ttf",
  "600": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizAREVNn1dOx-zrZ2X3pZvkTi3A_xIzoVrBicOg.ttf",
  "700": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizAREVNn1dOx-zrZ2X3pZvkTi2k_hIzoVrBicOg.ttf",
  "100italic": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizHREVNn1dOx-zrZ2X3pZvkTiUa41YTi3TNgNq55w.ttf",
  "200italic": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizGREVNn1dOx-zrZ2X3pZvkTiUa4_oyq17jjNOg_oc.ttf",
  "300italic": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizGREVNn1dOx-zrZ2X3pZvkTiUa454xq17jjNOg_oc.ttf",
  "regular": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizDREVNn1dOx-zrZ2X3pZvkThUY0TY7ikbI.ttf",
  "italic": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizBREVNn1dOx-zrZ2X3pZvkTiUa2zIZj1bIkNo.ttf",
  "500italic": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizGREVNn1dOx-zrZ2X3pZvkTiUa48Ywq17jjNOg_oc.ttf",
  "600italic": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizGREVNn1dOx-zrZ2X3pZvkTiUa4-o3q17jjNOg_oc.ttf",
  "700italic": "http://fonts.gstatic.com/s/ibmplexserif/v15/jizGREVNn1dOx-zrZ2X3pZvkTiUa4442q17jjNOg_oc.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IM Fell DW Pica",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imfelldwpica/v16/2sDGZGRQotv9nbn2qSl0TxXVYNw9ZAPUvi88MQ.ttf",
  "italic": "http://fonts.gstatic.com/s/imfelldwpica/v16/2sDEZGRQotv9nbn2qSl0TxXVYNwNZgnQnCosMXm0.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IM Fell DW Pica SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imfelldwpicasc/v21/0ybjGCAu5PfqkvtGVU15aBhXz3EUrnTW-BiKEUiBGA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IM Fell Double Pica",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imfelldoublepica/v14/3XF2EqMq_94s9PeKF7Fg4gOKINyMtZ8rT0S1UL5Ayp0.ttf",
  "italic": "http://fonts.gstatic.com/s/imfelldoublepica/v14/3XF0EqMq_94s9PeKF7Fg4gOKINyMtZ8rf0a_VJxF2p2G8g.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IM Fell Double Pica SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imfelldoublepicasc/v21/neIazDmuiMkFo6zj_sHpQ8teNbWlwBB_hXjJ4Y0Eeru2dGg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IM Fell English",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imfellenglish/v14/Ktk1ALSLW8zDe0rthJysWrnLsAz3F6mZVY9Y5w.ttf",
  "italic": "http://fonts.gstatic.com/s/imfellenglish/v14/Ktk3ALSLW8zDe0rthJysWrnLsAzHFaOdd4pI59zg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IM Fell English SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imfellenglishsc/v16/a8IENpD3CDX-4zrWfr1VY879qFF05pZLO4gOg0shzA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IM Fell French Canon",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imfellfrenchcanon/v21/-F6ufiNtDWYfYc-tDiyiw08rrghJszkK6coVPt1ozoPz.ttf",
  "italic": "http://fonts.gstatic.com/s/imfellfrenchcanon/v21/-F6gfiNtDWYfYc-tDiyiw08rrghJszkK6foXNNlKy5PzzrU.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IM Fell French Canon SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imfellfrenchcanonsc/v22/FBVmdCru5-ifcor2bgq9V89khWcmQghEURY7H3c0UBCVIVqH.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IM Fell Great Primer",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imfellgreatprimer/v21/bx6aNwSJtayYxOkbYFsT6hMsLzX7u85rJorXvDo3SQY1.ttf",
  "italic": "http://fonts.gstatic.com/s/imfellgreatprimer/v21/bx6UNwSJtayYxOkbYFsT6hMsLzX7u85rJrrVtj4VTBY1N6U.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "IM Fell Great Primer SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imfellgreatprimersc/v21/ga6daxBOxyt6sCqz3fjZCTFCTUDMHagsQKdDTLf9BXz0s8FG.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ibarra Real Nova",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/ibarrarealnova/v20/sZlSdQiA-DBIDCcaWtQzL4BZHoiDundw4ATyjed3EXdS5MDtVT9TWIvS.ttf",
  "600": "http://fonts.gstatic.com/s/ibarrarealnova/v20/sZlSdQiA-DBIDCcaWtQzL4BZHoiDundw4ATyjed3EXe-48DtVT9TWIvS.ttf",
  "700": "http://fonts.gstatic.com/s/ibarrarealnova/v20/sZlSdQiA-DBIDCcaWtQzL4BZHoiDundw4ATyjed3EXeH48DtVT9TWIvS.ttf",
  "regular": "http://fonts.gstatic.com/s/ibarrarealnova/v20/sZlSdQiA-DBIDCcaWtQzL4BZHoiDundw4ATyjed3EXdg5MDtVT9TWIvS.ttf",
  "italic": "http://fonts.gstatic.com/s/ibarrarealnova/v20/sZlsdQiA-DBIDCcaWtQzL4BZHoiDkH5CH9yb5n3ZFmKopyiuXztxXZvSkTo.ttf",
  "500italic": "http://fonts.gstatic.com/s/ibarrarealnova/v20/sZlsdQiA-DBIDCcaWtQzL4BZHoiDkH5CH9yb5n3ZFmKopxquXztxXZvSkTo.ttf",
  "600italic": "http://fonts.gstatic.com/s/ibarrarealnova/v20/sZlsdQiA-DBIDCcaWtQzL4BZHoiDkH5CH9yb5n3ZFmKop_apXztxXZvSkTo.ttf",
  "700italic": "http://fonts.gstatic.com/s/ibarrarealnova/v20/sZlsdQiA-DBIDCcaWtQzL4BZHoiDkH5CH9yb5n3ZFmKop8-pXztxXZvSkTo.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Iceberg",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/iceberg/v20/8QIJdijAiM7o-qnZuIgOq7jkAOw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Iceland",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/iceland/v16/rax9HiuFsdMNOnWPWKxGADBbg0s.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Imbue",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/imbue/v21/RLpXK5P16Ki3fXhj5cvGrqjocPk4n-gVX3M93TnrnvhoP8iWfOsNNK-Q4xY.ttf",
  "200": "http://fonts.gstatic.com/s/imbue/v21/RLpXK5P16Ki3fXhj5cvGrqjocPk4n-gVX3M93TnrnvhoP0iXfOsNNK-Q4xY.ttf",
  "300": "http://fonts.gstatic.com/s/imbue/v21/RLpXK5P16Ki3fXhj5cvGrqjocPk4n-gVX3M93TnrnvhoP5aXfOsNNK-Q4xY.ttf",
  "500": "http://fonts.gstatic.com/s/imbue/v21/RLpXK5P16Ki3fXhj5cvGrqjocPk4n-gVX3M93TnrnvhoP_qXfOsNNK-Q4xY.ttf",
  "600": "http://fonts.gstatic.com/s/imbue/v21/RLpXK5P16Ki3fXhj5cvGrqjocPk4n-gVX3M93TnrnvhoPxaQfOsNNK-Q4xY.ttf",
  "700": "http://fonts.gstatic.com/s/imbue/v21/RLpXK5P16Ki3fXhj5cvGrqjocPk4n-gVX3M93TnrnvhoPy-QfOsNNK-Q4xY.ttf",
  "800": "http://fonts.gstatic.com/s/imbue/v21/RLpXK5P16Ki3fXhj5cvGrqjocPk4n-gVX3M93TnrnvhoP0iQfOsNNK-Q4xY.ttf",
  "900": "http://fonts.gstatic.com/s/imbue/v21/RLpXK5P16Ki3fXhj5cvGrqjocPk4n-gVX3M93TnrnvhoP2GQfOsNNK-Q4xY.ttf",
  "regular": "http://fonts.gstatic.com/s/imbue/v21/RLpXK5P16Ki3fXhj5cvGrqjocPk4n-gVX3M93TnrnvhoP8iXfOsNNK-Q4xY.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Imperial Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imperialscript/v3/5DCPAKrpzy_H98IV2ISnZBbGrVNvPenlvttWNg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Imprima",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/imprima/v16/VEMxRoN7sY3yuy-7-oWHyDzktPo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Inconsolata",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v31",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/inconsolata/v31/QldgNThLqRwH-OJ1UHjlKENVzkWGVkL3GZQmAwLYxYWI2qfdm7LppwU8aRr8lleY2co.ttf",
  "300": "http://fonts.gstatic.com/s/inconsolata/v31/QldgNThLqRwH-OJ1UHjlKENVzkWGVkL3GZQmAwLYxYWI2qfdm7Lpp9s8aRr8lleY2co.ttf",
  "500": "http://fonts.gstatic.com/s/inconsolata/v31/QldgNThLqRwH-OJ1UHjlKENVzkWGVkL3GZQmAwLYxYWI2qfdm7Lpp7c8aRr8lleY2co.ttf",
  "600": "http://fonts.gstatic.com/s/inconsolata/v31/QldgNThLqRwH-OJ1UHjlKENVzkWGVkL3GZQmAwLYxYWI2qfdm7Lpp1s7aRr8lleY2co.ttf",
  "700": "http://fonts.gstatic.com/s/inconsolata/v31/QldgNThLqRwH-OJ1UHjlKENVzkWGVkL3GZQmAwLYxYWI2qfdm7Lpp2I7aRr8lleY2co.ttf",
  "800": "http://fonts.gstatic.com/s/inconsolata/v31/QldgNThLqRwH-OJ1UHjlKENVzkWGVkL3GZQmAwLYxYWI2qfdm7LppwU7aRr8lleY2co.ttf",
  "900": "http://fonts.gstatic.com/s/inconsolata/v31/QldgNThLqRwH-OJ1UHjlKENVzkWGVkL3GZQmAwLYxYWI2qfdm7Lppyw7aRr8lleY2co.ttf",
  "regular": "http://fonts.gstatic.com/s/inconsolata/v31/QldgNThLqRwH-OJ1UHjlKENVzkWGVkL3GZQmAwLYxYWI2qfdm7Lpp4U8aRr8lleY2co.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Inder",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/inder/v14/w8gUH2YoQe8_4vq6pw-P3U4O.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Indie Flower",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/indieflower/v17/m8JVjfNVeKWVnh3QMuKkFcZlbkGG1dKEDw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ingrid Darling",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ingriddarling/v2/LDIrapaJNxUtSuFdw-9yf4rCPsLOub458jGL.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Inika",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/inika/v21/rnCr-x5X3QP-pix7auM-mHnOSOuk.ttf",
  "regular": "http://fonts.gstatic.com/s/inika/v21/rnCm-x5X3QP-phTHRcc2s2XH.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Inknut Antiqua",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/inknutantiqua/v14/Y4GRYax7VC4ot_qNB4nYpBdaKU2vwrj5bBoIYJNf.ttf",
  "500": "http://fonts.gstatic.com/s/inknutantiqua/v14/Y4GRYax7VC4ot_qNB4nYpBdaKU33w7j5bBoIYJNf.ttf",
  "600": "http://fonts.gstatic.com/s/inknutantiqua/v14/Y4GRYax7VC4ot_qNB4nYpBdaKU3bxLj5bBoIYJNf.ttf",
  "700": "http://fonts.gstatic.com/s/inknutantiqua/v14/Y4GRYax7VC4ot_qNB4nYpBdaKU2_xbj5bBoIYJNf.ttf",
  "800": "http://fonts.gstatic.com/s/inknutantiqua/v14/Y4GRYax7VC4ot_qNB4nYpBdaKU2jxrj5bBoIYJNf.ttf",
  "900": "http://fonts.gstatic.com/s/inknutantiqua/v14/Y4GRYax7VC4ot_qNB4nYpBdaKU2Hx7j5bBoIYJNf.ttf",
  "regular": "http://fonts.gstatic.com/s/inknutantiqua/v14/Y4GSYax7VC4ot_qNB4nYpBdaKXUD6pzxRwYB.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Inria Sans",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/inriasans/v14/ptRPTiqXYfZMCOiVj9kQ3ELaDQtFqeY3fX4.ttf",
  "700": "http://fonts.gstatic.com/s/inriasans/v14/ptRPTiqXYfZMCOiVj9kQ3FLdDQtFqeY3fX4.ttf",
  "300italic": "http://fonts.gstatic.com/s/inriasans/v14/ptRRTiqXYfZMCOiVj9kQ1OzAgQlPrcQybX4pQA.ttf",
  "regular": "http://fonts.gstatic.com/s/inriasans/v14/ptRMTiqXYfZMCOiVj9kQ5O7yKQNute8.ttf",
  "italic": "http://fonts.gstatic.com/s/inriasans/v14/ptROTiqXYfZMCOiVj9kQ1Oz4LSFrpe8uZA.ttf",
  "700italic": "http://fonts.gstatic.com/s/inriasans/v14/ptRRTiqXYfZMCOiVj9kQ1OzAkQ5PrcQybX4pQA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Inria Serif",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/inriaserif/v14/fC14PYxPY3rXxEndZJAzN3wAVQjFhFyta3xN.ttf",
  "700": "http://fonts.gstatic.com/s/inriaserif/v14/fC14PYxPY3rXxEndZJAzN3wQUgjFhFyta3xN.ttf",
  "300italic": "http://fonts.gstatic.com/s/inriaserif/v14/fC16PYxPY3rXxEndZJAzN3SuT4THjliPbmxN0_E.ttf",
  "regular": "http://fonts.gstatic.com/s/inriaserif/v14/fC1lPYxPY3rXxEndZJAzN0SsfSzNr0Ck.ttf",
  "italic": "http://fonts.gstatic.com/s/inriaserif/v14/fC1nPYxPY3rXxEndZJAzN3SudyjvqlCkcmU.ttf",
  "700italic": "http://fonts.gstatic.com/s/inriaserif/v14/fC16PYxPY3rXxEndZJAzN3SuT5TAjliPbmxN0_E.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Inspiration",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/inspiration/v3/x3dkckPPZa6L4wIg5cZOEvoGnSrlBBsy.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Inter",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuLyeMZhrib2Bg-4.ttf",
  "200": "http://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuDyfMZhrib2Bg-4.ttf",
  "300": "http://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuOKfMZhrib2Bg-4.ttf",
  "500": "http://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuI6fMZhrib2Bg-4.ttf",
  "600": "http://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuGKYMZhrib2Bg-4.ttf",
  "700": "http://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuFuYMZhrib2Bg-4.ttf",
  "800": "http://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuDyYMZhrib2Bg-4.ttf",
  "900": "http://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuBWYMZhrib2Bg-4.ttf",
  "regular": "http://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuLyfMZhrib2Bg-4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Inter Tight",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/intertight/v1/NGSnv5HMAFg6IuGlBNMjxJEL2VmU3NS7Z2mjDw6qXCRToK8EPg.ttf",
  "200": "http://fonts.gstatic.com/s/intertight/v1/NGSnv5HMAFg6IuGlBNMjxJEL2VmU3NS7Z2mjjw-qXCRToK8EPg.ttf",
  "300": "http://fonts.gstatic.com/s/intertight/v1/NGSnv5HMAFg6IuGlBNMjxJEL2VmU3NS7Z2mjUQ-qXCRToK8EPg.ttf",
  "500": "http://fonts.gstatic.com/s/intertight/v1/NGSnv5HMAFg6IuGlBNMjxJEL2VmU3NS7Z2mjPQ-qXCRToK8EPg.ttf",
  "600": "http://fonts.gstatic.com/s/intertight/v1/NGSnv5HMAFg6IuGlBNMjxJEL2VmU3NS7Z2mj0QiqXCRToK8EPg.ttf",
  "700": "http://fonts.gstatic.com/s/intertight/v1/NGSnv5HMAFg6IuGlBNMjxJEL2VmU3NS7Z2mj6AiqXCRToK8EPg.ttf",
  "800": "http://fonts.gstatic.com/s/intertight/v1/NGSnv5HMAFg6IuGlBNMjxJEL2VmU3NS7Z2mjjwiqXCRToK8EPg.ttf",
  "900": "http://fonts.gstatic.com/s/intertight/v1/NGSnv5HMAFg6IuGlBNMjxJEL2VmU3NS7Z2mjpgiqXCRToK8EPg.ttf",
  "regular": "http://fonts.gstatic.com/s/intertight/v1/NGSnv5HMAFg6IuGlBNMjxJEL2VmU3NS7Z2mjDw-qXCRToK8EPg.ttf",
  "100italic": "http://fonts.gstatic.com/s/intertight/v1/NGShv5HMAFg6IuGlBNMjxLsC66ZMtb8hyW62x0xCHi5XgqoUPvi5.ttf",
  "200italic": "http://fonts.gstatic.com/s/intertight/v1/NGShv5HMAFg6IuGlBNMjxLsC66ZMtb8hyW62x0zCHy5XgqoUPvi5.ttf",
  "300italic": "http://fonts.gstatic.com/s/intertight/v1/NGShv5HMAFg6IuGlBNMjxLsC66ZMtb8hyW62x0wcHy5XgqoUPvi5.ttf",
  "italic": "http://fonts.gstatic.com/s/intertight/v1/NGShv5HMAFg6IuGlBNMjxLsC66ZMtb8hyW62x0xCHy5XgqoUPvi5.ttf",
  "500italic": "http://fonts.gstatic.com/s/intertight/v1/NGShv5HMAFg6IuGlBNMjxLsC66ZMtb8hyW62x0xwHy5XgqoUPvi5.ttf",
  "600italic": "http://fonts.gstatic.com/s/intertight/v1/NGShv5HMAFg6IuGlBNMjxLsC66ZMtb8hyW62x0ycGC5XgqoUPvi5.ttf",
  "700italic": "http://fonts.gstatic.com/s/intertight/v1/NGShv5HMAFg6IuGlBNMjxLsC66ZMtb8hyW62x0ylGC5XgqoUPvi5.ttf",
  "800italic": "http://fonts.gstatic.com/s/intertight/v1/NGShv5HMAFg6IuGlBNMjxLsC66ZMtb8hyW62x0zCGC5XgqoUPvi5.ttf",
  "900italic": "http://fonts.gstatic.com/s/intertight/v1/NGShv5HMAFg6IuGlBNMjxLsC66ZMtb8hyW62x0zrGC5XgqoUPvi5.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Irish Grover",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/irishgrover/v23/buExpoi6YtLz2QW7LA4flVgf-P5Oaiw4cw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Island Moments",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/islandmoments/v3/NaPBcZfVGvBdxIt7Ar0qzkXJF-TGIohbZ6SY.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Istok Web",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/istokweb/v20/3qTqojGmgSyUukBzKslhvU5a_mkUYBfcMw.ttf",
  "regular": "http://fonts.gstatic.com/s/istokweb/v20/3qTvojGmgSyUukBzKslZAWF-9kIIaQ.ttf",
  "italic": "http://fonts.gstatic.com/s/istokweb/v20/3qTpojGmgSyUukBzKslpA2t61EcYaQ7F.ttf",
  "700italic": "http://fonts.gstatic.com/s/istokweb/v20/3qT0ojGmgSyUukBzKslpA1PG-2MQQhLMMygN.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Italiana",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/italiana/v16/QldNNTtLsx4E__B0XTmRY31Wx7Vv.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Italianno",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/italianno/v16/dg4n_p3sv6gCJkwzT6Rnj5YpQwM-gg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Itim",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/itim/v10/0nknC9ziJOYewARKkc7ZdwU.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jacques Francois",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/jacquesfrancois/v20/ZXu9e04ZvKeOOHIe1TMahbcIU2cgmcPqoeRWfbs.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jacques Francois Shadow",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/jacquesfrancoisshadow/v21/KR1FBtOz8PKTMk-kqdkLVrvR0ECFrB6Pin-2_q8VsHuV5ULS.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jaldi",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/jaldi/v12/or3hQ67z0_CI33voSbT3LLQ1niPn.ttf",
  "regular": "http://fonts.gstatic.com/s/jaldi/v12/or3sQ67z0_CI30NUZpD_B6g8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "JetBrains Mono",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8yK1jPVmUsaaDhw.ttf",
  "200": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8SKxjPVmUsaaDhw.ttf",
  "300": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8lqxjPVmUsaaDhw.ttf",
  "500": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8-qxjPVmUsaaDhw.ttf",
  "600": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8FqtjPVmUsaaDhw.ttf",
  "700": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8L6tjPVmUsaaDhw.ttf",
  "800": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8SKtjPVmUsaaDhw.ttf",
  "regular": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8yKxjPVmUsaaDhw.ttf",
  "100italic": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDba2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO-Lf1OQk6OThxPA.ttf",
  "200italic": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDba2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO8LflOQk6OThxPA.ttf",
  "300italic": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDba2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO_VflOQk6OThxPA.ttf",
  "italic": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDba2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO-LflOQk6OThxPA.ttf",
  "500italic": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDba2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO-5flOQk6OThxPA.ttf",
  "600italic": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDba2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO9VeVOQk6OThxPA.ttf",
  "700italic": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDba2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO9seVOQk6OThxPA.ttf",
  "800italic": "http://fonts.gstatic.com/s/jetbrainsmono/v13/tDba2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO8LeVOQk6OThxPA.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jim Nightshade",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/jimnightshade/v20/PlIkFlu9Pb08Q8HLM1PxmB0g-OS4V3qKaMxD.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Joan",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/joan/v1/ZXupe1oZsqWRbRdH8X1p_Ng.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jockey One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/jockeyone/v15/HTxpL2g2KjCFj4x8WI6ArIb7HYOk4xc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jolly Lodger",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/jollylodger/v20/BXRsvFTAh_bGkA1uQ48dlB3VWerT3ZyuqA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jomhuria",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/jomhuria/v18/Dxxp8j-TMXf-llKur2b1MOGbC3Dh.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jomolhari",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "tibetan"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/jomolhari/v14/EvONzA1M1Iw_CBd2hsQCF1IZKq5INg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Josefin Sans",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3PZQNVED7rKGKxtqIqX5E-AVSJrOCfjY46_DjRXMFrLgTsQV0.ttf",
  "200": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3PZQNVED7rKGKxtqIqX5E-AVSJrOCfjY46_LjQXMFrLgTsQV0.ttf",
  "300": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3PZQNVED7rKGKxtqIqX5E-AVSJrOCfjY46_GbQXMFrLgTsQV0.ttf",
  "500": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3PZQNVED7rKGKxtqIqX5E-AVSJrOCfjY46_ArQXMFrLgTsQV0.ttf",
  "600": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3PZQNVED7rKGKxtqIqX5E-AVSJrOCfjY46_ObXXMFrLgTsQV0.ttf",
  "700": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3PZQNVED7rKGKxtqIqX5E-AVSJrOCfjY46_N_XXMFrLgTsQV0.ttf",
  "regular": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3PZQNVED7rKGKxtqIqX5E-AVSJrOCfjY46_DjQXMFrLgTsQV0.ttf",
  "100italic": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3JZQNVED7rKGKxtqIqX5EUCGZ2dIn0FyA96fCTtINhKibpUV3MEQ.ttf",
  "200italic": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3JZQNVED7rKGKxtqIqX5EUCGZ2dIn0FyA96fCTNIJhKibpUV3MEQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3JZQNVED7rKGKxtqIqX5EUCGZ2dIn0FyA96fCT6oJhKibpUV3MEQ.ttf",
  "italic": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3JZQNVED7rKGKxtqIqX5EUCGZ2dIn0FyA96fCTtIJhKibpUV3MEQ.ttf",
  "500italic": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3JZQNVED7rKGKxtqIqX5EUCGZ2dIn0FyA96fCThoJhKibpUV3MEQ.ttf",
  "600italic": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3JZQNVED7rKGKxtqIqX5EUCGZ2dIn0FyA96fCTaoVhKibpUV3MEQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/josefinsans/v25/Qw3JZQNVED7rKGKxtqIqX5EUCGZ2dIn0FyA96fCTU4VhKibpUV3MEQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Josefin Slab",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-07-12",
  "files": {
  "100": "http://fonts.gstatic.com/s/josefinslab/v20/lW-swjwOK3Ps5GSJlNNkMalNpiZe_ldbOR4W71mtd3k3K6CcEyI.ttf",
  "200": "http://fonts.gstatic.com/s/josefinslab/v20/lW-swjwOK3Ps5GSJlNNkMalNpiZe_ldbOR4W79msd3k3K6CcEyI.ttf",
  "300": "http://fonts.gstatic.com/s/josefinslab/v20/lW-swjwOK3Ps5GSJlNNkMalNpiZe_ldbOR4W7wesd3k3K6CcEyI.ttf",
  "500": "http://fonts.gstatic.com/s/josefinslab/v20/lW-swjwOK3Ps5GSJlNNkMalNpiZe_ldbOR4W72usd3k3K6CcEyI.ttf",
  "600": "http://fonts.gstatic.com/s/josefinslab/v20/lW-swjwOK3Ps5GSJlNNkMalNpiZe_ldbOR4W74erd3k3K6CcEyI.ttf",
  "700": "http://fonts.gstatic.com/s/josefinslab/v20/lW-swjwOK3Ps5GSJlNNkMalNpiZe_ldbOR4W776rd3k3K6CcEyI.ttf",
  "regular": "http://fonts.gstatic.com/s/josefinslab/v20/lW-swjwOK3Ps5GSJlNNkMalNpiZe_ldbOR4W71msd3k3K6CcEyI.ttf",
  "100italic": "http://fonts.gstatic.com/s/josefinslab/v20/lW-qwjwOK3Ps5GSJlNNkMalnrxShJj4wo7AR-pHvnzs9L4KZAyK43w.ttf",
  "200italic": "http://fonts.gstatic.com/s/josefinslab/v20/lW-qwjwOK3Ps5GSJlNNkMalnrxShJj4wo7AR-pHvHzo9L4KZAyK43w.ttf",
  "300italic": "http://fonts.gstatic.com/s/josefinslab/v20/lW-qwjwOK3Ps5GSJlNNkMalnrxShJj4wo7AR-pHvwTo9L4KZAyK43w.ttf",
  "italic": "http://fonts.gstatic.com/s/josefinslab/v20/lW-qwjwOK3Ps5GSJlNNkMalnrxShJj4wo7AR-pHvnzo9L4KZAyK43w.ttf",
  "500italic": "http://fonts.gstatic.com/s/josefinslab/v20/lW-qwjwOK3Ps5GSJlNNkMalnrxShJj4wo7AR-pHvrTo9L4KZAyK43w.ttf",
  "600italic": "http://fonts.gstatic.com/s/josefinslab/v20/lW-qwjwOK3Ps5GSJlNNkMalnrxShJj4wo7AR-pHvQT09L4KZAyK43w.ttf",
  "700italic": "http://fonts.gstatic.com/s/josefinslab/v20/lW-qwjwOK3Ps5GSJlNNkMalnrxShJj4wo7AR-pHveD09L4KZAyK43w.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jost",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/jost/v14/92zPtBhPNqw79Ij1E865zBUv7myjJAVGPokMmuHL.ttf",
  "200": "http://fonts.gstatic.com/s/jost/v14/92zPtBhPNqw79Ij1E865zBUv7mwjJQVGPokMmuHL.ttf",
  "300": "http://fonts.gstatic.com/s/jost/v14/92zPtBhPNqw79Ij1E865zBUv7mz9JQVGPokMmuHL.ttf",
  "500": "http://fonts.gstatic.com/s/jost/v14/92zPtBhPNqw79Ij1E865zBUv7myRJQVGPokMmuHL.ttf",
  "600": "http://fonts.gstatic.com/s/jost/v14/92zPtBhPNqw79Ij1E865zBUv7mx9IgVGPokMmuHL.ttf",
  "700": "http://fonts.gstatic.com/s/jost/v14/92zPtBhPNqw79Ij1E865zBUv7mxEIgVGPokMmuHL.ttf",
  "800": "http://fonts.gstatic.com/s/jost/v14/92zPtBhPNqw79Ij1E865zBUv7mwjIgVGPokMmuHL.ttf",
  "900": "http://fonts.gstatic.com/s/jost/v14/92zPtBhPNqw79Ij1E865zBUv7mwKIgVGPokMmuHL.ttf",
  "regular": "http://fonts.gstatic.com/s/jost/v14/92zPtBhPNqw79Ij1E865zBUv7myjJQVGPokMmuHL.ttf",
  "100italic": "http://fonts.gstatic.com/s/jost/v14/92zJtBhPNqw73oHH7BbQp4-B6XlrZu0ENI0un_HLMEo.ttf",
  "200italic": "http://fonts.gstatic.com/s/jost/v14/92zJtBhPNqw73oHH7BbQp4-B6XlrZm0FNI0un_HLMEo.ttf",
  "300italic": "http://fonts.gstatic.com/s/jost/v14/92zJtBhPNqw73oHH7BbQp4-B6XlrZrMFNI0un_HLMEo.ttf",
  "italic": "http://fonts.gstatic.com/s/jost/v14/92zJtBhPNqw73oHH7BbQp4-B6XlrZu0FNI0un_HLMEo.ttf",
  "500italic": "http://fonts.gstatic.com/s/jost/v14/92zJtBhPNqw73oHH7BbQp4-B6XlrZt8FNI0un_HLMEo.ttf",
  "600italic": "http://fonts.gstatic.com/s/jost/v14/92zJtBhPNqw73oHH7BbQp4-B6XlrZjMCNI0un_HLMEo.ttf",
  "700italic": "http://fonts.gstatic.com/s/jost/v14/92zJtBhPNqw73oHH7BbQp4-B6XlrZgoCNI0un_HLMEo.ttf",
  "800italic": "http://fonts.gstatic.com/s/jost/v14/92zJtBhPNqw73oHH7BbQp4-B6XlrZm0CNI0un_HLMEo.ttf",
  "900italic": "http://fonts.gstatic.com/s/jost/v14/92zJtBhPNqw73oHH7BbQp4-B6XlrZkQCNI0un_HLMEo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Joti One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/jotione/v21/Z9XVDmdJQAmWm9TwaYTe4u2El6GC.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jua",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/jua/v13/co3KmW9ljjAjc-DZCsKgsg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Judson",
  "variants": [
  "regular",
  "italic",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/judson/v18/FeVSS0Fbvbc14Vxps5xQ3Z5nm29Gww.ttf",
  "regular": "http://fonts.gstatic.com/s/judson/v18/FeVRS0Fbvbc14VxRD7N01bV7kg.ttf",
  "italic": "http://fonts.gstatic.com/s/judson/v18/FeVTS0Fbvbc14VxhDblw97BrknZf.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Julee",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/julee/v22/TuGfUVB3RpZPQ6ZLodgzydtk.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Julius Sans One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/juliussansone/v14/1Pt2g8TAX_SGgBGUi0tGOYEga5W-xXEW6aGXHw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Junge",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/junge/v20/gokgH670Gl1lUqAdvhB7SnKm.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Jura",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "kayah-li",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/jura/v24/z7NOdRfiaC4Vd8hhoPzfb5vBTP0D7auhTfmrH_rt.ttf",
  "500": "http://fonts.gstatic.com/s/jura/v24/z7NOdRfiaC4Vd8hhoPzfb5vBTP1v7auhTfmrH_rt.ttf",
  "600": "http://fonts.gstatic.com/s/jura/v24/z7NOdRfiaC4Vd8hhoPzfb5vBTP2D6quhTfmrH_rt.ttf",
  "700": "http://fonts.gstatic.com/s/jura/v24/z7NOdRfiaC4Vd8hhoPzfb5vBTP266quhTfmrH_rt.ttf",
  "regular": "http://fonts.gstatic.com/s/jura/v24/z7NOdRfiaC4Vd8hhoPzfb5vBTP1d7auhTfmrH_rt.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Just Another Hand",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/justanotherhand/v19/845CNN4-AJyIGvIou-6yJKyptyOpOcr_BmmlS5aw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Just Me Again Down Here",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/justmeagaindownhere/v24/MwQmbgXtz-Wc6RUEGNMc0QpRrfUh2hSdBBMoAuwHvqDwc_fg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "K2D",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/k2d/v9/J7aRnpF2V0ErE6UpvrIw74NL.ttf",
  "200": "http://fonts.gstatic.com/s/k2d/v9/J7aenpF2V0Erv4QJlJw85ppSGw.ttf",
  "300": "http://fonts.gstatic.com/s/k2d/v9/J7aenpF2V0Er24cJlJw85ppSGw.ttf",
  "500": "http://fonts.gstatic.com/s/k2d/v9/J7aenpF2V0Erg4YJlJw85ppSGw.ttf",
  "600": "http://fonts.gstatic.com/s/k2d/v9/J7aenpF2V0Err4EJlJw85ppSGw.ttf",
  "700": "http://fonts.gstatic.com/s/k2d/v9/J7aenpF2V0Ery4AJlJw85ppSGw.ttf",
  "800": "http://fonts.gstatic.com/s/k2d/v9/J7aenpF2V0Er14MJlJw85ppSGw.ttf",
  "100italic": "http://fonts.gstatic.com/s/k2d/v9/J7afnpF2V0EjdZ1NtLYS6pNLAjk.ttf",
  "200italic": "http://fonts.gstatic.com/s/k2d/v9/J7acnpF2V0EjdZ3hlZY4xJ9CGyAa.ttf",
  "300italic": "http://fonts.gstatic.com/s/k2d/v9/J7acnpF2V0EjdZ2FlpY4xJ9CGyAa.ttf",
  "regular": "http://fonts.gstatic.com/s/k2d/v9/J7aTnpF2V0ETd68tnLcg7w.ttf",
  "italic": "http://fonts.gstatic.com/s/k2d/v9/J7aRnpF2V0EjdaUpvrIw74NL.ttf",
  "500italic": "http://fonts.gstatic.com/s/k2d/v9/J7acnpF2V0EjdZ3dl5Y4xJ9CGyAa.ttf",
  "600italic": "http://fonts.gstatic.com/s/k2d/v9/J7acnpF2V0EjdZ3xkJY4xJ9CGyAa.ttf",
  "700italic": "http://fonts.gstatic.com/s/k2d/v9/J7acnpF2V0EjdZ2VkZY4xJ9CGyAa.ttf",
  "800italic": "http://fonts.gstatic.com/s/k2d/v9/J7acnpF2V0EjdZ2JkpY4xJ9CGyAa.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kadwa",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/kadwa/v10/rnCr-x5V0g7ipix7auM-mHnOSOuk.ttf",
  "regular": "http://fonts.gstatic.com/s/kadwa/v10/rnCm-x5V0g7iphTHRcc2s2XH.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kaisei Decol",
  "variants": [
  "regular",
  "500",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v8",
  "lastModified": "2022-09-27",
  "files": {
  "500": "http://fonts.gstatic.com/s/kaiseidecol/v8/bMrvmSqP45sidWf3QmfFW6iKr3gr00i_qb57kA.ttf",
  "700": "http://fonts.gstatic.com/s/kaiseidecol/v8/bMrvmSqP45sidWf3QmfFW6iK534r00i_qb57kA.ttf",
  "regular": "http://fonts.gstatic.com/s/kaiseidecol/v8/bMrwmSqP45sidWf3QmfFW6iyW1EP22OjoA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kaisei HarunoUmi",
  "variants": [
  "regular",
  "500",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v8",
  "lastModified": "2022-09-27",
  "files": {
  "500": "http://fonts.gstatic.com/s/kaiseiharunoumi/v8/HI_WiZQSLqBQoAHhK_C6N_nzy_jcIj_QlMcFwmC9FAU.ttf",
  "700": "http://fonts.gstatic.com/s/kaiseiharunoumi/v8/HI_WiZQSLqBQoAHhK_C6N_nzy_jcInfWlMcFwmC9FAU.ttf",
  "regular": "http://fonts.gstatic.com/s/kaiseiharunoumi/v8/HI_RiZQSLqBQoAHhK_C6N_nzy_jcGsv5sM8u3mk.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kaisei Opti",
  "variants": [
  "regular",
  "500",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v8",
  "lastModified": "2022-09-27",
  "files": {
  "500": "http://fonts.gstatic.com/s/kaiseiopti/v8/QldXNThJphYb8_g6c2nlIGGqxY1u7f34DYwn.ttf",
  "700": "http://fonts.gstatic.com/s/kaiseiopti/v8/QldXNThJphYb8_g6c2nlIGHiw41u7f34DYwn.ttf",
  "regular": "http://fonts.gstatic.com/s/kaiseiopti/v8/QldKNThJphYb8_g6c2nlIFle7KlmxuHx.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kaisei Tokumin",
  "variants": [
  "regular",
  "500",
  "700",
  "800"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v8",
  "lastModified": "2022-09-27",
  "files": {
  "500": "http://fonts.gstatic.com/s/kaiseitokumin/v8/Gg8vN5wdZg7xCwuMsylww2ZiQnqr_3khpMIzeI6v.ttf",
  "700": "http://fonts.gstatic.com/s/kaiseitokumin/v8/Gg8vN5wdZg7xCwuMsylww2ZiQnrj-XkhpMIzeI6v.ttf",
  "800": "http://fonts.gstatic.com/s/kaiseitokumin/v8/Gg8vN5wdZg7xCwuMsylww2ZiQnr_-nkhpMIzeI6v.ttf",
  "regular": "http://fonts.gstatic.com/s/kaiseitokumin/v8/Gg8sN5wdZg7xCwuMsylww2ZiQkJf1l0pj946.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kalam",
  "variants": [
  "300",
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/kalam/v16/YA9Qr0Wd4kDdMtD6GgLLmCUItqGt.ttf",
  "700": "http://fonts.gstatic.com/s/kalam/v16/YA9Qr0Wd4kDdMtDqHQLLmCUItqGt.ttf",
  "regular": "http://fonts.gstatic.com/s/kalam/v16/YA9dr0Wd4kDdMuhWMibDszkB.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kameron",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/kameron/v15/vm8zdR7vXErQxuzniAIfC-3jfHb--NY.ttf",
  "regular": "http://fonts.gstatic.com/s/kameron/v15/vm82dR7vXErQxuznsL4wL-XIYH8.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kanit",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/kanit/v12/nKKX-Go6G5tXcr72GwWKcaxALFs.ttf",
  "200": "http://fonts.gstatic.com/s/kanit/v12/nKKU-Go6G5tXcr5aOiWgX6BJNUJy.ttf",
  "300": "http://fonts.gstatic.com/s/kanit/v12/nKKU-Go6G5tXcr4-OSWgX6BJNUJy.ttf",
  "500": "http://fonts.gstatic.com/s/kanit/v12/nKKU-Go6G5tXcr5mOCWgX6BJNUJy.ttf",
  "600": "http://fonts.gstatic.com/s/kanit/v12/nKKU-Go6G5tXcr5KPyWgX6BJNUJy.ttf",
  "700": "http://fonts.gstatic.com/s/kanit/v12/nKKU-Go6G5tXcr4uPiWgX6BJNUJy.ttf",
  "800": "http://fonts.gstatic.com/s/kanit/v12/nKKU-Go6G5tXcr4yPSWgX6BJNUJy.ttf",
  "900": "http://fonts.gstatic.com/s/kanit/v12/nKKU-Go6G5tXcr4WPCWgX6BJNUJy.ttf",
  "100italic": "http://fonts.gstatic.com/s/kanit/v12/nKKV-Go6G5tXcraQI2GAdY5FPFtrGw.ttf",
  "200italic": "http://fonts.gstatic.com/s/kanit/v12/nKKS-Go6G5tXcraQI82hVaRrMFJyAu4.ttf",
  "300italic": "http://fonts.gstatic.com/s/kanit/v12/nKKS-Go6G5tXcraQI6miVaRrMFJyAu4.ttf",
  "regular": "http://fonts.gstatic.com/s/kanit/v12/nKKZ-Go6G5tXcoaSEQGodLxA.ttf",
  "italic": "http://fonts.gstatic.com/s/kanit/v12/nKKX-Go6G5tXcraQGwWKcaxALFs.ttf",
  "500italic": "http://fonts.gstatic.com/s/kanit/v12/nKKS-Go6G5tXcraQI_GjVaRrMFJyAu4.ttf",
  "600italic": "http://fonts.gstatic.com/s/kanit/v12/nKKS-Go6G5tXcraQI92kVaRrMFJyAu4.ttf",
  "700italic": "http://fonts.gstatic.com/s/kanit/v12/nKKS-Go6G5tXcraQI7mlVaRrMFJyAu4.ttf",
  "800italic": "http://fonts.gstatic.com/s/kanit/v12/nKKS-Go6G5tXcraQI6WmVaRrMFJyAu4.ttf",
  "900italic": "http://fonts.gstatic.com/s/kanit/v12/nKKS-Go6G5tXcraQI4GnVaRrMFJyAu4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kantumruy",
  "variants": [
  "300",
  "regular",
  "700"
  ],
  "subsets": [
  "khmer"
  ],
  "version": "v21",
  "lastModified": "2022-04-26",
  "files": {
  "300": "http://fonts.gstatic.com/s/kantumruy/v21/syk0-yJ0m7wyVb-f4FOPUtDlpn-UJ1H6Uw.ttf",
  "700": "http://fonts.gstatic.com/s/kantumruy/v21/syk0-yJ0m7wyVb-f4FOPQtflpn-UJ1H6Uw.ttf",
  "regular": "http://fonts.gstatic.com/s/kantumruy/v21/sykx-yJ0m7wyVb-f4FO3_vjBrlSILg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kantumruy Pro",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "khmer",
  "latin",
  "latin-ext"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2TY5aECkp34vEBSPFOmJxwvk_pilU8OGNfyg1urUs0M34dR6dW.ttf",
  "200": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2TY5aECkp34vEBSPFOmJxwvk_pilU8OGNfyg3urEs0M34dR6dW.ttf",
  "300": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2TY5aECkp34vEBSPFOmJxwvk_pilU8OGNfyg0wrEs0M34dR6dW.ttf",
  "500": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2TY5aECkp34vEBSPFOmJxwvk_pilU8OGNfyg1crEs0M34dR6dW.ttf",
  "600": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2TY5aECkp34vEBSPFOmJxwvk_pilU8OGNfyg2wq0s0M34dR6dW.ttf",
  "700": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2TY5aECkp34vEBSPFOmJxwvk_pilU8OGNfyg2Jq0s0M34dR6dW.ttf",
  "regular": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2TY5aECkp34vEBSPFOmJxwvk_pilU8OGNfyg1urEs0M34dR6dW.ttf",
  "100italic": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2RY5aECkp34vEBSPFOmJxwlEbbdY1VU_nxzRim76N2OXo_QrdWlcU.ttf",
  "200italic": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2RY5aECkp34vEBSPFOmJxwlEbbdY1VU_nxzRim7yN3OXo_QrdWlcU.ttf",
  "300italic": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2RY5aECkp34vEBSPFOmJxwlEbbdY1VU_nxzRim7_13OXo_QrdWlcU.ttf",
  "italic": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2RY5aECkp34vEBSPFOmJxwlEbbdY1VU_nxzRim76N3OXo_QrdWlcU.ttf",
  "500italic": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2RY5aECkp34vEBSPFOmJxwlEbbdY1VU_nxzRim75F3OXo_QrdWlcU.ttf",
  "600italic": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2RY5aECkp34vEBSPFOmJxwlEbbdY1VU_nxzRim731wOXo_QrdWlcU.ttf",
  "700italic": "http://fonts.gstatic.com/s/kantumruypro/v3/1q2RY5aECkp34vEBSPFOmJxwlEbbdY1VU_nxzRim70RwOXo_QrdWlcU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Karantina",
  "variants": [
  "300",
  "regular",
  "700"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/karantina/v11/buExpo24ccnh31GVMABxXCgf-P5Oaiw4cw.ttf",
  "700": "http://fonts.gstatic.com/s/karantina/v11/buExpo24ccnh31GVMABxTC8f-P5Oaiw4cw.ttf",
  "regular": "http://fonts.gstatic.com/s/karantina/v11/buE0po24ccnh31GVMABJ8AA78NVSYw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Karla",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/karla/v23/qkBIXvYC6trAT55ZBi1ueQVIjQTDeJqqFENLR7fHGw.ttf",
  "300": "http://fonts.gstatic.com/s/karla/v23/qkBIXvYC6trAT55ZBi1ueQVIjQTDppqqFENLR7fHGw.ttf",
  "500": "http://fonts.gstatic.com/s/karla/v23/qkBIXvYC6trAT55ZBi1ueQVIjQTDypqqFENLR7fHGw.ttf",
  "600": "http://fonts.gstatic.com/s/karla/v23/qkBIXvYC6trAT55ZBi1ueQVIjQTDJp2qFENLR7fHGw.ttf",
  "700": "http://fonts.gstatic.com/s/karla/v23/qkBIXvYC6trAT55ZBi1ueQVIjQTDH52qFENLR7fHGw.ttf",
  "800": "http://fonts.gstatic.com/s/karla/v23/qkBIXvYC6trAT55ZBi1ueQVIjQTDeJ2qFENLR7fHGw.ttf",
  "regular": "http://fonts.gstatic.com/s/karla/v23/qkBIXvYC6trAT55ZBi1ueQVIjQTD-JqqFENLR7fHGw.ttf",
  "200italic": "http://fonts.gstatic.com/s/karla/v23/qkBKXvYC6trAT7RQNNK2EG7SIwPWMNnCV0lPZbLXGxGR.ttf",
  "300italic": "http://fonts.gstatic.com/s/karla/v23/qkBKXvYC6trAT7RQNNK2EG7SIwPWMNkcV0lPZbLXGxGR.ttf",
  "italic": "http://fonts.gstatic.com/s/karla/v23/qkBKXvYC6trAT7RQNNK2EG7SIwPWMNlCV0lPZbLXGxGR.ttf",
  "500italic": "http://fonts.gstatic.com/s/karla/v23/qkBKXvYC6trAT7RQNNK2EG7SIwPWMNlwV0lPZbLXGxGR.ttf",
  "600italic": "http://fonts.gstatic.com/s/karla/v23/qkBKXvYC6trAT7RQNNK2EG7SIwPWMNmcUElPZbLXGxGR.ttf",
  "700italic": "http://fonts.gstatic.com/s/karla/v23/qkBKXvYC6trAT7RQNNK2EG7SIwPWMNmlUElPZbLXGxGR.ttf",
  "800italic": "http://fonts.gstatic.com/s/karla/v23/qkBKXvYC6trAT7RQNNK2EG7SIwPWMNnCUElPZbLXGxGR.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Karma",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/karma/v16/va9F4kzAzMZRGLjDY8Z_uqzGQC_-.ttf",
  "500": "http://fonts.gstatic.com/s/karma/v16/va9F4kzAzMZRGLibYsZ_uqzGQC_-.ttf",
  "600": "http://fonts.gstatic.com/s/karma/v16/va9F4kzAzMZRGLi3ZcZ_uqzGQC_-.ttf",
  "700": "http://fonts.gstatic.com/s/karma/v16/va9F4kzAzMZRGLjTZMZ_uqzGQC_-.ttf",
  "regular": "http://fonts.gstatic.com/s/karma/v16/va9I4kzAzMZRGIBvS-J3kbDP.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Katibeh",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/katibeh/v17/ZGjXol5MQJog4bxDaC1RVDNdGDs.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kaushan Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kaushanscript/v14/vm8vdRfvXFLG3OLnsO15WYS5DF7_ytN3M48a.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kavivanar",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kavivanar/v18/o-0IIpQgyXYSwhxP7_Jb4j5Ba_2c7A.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kavoon",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kavoon/v21/pxiFyp4_scRYhlU4NLr6f1pdEQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kdam Thmor Pro",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kdamthmorpro/v1/EJRPQgAzVdcI-Qdvt34jzurnGA7_j89I8ZWb.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Keania One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/keaniaone/v20/zOL54pXJk65E8pXardnuycRuv-hHkOs.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kelly Slab",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kellyslab/v15/-W_7XJX0Rz3cxUnJC5t6TkMBf50kbiM.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kenia",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kenia/v24/jizURE5PuHQH9qCONUGswfGM.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Khand",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/khand/v14/TwMN-IINQlQQ0bL5cFE3ZwaH__-C.ttf",
  "500": "http://fonts.gstatic.com/s/khand/v14/TwMN-IINQlQQ0bKhcVE3ZwaH__-C.ttf",
  "600": "http://fonts.gstatic.com/s/khand/v14/TwMN-IINQlQQ0bKNdlE3ZwaH__-C.ttf",
  "700": "http://fonts.gstatic.com/s/khand/v14/TwMN-IINQlQQ0bLpd1E3ZwaH__-C.ttf",
  "regular": "http://fonts.gstatic.com/s/khand/v14/TwMA-IINQlQQ0YpVWHU_TBqO.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Khmer",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer"
  ],
  "version": "v25",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/khmer/v25/MjQImit_vPPwpF-BpN2EeYmD.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Khula",
  "variants": [
  "300",
  "regular",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/khula/v12/OpNPnoEOns3V7G-ljCvUrC59XwXD.ttf",
  "600": "http://fonts.gstatic.com/s/khula/v12/OpNPnoEOns3V7G_RiivUrC59XwXD.ttf",
  "700": "http://fonts.gstatic.com/s/khula/v12/OpNPnoEOns3V7G-1iyvUrC59XwXD.ttf",
  "800": "http://fonts.gstatic.com/s/khula/v12/OpNPnoEOns3V7G-piCvUrC59XwXD.ttf",
  "regular": "http://fonts.gstatic.com/s/khula/v12/OpNCnoEOns3V7FcJpA_chzJ0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kings",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kings/v5/8AtnGsK4O5CYXU_Iq6GSPaHS.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kirang Haerang",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kiranghaerang/v20/E21-_dn_gvvIjhYON1lpIU4-bcqvWPaJq4no.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kite One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kiteone/v20/70lQu7shLnA_E02vyq1b6HnGO4uA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kiwi Maru",
  "variants": [
  "300",
  "regular",
  "500"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-27",
  "files": {
  "300": "http://fonts.gstatic.com/s/kiwimaru/v14/R70djykGkuuDep-hRg6gNCi0Vxn9R5ShnA.ttf",
  "500": "http://fonts.gstatic.com/s/kiwimaru/v14/R70djykGkuuDep-hRg6gbCm0Vxn9R5ShnA.ttf",
  "regular": "http://fonts.gstatic.com/s/kiwimaru/v14/R70YjykGkuuDep-hRg6YmACQXzLhTg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Klee One",
  "variants": [
  "regular",
  "600"
  ],
  "subsets": [
  "cyrillic",
  "greek-ext",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-27",
  "files": {
  "600": "http://fonts.gstatic.com/s/kleeone/v7/LDI2apCLNRc6A8oT4pbYF8Osc-bGkqIw.ttf",
  "regular": "http://fonts.gstatic.com/s/kleeone/v7/LDIxapCLNRc6A8oT4q4AOeekWPrP.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Knewave",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/knewave/v14/sykz-yx0lLcxQaSItSq9-trEvlQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "KoHo",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/koho/v16/K2FxfZ5fmddNPuE1WJ75JoKhHys.ttf",
  "300": "http://fonts.gstatic.com/s/koho/v16/K2FxfZ5fmddNPoU2WJ75JoKhHys.ttf",
  "500": "http://fonts.gstatic.com/s/koho/v16/K2FxfZ5fmddNPt03WJ75JoKhHys.ttf",
  "600": "http://fonts.gstatic.com/s/koho/v16/K2FxfZ5fmddNPvEwWJ75JoKhHys.ttf",
  "700": "http://fonts.gstatic.com/s/koho/v16/K2FxfZ5fmddNPpUxWJ75JoKhHys.ttf",
  "200italic": "http://fonts.gstatic.com/s/koho/v16/K2FzfZ5fmddNNisssJ_zIqCkDyvqZA.ttf",
  "300italic": "http://fonts.gstatic.com/s/koho/v16/K2FzfZ5fmddNNiss1JzzIqCkDyvqZA.ttf",
  "regular": "http://fonts.gstatic.com/s/koho/v16/K2F-fZ5fmddNBikefJbSOos.ttf",
  "italic": "http://fonts.gstatic.com/s/koho/v16/K2FwfZ5fmddNNisUeLTXKou4Bg.ttf",
  "500italic": "http://fonts.gstatic.com/s/koho/v16/K2FzfZ5fmddNNissjJ3zIqCkDyvqZA.ttf",
  "600italic": "http://fonts.gstatic.com/s/koho/v16/K2FzfZ5fmddNNissoJrzIqCkDyvqZA.ttf",
  "700italic": "http://fonts.gstatic.com/s/koho/v16/K2FzfZ5fmddNNissxJvzIqCkDyvqZA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kodchasan",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/kodchasan/v16/1cX0aUPOAJv9sG4I-DJeR1Cggeqo3eMeoA.ttf",
  "300": "http://fonts.gstatic.com/s/kodchasan/v16/1cX0aUPOAJv9sG4I-DJeI1Oggeqo3eMeoA.ttf",
  "500": "http://fonts.gstatic.com/s/kodchasan/v16/1cX0aUPOAJv9sG4I-DJee1Kggeqo3eMeoA.ttf",
  "600": "http://fonts.gstatic.com/s/kodchasan/v16/1cX0aUPOAJv9sG4I-DJeV1Wggeqo3eMeoA.ttf",
  "700": "http://fonts.gstatic.com/s/kodchasan/v16/1cX0aUPOAJv9sG4I-DJeM1Sggeqo3eMeoA.ttf",
  "200italic": "http://fonts.gstatic.com/s/kodchasan/v16/1cXqaUPOAJv9sG4I-DJWjUlIgOCs_-YOoIgN.ttf",
  "300italic": "http://fonts.gstatic.com/s/kodchasan/v16/1cXqaUPOAJv9sG4I-DJWjUksg-Cs_-YOoIgN.ttf",
  "regular": "http://fonts.gstatic.com/s/kodchasan/v16/1cXxaUPOAJv9sG4I-DJmj3uEicG01A.ttf",
  "italic": "http://fonts.gstatic.com/s/kodchasan/v16/1cX3aUPOAJv9sG4I-DJWjXGAq8Sk1PoH.ttf",
  "500italic": "http://fonts.gstatic.com/s/kodchasan/v16/1cXqaUPOAJv9sG4I-DJWjUl0guCs_-YOoIgN.ttf",
  "600italic": "http://fonts.gstatic.com/s/kodchasan/v16/1cXqaUPOAJv9sG4I-DJWjUlYheCs_-YOoIgN.ttf",
  "700italic": "http://fonts.gstatic.com/s/kodchasan/v16/1cXqaUPOAJv9sG4I-DJWjUk8hOCs_-YOoIgN.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Koh Santepheap",
  "variants": [
  "100",
  "300",
  "regular",
  "700",
  "900"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v9",
  "lastModified": "2022-04-26",
  "files": {
  "100": "http://fonts.gstatic.com/s/kohsantepheap/v9/gNMfW3p6SJbwyGj2rBZyeOrTjNuFHVyTtjNJUWU.ttf",
  "300": "http://fonts.gstatic.com/s/kohsantepheap/v9/gNMeW3p6SJbwyGj2rBZyeOrTjNtNP3y5mD9ASHz5.ttf",
  "700": "http://fonts.gstatic.com/s/kohsantepheap/v9/gNMeW3p6SJbwyGj2rBZyeOrTjNtdOHy5mD9ASHz5.ttf",
  "900": "http://fonts.gstatic.com/s/kohsantepheap/v9/gNMeW3p6SJbwyGj2rBZyeOrTjNtlOny5mD9ASHz5.ttf",
  "regular": "http://fonts.gstatic.com/s/kohsantepheap/v9/gNMdW3p6SJbwyGj2rBZyeOrTjOPhF1ixsyNJ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kolker Brush",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kolkerbrush/v3/iJWDBXWRZjfKWdvmzwvvog3-7KJ6x8qNUQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kosugi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kosugi/v14/pxiFyp4_v8FCjlI4NLr6f1pdEQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kosugi Maru",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kosugimaru/v14/0nksC9PgP_wGh21A2KeqGiTqivr9iBq_.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kotta One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kottaone/v20/S6u_w41LXzPc_jlfNWqPHA3s5dwt7w.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Koulen",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/koulen/v25/AMOQz46as3KIBPeWgnA9kuYMUg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kranky",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kranky/v24/hESw6XVgJzlPsFnMpheEZo_H_w.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kreon",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v32",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/kreon/v32/t5t9IRIUKY-TFF_LW5lnMR3v2DnvPNimejUfp2dWNg.ttf",
  "500": "http://fonts.gstatic.com/s/kreon/v32/t5t9IRIUKY-TFF_LW5lnMR3v2DnvUNimejUfp2dWNg.ttf",
  "600": "http://fonts.gstatic.com/s/kreon/v32/t5t9IRIUKY-TFF_LW5lnMR3v2DnvvN-mejUfp2dWNg.ttf",
  "700": "http://fonts.gstatic.com/s/kreon/v32/t5t9IRIUKY-TFF_LW5lnMR3v2Dnvhd-mejUfp2dWNg.ttf",
  "regular": "http://fonts.gstatic.com/s/kreon/v32/t5t9IRIUKY-TFF_LW5lnMR3v2DnvYtimejUfp2dWNg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kristi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kristi/v17/uK_y4ricdeU6zwdRCh0TMv6EXw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Krona One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kronaone/v14/jAnEgHdjHcjgfIb1ZcUCMY-h3cWkWg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Krub",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/krub/v9/sZlEdRyC6CRYZo47KLF4R6gWaf8.ttf",
  "300": "http://fonts.gstatic.com/s/krub/v9/sZlEdRyC6CRYZuo4KLF4R6gWaf8.ttf",
  "500": "http://fonts.gstatic.com/s/krub/v9/sZlEdRyC6CRYZrI5KLF4R6gWaf8.ttf",
  "600": "http://fonts.gstatic.com/s/krub/v9/sZlEdRyC6CRYZp4-KLF4R6gWaf8.ttf",
  "700": "http://fonts.gstatic.com/s/krub/v9/sZlEdRyC6CRYZvo_KLF4R6gWaf8.ttf",
  "200italic": "http://fonts.gstatic.com/s/krub/v9/sZlGdRyC6CRYbkQiwLByQ4oTef_6gQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/krub/v9/sZlGdRyC6CRYbkQipLNyQ4oTef_6gQ.ttf",
  "regular": "http://fonts.gstatic.com/s/krub/v9/sZlLdRyC6CRYXkYQDLlTW6E.ttf",
  "italic": "http://fonts.gstatic.com/s/krub/v9/sZlFdRyC6CRYbkQaCJtWS6EPcA.ttf",
  "500italic": "http://fonts.gstatic.com/s/krub/v9/sZlGdRyC6CRYbkQi_LJyQ4oTef_6gQ.ttf",
  "600italic": "http://fonts.gstatic.com/s/krub/v9/sZlGdRyC6CRYbkQi0LVyQ4oTef_6gQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/krub/v9/sZlGdRyC6CRYbkQitLRyQ4oTef_6gQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kufam",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/kufam/v20/C8c-4cY7pG7w_oSJDszBXsKCcBH3pKk7qQCJHvIwYg.ttf",
  "600": "http://fonts.gstatic.com/s/kufam/v20/C8c-4cY7pG7w_oSJDszBXsKCcBH3SK47qQCJHvIwYg.ttf",
  "700": "http://fonts.gstatic.com/s/kufam/v20/C8c-4cY7pG7w_oSJDszBXsKCcBH3ca47qQCJHvIwYg.ttf",
  "800": "http://fonts.gstatic.com/s/kufam/v20/C8c-4cY7pG7w_oSJDszBXsKCcBH3Fq47qQCJHvIwYg.ttf",
  "900": "http://fonts.gstatic.com/s/kufam/v20/C8c-4cY7pG7w_oSJDszBXsKCcBH3P647qQCJHvIwYg.ttf",
  "regular": "http://fonts.gstatic.com/s/kufam/v20/C8c-4cY7pG7w_oSJDszBXsKCcBH3lqk7qQCJHvIwYg.ttf",
  "italic": "http://fonts.gstatic.com/s/kufam/v20/C8c84cY7pG7w_q6APDMZN6kY3hbiXurT6gqNPPcgYp0i.ttf",
  "500italic": "http://fonts.gstatic.com/s/kufam/v20/C8c84cY7pG7w_q6APDMZN6kY3hbiXurh6gqNPPcgYp0i.ttf",
  "600italic": "http://fonts.gstatic.com/s/kufam/v20/C8c84cY7pG7w_q6APDMZN6kY3hbiXuoN7QqNPPcgYp0i.ttf",
  "700italic": "http://fonts.gstatic.com/s/kufam/v20/C8c84cY7pG7w_q6APDMZN6kY3hbiXuo07QqNPPcgYp0i.ttf",
  "800italic": "http://fonts.gstatic.com/s/kufam/v20/C8c84cY7pG7w_q6APDMZN6kY3hbiXupT7QqNPPcgYp0i.ttf",
  "900italic": "http://fonts.gstatic.com/s/kufam/v20/C8c84cY7pG7w_q6APDMZN6kY3hbiXup67QqNPPcgYp0i.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kulim Park",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/kulimpark/v14/fdN49secq3hflz1Uu3IwjJYNwa5aZbUvGjU.ttf",
  "300": "http://fonts.gstatic.com/s/kulimpark/v14/fdN49secq3hflz1Uu3IwjPIOwa5aZbUvGjU.ttf",
  "600": "http://fonts.gstatic.com/s/kulimpark/v14/fdN49secq3hflz1Uu3IwjIYIwa5aZbUvGjU.ttf",
  "700": "http://fonts.gstatic.com/s/kulimpark/v14/fdN49secq3hflz1Uu3IwjOIJwa5aZbUvGjU.ttf",
  "200italic": "http://fonts.gstatic.com/s/kulimpark/v14/fdNm9secq3hflz1Uu3IwhFwUKa9QYZcqCjVVUA.ttf",
  "300italic": "http://fonts.gstatic.com/s/kulimpark/v14/fdNm9secq3hflz1Uu3IwhFwUTaxQYZcqCjVVUA.ttf",
  "regular": "http://fonts.gstatic.com/s/kulimpark/v14/fdN79secq3hflz1Uu3IwtF4m5aZxebw.ttf",
  "italic": "http://fonts.gstatic.com/s/kulimpark/v14/fdN59secq3hflz1Uu3IwhFws4YR0abw2Aw.ttf",
  "600italic": "http://fonts.gstatic.com/s/kulimpark/v14/fdNm9secq3hflz1Uu3IwhFwUOapQYZcqCjVVUA.ttf",
  "700italic": "http://fonts.gstatic.com/s/kulimpark/v14/fdNm9secq3hflz1Uu3IwhFwUXatQYZcqCjVVUA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kumar One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kumarone/v17/bMr1mS-P958wYi6YaGeGNO6WU3oT0g.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kumar One Outline",
  "variants": [
  "regular"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kumaroneoutline/v17/Noao6VH62pyLP0fsrZ-v18wlUEcX9zDwRQu8EGKF.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kumbh Sans",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/kumbhsans/v12/c4mw1n92AsfhuCq6tVsaoIx1CHIi4kToNorqSyNIXIwSP0XD.ttf",
  "200": "http://fonts.gstatic.com/s/kumbhsans/v12/c4mw1n92AsfhuCq6tVsaoIx1CHIi4kToNopqSiNIXIwSP0XD.ttf",
  "300": "http://fonts.gstatic.com/s/kumbhsans/v12/c4mw1n92AsfhuCq6tVsaoIx1CHIi4kToNoq0SiNIXIwSP0XD.ttf",
  "500": "http://fonts.gstatic.com/s/kumbhsans/v12/c4mw1n92AsfhuCq6tVsaoIx1CHIi4kToNorYSiNIXIwSP0XD.ttf",
  "600": "http://fonts.gstatic.com/s/kumbhsans/v12/c4mw1n92AsfhuCq6tVsaoIx1CHIi4kToNoo0TSNIXIwSP0XD.ttf",
  "700": "http://fonts.gstatic.com/s/kumbhsans/v12/c4mw1n92AsfhuCq6tVsaoIx1CHIi4kToNooNTSNIXIwSP0XD.ttf",
  "800": "http://fonts.gstatic.com/s/kumbhsans/v12/c4mw1n92AsfhuCq6tVsaoIx1CHIi4kToNopqTSNIXIwSP0XD.ttf",
  "900": "http://fonts.gstatic.com/s/kumbhsans/v12/c4mw1n92AsfhuCq6tVsaoIx1CHIi4kToNopDTSNIXIwSP0XD.ttf",
  "regular": "http://fonts.gstatic.com/s/kumbhsans/v12/c4mw1n92AsfhuCq6tVsaoIx1CHIi4kToNorqSiNIXIwSP0XD.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Kurale",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/kurale/v11/4iCs6KV9e9dXjho6eAT3v02QFg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "La Belle Aurore",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/labelleaurore/v16/RrQIbot8-mNYKnGNDkWlocovHeIIG-eFNVmULg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lacquer",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lacquer/v15/EYqzma1QwqpG4_BBB7-AXhttQ5I.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Laila",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/laila/v13/LYjBdG_8nE8jDLzxogNAh14nVcfe.ttf",
  "500": "http://fonts.gstatic.com/s/laila/v13/LYjBdG_8nE8jDLypowNAh14nVcfe.ttf",
  "600": "http://fonts.gstatic.com/s/laila/v13/LYjBdG_8nE8jDLyFpANAh14nVcfe.ttf",
  "700": "http://fonts.gstatic.com/s/laila/v13/LYjBdG_8nE8jDLzhpQNAh14nVcfe.ttf",
  "regular": "http://fonts.gstatic.com/s/laila/v13/LYjMdG_8nE8jDIRdiidIrEIu.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lakki Reddy",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lakkireddy/v19/S6u5w49MUSzD9jlCPmvLZQfox9k97-xZ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lalezar",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lalezar/v14/zrfl0HLVx-HwTP82UaDyIiL0RCg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lancelot",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lancelot/v22/J7acnppxBGtQEulG4JY4xJ9CGyAa.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Langar",
  "variants": [
  "regular"
  ],
  "subsets": [
  "gurmukhi",
  "latin",
  "latin-ext"
  ],
  "version": "v26",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/langar/v26/kJEyBukW7AIlgjGVrTVZ99sqrQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lateef",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/lateef/v24/hESz6XVnNCxEvkb0bjygbqTb9nQ-RA.ttf",
  "300": "http://fonts.gstatic.com/s/lateef/v24/hESz6XVnNCxEvkb0Cj-gbqTb9nQ-RA.ttf",
  "500": "http://fonts.gstatic.com/s/lateef/v24/hESz6XVnNCxEvkb0Uj6gbqTb9nQ-RA.ttf",
  "600": "http://fonts.gstatic.com/s/lateef/v24/hESz6XVnNCxEvkb0fjmgbqTb9nQ-RA.ttf",
  "700": "http://fonts.gstatic.com/s/lateef/v24/hESz6XVnNCxEvkb0GjigbqTb9nQ-RA.ttf",
  "800": "http://fonts.gstatic.com/s/lateef/v24/hESz6XVnNCxEvkb0BjugbqTb9nQ-RA.ttf",
  "regular": "http://fonts.gstatic.com/s/lateef/v24/hESw6XVnNCxEvkbMpheEZo_H_w.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lato",
  "variants": [
  "100",
  "100italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/lato/v23/S6u8w4BMUTPHh30wWyWrFCbw7A.ttf",
  "300": "http://fonts.gstatic.com/s/lato/v23/S6u9w4BMUTPHh7USew-FGC_p9dw.ttf",
  "700": "http://fonts.gstatic.com/s/lato/v23/S6u9w4BMUTPHh6UVew-FGC_p9dw.ttf",
  "900": "http://fonts.gstatic.com/s/lato/v23/S6u9w4BMUTPHh50Xew-FGC_p9dw.ttf",
  "100italic": "http://fonts.gstatic.com/s/lato/v23/S6u-w4BMUTPHjxsIPy-vNiPg7MU0.ttf",
  "300italic": "http://fonts.gstatic.com/s/lato/v23/S6u_w4BMUTPHjxsI9w2PHA3s5dwt7w.ttf",
  "regular": "http://fonts.gstatic.com/s/lato/v23/S6uyw4BMUTPHvxk6XweuBCY.ttf",
  "italic": "http://fonts.gstatic.com/s/lato/v23/S6u8w4BMUTPHjxswWyWrFCbw7A.ttf",
  "700italic": "http://fonts.gstatic.com/s/lato/v23/S6u_w4BMUTPHjxsI5wqPHA3s5dwt7w.ttf",
  "900italic": "http://fonts.gstatic.com/s/lato/v23/S6u_w4BMUTPHjxsI3wiPHA3s5dwt7w.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lavishly Yours",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lavishlyyours/v2/jizDREVIvGwH5OjiZmX9r5z_WxUY0TY7ikbI.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "League Gothic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v6",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/leaguegothic/v6/qFdR35CBi4tvBz81xy7WG7ep-BQAY7Krj7feObpH_-amidQ6Q9hn.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "League Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/leaguescript/v24/CSR54zpSlumSWj9CGVsoBZdeaNNUuOwkC2s.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "League Spartan",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v6",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/leaguespartan/v6/kJEnBuEW6A0lliaV_m88ja5Twtx8BWhtkDVmjZvM_oXpBMdcFguczA.ttf",
  "200": "http://fonts.gstatic.com/s/leaguespartan/v6/kJEnBuEW6A0lliaV_m88ja5Twtx8BWhtkDVmjZvMfoTpBMdcFguczA.ttf",
  "300": "http://fonts.gstatic.com/s/leaguespartan/v6/kJEnBuEW6A0lliaV_m88ja5Twtx8BWhtkDVmjZvMoITpBMdcFguczA.ttf",
  "500": "http://fonts.gstatic.com/s/leaguespartan/v6/kJEnBuEW6A0lliaV_m88ja5Twtx8BWhtkDVmjZvMzITpBMdcFguczA.ttf",
  "600": "http://fonts.gstatic.com/s/leaguespartan/v6/kJEnBuEW6A0lliaV_m88ja5Twtx8BWhtkDVmjZvMIIPpBMdcFguczA.ttf",
  "700": "http://fonts.gstatic.com/s/leaguespartan/v6/kJEnBuEW6A0lliaV_m88ja5Twtx8BWhtkDVmjZvMGYPpBMdcFguczA.ttf",
  "800": "http://fonts.gstatic.com/s/leaguespartan/v6/kJEnBuEW6A0lliaV_m88ja5Twtx8BWhtkDVmjZvMfoPpBMdcFguczA.ttf",
  "900": "http://fonts.gstatic.com/s/leaguespartan/v6/kJEnBuEW6A0lliaV_m88ja5Twtx8BWhtkDVmjZvMV4PpBMdcFguczA.ttf",
  "regular": "http://fonts.gstatic.com/s/leaguespartan/v6/kJEnBuEW6A0lliaV_m88ja5Twtx8BWhtkDVmjZvM_oTpBMdcFguczA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Leckerli One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/leckerlione/v16/V8mCoQH8VCsNttEnxnGQ-1itLZxcBtItFw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ledger",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ledger/v16/j8_q6-HK1L3if_sxm8DwHTBhHw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lekton",
  "variants": [
  "regular",
  "italic",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/lekton/v17/SZc73FDmLaWmWpBm4zjMlWjX4DJXgQ.ttf",
  "regular": "http://fonts.gstatic.com/s/lekton/v17/SZc43FDmLaWmWpBeXxfonUPL6Q.ttf",
  "italic": "http://fonts.gstatic.com/s/lekton/v17/SZc63FDmLaWmWpBuXR3sv0bb6StO.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lemon",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lemon/v14/HI_EiYEVKqRMq0jBSZXAQ4-d.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lemonada",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/lemonada/v20/0QI-MXFD9oygTWy_R-FFlwV-bgfR7QJGJOt2mfWc3Z2pTg.ttf",
  "500": "http://fonts.gstatic.com/s/lemonada/v20/0QI-MXFD9oygTWy_R-FFlwV-bgfR7QJGSOt2mfWc3Z2pTg.ttf",
  "600": "http://fonts.gstatic.com/s/lemonada/v20/0QI-MXFD9oygTWy_R-FFlwV-bgfR7QJGpOx2mfWc3Z2pTg.ttf",
  "700": "http://fonts.gstatic.com/s/lemonada/v20/0QI-MXFD9oygTWy_R-FFlwV-bgfR7QJGnex2mfWc3Z2pTg.ttf",
  "regular": "http://fonts.gstatic.com/s/lemonada/v20/0QI-MXFD9oygTWy_R-FFlwV-bgfR7QJGeut2mfWc3Z2pTg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lexend",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/lexend/v17/wlptgwvFAVdoq2_F94zlCfv0bz1WCzsX_LBte6KuGEo.ttf",
  "200": "http://fonts.gstatic.com/s/lexend/v17/wlptgwvFAVdoq2_F94zlCfv0bz1WC7sW_LBte6KuGEo.ttf",
  "300": "http://fonts.gstatic.com/s/lexend/v17/wlptgwvFAVdoq2_F94zlCfv0bz1WC2UW_LBte6KuGEo.ttf",
  "500": "http://fonts.gstatic.com/s/lexend/v17/wlptgwvFAVdoq2_F94zlCfv0bz1WCwkW_LBte6KuGEo.ttf",
  "600": "http://fonts.gstatic.com/s/lexend/v17/wlptgwvFAVdoq2_F94zlCfv0bz1WC-UR_LBte6KuGEo.ttf",
  "700": "http://fonts.gstatic.com/s/lexend/v17/wlptgwvFAVdoq2_F94zlCfv0bz1WC9wR_LBte6KuGEo.ttf",
  "800": "http://fonts.gstatic.com/s/lexend/v17/wlptgwvFAVdoq2_F94zlCfv0bz1WC7sR_LBte6KuGEo.ttf",
  "900": "http://fonts.gstatic.com/s/lexend/v17/wlptgwvFAVdoq2_F94zlCfv0bz1WC5IR_LBte6KuGEo.ttf",
  "regular": "http://fonts.gstatic.com/s/lexend/v17/wlptgwvFAVdoq2_F94zlCfv0bz1WCzsW_LBte6KuGEo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lexend Deca",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/lexenddeca/v17/K2FifZFYk-dHSE0UPPuwQ7CrD94i-NCKm-U48MxArBPCqLNflg.ttf",
  "200": "http://fonts.gstatic.com/s/lexenddeca/v17/K2FifZFYk-dHSE0UPPuwQ7CrD94i-NCKm-U4cM1ArBPCqLNflg.ttf",
  "300": "http://fonts.gstatic.com/s/lexenddeca/v17/K2FifZFYk-dHSE0UPPuwQ7CrD94i-NCKm-U4rs1ArBPCqLNflg.ttf",
  "500": "http://fonts.gstatic.com/s/lexenddeca/v17/K2FifZFYk-dHSE0UPPuwQ7CrD94i-NCKm-U4ws1ArBPCqLNflg.ttf",
  "600": "http://fonts.gstatic.com/s/lexenddeca/v17/K2FifZFYk-dHSE0UPPuwQ7CrD94i-NCKm-U4LspArBPCqLNflg.ttf",
  "700": "http://fonts.gstatic.com/s/lexenddeca/v17/K2FifZFYk-dHSE0UPPuwQ7CrD94i-NCKm-U4F8pArBPCqLNflg.ttf",
  "800": "http://fonts.gstatic.com/s/lexenddeca/v17/K2FifZFYk-dHSE0UPPuwQ7CrD94i-NCKm-U4cMpArBPCqLNflg.ttf",
  "900": "http://fonts.gstatic.com/s/lexenddeca/v17/K2FifZFYk-dHSE0UPPuwQ7CrD94i-NCKm-U4WcpArBPCqLNflg.ttf",
  "regular": "http://fonts.gstatic.com/s/lexenddeca/v17/K2FifZFYk-dHSE0UPPuwQ7CrD94i-NCKm-U48M1ArBPCqLNflg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lexend Exa",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/lexendexa/v24/UMBCrPdOoHOnxExyjdBeQCH18mulUxBvI9r7T6bHHJ8BRq0b.ttf",
  "200": "http://fonts.gstatic.com/s/lexendexa/v24/UMBCrPdOoHOnxExyjdBeQCH18mulUxBvI9p7TqbHHJ8BRq0b.ttf",
  "300": "http://fonts.gstatic.com/s/lexendexa/v24/UMBCrPdOoHOnxExyjdBeQCH18mulUxBvI9qlTqbHHJ8BRq0b.ttf",
  "500": "http://fonts.gstatic.com/s/lexendexa/v24/UMBCrPdOoHOnxExyjdBeQCH18mulUxBvI9rJTqbHHJ8BRq0b.ttf",
  "600": "http://fonts.gstatic.com/s/lexendexa/v24/UMBCrPdOoHOnxExyjdBeQCH18mulUxBvI9olSabHHJ8BRq0b.ttf",
  "700": "http://fonts.gstatic.com/s/lexendexa/v24/UMBCrPdOoHOnxExyjdBeQCH18mulUxBvI9ocSabHHJ8BRq0b.ttf",
  "800": "http://fonts.gstatic.com/s/lexendexa/v24/UMBCrPdOoHOnxExyjdBeQCH18mulUxBvI9p7SabHHJ8BRq0b.ttf",
  "900": "http://fonts.gstatic.com/s/lexendexa/v24/UMBCrPdOoHOnxExyjdBeQCH18mulUxBvI9pSSabHHJ8BRq0b.ttf",
  "regular": "http://fonts.gstatic.com/s/lexendexa/v24/UMBCrPdOoHOnxExyjdBeQCH18mulUxBvI9r7TqbHHJ8BRq0b.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lexend Giga",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/lexendgiga/v24/PlIuFl67Mah5Y8yMHE7lkUZPlTBo4MWFfNRC2LmE68oo6eepYQ.ttf",
  "200": "http://fonts.gstatic.com/s/lexendgiga/v24/PlIuFl67Mah5Y8yMHE7lkUZPlTBo4MWFfNRCWLiE68oo6eepYQ.ttf",
  "300": "http://fonts.gstatic.com/s/lexendgiga/v24/PlIuFl67Mah5Y8yMHE7lkUZPlTBo4MWFfNRChriE68oo6eepYQ.ttf",
  "500": "http://fonts.gstatic.com/s/lexendgiga/v24/PlIuFl67Mah5Y8yMHE7lkUZPlTBo4MWFfNRC6riE68oo6eepYQ.ttf",
  "600": "http://fonts.gstatic.com/s/lexendgiga/v24/PlIuFl67Mah5Y8yMHE7lkUZPlTBo4MWFfNRCBr-E68oo6eepYQ.ttf",
  "700": "http://fonts.gstatic.com/s/lexendgiga/v24/PlIuFl67Mah5Y8yMHE7lkUZPlTBo4MWFfNRCP7-E68oo6eepYQ.ttf",
  "800": "http://fonts.gstatic.com/s/lexendgiga/v24/PlIuFl67Mah5Y8yMHE7lkUZPlTBo4MWFfNRCWL-E68oo6eepYQ.ttf",
  "900": "http://fonts.gstatic.com/s/lexendgiga/v24/PlIuFl67Mah5Y8yMHE7lkUZPlTBo4MWFfNRCcb-E68oo6eepYQ.ttf",
  "regular": "http://fonts.gstatic.com/s/lexendgiga/v24/PlIuFl67Mah5Y8yMHE7lkUZPlTBo4MWFfNRC2LiE68oo6eepYQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lexend Mega",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/lexendmega/v24/qFdX35aBi5JtHD41zSTFEuTByuvYFuE9IbDL8fivveyiq9EqQw.ttf",
  "200": "http://fonts.gstatic.com/s/lexendmega/v24/qFdX35aBi5JtHD41zSTFEuTByuvYFuE9IbDLcfmvveyiq9EqQw.ttf",
  "300": "http://fonts.gstatic.com/s/lexendmega/v24/qFdX35aBi5JtHD41zSTFEuTByuvYFuE9IbDLr_mvveyiq9EqQw.ttf",
  "500": "http://fonts.gstatic.com/s/lexendmega/v24/qFdX35aBi5JtHD41zSTFEuTByuvYFuE9IbDLw_mvveyiq9EqQw.ttf",
  "600": "http://fonts.gstatic.com/s/lexendmega/v24/qFdX35aBi5JtHD41zSTFEuTByuvYFuE9IbDLL_6vveyiq9EqQw.ttf",
  "700": "http://fonts.gstatic.com/s/lexendmega/v24/qFdX35aBi5JtHD41zSTFEuTByuvYFuE9IbDLFv6vveyiq9EqQw.ttf",
  "800": "http://fonts.gstatic.com/s/lexendmega/v24/qFdX35aBi5JtHD41zSTFEuTByuvYFuE9IbDLcf6vveyiq9EqQw.ttf",
  "900": "http://fonts.gstatic.com/s/lexendmega/v24/qFdX35aBi5JtHD41zSTFEuTByuvYFuE9IbDLWP6vveyiq9EqQw.ttf",
  "regular": "http://fonts.gstatic.com/s/lexendmega/v24/qFdX35aBi5JtHD41zSTFEuTByuvYFuE9IbDL8fmvveyiq9EqQw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lexend Peta",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/lexendpeta/v24/BXR4vFPGjeLPh0kCfI4OkFX-UTQHSCaxvBgR6SFyW1YuRTsnfw.ttf",
  "200": "http://fonts.gstatic.com/s/lexendpeta/v24/BXR4vFPGjeLPh0kCfI4OkFX-UTQHSCaxvBgRaSByW1YuRTsnfw.ttf",
  "300": "http://fonts.gstatic.com/s/lexendpeta/v24/BXR4vFPGjeLPh0kCfI4OkFX-UTQHSCaxvBgRtyByW1YuRTsnfw.ttf",
  "500": "http://fonts.gstatic.com/s/lexendpeta/v24/BXR4vFPGjeLPh0kCfI4OkFX-UTQHSCaxvBgR2yByW1YuRTsnfw.ttf",
  "600": "http://fonts.gstatic.com/s/lexendpeta/v24/BXR4vFPGjeLPh0kCfI4OkFX-UTQHSCaxvBgRNydyW1YuRTsnfw.ttf",
  "700": "http://fonts.gstatic.com/s/lexendpeta/v24/BXR4vFPGjeLPh0kCfI4OkFX-UTQHSCaxvBgRDidyW1YuRTsnfw.ttf",
  "800": "http://fonts.gstatic.com/s/lexendpeta/v24/BXR4vFPGjeLPh0kCfI4OkFX-UTQHSCaxvBgRaSdyW1YuRTsnfw.ttf",
  "900": "http://fonts.gstatic.com/s/lexendpeta/v24/BXR4vFPGjeLPh0kCfI4OkFX-UTQHSCaxvBgRQCdyW1YuRTsnfw.ttf",
  "regular": "http://fonts.gstatic.com/s/lexendpeta/v24/BXR4vFPGjeLPh0kCfI4OkFX-UTQHSCaxvBgR6SByW1YuRTsnfw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lexend Tera",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/lexendtera/v24/RrQDbo98_jt_IXnBPwCWtYJLZ3P4hnaGKFiM5zITdpz0fYxcrQ.ttf",
  "200": "http://fonts.gstatic.com/s/lexendtera/v24/RrQDbo98_jt_IXnBPwCWtYJLZ3P4hnaGKFiMZzMTdpz0fYxcrQ.ttf",
  "300": "http://fonts.gstatic.com/s/lexendtera/v24/RrQDbo98_jt_IXnBPwCWtYJLZ3P4hnaGKFiMuTMTdpz0fYxcrQ.ttf",
  "500": "http://fonts.gstatic.com/s/lexendtera/v24/RrQDbo98_jt_IXnBPwCWtYJLZ3P4hnaGKFiM1TMTdpz0fYxcrQ.ttf",
  "600": "http://fonts.gstatic.com/s/lexendtera/v24/RrQDbo98_jt_IXnBPwCWtYJLZ3P4hnaGKFiMOTQTdpz0fYxcrQ.ttf",
  "700": "http://fonts.gstatic.com/s/lexendtera/v24/RrQDbo98_jt_IXnBPwCWtYJLZ3P4hnaGKFiMADQTdpz0fYxcrQ.ttf",
  "800": "http://fonts.gstatic.com/s/lexendtera/v24/RrQDbo98_jt_IXnBPwCWtYJLZ3P4hnaGKFiMZzQTdpz0fYxcrQ.ttf",
  "900": "http://fonts.gstatic.com/s/lexendtera/v24/RrQDbo98_jt_IXnBPwCWtYJLZ3P4hnaGKFiMTjQTdpz0fYxcrQ.ttf",
  "regular": "http://fonts.gstatic.com/s/lexendtera/v24/RrQDbo98_jt_IXnBPwCWtYJLZ3P4hnaGKFiM5zMTdpz0fYxcrQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lexend Zetta",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/lexendzetta/v24/ll8uK2KYXje7CdOFnEWcU8synQbuVYjYB3BCy9bH0z5jbs8qbts.ttf",
  "200": "http://fonts.gstatic.com/s/lexendzetta/v24/ll8uK2KYXje7CdOFnEWcU8synQbuVYjYB3BCy1bG0z5jbs8qbts.ttf",
  "300": "http://fonts.gstatic.com/s/lexendzetta/v24/ll8uK2KYXje7CdOFnEWcU8synQbuVYjYB3BCy4jG0z5jbs8qbts.ttf",
  "500": "http://fonts.gstatic.com/s/lexendzetta/v24/ll8uK2KYXje7CdOFnEWcU8synQbuVYjYB3BCy-TG0z5jbs8qbts.ttf",
  "600": "http://fonts.gstatic.com/s/lexendzetta/v24/ll8uK2KYXje7CdOFnEWcU8synQbuVYjYB3BCywjB0z5jbs8qbts.ttf",
  "700": "http://fonts.gstatic.com/s/lexendzetta/v24/ll8uK2KYXje7CdOFnEWcU8synQbuVYjYB3BCyzHB0z5jbs8qbts.ttf",
  "800": "http://fonts.gstatic.com/s/lexendzetta/v24/ll8uK2KYXje7CdOFnEWcU8synQbuVYjYB3BCy1bB0z5jbs8qbts.ttf",
  "900": "http://fonts.gstatic.com/s/lexendzetta/v24/ll8uK2KYXje7CdOFnEWcU8synQbuVYjYB3BCy3_B0z5jbs8qbts.ttf",
  "regular": "http://fonts.gstatic.com/s/lexendzetta/v24/ll8uK2KYXje7CdOFnEWcU8synQbuVYjYB3BCy9bG0z5jbs8qbts.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Barcode 128",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/librebarcode128/v26/cIfnMbdUsUoiW3O_hVviCwVjuLtXeJ_A_gMk0izH.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Barcode 128 Text",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/librebarcode128text/v26/fdNv9tubt3ZEnz1Gu3I4-zppwZ9CWZ16Z0w5cV3Y6M90w4k.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Barcode 39",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/librebarcode39/v19/-nFnOHM08vwC6h8Li1eQnP_AHzI2K_d709jy92k.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Barcode 39 Extended",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/librebarcode39extended/v25/8At7Gt6_O5yNS0-K4Nf5U922qSzhJ3dUdfJpwNUgfNRCOZ1GOBw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Barcode 39 Extended Text",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/librebarcode39extendedtext/v25/eLG1P_rwIgOiDA7yrs9LoKaYRVLQ1YldrrOnnL7xPO4jNP68fLIiPopNNA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Barcode 39 Text",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/librebarcode39text/v26/sJoa3KhViNKANw_E3LwoDXvs5Un0HQ1vT-031RRL-9rYaw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Barcode EAN13 Text",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/librebarcodeean13text/v19/wlpigxXFDU1_oCu9nfZytgIqSG0XRcJm_OQiB96PAGEki52WfA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Baskerville",
  "variants": [
  "regular",
  "italic",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/librebaskerville/v14/kmKiZrc3Hgbbcjq75U4uslyuy4kn0qviTjYwI8Gcw6Oi.ttf",
  "regular": "http://fonts.gstatic.com/s/librebaskerville/v14/kmKnZrc3Hgbbcjq75U4uslyuy4kn0pNeYRI4CN2V.ttf",
  "italic": "http://fonts.gstatic.com/s/librebaskerville/v14/kmKhZrc3Hgbbcjq75U4uslyuy4kn0qNcaxYaDc2V2ro.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Bodoni",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/librebodoni/v3/_Xm--H45qDWDYULr5OfyZudXzSBgY2oMBGte6L9fwWzZcOb3U3s.ttf",
  "600": "http://fonts.gstatic.com/s/librebodoni/v3/_Xm--H45qDWDYULr5OfyZudXzSBgY2oMBGte6FNYwWzZcOb3U3s.ttf",
  "700": "http://fonts.gstatic.com/s/librebodoni/v3/_Xm--H45qDWDYULr5OfyZudXzSBgY2oMBGte6GpYwWzZcOb3U3s.ttf",
  "regular": "http://fonts.gstatic.com/s/librebodoni/v3/_Xm--H45qDWDYULr5OfyZudXzSBgY2oMBGte6I1fwWzZcOb3U3s.ttf",
  "italic": "http://fonts.gstatic.com/s/librebodoni/v3/_Xm4-H45qDWDYULr5OfyZud9xBKfuwNnnsVZ_UUcKS_TdMTyQ3syLg.ttf",
  "500italic": "http://fonts.gstatic.com/s/librebodoni/v3/_Xm4-H45qDWDYULr5OfyZud9xBKfuwNnnsVZ_UUcGy_TdMTyQ3syLg.ttf",
  "600italic": "http://fonts.gstatic.com/s/librebodoni/v3/_Xm4-H45qDWDYULr5OfyZud9xBKfuwNnnsVZ_UUc9yjTdMTyQ3syLg.ttf",
  "700italic": "http://fonts.gstatic.com/s/librebodoni/v3/_Xm4-H45qDWDYULr5OfyZud9xBKfuwNnnsVZ_UUczijTdMTyQ3syLg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Caslon Display",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/librecaslondisplay/v14/TuGOUUFxWphYQ6YI6q9Xp61FQzxDRKmzr2lRdRhtCC4d.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Caslon Text",
  "variants": [
  "regular",
  "italic",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/librecaslontext/v3/DdT578IGsGw1aF1JU10PUbTvNNaDMfID8sdjNR-8ssPt.ttf",
  "regular": "http://fonts.gstatic.com/s/librecaslontext/v3/DdT878IGsGw1aF1JU10PUbTvNNaDMcq_3eNrHgO1.ttf",
  "italic": "http://fonts.gstatic.com/s/librecaslontext/v3/DdT678IGsGw1aF1JU10PUbTvNNaDMfq91-dJGxO1q9o.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Libre Franklin",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/librefranklin/v13/jizOREVItHgc8qDIbSTKq4XkRg8T88bjFuXOnduhLsSUB9rIb-JH1g.ttf",
  "200": "http://fonts.gstatic.com/s/librefranklin/v13/jizOREVItHgc8qDIbSTKq4XkRg8T88bjFuXOnduhrsWUB9rIb-JH1g.ttf",
  "300": "http://fonts.gstatic.com/s/librefranklin/v13/jizOREVItHgc8qDIbSTKq4XkRg8T88bjFuXOnduhcMWUB9rIb-JH1g.ttf",
  "500": "http://fonts.gstatic.com/s/librefranklin/v13/jizOREVItHgc8qDIbSTKq4XkRg8T88bjFuXOnduhHMWUB9rIb-JH1g.ttf",
  "600": "http://fonts.gstatic.com/s/librefranklin/v13/jizOREVItHgc8qDIbSTKq4XkRg8T88bjFuXOnduh8MKUB9rIb-JH1g.ttf",
  "700": "http://fonts.gstatic.com/s/librefranklin/v13/jizOREVItHgc8qDIbSTKq4XkRg8T88bjFuXOnduhycKUB9rIb-JH1g.ttf",
  "800": "http://fonts.gstatic.com/s/librefranklin/v13/jizOREVItHgc8qDIbSTKq4XkRg8T88bjFuXOnduhrsKUB9rIb-JH1g.ttf",
  "900": "http://fonts.gstatic.com/s/librefranklin/v13/jizOREVItHgc8qDIbSTKq4XkRg8T88bjFuXOnduhh8KUB9rIb-JH1g.ttf",
  "regular": "http://fonts.gstatic.com/s/librefranklin/v13/jizOREVItHgc8qDIbSTKq4XkRg8T88bjFuXOnduhLsWUB9rIb-JH1g.ttf",
  "100italic": "http://fonts.gstatic.com/s/librefranklin/v13/jizMREVItHgc8qDIbSTKq4XkRiUawTk7f45UM9y05oZ8RdDMTedX1sGE.ttf",
  "200italic": "http://fonts.gstatic.com/s/librefranklin/v13/jizMREVItHgc8qDIbSTKq4XkRiUawTk7f45UM9y05ob8RNDMTedX1sGE.ttf",
  "300italic": "http://fonts.gstatic.com/s/librefranklin/v13/jizMREVItHgc8qDIbSTKq4XkRiUawTk7f45UM9y05oYiRNDMTedX1sGE.ttf",
  "italic": "http://fonts.gstatic.com/s/librefranklin/v13/jizMREVItHgc8qDIbSTKq4XkRiUawTk7f45UM9y05oZ8RNDMTedX1sGE.ttf",
  "500italic": "http://fonts.gstatic.com/s/librefranklin/v13/jizMREVItHgc8qDIbSTKq4XkRiUawTk7f45UM9y05oZORNDMTedX1sGE.ttf",
  "600italic": "http://fonts.gstatic.com/s/librefranklin/v13/jizMREVItHgc8qDIbSTKq4XkRiUawTk7f45UM9y05oaiQ9DMTedX1sGE.ttf",
  "700italic": "http://fonts.gstatic.com/s/librefranklin/v13/jizMREVItHgc8qDIbSTKq4XkRiUawTk7f45UM9y05oabQ9DMTedX1sGE.ttf",
  "800italic": "http://fonts.gstatic.com/s/librefranklin/v13/jizMREVItHgc8qDIbSTKq4XkRiUawTk7f45UM9y05ob8Q9DMTedX1sGE.ttf",
  "900italic": "http://fonts.gstatic.com/s/librefranklin/v13/jizMREVItHgc8qDIbSTKq4XkRiUawTk7f45UM9y05obVQ9DMTedX1sGE.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Licorice",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/licorice/v3/t5tjIR8TMomTCAyjNk23hqLgzCHu.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Life Savers",
  "variants": [
  "regular",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/lifesavers/v18/ZXu_e1UftKKabUQMgxAal8HXOS5Tk8fIpPRW.ttf",
  "800": "http://fonts.gstatic.com/s/lifesavers/v18/ZXu_e1UftKKabUQMgxAal8HLOi5Tk8fIpPRW.ttf",
  "regular": "http://fonts.gstatic.com/s/lifesavers/v18/ZXuie1UftKKabUQMgxAal_lrFgpbuNvB.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lilita One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lilitaone/v13/i7dPIFZ9Zz-WBtRtedDbUEZ2RFq7AwU.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lily Script One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lilyscriptone/v15/LhW9MV7ZMfIPdMxeBjBvFN8SXLS4gsSjQNsRMg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Limelight",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/limelight/v16/XLYkIZL7aopJVbZJHDuYPeNGrnY2TA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Linden Hill",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lindenhill/v22/-F61fjxoKSg9Yc3hZgO8ygFI7CwC009k.ttf",
  "italic": "http://fonts.gstatic.com/s/lindenhill/v22/-F63fjxoKSg9Yc3hZgO8yjFK5igg1l9kn-s.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Literata",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v30",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/literata/v30/or3PQ6P12-iJxAIgLa78DkrbXsDgk0oVDaDPYLanFLHpPf2TbJG_F_bcTWCWp8g.ttf",
  "300": "http://fonts.gstatic.com/s/literata/v30/or3PQ6P12-iJxAIgLa78DkrbXsDgk0oVDaDPYLanFLHpPf2TbE-_F_bcTWCWp8g.ttf",
  "500": "http://fonts.gstatic.com/s/literata/v30/or3PQ6P12-iJxAIgLa78DkrbXsDgk0oVDaDPYLanFLHpPf2TbCO_F_bcTWCWp8g.ttf",
  "600": "http://fonts.gstatic.com/s/literata/v30/or3PQ6P12-iJxAIgLa78DkrbXsDgk0oVDaDPYLanFLHpPf2TbM-4F_bcTWCWp8g.ttf",
  "700": "http://fonts.gstatic.com/s/literata/v30/or3PQ6P12-iJxAIgLa78DkrbXsDgk0oVDaDPYLanFLHpPf2TbPa4F_bcTWCWp8g.ttf",
  "800": "http://fonts.gstatic.com/s/literata/v30/or3PQ6P12-iJxAIgLa78DkrbXsDgk0oVDaDPYLanFLHpPf2TbJG4F_bcTWCWp8g.ttf",
  "900": "http://fonts.gstatic.com/s/literata/v30/or3PQ6P12-iJxAIgLa78DkrbXsDgk0oVDaDPYLanFLHpPf2TbLi4F_bcTWCWp8g.ttf",
  "regular": "http://fonts.gstatic.com/s/literata/v30/or3PQ6P12-iJxAIgLa78DkrbXsDgk0oVDaDPYLanFLHpPf2TbBG_F_bcTWCWp8g.ttf",
  "200italic": "http://fonts.gstatic.com/s/literata/v30/or3NQ6P12-iJxAIgLYT1PLs1Zd0nfUwAbeGVKoRYzNiCp1OUedn8f7XWSUKTt8iVow.ttf",
  "300italic": "http://fonts.gstatic.com/s/literata/v30/or3NQ6P12-iJxAIgLYT1PLs1Zd0nfUwAbeGVKoRYzNiCp1OUedn8obXWSUKTt8iVow.ttf",
  "italic": "http://fonts.gstatic.com/s/literata/v30/or3NQ6P12-iJxAIgLYT1PLs1Zd0nfUwAbeGVKoRYzNiCp1OUedn8_7XWSUKTt8iVow.ttf",
  "500italic": "http://fonts.gstatic.com/s/literata/v30/or3NQ6P12-iJxAIgLYT1PLs1Zd0nfUwAbeGVKoRYzNiCp1OUedn8zbXWSUKTt8iVow.ttf",
  "600italic": "http://fonts.gstatic.com/s/literata/v30/or3NQ6P12-iJxAIgLYT1PLs1Zd0nfUwAbeGVKoRYzNiCp1OUedn8IbLWSUKTt8iVow.ttf",
  "700italic": "http://fonts.gstatic.com/s/literata/v30/or3NQ6P12-iJxAIgLYT1PLs1Zd0nfUwAbeGVKoRYzNiCp1OUedn8GLLWSUKTt8iVow.ttf",
  "800italic": "http://fonts.gstatic.com/s/literata/v30/or3NQ6P12-iJxAIgLYT1PLs1Zd0nfUwAbeGVKoRYzNiCp1OUedn8f7LWSUKTt8iVow.ttf",
  "900italic": "http://fonts.gstatic.com/s/literata/v30/or3NQ6P12-iJxAIgLYT1PLs1Zd0nfUwAbeGVKoRYzNiCp1OUedn8VrLWSUKTt8iVow.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Liu Jian Mao Cao",
  "variants": [
  "regular"
  ],
  "subsets": [
  "chinese-simplified",
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/liujianmaocao/v15/~ChIKEExpdSBKaWFuIE1hbyBDYW8gACoECAEYAQ==.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Livvic",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/livvic/v13/rnCr-x1S2hzjrlffC-M-mHnOSOuk.ttf",
  "200": "http://fonts.gstatic.com/s/livvic/v13/rnCq-x1S2hzjrlffp8IeslfCQfK9WQ.ttf",
  "300": "http://fonts.gstatic.com/s/livvic/v13/rnCq-x1S2hzjrlffw8EeslfCQfK9WQ.ttf",
  "500": "http://fonts.gstatic.com/s/livvic/v13/rnCq-x1S2hzjrlffm8AeslfCQfK9WQ.ttf",
  "600": "http://fonts.gstatic.com/s/livvic/v13/rnCq-x1S2hzjrlfft8ceslfCQfK9WQ.ttf",
  "700": "http://fonts.gstatic.com/s/livvic/v13/rnCq-x1S2hzjrlff08YeslfCQfK9WQ.ttf",
  "900": "http://fonts.gstatic.com/s/livvic/v13/rnCq-x1S2hzjrlff68QeslfCQfK9WQ.ttf",
  "100italic": "http://fonts.gstatic.com/s/livvic/v13/rnCt-x1S2hzjrlfXbdtakn3sTfukQHs.ttf",
  "200italic": "http://fonts.gstatic.com/s/livvic/v13/rnCs-x1S2hzjrlfXbdv2s13GY_etWWIJ.ttf",
  "300italic": "http://fonts.gstatic.com/s/livvic/v13/rnCs-x1S2hzjrlfXbduSsF3GY_etWWIJ.ttf",
  "regular": "http://fonts.gstatic.com/s/livvic/v13/rnCp-x1S2hzjrlfnb-k6unzeSA.ttf",
  "italic": "http://fonts.gstatic.com/s/livvic/v13/rnCr-x1S2hzjrlfXbeM-mHnOSOuk.ttf",
  "500italic": "http://fonts.gstatic.com/s/livvic/v13/rnCs-x1S2hzjrlfXbdvKsV3GY_etWWIJ.ttf",
  "600italic": "http://fonts.gstatic.com/s/livvic/v13/rnCs-x1S2hzjrlfXbdvmtl3GY_etWWIJ.ttf",
  "700italic": "http://fonts.gstatic.com/s/livvic/v13/rnCs-x1S2hzjrlfXbduCt13GY_etWWIJ.ttf",
  "900italic": "http://fonts.gstatic.com/s/livvic/v13/rnCs-x1S2hzjrlfXbdu6tV3GY_etWWIJ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lobster",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v28",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lobster/v28/neILzCirqoswsqX9_oWsMqEzSJQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lobster Two",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/lobstertwo/v18/BngRUXZGTXPUvIoyV6yN5-92w4CByxyKeuDp.ttf",
  "regular": "http://fonts.gstatic.com/s/lobstertwo/v18/BngMUXZGTXPUvIoyV6yN59fK7KSJ4ACD.ttf",
  "italic": "http://fonts.gstatic.com/s/lobstertwo/v18/BngOUXZGTXPUvIoyV6yN5-fI5qCr5RCDY_k.ttf",
  "700italic": "http://fonts.gstatic.com/s/lobstertwo/v18/BngTUXZGTXPUvIoyV6yN5-fI3hyEwRiof_DpXMY.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Londrina Outline",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/londrinaoutline/v23/C8c44dM8vmb14dfsZxhetg3pDH-SfuoxrSKMDvI.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Londrina Shadow",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/londrinashadow/v22/oPWX_kB4kOQoWNJmjxLV5JuoCUlXRlaSxkrMCQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Londrina Sketch",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/londrinasketch/v21/c4m41npxGMTnomOHtRU68eIJn8qfWWn5Pos6CA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Londrina Solid",
  "variants": [
  "100",
  "300",
  "regular",
  "900"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/londrinasolid/v15/flUjRq6sw40kQEJxWNgkLuudGfs9KBYesZHhV64.ttf",
  "300": "http://fonts.gstatic.com/s/londrinasolid/v15/flUiRq6sw40kQEJxWNgkLuudGfv1CjY0n53oTrcL.ttf",
  "900": "http://fonts.gstatic.com/s/londrinasolid/v15/flUiRq6sw40kQEJxWNgkLuudGfvdDzY0n53oTrcL.ttf",
  "regular": "http://fonts.gstatic.com/s/londrinasolid/v15/flUhRq6sw40kQEJxWNgkLuudGcNZIhI8tIHh.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Long Cang",
  "variants": [
  "regular"
  ],
  "subsets": [
  "chinese-simplified",
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/longcang/v17/LYjAdGP8kkgoTec8zkRgrXArXN7HWQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lora",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v26",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/lora/v26/0QI6MX1D_JOuGQbT0gvTJPa787wsuyJGmKxemMeZ.ttf",
  "600": "http://fonts.gstatic.com/s/lora/v26/0QI6MX1D_JOuGQbT0gvTJPa787zAvCJGmKxemMeZ.ttf",
  "700": "http://fonts.gstatic.com/s/lora/v26/0QI6MX1D_JOuGQbT0gvTJPa787z5vCJGmKxemMeZ.ttf",
  "regular": "http://fonts.gstatic.com/s/lora/v26/0QI6MX1D_JOuGQbT0gvTJPa787weuyJGmKxemMeZ.ttf",
  "italic": "http://fonts.gstatic.com/s/lora/v26/0QI8MX1D_JOuMw_hLdO6T2wV9KnW-MoFkqh8ndeZzZ0.ttf",
  "500italic": "http://fonts.gstatic.com/s/lora/v26/0QI8MX1D_JOuMw_hLdO6T2wV9KnW-PgFkqh8ndeZzZ0.ttf",
  "600italic": "http://fonts.gstatic.com/s/lora/v26/0QI8MX1D_JOuMw_hLdO6T2wV9KnW-BQCkqh8ndeZzZ0.ttf",
  "700italic": "http://fonts.gstatic.com/s/lora/v26/0QI8MX1D_JOuMw_hLdO6T2wV9KnW-C0Ckqh8ndeZzZ0.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Love Light",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lovelight/v3/t5tlIR0TNJyZWimpNAXDjKbCyTHuspo.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Love Ya Like A Sister",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/loveyalikeasister/v16/R70EjzUBlOqPeouhFDfR80-0FhOqJubN-Be78nZcsGGycA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Loved by the King",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lovedbytheking/v17/Gw6gwdP76VDVJNXerebZxUMeRXUF2PiNlXFu2R64.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lovers Quarrel",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/loversquarrel/v21/Yq6N-LSKXTL-5bCy8ksBzpQ_-zAsY7pO6siz.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Luckiest Guy",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/luckiestguy/v18/_gP_1RrxsjcxVyin9l9n_j2RStR3qDpraA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lusitana",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/lusitana/v13/CSR74z9ShvucWzsMKyDmaccqYtd2vfwk.ttf",
  "regular": "http://fonts.gstatic.com/s/lusitana/v13/CSR84z9ShvucWzsMKxhaRuMiSct_.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Lustria",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/lustria/v13/9oRONYodvDEyjuhOrCg5MtPyAcg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Luxurious Roman",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/luxuriousroman/v3/buEupou_ZcP1w0yTKxJJokVSmbpqYgckeo9RMw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Luxurious Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/luxuriousscript/v5/ahcCv9e7yydulT32KZ0rBIoD7DzMg0rOby1JtYk.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "M PLUS 1",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v6",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/mplus1/v6/R70EjygA28ymD4HgBUGzkN5Eyoj-WpW5VSe78nZcsGGycA.ttf",
  "200": "http://fonts.gstatic.com/s/mplus1/v6/R70EjygA28ymD4HgBUGzkN5Eyoj-WpW51Sa78nZcsGGycA.ttf",
  "300": "http://fonts.gstatic.com/s/mplus1/v6/R70EjygA28ymD4HgBUGzkN5Eyoj-WpW5Cya78nZcsGGycA.ttf",
  "500": "http://fonts.gstatic.com/s/mplus1/v6/R70EjygA28ymD4HgBUGzkN5Eyoj-WpW5Zya78nZcsGGycA.ttf",
  "600": "http://fonts.gstatic.com/s/mplus1/v6/R70EjygA28ymD4HgBUGzkN5Eyoj-WpW5iyG78nZcsGGycA.ttf",
  "700": "http://fonts.gstatic.com/s/mplus1/v6/R70EjygA28ymD4HgBUGzkN5Eyoj-WpW5siG78nZcsGGycA.ttf",
  "800": "http://fonts.gstatic.com/s/mplus1/v6/R70EjygA28ymD4HgBUGzkN5Eyoj-WpW51SG78nZcsGGycA.ttf",
  "900": "http://fonts.gstatic.com/s/mplus1/v6/R70EjygA28ymD4HgBUGzkN5Eyoj-WpW5_CG78nZcsGGycA.ttf",
  "regular": "http://fonts.gstatic.com/s/mplus1/v6/R70EjygA28ymD4HgBUGzkN5Eyoj-WpW5VSa78nZcsGGycA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "M PLUS 1 Code",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/mplus1code/v7/ypvMbXOOx2xFpzmYJS3N2_J2hBN6RZ5oIp8m_7iN0XHpapwmdZhY.ttf",
  "200": "http://fonts.gstatic.com/s/mplus1code/v7/ypvMbXOOx2xFpzmYJS3N2_J2hBN6RZ5oIp8m_7gN0HHpapwmdZhY.ttf",
  "300": "http://fonts.gstatic.com/s/mplus1code/v7/ypvMbXOOx2xFpzmYJS3N2_J2hBN6RZ5oIp8m_7jT0HHpapwmdZhY.ttf",
  "500": "http://fonts.gstatic.com/s/mplus1code/v7/ypvMbXOOx2xFpzmYJS3N2_J2hBN6RZ5oIp8m_7i_0HHpapwmdZhY.ttf",
  "600": "http://fonts.gstatic.com/s/mplus1code/v7/ypvMbXOOx2xFpzmYJS3N2_J2hBN6RZ5oIp8m_7hT13HpapwmdZhY.ttf",
  "700": "http://fonts.gstatic.com/s/mplus1code/v7/ypvMbXOOx2xFpzmYJS3N2_J2hBN6RZ5oIp8m_7hq13HpapwmdZhY.ttf",
  "regular": "http://fonts.gstatic.com/s/mplus1code/v7/ypvMbXOOx2xFpzmYJS3N2_J2hBN6RZ5oIp8m_7iN0HHpapwmdZhY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "M PLUS 1p",
  "variants": [
  "100",
  "300",
  "regular",
  "500",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "hebrew",
  "japanese",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v27",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/mplus1p/v27/e3tleuShHdiFyPFzBRrQnDQAUW3aq-5N.ttf",
  "300": "http://fonts.gstatic.com/s/mplus1p/v27/e3tmeuShHdiFyPFzBRrQVBYge0PWovdU4w.ttf",
  "500": "http://fonts.gstatic.com/s/mplus1p/v27/e3tmeuShHdiFyPFzBRrQDBcge0PWovdU4w.ttf",
  "700": "http://fonts.gstatic.com/s/mplus1p/v27/e3tmeuShHdiFyPFzBRrQRBEge0PWovdU4w.ttf",
  "800": "http://fonts.gstatic.com/s/mplus1p/v27/e3tmeuShHdiFyPFzBRrQWBIge0PWovdU4w.ttf",
  "900": "http://fonts.gstatic.com/s/mplus1p/v27/e3tmeuShHdiFyPFzBRrQfBMge0PWovdU4w.ttf",
  "regular": "http://fonts.gstatic.com/s/mplus1p/v27/e3tjeuShHdiFyPFzBRro-D4Ec2jKqw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "M PLUS 2",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v6",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/mplus2/v6/7Auhp_Eq3gO_OGbGGhjdwrDdpeIBxlkwOa-VxlqHrzNgAw.ttf",
  "200": "http://fonts.gstatic.com/s/mplus2/v6/7Auhp_Eq3gO_OGbGGhjdwrDdpeIBxlkwua6VxlqHrzNgAw.ttf",
  "300": "http://fonts.gstatic.com/s/mplus2/v6/7Auhp_Eq3gO_OGbGGhjdwrDdpeIBxlkwZ66VxlqHrzNgAw.ttf",
  "500": "http://fonts.gstatic.com/s/mplus2/v6/7Auhp_Eq3gO_OGbGGhjdwrDdpeIBxlkwC66VxlqHrzNgAw.ttf",
  "600": "http://fonts.gstatic.com/s/mplus2/v6/7Auhp_Eq3gO_OGbGGhjdwrDdpeIBxlkw56mVxlqHrzNgAw.ttf",
  "700": "http://fonts.gstatic.com/s/mplus2/v6/7Auhp_Eq3gO_OGbGGhjdwrDdpeIBxlkw3qmVxlqHrzNgAw.ttf",
  "800": "http://fonts.gstatic.com/s/mplus2/v6/7Auhp_Eq3gO_OGbGGhjdwrDdpeIBxlkwuamVxlqHrzNgAw.ttf",
  "900": "http://fonts.gstatic.com/s/mplus2/v6/7Auhp_Eq3gO_OGbGGhjdwrDdpeIBxlkwkKmVxlqHrzNgAw.ttf",
  "regular": "http://fonts.gstatic.com/s/mplus2/v6/7Auhp_Eq3gO_OGbGGhjdwrDdpeIBxlkwOa6VxlqHrzNgAw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "M PLUS Code Latin",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/mpluscodelatin/v7/hv-ylyV-aXg7x7tULiNXXBA0Np4WMS8fDIymHY8fy8wn4_ifLAtrObKDO0Xf1EbB6i5MqF9TRwg.ttf",
  "200": "http://fonts.gstatic.com/s/mpluscodelatin/v7/hv-ylyV-aXg7x7tULiNXXBA0Np4WMS8fDIymHY8fy8wn4_ifLAtrObKDO0Xf1MbA6i5MqF9TRwg.ttf",
  "300": "http://fonts.gstatic.com/s/mpluscodelatin/v7/hv-ylyV-aXg7x7tULiNXXBA0Np4WMS8fDIymHY8fy8wn4_ifLAtrObKDO0Xf1BjA6i5MqF9TRwg.ttf",
  "500": "http://fonts.gstatic.com/s/mpluscodelatin/v7/hv-ylyV-aXg7x7tULiNXXBA0Np4WMS8fDIymHY8fy8wn4_ifLAtrObKDO0Xf1HTA6i5MqF9TRwg.ttf",
  "600": "http://fonts.gstatic.com/s/mpluscodelatin/v7/hv-ylyV-aXg7x7tULiNXXBA0Np4WMS8fDIymHY8fy8wn4_ifLAtrObKDO0Xf1JjH6i5MqF9TRwg.ttf",
  "700": "http://fonts.gstatic.com/s/mpluscodelatin/v7/hv-ylyV-aXg7x7tULiNXXBA0Np4WMS8fDIymHY8fy8wn4_ifLAtrObKDO0Xf1KHH6i5MqF9TRwg.ttf",
  "regular": "http://fonts.gstatic.com/s/mpluscodelatin/v7/hv-ylyV-aXg7x7tULiNXXBA0Np4WMS8fDIymHY8fy8wn4_ifLAtrObKDO0Xf1EbA6i5MqF9TRwg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "M PLUS Rounded 1c",
  "variants": [
  "100",
  "300",
  "regular",
  "500",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "hebrew",
  "japanese",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/mplusrounded1c/v15/VdGCAYIAV6gnpUpoWwNkYvrugw9RuM3ixLsg6-av1x0.ttf",
  "300": "http://fonts.gstatic.com/s/mplusrounded1c/v15/VdGBAYIAV6gnpUpoWwNkYvrugw9RuM0q5psKxeqmzgRK.ttf",
  "500": "http://fonts.gstatic.com/s/mplusrounded1c/v15/VdGBAYIAV6gnpUpoWwNkYvrugw9RuM1y55sKxeqmzgRK.ttf",
  "700": "http://fonts.gstatic.com/s/mplusrounded1c/v15/VdGBAYIAV6gnpUpoWwNkYvrugw9RuM064ZsKxeqmzgRK.ttf",
  "800": "http://fonts.gstatic.com/s/mplusrounded1c/v15/VdGBAYIAV6gnpUpoWwNkYvrugw9RuM0m4psKxeqmzgRK.ttf",
  "900": "http://fonts.gstatic.com/s/mplusrounded1c/v15/VdGBAYIAV6gnpUpoWwNkYvrugw9RuM0C45sKxeqmzgRK.ttf",
  "regular": "http://fonts.gstatic.com/s/mplusrounded1c/v15/VdGEAYIAV6gnpUpoWwNkYvrugw9RuPWGzr8C7vav.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ma Shan Zheng",
  "variants": [
  "regular"
  ],
  "subsets": [
  "chinese-simplified",
  "latin"
  ],
  "version": "v10",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mashanzheng/v10/NaPecZTRCLxvwo41b4gvzkXaRMTsDIRSfr0.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Macondo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/macondo/v21/RrQQboN9-iB1IXmOS2XO0LBBd4Y.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Macondo Swash Caps",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/macondoswashcaps/v20/6NUL8EaAJgGKZA7lpt941Z9s6ZYgDq6Oekoa_mm5bA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mada",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "900"
  ],
  "subsets": [
  "arabic",
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-04-26",
  "files": {
  "200": "http://fonts.gstatic.com/s/mada/v16/7Au_p_0qnzeSdf3nCCL8zkwMIFg.ttf",
  "300": "http://fonts.gstatic.com/s/mada/v16/7Au_p_0qnzeSdZnkCCL8zkwMIFg.ttf",
  "500": "http://fonts.gstatic.com/s/mada/v16/7Au_p_0qnzeSdcHlCCL8zkwMIFg.ttf",
  "600": "http://fonts.gstatic.com/s/mada/v16/7Au_p_0qnzeSde3iCCL8zkwMIFg.ttf",
  "700": "http://fonts.gstatic.com/s/mada/v16/7Au_p_0qnzeSdYnjCCL8zkwMIFg.ttf",
  "900": "http://fonts.gstatic.com/s/mada/v16/7Au_p_0qnzeSdbHhCCL8zkwMIFg.ttf",
  "regular": "http://fonts.gstatic.com/s/mada/v16/7Auwp_0qnzeSTTXMLCrX0kU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Magra",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/magra/v14/uK_w4ruaZus72nbNDxcXEPuUX1ow.ttf",
  "regular": "http://fonts.gstatic.com/s/magra/v14/uK_94ruaZus72k5xIDMfO-ed.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Maiden Orange",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/maidenorange/v25/kJE1BuIX7AUmhi2V4m08kb1XjOZdCZS8FY8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Maitree",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/maitree/v10/MjQDmil5tffhpBrklhGNWJGovLdh6OE.ttf",
  "300": "http://fonts.gstatic.com/s/maitree/v10/MjQDmil5tffhpBrklnWOWJGovLdh6OE.ttf",
  "500": "http://fonts.gstatic.com/s/maitree/v10/MjQDmil5tffhpBrkli2PWJGovLdh6OE.ttf",
  "600": "http://fonts.gstatic.com/s/maitree/v10/MjQDmil5tffhpBrklgGIWJGovLdh6OE.ttf",
  "700": "http://fonts.gstatic.com/s/maitree/v10/MjQDmil5tffhpBrklmWJWJGovLdh6OE.ttf",
  "regular": "http://fonts.gstatic.com/s/maitree/v10/MjQGmil5tffhpBrkrtmmfJmDoL4.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Major Mono Display",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/majormonodisplay/v12/RWmVoLyb5fEqtsfBX9PDZIGr2tFubRhLCn2QIndPww.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mako",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mako/v18/H4coBX6Mmc_Z0ST09g478Lo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mali",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/mali/v9/N0bV2SRONuN4QOLlKlRaJdbWgdY.ttf",
  "300": "http://fonts.gstatic.com/s/mali/v9/N0bV2SRONuN4QIbmKlRaJdbWgdY.ttf",
  "500": "http://fonts.gstatic.com/s/mali/v9/N0bV2SRONuN4QN7nKlRaJdbWgdY.ttf",
  "600": "http://fonts.gstatic.com/s/mali/v9/N0bV2SRONuN4QPLgKlRaJdbWgdY.ttf",
  "700": "http://fonts.gstatic.com/s/mali/v9/N0bV2SRONuN4QJbhKlRaJdbWgdY.ttf",
  "200italic": "http://fonts.gstatic.com/s/mali/v9/N0bX2SRONuN4SCj8wlVQIfTTkdbJYA.ttf",
  "300italic": "http://fonts.gstatic.com/s/mali/v9/N0bX2SRONuN4SCj8plZQIfTTkdbJYA.ttf",
  "regular": "http://fonts.gstatic.com/s/mali/v9/N0ba2SRONuN4eCrODlxxOd8.ttf",
  "italic": "http://fonts.gstatic.com/s/mali/v9/N0bU2SRONuN4SCjECn50Kd_PmA.ttf",
  "500italic": "http://fonts.gstatic.com/s/mali/v9/N0bX2SRONuN4SCj8_ldQIfTTkdbJYA.ttf",
  "600italic": "http://fonts.gstatic.com/s/mali/v9/N0bX2SRONuN4SCj80lBQIfTTkdbJYA.ttf",
  "700italic": "http://fonts.gstatic.com/s/mali/v9/N0bX2SRONuN4SCj8tlFQIfTTkdbJYA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mallanna",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v13",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mallanna/v13/hv-Vlzx-KEQb84YaDGwzEzRwVvJ-.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mandali",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v14",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mandali/v14/LhWlMVbYOfASNfNUVFk1ZPdcKtA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Manjari",
  "variants": [
  "100",
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "malayalam"
  ],
  "version": "v9",
  "lastModified": "2022-04-26",
  "files": {
  "100": "http://fonts.gstatic.com/s/manjari/v9/k3kSo8UPMOBO2w1UdbroK2vFIaOV8A.ttf",
  "700": "http://fonts.gstatic.com/s/manjari/v9/k3kVo8UPMOBO2w1UdWLNC0HrLaqM6Q4.ttf",
  "regular": "http://fonts.gstatic.com/s/manjari/v9/k3kQo8UPMOBO2w1UTd7iL0nAMaM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Manrope",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/manrope/v13/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk59FO_F87jxeN7B.ttf",
  "300": "http://fonts.gstatic.com/s/manrope/v13/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk6jFO_F87jxeN7B.ttf",
  "500": "http://fonts.gstatic.com/s/manrope/v13/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk7PFO_F87jxeN7B.ttf",
  "600": "http://fonts.gstatic.com/s/manrope/v13/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk4jE-_F87jxeN7B.ttf",
  "700": "http://fonts.gstatic.com/s/manrope/v13/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk4aE-_F87jxeN7B.ttf",
  "800": "http://fonts.gstatic.com/s/manrope/v13/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk59E-_F87jxeN7B.ttf",
  "regular": "http://fonts.gstatic.com/s/manrope/v13/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk79FO_F87jxeN7B.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mansalva",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mansalva/v9/aWB4m0aacbtDfvq5NJllI47vdyBg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Manuale",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/manuale/v23/f0Xp0eas_8Z-TFZdHv3mMxFaSqASeeG6e7wD1TB_JHHY.ttf",
  "500": "http://fonts.gstatic.com/s/manuale/v23/f0Xp0eas_8Z-TFZdHv3mMxFaSqASeeHWe7wD1TB_JHHY.ttf",
  "600": "http://fonts.gstatic.com/s/manuale/v23/f0Xp0eas_8Z-TFZdHv3mMxFaSqASeeE6fLwD1TB_JHHY.ttf",
  "700": "http://fonts.gstatic.com/s/manuale/v23/f0Xp0eas_8Z-TFZdHv3mMxFaSqASeeEDfLwD1TB_JHHY.ttf",
  "800": "http://fonts.gstatic.com/s/manuale/v23/f0Xp0eas_8Z-TFZdHv3mMxFaSqASeeFkfLwD1TB_JHHY.ttf",
  "regular": "http://fonts.gstatic.com/s/manuale/v23/f0Xp0eas_8Z-TFZdHv3mMxFaSqASeeHke7wD1TB_JHHY.ttf",
  "300italic": "http://fonts.gstatic.com/s/manuale/v23/f0Xn0eas_8Z-TFZdNPTUzMkzITq8fvQsOApA3zRdIWHYr8M.ttf",
  "italic": "http://fonts.gstatic.com/s/manuale/v23/f0Xn0eas_8Z-TFZdNPTUzMkzITq8fvQsOFRA3zRdIWHYr8M.ttf",
  "500italic": "http://fonts.gstatic.com/s/manuale/v23/f0Xn0eas_8Z-TFZdNPTUzMkzITq8fvQsOGZA3zRdIWHYr8M.ttf",
  "600italic": "http://fonts.gstatic.com/s/manuale/v23/f0Xn0eas_8Z-TFZdNPTUzMkzITq8fvQsOIpH3zRdIWHYr8M.ttf",
  "700italic": "http://fonts.gstatic.com/s/manuale/v23/f0Xn0eas_8Z-TFZdNPTUzMkzITq8fvQsOLNH3zRdIWHYr8M.ttf",
  "800italic": "http://fonts.gstatic.com/s/manuale/v23/f0Xn0eas_8Z-TFZdNPTUzMkzITq8fvQsONRH3zRdIWHYr8M.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Marcellus",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/marcellus/v13/wEO_EBrOk8hQLDvIAF8FUfAL3EsHiA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Marcellus SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/marcellussc/v13/ke8iOgUHP1dg-Rmi6RWjbLEPgdydGKikhA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Marck Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/marckscript/v16/nwpTtK2oNgBA3Or78gapdwuCzyI-aMPF7Q.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Margarine",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/margarine/v21/qkBXXvoE6trLT9Y7YLye5JRLkAXbMQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Markazi Text",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/markazitext/v22/sykh-ydym6AtQaiEtX7yhqb_rV1k_81ZVYYZtcaQT4MlBekmJLo.ttf",
  "600": "http://fonts.gstatic.com/s/markazitext/v22/sykh-ydym6AtQaiEtX7yhqb_rV1k_81ZVYYZtSqXT4MlBekmJLo.ttf",
  "700": "http://fonts.gstatic.com/s/markazitext/v22/sykh-ydym6AtQaiEtX7yhqb_rV1k_81ZVYYZtROXT4MlBekmJLo.ttf",
  "regular": "http://fonts.gstatic.com/s/markazitext/v22/sykh-ydym6AtQaiEtX7yhqb_rV1k_81ZVYYZtfSQT4MlBekmJLo.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Marko One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/markoone/v22/9Btq3DFG0cnVM5lw1haaKpUfrHPzUw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Marmelad",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/marmelad/v15/Qw3eZQdSHj_jK2e-8tFLG-YMC0R8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Martel",
  "variants": [
  "200",
  "300",
  "regular",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/martel/v10/PN_yRfK9oXHga0XVqekahRbX9vnDzw.ttf",
  "300": "http://fonts.gstatic.com/s/martel/v10/PN_yRfK9oXHga0XVzeoahRbX9vnDzw.ttf",
  "600": "http://fonts.gstatic.com/s/martel/v10/PN_yRfK9oXHga0XVuewahRbX9vnDzw.ttf",
  "700": "http://fonts.gstatic.com/s/martel/v10/PN_yRfK9oXHga0XV3e0ahRbX9vnDzw.ttf",
  "800": "http://fonts.gstatic.com/s/martel/v10/PN_yRfK9oXHga0XVwe4ahRbX9vnDzw.ttf",
  "900": "http://fonts.gstatic.com/s/martel/v10/PN_yRfK9oXHga0XV5e8ahRbX9vnDzw.ttf",
  "regular": "http://fonts.gstatic.com/s/martel/v10/PN_xRfK9oXHga0XtYcI-jT3L_w.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Martel Sans",
  "variants": [
  "200",
  "300",
  "regular",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/martelsans/v12/h0GxssGi7VdzDgKjM-4d8hAX5suHFUknqMxQ.ttf",
  "300": "http://fonts.gstatic.com/s/martelsans/v12/h0GxssGi7VdzDgKjM-4d8hBz5cuHFUknqMxQ.ttf",
  "600": "http://fonts.gstatic.com/s/martelsans/v12/h0GxssGi7VdzDgKjM-4d8hAH48uHFUknqMxQ.ttf",
  "700": "http://fonts.gstatic.com/s/martelsans/v12/h0GxssGi7VdzDgKjM-4d8hBj4suHFUknqMxQ.ttf",
  "800": "http://fonts.gstatic.com/s/martelsans/v12/h0GxssGi7VdzDgKjM-4d8hB_4cuHFUknqMxQ.ttf",
  "900": "http://fonts.gstatic.com/s/martelsans/v12/h0GxssGi7VdzDgKjM-4d8hBb4MuHFUknqMxQ.ttf",
  "regular": "http://fonts.gstatic.com/s/martelsans/v12/h0GsssGi7VdzDgKjM-4d8ijfze-PPlUu.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Marvel",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/marvel/v14/nwpWtKeoNgBV0qawLXHgB1WmxwkiYQ.ttf",
  "regular": "http://fonts.gstatic.com/s/marvel/v14/nwpVtKeoNgBV0qaIkV7ED366zg.ttf",
  "italic": "http://fonts.gstatic.com/s/marvel/v14/nwpXtKeoNgBV0qa4k1TALXuqzhA7.ttf",
  "700italic": "http://fonts.gstatic.com/s/marvel/v14/nwpQtKeoNgBV0qa4k2x8Al-i5QwyYdrc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mate",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mate/v14/m8JdjftRd7WZ2z28WoXSaLU.ttf",
  "italic": "http://fonts.gstatic.com/s/mate/v14/m8JTjftRd7WZ6z-2XqfXeLVdbw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mate SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/matesc/v21/-nF8OGQ1-uoVr2wKyiXZ95OkJwA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Maven Pro",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v32",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/mavenpro/v32/7Auup_AqnyWWAxW2Wk3swUz56MS91Eww8Rf25nCpozp5GvU.ttf",
  "600": "http://fonts.gstatic.com/s/mavenpro/v32/7Auup_AqnyWWAxW2Wk3swUz56MS91Eww8fvx5nCpozp5GvU.ttf",
  "700": "http://fonts.gstatic.com/s/mavenpro/v32/7Auup_AqnyWWAxW2Wk3swUz56MS91Eww8cLx5nCpozp5GvU.ttf",
  "800": "http://fonts.gstatic.com/s/mavenpro/v32/7Auup_AqnyWWAxW2Wk3swUz56MS91Eww8aXx5nCpozp5GvU.ttf",
  "900": "http://fonts.gstatic.com/s/mavenpro/v32/7Auup_AqnyWWAxW2Wk3swUz56MS91Eww8Yzx5nCpozp5GvU.ttf",
  "regular": "http://fonts.gstatic.com/s/mavenpro/v32/7Auup_AqnyWWAxW2Wk3swUz56MS91Eww8SX25nCpozp5GvU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "McLaren",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mclaren/v13/2EbnL-ZuAXFqZFXISYYf8z2Yt_c.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mea Culpa",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/meaculpa/v3/AMOTz4GcuWbEIuza8jsZms0QW3mqyg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Meddon",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/meddon/v20/kmK8ZqA2EgDNeHTZhBdB3y_Aow.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "MedievalSharp",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/medievalsharp/v24/EvOJzAlL3oU5AQl2mP5KdgptAq96MwvXLDk.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Medula One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/medulaone/v19/YA9Wr0qb5kjJM6l2V0yukiEqs7GtlvY.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Meera Inimai",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "tamil"
  ],
  "version": "v12",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/meerainimai/v12/845fNMM5EIqOW5MPuvO3ILep_2jDVevnLQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Megrim",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/megrim/v16/46kulbz5WjvLqJZlbWXgd0RY1g.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Meie Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/meiescript/v21/_LOImzDK7erRjhunIspaMjxn5IXg0WDz.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Meow Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/meowscript/v5/0FlQVPqanlaJrtr8AnJ0ESch0_0CfDf1.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Merienda",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/merienda/v14/gNMAW3x8Qoy5_mf8uWu-Fa-y1sfpPES4.ttf",
  "regular": "http://fonts.gstatic.com/s/merienda/v14/gNMHW3x8Qoy5_mf8uVMCOou6_dvg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Merienda One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/meriendaone/v16/H4cgBXaMndbflEq6kyZ1ht6YgoyyYzFzFw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Merriweather",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v30",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/merriweather/v30/u-4n0qyriQwlOrhSvowK_l521wRpX837pvjxPA.ttf",
  "700": "http://fonts.gstatic.com/s/merriweather/v30/u-4n0qyriQwlOrhSvowK_l52xwNpX837pvjxPA.ttf",
  "900": "http://fonts.gstatic.com/s/merriweather/v30/u-4n0qyriQwlOrhSvowK_l52_wFpX837pvjxPA.ttf",
  "300italic": "http://fonts.gstatic.com/s/merriweather/v30/u-4l0qyriQwlOrhSvowK_l5-eR7lXcf_hP3hPGWH.ttf",
  "regular": "http://fonts.gstatic.com/s/merriweather/v30/u-440qyriQwlOrhSvowK_l5OeyxNV-bnrw.ttf",
  "italic": "http://fonts.gstatic.com/s/merriweather/v30/u-4m0qyriQwlOrhSvowK_l5-eSZJdeP3r-Ho.ttf",
  "700italic": "http://fonts.gstatic.com/s/merriweather/v30/u-4l0qyriQwlOrhSvowK_l5-eR71Wsf_hP3hPGWH.ttf",
  "900italic": "http://fonts.gstatic.com/s/merriweather/v30/u-4l0qyriQwlOrhSvowK_l5-eR7NWMf_hP3hPGWH.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Merriweather Sans",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cO9IRs1JiJN1FRAMjTN5zd9vgsFF_5asQTb6hZ2JKZ_O4ljuEG7xFHnQ.ttf",
  "500": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cO9IRs1JiJN1FRAMjTN5zd9vgsFF_5asQTb6hZ2JKZkO4ljuEG7xFHnQ.ttf",
  "600": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cO9IRs1JiJN1FRAMjTN5zd9vgsFF_5asQTb6hZ2JKZfOkljuEG7xFHnQ.ttf",
  "700": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cO9IRs1JiJN1FRAMjTN5zd9vgsFF_5asQTb6hZ2JKZRekljuEG7xFHnQ.ttf",
  "800": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cO9IRs1JiJN1FRAMjTN5zd9vgsFF_5asQTb6hZ2JKZIukljuEG7xFHnQ.ttf",
  "regular": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cO9IRs1JiJN1FRAMjTN5zd9vgsFF_5asQTb6hZ2JKZou4ljuEG7xFHnQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cM9IRs1JiJN1FRAMjTN5zd9vgsFHXwWDvLBsPDdpWMaq2TzesCzRRXnaur.ttf",
  "italic": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cM9IRs1JiJN1FRAMjTN5zd9vgsFHXwWDvLBsPDdpWMaq3NzesCzRRXnaur.ttf",
  "500italic": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cM9IRs1JiJN1FRAMjTN5zd9vgsFHXwWDvLBsPDdpWMaq3_zesCzRRXnaur.ttf",
  "600italic": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cM9IRs1JiJN1FRAMjTN5zd9vgsFHXwWDvLBsPDdpWMaq0TyusCzRRXnaur.ttf",
  "700italic": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cM9IRs1JiJN1FRAMjTN5zd9vgsFHXwWDvLBsPDdpWMaq0qyusCzRRXnaur.ttf",
  "800italic": "http://fonts.gstatic.com/s/merriweathersans/v22/2-cM9IRs1JiJN1FRAMjTN5zd9vgsFHXwWDvLBsPDdpWMaq1NyusCzRRXnaur.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Metal",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v28",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/metal/v28/lW-wwjUJIXTo7i3nnoQAUdN2.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Metal Mania",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/metalmania/v22/RWmMoKWb4e8kqMfBUdPFJeXCg6UKDXlq.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Metamorphous",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/metamorphous/v18/Wnz8HA03aAXcC39ZEX5y1330PCCthTsmaQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Metrophobic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/metrophobic/v19/sJoA3LZUhMSAPV_u0qwiAT-J737FPEEL.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Michroma",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/michroma/v16/PN_zRfy9qWD8fEagAMg6rzjb_-Da.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Milonga",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/milonga/v20/SZc53FHnIaK9W5kffz3GkUrS8DI.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Miltonian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/miltonian/v26/zOL-4pbPn6Ne9JqTg9mr6e5As-FeiQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Miltonian Tattoo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v28",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/miltoniantattoo/v28/EvOUzBRL0o0kCxF-lcMCQxlpVsA_FwP8MDBku-s.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mina",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "bengali",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/mina/v11/-nF8OGc18vARl4NMyiXZ95OkJwA.ttf",
  "regular": "http://fonts.gstatic.com/s/mina/v11/-nFzOGc18vARrz9j7i3y65o.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mingzat",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "lepcha"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mingzat/v1/0QIgMX5C-o-oWWyvBttkm_mv670.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Miniver",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/miniver/v21/eLGcP-PxIg-5H0vC770Cy8r8fWA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Miriam Libre",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/miriamlibre/v13/DdT-798HsHwubBAqfkcBTL_X3LbbRcC7_-Z7Hg.ttf",
  "regular": "http://fonts.gstatic.com/s/miriamlibre/v13/DdTh798HsHwubBAqfkcBTL_vYJn_Teun9g.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mirza",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/mirza/v15/co3FmWlikiN5EtIpAeO4mafBomDi.ttf",
  "600": "http://fonts.gstatic.com/s/mirza/v15/co3FmWlikiN5EtIFBuO4mafBomDi.ttf",
  "700": "http://fonts.gstatic.com/s/mirza/v15/co3FmWlikiN5EtJhB-O4mafBomDi.ttf",
  "regular": "http://fonts.gstatic.com/s/mirza/v15/co3ImWlikiN5EurdKMewsrvI.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Miss Fajardose",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/missfajardose/v22/E21-_dn5gvrawDdPFVl-N0Ajb8qvWPaJq4no.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mitr",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/mitr/v11/pxiEypw5ucZF8fMZFJDUc1NECPY.ttf",
  "300": "http://fonts.gstatic.com/s/mitr/v11/pxiEypw5ucZF8ZcaFJDUc1NECPY.ttf",
  "500": "http://fonts.gstatic.com/s/mitr/v11/pxiEypw5ucZF8c8bFJDUc1NECPY.ttf",
  "600": "http://fonts.gstatic.com/s/mitr/v11/pxiEypw5ucZF8eMcFJDUc1NECPY.ttf",
  "700": "http://fonts.gstatic.com/s/mitr/v11/pxiEypw5ucZF8YcdFJDUc1NECPY.ttf",
  "regular": "http://fonts.gstatic.com/s/mitr/v11/pxiLypw5ucZFyTsyMJj_b1o.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mochiy Pop One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "japanese",
  "latin"
  ],
  "version": "v7",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mochiypopone/v7/QdVPSTA9Jh-gg-5XZP2UmU4O9kwwD3s6ZKAi.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mochiy Pop P One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "japanese",
  "latin"
  ],
  "version": "v7",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mochiypoppone/v7/Ktk2AKuPeY_td1-h9LayHYWCjAqyN4O3WYZB_sU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Modak",
  "variants": [
  "regular"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/modak/v18/EJRYQgs1XtIEsnMH8BVZ76KU.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Modern Antiqua",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/modernantiqua/v22/NGStv5TIAUg6Iq_RLNo_2dp1sI1Ea2u0c3Gi.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mogra",
  "variants": [
  "regular"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mogra/v19/f0X40eSs8c95TBo4DvLmxtnG.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mohave",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/mohave/v8/7cH0v4ksjJunKqMVAOPIMOeSmiojdif_HvCQopLSvBk.ttf",
  "500": "http://fonts.gstatic.com/s/mohave/v8/7cH0v4ksjJunKqMVAOPIMOeSmiojdkv_HvCQopLSvBk.ttf",
  "600": "http://fonts.gstatic.com/s/mohave/v8/7cH0v4ksjJunKqMVAOPIMOeSmiojdqf4HvCQopLSvBk.ttf",
  "700": "http://fonts.gstatic.com/s/mohave/v8/7cH0v4ksjJunKqMVAOPIMOeSmiojdp74HvCQopLSvBk.ttf",
  "regular": "http://fonts.gstatic.com/s/mohave/v8/7cH0v4ksjJunKqMVAOPIMOeSmiojdnn_HvCQopLSvBk.ttf",
  "300italic": "http://fonts.gstatic.com/s/mohave/v8/7cH2v4ksjJunKqM_CdE36I75AIQkY7G8qLOaprDXrBlSVw.ttf",
  "italic": "http://fonts.gstatic.com/s/mohave/v8/7cH2v4ksjJunKqM_CdE36I75AIQkY7G89rOaprDXrBlSVw.ttf",
  "500italic": "http://fonts.gstatic.com/s/mohave/v8/7cH2v4ksjJunKqM_CdE36I75AIQkY7G8xLOaprDXrBlSVw.ttf",
  "600italic": "http://fonts.gstatic.com/s/mohave/v8/7cH2v4ksjJunKqM_CdE36I75AIQkY7G8KLSaprDXrBlSVw.ttf",
  "700italic": "http://fonts.gstatic.com/s/mohave/v8/7cH2v4ksjJunKqM_CdE36I75AIQkY7G8EbSaprDXrBlSVw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Molengo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/molengo/v16/I_uuMpWeuBzZNBtQbbRQkiCvs5Y.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Molle",
  "variants": [
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-04-26",
  "files": {
  "italic": "http://fonts.gstatic.com/s/molle/v21/E21n_dL5hOXFhWEsXzgmVydREus.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Monda",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/monda/v16/TK3gWkYFABsmjsLaGz8Dl-tPKo2t.ttf",
  "regular": "http://fonts.gstatic.com/s/monda/v16/TK3tWkYFABsmjvpmNBsLvPdG.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Monofett",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/monofett/v22/mFTyWbofw6zc9NtnW43SuRwr0VJ7.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Monoton",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/monoton/v15/5h1aiZUrOngCibe4fkbBQ2S7FU8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Monsieur La Doulaise",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/monsieurladoulaise/v14/_Xmz-GY4rjmCbQfc-aPRaa4pqV340p7EZl5ewkEU4HTy.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Montaga",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/montaga/v13/H4cnBX2Ml8rCkEO_0gYQ7LO5mqc.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Montagu Slab",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v6",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/montaguslab/v6/6qLhKZIQtB_zv0xUaXRDWkY_HXsphdLRZF40vm_jzR2jhk_n3T6ACkDbE3P9Fs7bOSO7.ttf",
  "200": "http://fonts.gstatic.com/s/montaguslab/v6/6qLhKZIQtB_zv0xUaXRDWkY_HXsphdLRZF40vm_jzR2jhk_n3T6ACkBbEnP9Fs7bOSO7.ttf",
  "300": "http://fonts.gstatic.com/s/montaguslab/v6/6qLhKZIQtB_zv0xUaXRDWkY_HXsphdLRZF40vm_jzR2jhk_n3T6ACkCFEnP9Fs7bOSO7.ttf",
  "500": "http://fonts.gstatic.com/s/montaguslab/v6/6qLhKZIQtB_zv0xUaXRDWkY_HXsphdLRZF40vm_jzR2jhk_n3T6ACkDpEnP9Fs7bOSO7.ttf",
  "600": "http://fonts.gstatic.com/s/montaguslab/v6/6qLhKZIQtB_zv0xUaXRDWkY_HXsphdLRZF40vm_jzR2jhk_n3T6ACkAFFXP9Fs7bOSO7.ttf",
  "700": "http://fonts.gstatic.com/s/montaguslab/v6/6qLhKZIQtB_zv0xUaXRDWkY_HXsphdLRZF40vm_jzR2jhk_n3T6ACkA8FXP9Fs7bOSO7.ttf",
  "regular": "http://fonts.gstatic.com/s/montaguslab/v6/6qLhKZIQtB_zv0xUaXRDWkY_HXsphdLRZF40vm_jzR2jhk_n3T6ACkDbEnP9Fs7bOSO7.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "MonteCarlo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/montecarlo/v7/buEzpo6-f9X01GadLA0G0CoV_NxLeiw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Montez",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/montez/v18/845ZNMk5GoGIX8lm1LDeSd-R_g.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Montserrat",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCtr6Uw-Y3tcoqK5.ttf",
  "200": "http://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCvr6Ew-Y3tcoqK5.ttf",
  "300": "http://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCs16Ew-Y3tcoqK5.ttf",
  "500": "http://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCtZ6Ew-Y3tcoqK5.ttf",
  "600": "http://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCu170w-Y3tcoqK5.ttf",
  "700": "http://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCuM70w-Y3tcoqK5.ttf",
  "800": "http://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCvr70w-Y3tcoqK5.ttf",
  "900": "http://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCvC70w-Y3tcoqK5.ttf",
  "regular": "http://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCtr6Ew-Y3tcoqK5.ttf",
  "100italic": "http://fonts.gstatic.com/s/montserrat/v25/JTUFjIg1_i6t8kCHKm459Wx7xQYXK0vOoz6jq6R8aX9-p7K5ILg.ttf",
  "200italic": "http://fonts.gstatic.com/s/montserrat/v25/JTUFjIg1_i6t8kCHKm459Wx7xQYXK0vOoz6jqyR9aX9-p7K5ILg.ttf",
  "300italic": "http://fonts.gstatic.com/s/montserrat/v25/JTUFjIg1_i6t8kCHKm459Wx7xQYXK0vOoz6jq_p9aX9-p7K5ILg.ttf",
  "italic": "http://fonts.gstatic.com/s/montserrat/v25/JTUFjIg1_i6t8kCHKm459Wx7xQYXK0vOoz6jq6R9aX9-p7K5ILg.ttf",
  "500italic": "http://fonts.gstatic.com/s/montserrat/v25/JTUFjIg1_i6t8kCHKm459Wx7xQYXK0vOoz6jq5Z9aX9-p7K5ILg.ttf",
  "600italic": "http://fonts.gstatic.com/s/montserrat/v25/JTUFjIg1_i6t8kCHKm459Wx7xQYXK0vOoz6jq3p6aX9-p7K5ILg.ttf",
  "700italic": "http://fonts.gstatic.com/s/montserrat/v25/JTUFjIg1_i6t8kCHKm459Wx7xQYXK0vOoz6jq0N6aX9-p7K5ILg.ttf",
  "800italic": "http://fonts.gstatic.com/s/montserrat/v25/JTUFjIg1_i6t8kCHKm459Wx7xQYXK0vOoz6jqyR6aX9-p7K5ILg.ttf",
  "900italic": "http://fonts.gstatic.com/s/montserrat/v25/JTUFjIg1_i6t8kCHKm459Wx7xQYXK0vOoz6jqw16aX9-p7K5ILg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Montserrat Alternates",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/montserratalternates/v17/mFThWacfw6zH4dthXcyms1lPpC8I_b0juU0xiKfVKphL03l4.ttf",
  "200": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTiWacfw6zH4dthXcyms1lPpC8I_b0juU0xJIb1ALZH2mBhkw.ttf",
  "300": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTiWacfw6zH4dthXcyms1lPpC8I_b0juU0xQIX1ALZH2mBhkw.ttf",
  "500": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTiWacfw6zH4dthXcyms1lPpC8I_b0juU0xGIT1ALZH2mBhkw.ttf",
  "600": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTiWacfw6zH4dthXcyms1lPpC8I_b0juU0xNIP1ALZH2mBhkw.ttf",
  "700": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTiWacfw6zH4dthXcyms1lPpC8I_b0juU0xUIL1ALZH2mBhkw.ttf",
  "800": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTiWacfw6zH4dthXcyms1lPpC8I_b0juU0xTIH1ALZH2mBhkw.ttf",
  "900": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTiWacfw6zH4dthXcyms1lPpC8I_b0juU0xaID1ALZH2mBhkw.ttf",
  "100italic": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTjWacfw6zH4dthXcyms1lPpC8I_b0juU057p-xIJxp1ml4imo.ttf",
  "200italic": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTkWacfw6zH4dthXcyms1lPpC8I_b0juU057p8dAbxD-GVxk3Nd.ttf",
  "300italic": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTkWacfw6zH4dthXcyms1lPpC8I_b0juU057p95ArxD-GVxk3Nd.ttf",
  "regular": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTvWacfw6zH4dthXcyms1lPpC8I_b0juU0J7K3RCJ1b0w.ttf",
  "italic": "http://fonts.gstatic.com/s/montserratalternates/v17/mFThWacfw6zH4dthXcyms1lPpC8I_b0juU057qfVKphL03l4.ttf",
  "500italic": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTkWacfw6zH4dthXcyms1lPpC8I_b0juU057p8hA7xD-GVxk3Nd.ttf",
  "600italic": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTkWacfw6zH4dthXcyms1lPpC8I_b0juU057p8NBLxD-GVxk3Nd.ttf",
  "700italic": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTkWacfw6zH4dthXcyms1lPpC8I_b0juU057p9pBbxD-GVxk3Nd.ttf",
  "800italic": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTkWacfw6zH4dthXcyms1lPpC8I_b0juU057p91BrxD-GVxk3Nd.ttf",
  "900italic": "http://fonts.gstatic.com/s/montserratalternates/v17/mFTkWacfw6zH4dthXcyms1lPpC8I_b0juU057p9RB7xD-GVxk3Nd.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Montserrat Subrayada",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/montserratsubrayada/v17/U9MM6c-o9H7PgjlTHThBnNHGVUORwteQQHe3TcMWg3j36Ebz.ttf",
  "regular": "http://fonts.gstatic.com/s/montserratsubrayada/v17/U9MD6c-o9H7PgjlTHThBnNHGVUORwteQQE8LYuceqGT-.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Moo Lah Lah",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/moolahlah/v3/dg4h_p_opKZOA0w1AYcm55wtYQYugjW4.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Moon Dance",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/moondance/v3/WBLgrEbUbFlYW9ekmGawe2XiKMiokE4.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Moul",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/moul/v25/nuF2D__FSo_3E-RYiJCy-00.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Moulpali",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v28",
  "lastModified": "2022-04-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/moulpali/v28/H4ckBXKMl9HagUWymyY6wr-wg763.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mountains of Christmas",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/mountainsofchristmas/v20/3y9z6a4zcCnn5X0FDyrKi2ZRUBIy8uxoUo7eBGqJFPtCOp6IaEA.ttf",
  "regular": "http://fonts.gstatic.com/s/mountainsofchristmas/v20/3y9w6a4zcCnn5X0FDyrKi2ZRUBIy8uxoUo7ePNamMPNpJpc.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mouse Memoirs",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mousememoirs/v13/t5tmIRoSNJ-PH0WNNgDYxdSb7TnFrpOHYh4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mr Bedfort",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mrbedfort/v21/MQpR-WCtNZSWAdTMwBicliq0XZe_Iy8.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mr Dafoe",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mrdafoe/v14/lJwE-pIzkS5NXuMMrGiqg7MCxz_C.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mr De Haviland",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mrdehaviland/v14/OpNVnooIhJj96FdB73296ksbOj3C4ULVNTlB.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mrs Saint Delafield",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mrssaintdelafield/v13/v6-IGZDIOVXH9xtmTZfRagunqBw5WC62cK4tLsubB2w.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mrs Sheppards",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mrssheppards/v21/PN_2Rfm9snC0XUGoEZhb91ig3vjxynMix4Y.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ms Madi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/msmadi/v2/HTxsL2UxNnOji5E1N-DPiI7QAYo.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mukta",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/mukta/v13/iJWHBXyXfDDVXbEOjFma-2HW7ZB_.ttf",
  "300": "http://fonts.gstatic.com/s/mukta/v13/iJWHBXyXfDDVXbFqj1ma-2HW7ZB_.ttf",
  "500": "http://fonts.gstatic.com/s/mukta/v13/iJWHBXyXfDDVXbEyjlma-2HW7ZB_.ttf",
  "600": "http://fonts.gstatic.com/s/mukta/v13/iJWHBXyXfDDVXbEeiVma-2HW7ZB_.ttf",
  "700": "http://fonts.gstatic.com/s/mukta/v13/iJWHBXyXfDDVXbF6iFma-2HW7ZB_.ttf",
  "800": "http://fonts.gstatic.com/s/mukta/v13/iJWHBXyXfDDVXbFmi1ma-2HW7ZB_.ttf",
  "regular": "http://fonts.gstatic.com/s/mukta/v13/iJWKBXyXfDDVXYnGp32S0H3f.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mukta Mahee",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "gurmukhi",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/muktamahee/v15/XRXN3IOIi0hcP8iVU67hA9MFcBoHJndqZCsW.ttf",
  "300": "http://fonts.gstatic.com/s/muktamahee/v15/XRXN3IOIi0hcP8iVU67hA9NhcxoHJndqZCsW.ttf",
  "500": "http://fonts.gstatic.com/s/muktamahee/v15/XRXN3IOIi0hcP8iVU67hA9M5choHJndqZCsW.ttf",
  "600": "http://fonts.gstatic.com/s/muktamahee/v15/XRXN3IOIi0hcP8iVU67hA9MVdRoHJndqZCsW.ttf",
  "700": "http://fonts.gstatic.com/s/muktamahee/v15/XRXN3IOIi0hcP8iVU67hA9NxdBoHJndqZCsW.ttf",
  "800": "http://fonts.gstatic.com/s/muktamahee/v15/XRXN3IOIi0hcP8iVU67hA9NtdxoHJndqZCsW.ttf",
  "regular": "http://fonts.gstatic.com/s/muktamahee/v15/XRXQ3IOIi0hcP8iVU67hA-vNWz4PDWtj.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mukta Malar",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/muktamalar/v12/MCoKzAXyz8LOE2FpJMxZqIMwBtAB62ruoAZW.ttf",
  "300": "http://fonts.gstatic.com/s/muktamalar/v12/MCoKzAXyz8LOE2FpJMxZqINUBdAB62ruoAZW.ttf",
  "500": "http://fonts.gstatic.com/s/muktamalar/v12/MCoKzAXyz8LOE2FpJMxZqIMMBNAB62ruoAZW.ttf",
  "600": "http://fonts.gstatic.com/s/muktamalar/v12/MCoKzAXyz8LOE2FpJMxZqIMgA9AB62ruoAZW.ttf",
  "700": "http://fonts.gstatic.com/s/muktamalar/v12/MCoKzAXyz8LOE2FpJMxZqINEAtAB62ruoAZW.ttf",
  "800": "http://fonts.gstatic.com/s/muktamalar/v12/MCoKzAXyz8LOE2FpJMxZqINYAdAB62ruoAZW.ttf",
  "regular": "http://fonts.gstatic.com/s/muktamalar/v12/MCoXzAXyz8LOE2FpJMxZqLv4LfQJwHbn.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mukta Vaani",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/muktavaani/v13/3JnkSD_-ynaxmxnEfVHPIGXNV8BD-u97MW1a.ttf",
  "300": "http://fonts.gstatic.com/s/muktavaani/v13/3JnkSD_-ynaxmxnEfVHPIGWpVMBD-u97MW1a.ttf",
  "500": "http://fonts.gstatic.com/s/muktavaani/v13/3JnkSD_-ynaxmxnEfVHPIGXxVcBD-u97MW1a.ttf",
  "600": "http://fonts.gstatic.com/s/muktavaani/v13/3JnkSD_-ynaxmxnEfVHPIGXdUsBD-u97MW1a.ttf",
  "700": "http://fonts.gstatic.com/s/muktavaani/v13/3JnkSD_-ynaxmxnEfVHPIGW5U8BD-u97MW1a.ttf",
  "800": "http://fonts.gstatic.com/s/muktavaani/v13/3JnkSD_-ynaxmxnEfVHPIGWlUMBD-u97MW1a.ttf",
  "regular": "http://fonts.gstatic.com/s/muktavaani/v13/3Jn5SD_-ynaxmxnEfVHPIF0FfORL0fNy.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mulish",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/mulish/v12/1Ptyg83HX_SGhgqO0yLcmjzUAuWexRNRwaClGrw-PTY.ttf",
  "300": "http://fonts.gstatic.com/s/mulish/v12/1Ptyg83HX_SGhgqO0yLcmjzUAuWexc1RwaClGrw-PTY.ttf",
  "500": "http://fonts.gstatic.com/s/mulish/v12/1Ptyg83HX_SGhgqO0yLcmjzUAuWexaFRwaClGrw-PTY.ttf",
  "600": "http://fonts.gstatic.com/s/mulish/v12/1Ptyg83HX_SGhgqO0yLcmjzUAuWexU1WwaClGrw-PTY.ttf",
  "700": "http://fonts.gstatic.com/s/mulish/v12/1Ptyg83HX_SGhgqO0yLcmjzUAuWexXRWwaClGrw-PTY.ttf",
  "800": "http://fonts.gstatic.com/s/mulish/v12/1Ptyg83HX_SGhgqO0yLcmjzUAuWexRNWwaClGrw-PTY.ttf",
  "900": "http://fonts.gstatic.com/s/mulish/v12/1Ptyg83HX_SGhgqO0yLcmjzUAuWexTpWwaClGrw-PTY.ttf",
  "regular": "http://fonts.gstatic.com/s/mulish/v12/1Ptyg83HX_SGhgqO0yLcmjzUAuWexZNRwaClGrw-PTY.ttf",
  "200italic": "http://fonts.gstatic.com/s/mulish/v12/1Ptwg83HX_SGhgqk2hAjQlW_mEuZ0FsSqeOvHp47LTZFwA.ttf",
  "300italic": "http://fonts.gstatic.com/s/mulish/v12/1Ptwg83HX_SGhgqk2hAjQlW_mEuZ0FsSd-OvHp47LTZFwA.ttf",
  "italic": "http://fonts.gstatic.com/s/mulish/v12/1Ptwg83HX_SGhgqk2hAjQlW_mEuZ0FsSKeOvHp47LTZFwA.ttf",
  "500italic": "http://fonts.gstatic.com/s/mulish/v12/1Ptwg83HX_SGhgqk2hAjQlW_mEuZ0FsSG-OvHp47LTZFwA.ttf",
  "600italic": "http://fonts.gstatic.com/s/mulish/v12/1Ptwg83HX_SGhgqk2hAjQlW_mEuZ0FsS9-SvHp47LTZFwA.ttf",
  "700italic": "http://fonts.gstatic.com/s/mulish/v12/1Ptwg83HX_SGhgqk2hAjQlW_mEuZ0FsSzuSvHp47LTZFwA.ttf",
  "800italic": "http://fonts.gstatic.com/s/mulish/v12/1Ptwg83HX_SGhgqk2hAjQlW_mEuZ0FsSqeSvHp47LTZFwA.ttf",
  "900italic": "http://fonts.gstatic.com/s/mulish/v12/1Ptwg83HX_SGhgqk2hAjQlW_mEuZ0FsSgOSvHp47LTZFwA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Murecho",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v6",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/murecho/v6/q5uYsoq3NOBn_I-ggCJg98TBOoNFCMpr5HWZLCpUOaM6.ttf",
  "200": "http://fonts.gstatic.com/s/murecho/v6/q5uYsoq3NOBn_I-ggCJg98TBOoNFCMrr5XWZLCpUOaM6.ttf",
  "300": "http://fonts.gstatic.com/s/murecho/v6/q5uYsoq3NOBn_I-ggCJg98TBOoNFCMo15XWZLCpUOaM6.ttf",
  "500": "http://fonts.gstatic.com/s/murecho/v6/q5uYsoq3NOBn_I-ggCJg98TBOoNFCMpZ5XWZLCpUOaM6.ttf",
  "600": "http://fonts.gstatic.com/s/murecho/v6/q5uYsoq3NOBn_I-ggCJg98TBOoNFCMq14nWZLCpUOaM6.ttf",
  "700": "http://fonts.gstatic.com/s/murecho/v6/q5uYsoq3NOBn_I-ggCJg98TBOoNFCMqM4nWZLCpUOaM6.ttf",
  "800": "http://fonts.gstatic.com/s/murecho/v6/q5uYsoq3NOBn_I-ggCJg98TBOoNFCMrr4nWZLCpUOaM6.ttf",
  "900": "http://fonts.gstatic.com/s/murecho/v6/q5uYsoq3NOBn_I-ggCJg98TBOoNFCMrC4nWZLCpUOaM6.ttf",
  "regular": "http://fonts.gstatic.com/s/murecho/v6/q5uYsoq3NOBn_I-ggCJg98TBOoNFCMpr5XWZLCpUOaM6.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "MuseoModerno",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/museomoderno/v22/zrf30HnU0_7wWdMrFcWqSEXPVyEaWJ55pTleMlZFuewajeKlCdo.ttf",
  "200": "http://fonts.gstatic.com/s/museomoderno/v22/zrf30HnU0_7wWdMrFcWqSEXPVyEaWJ55pTleMtZEuewajeKlCdo.ttf",
  "300": "http://fonts.gstatic.com/s/museomoderno/v22/zrf30HnU0_7wWdMrFcWqSEXPVyEaWJ55pTleMghEuewajeKlCdo.ttf",
  "500": "http://fonts.gstatic.com/s/museomoderno/v22/zrf30HnU0_7wWdMrFcWqSEXPVyEaWJ55pTleMmREuewajeKlCdo.ttf",
  "600": "http://fonts.gstatic.com/s/museomoderno/v22/zrf30HnU0_7wWdMrFcWqSEXPVyEaWJ55pTleMohDuewajeKlCdo.ttf",
  "700": "http://fonts.gstatic.com/s/museomoderno/v22/zrf30HnU0_7wWdMrFcWqSEXPVyEaWJ55pTleMrFDuewajeKlCdo.ttf",
  "800": "http://fonts.gstatic.com/s/museomoderno/v22/zrf30HnU0_7wWdMrFcWqSEXPVyEaWJ55pTleMtZDuewajeKlCdo.ttf",
  "900": "http://fonts.gstatic.com/s/museomoderno/v22/zrf30HnU0_7wWdMrFcWqSEXPVyEaWJ55pTleMv9DuewajeKlCdo.ttf",
  "regular": "http://fonts.gstatic.com/s/museomoderno/v22/zrf30HnU0_7wWdMrFcWqSEXPVyEaWJ55pTleMlZEuewajeKlCdo.ttf",
  "100italic": "http://fonts.gstatic.com/s/museomoderno/v22/zrfx0HnU0_7wWdMrFcWqSEXlXhPlgPcSP5dZJ54HUa4QicCgGdrS3g.ttf",
  "200italic": "http://fonts.gstatic.com/s/museomoderno/v22/zrfx0HnU0_7wWdMrFcWqSEXlXhPlgPcSP5dZJ54H0a8QicCgGdrS3g.ttf",
  "300italic": "http://fonts.gstatic.com/s/museomoderno/v22/zrfx0HnU0_7wWdMrFcWqSEXlXhPlgPcSP5dZJ54HD68QicCgGdrS3g.ttf",
  "italic": "http://fonts.gstatic.com/s/museomoderno/v22/zrfx0HnU0_7wWdMrFcWqSEXlXhPlgPcSP5dZJ54HUa8QicCgGdrS3g.ttf",
  "500italic": "http://fonts.gstatic.com/s/museomoderno/v22/zrfx0HnU0_7wWdMrFcWqSEXlXhPlgPcSP5dZJ54HY68QicCgGdrS3g.ttf",
  "600italic": "http://fonts.gstatic.com/s/museomoderno/v22/zrfx0HnU0_7wWdMrFcWqSEXlXhPlgPcSP5dZJ54Hj6gQicCgGdrS3g.ttf",
  "700italic": "http://fonts.gstatic.com/s/museomoderno/v22/zrfx0HnU0_7wWdMrFcWqSEXlXhPlgPcSP5dZJ54HtqgQicCgGdrS3g.ttf",
  "800italic": "http://fonts.gstatic.com/s/museomoderno/v22/zrfx0HnU0_7wWdMrFcWqSEXlXhPlgPcSP5dZJ54H0agQicCgGdrS3g.ttf",
  "900italic": "http://fonts.gstatic.com/s/museomoderno/v22/zrfx0HnU0_7wWdMrFcWqSEXlXhPlgPcSP5dZJ54H-KgQicCgGdrS3g.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "My Soul",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mysoul/v2/3XFqErcuy945_u6KF_Ulk2nnXf0.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Mystery Quest",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/mysteryquest/v20/-nF6OG414u0E6k0wynSGlujRHwElD_9Qz9E.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "NTR",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ntr/v15/RLpzK5Xy0ZjiGGhs5TA4bg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nabla",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "math",
  "vietnamese"
  ],
  "version": "v6",
  "lastModified": "2022-09-14",
  "files": {
  "regular": "http://fonts.gstatic.com/s/nabla/v6/j8_D6-LI0Lvpe7Makz5UhJt9C3uqg_X_75gyGS4jAxsNIjrRNRBUFFR_198.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nanum Brush Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/nanumbrushscript/v22/wXK2E2wfpokopxzthSqPbcR5_gVaxazyjqBr1lO97Q.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nanum Gothic",
  "variants": [
  "regular",
  "700",
  "800"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-27",
  "files": {
  "700": "http://fonts.gstatic.com/s/nanumgothic/v21/PN_oRfi-oW3hYwmKDpxS7F_LQv37zlEn14YEUQ.ttf",
  "800": "http://fonts.gstatic.com/s/nanumgothic/v21/PN_oRfi-oW3hYwmKDpxS7F_LXv77zlEn14YEUQ.ttf",
  "regular": "http://fonts.gstatic.com/s/nanumgothic/v21/PN_3Rfi-oW3hYwmKDpxS7F_z_tLfxno73g.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nanum Gothic Coding",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-27",
  "files": {
  "700": "http://fonts.gstatic.com/s/nanumgothiccoding/v19/8QIYdjzHisX_8vv59_xMxtPFW4IXROws8xgecsV88t5V9r4.ttf",
  "regular": "http://fonts.gstatic.com/s/nanumgothiccoding/v19/8QIVdjzHisX_8vv59_xMxtPFW4IXROwsy6QxVs1X7tc.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nanum Myeongjo",
  "variants": [
  "regular",
  "700",
  "800"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-27",
  "files": {
  "700": "http://fonts.gstatic.com/s/nanummyeongjo/v20/9Bty3DZF0dXLMZlywRbVRNhxy2pXV1A0pfCs5Kos.ttf",
  "800": "http://fonts.gstatic.com/s/nanummyeongjo/v20/9Bty3DZF0dXLMZlywRbVRNhxy2pLVFA0pfCs5Kos.ttf",
  "regular": "http://fonts.gstatic.com/s/nanummyeongjo/v20/9Btx3DZF0dXLMZlywRbVRNhxy1LreHQ8juyl.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nanum Pen Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/nanumpenscript/v19/daaDSSYiLGqEal3MvdA_FOL_3FkN2z7-aMFCcTU.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Neonderthaw",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/neonderthaw/v3/Iure6Yx5-oWVZI0r-17AeZZJprVA4XQ0.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nerko One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/nerkoone/v15/m8JQjfZSc7OXlB3ZMOjzcJ5BZmqa3A.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Neucha",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/neucha/v17/q5uGsou0JOdh94bvugNsCxVEgA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Neuton",
  "variants": [
  "200",
  "300",
  "regular",
  "italic",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/neuton/v18/UMBQrPtMoH62xUZKAKkfegD5Drog6Q.ttf",
  "300": "http://fonts.gstatic.com/s/neuton/v18/UMBQrPtMoH62xUZKZKofegD5Drog6Q.ttf",
  "700": "http://fonts.gstatic.com/s/neuton/v18/UMBQrPtMoH62xUZKdK0fegD5Drog6Q.ttf",
  "800": "http://fonts.gstatic.com/s/neuton/v18/UMBQrPtMoH62xUZKaK4fegD5Drog6Q.ttf",
  "regular": "http://fonts.gstatic.com/s/neuton/v18/UMBTrPtMoH62xUZyyII7civlBw.ttf",
  "italic": "http://fonts.gstatic.com/s/neuton/v18/UMBRrPtMoH62xUZCyog_UC71B6M5.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "New Rocker",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/newrocker/v16/MwQzbhjp3-HImzcCU_cJkGMViblPtXs.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "New Tegomin",
  "variants": [
  "regular"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/newtegomin/v10/SLXMc1fV7Gd9USdBAfPlqfN0Q3ptkDMN.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "News Cycle",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/newscycle/v22/CSR54z1Qlv-GDxkbKVQ_dFsvaNNUuOwkC2s.ttf",
  "regular": "http://fonts.gstatic.com/s/newscycle/v22/CSR64z1Qlv-GDxkbKVQ_TOcATNt_pOU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Newsreader",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/newsreader/v19/cY9qfjOCX1hbuyalUrK49dLac06G1ZGsZBtoBCzBDXXD9JVF438w-I_ADOxEPjCggA.ttf",
  "300": "http://fonts.gstatic.com/s/newsreader/v19/cY9qfjOCX1hbuyalUrK49dLac06G1ZGsZBtoBCzBDXXD9JVF438wJo_ADOxEPjCggA.ttf",
  "500": "http://fonts.gstatic.com/s/newsreader/v19/cY9qfjOCX1hbuyalUrK49dLac06G1ZGsZBtoBCzBDXXD9JVF438wSo_ADOxEPjCggA.ttf",
  "600": "http://fonts.gstatic.com/s/newsreader/v19/cY9qfjOCX1hbuyalUrK49dLac06G1ZGsZBtoBCzBDXXD9JVF438wpojADOxEPjCggA.ttf",
  "700": "http://fonts.gstatic.com/s/newsreader/v19/cY9qfjOCX1hbuyalUrK49dLac06G1ZGsZBtoBCzBDXXD9JVF438wn4jADOxEPjCggA.ttf",
  "800": "http://fonts.gstatic.com/s/newsreader/v19/cY9qfjOCX1hbuyalUrK49dLac06G1ZGsZBtoBCzBDXXD9JVF438w-IjADOxEPjCggA.ttf",
  "regular": "http://fonts.gstatic.com/s/newsreader/v19/cY9qfjOCX1hbuyalUrK49dLac06G1ZGsZBtoBCzBDXXD9JVF438weI_ADOxEPjCggA.ttf",
  "200italic": "http://fonts.gstatic.com/s/newsreader/v19/cY9kfjOCX1hbuyalUrK439vogqC9yFZCYg7oRZaLP4obnf7fTXglsMyoT-ZAHDWwgECi.ttf",
  "300italic": "http://fonts.gstatic.com/s/newsreader/v19/cY9kfjOCX1hbuyalUrK439vogqC9yFZCYg7oRZaLP4obnf7fTXglsMx2T-ZAHDWwgECi.ttf",
  "italic": "http://fonts.gstatic.com/s/newsreader/v19/cY9kfjOCX1hbuyalUrK439vogqC9yFZCYg7oRZaLP4obnf7fTXglsMwoT-ZAHDWwgECi.ttf",
  "500italic": "http://fonts.gstatic.com/s/newsreader/v19/cY9kfjOCX1hbuyalUrK439vogqC9yFZCYg7oRZaLP4obnf7fTXglsMwaT-ZAHDWwgECi.ttf",
  "600italic": "http://fonts.gstatic.com/s/newsreader/v19/cY9kfjOCX1hbuyalUrK439vogqC9yFZCYg7oRZaLP4obnf7fTXglsMz2SOZAHDWwgECi.ttf",
  "700italic": "http://fonts.gstatic.com/s/newsreader/v19/cY9kfjOCX1hbuyalUrK439vogqC9yFZCYg7oRZaLP4obnf7fTXglsMzPSOZAHDWwgECi.ttf",
  "800italic": "http://fonts.gstatic.com/s/newsreader/v19/cY9kfjOCX1hbuyalUrK439vogqC9yFZCYg7oRZaLP4obnf7fTXglsMyoSOZAHDWwgECi.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Niconne",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/niconne/v15/w8gaH2QvRug1_rTfrQut2F4OuOo.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Niramit",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/niramit/v10/I_urMpWdvgLdNxVLVXx7tiiEr5_BdZ8.ttf",
  "300": "http://fonts.gstatic.com/s/niramit/v10/I_urMpWdvgLdNxVLVRh4tiiEr5_BdZ8.ttf",
  "500": "http://fonts.gstatic.com/s/niramit/v10/I_urMpWdvgLdNxVLVUB5tiiEr5_BdZ8.ttf",
  "600": "http://fonts.gstatic.com/s/niramit/v10/I_urMpWdvgLdNxVLVWx-tiiEr5_BdZ8.ttf",
  "700": "http://fonts.gstatic.com/s/niramit/v10/I_urMpWdvgLdNxVLVQh_tiiEr5_BdZ8.ttf",
  "200italic": "http://fonts.gstatic.com/s/niramit/v10/I_upMpWdvgLdNxVLXbZiXimOq73EZZ_f6w.ttf",
  "300italic": "http://fonts.gstatic.com/s/niramit/v10/I_upMpWdvgLdNxVLXbZiOiqOq73EZZ_f6w.ttf",
  "regular": "http://fonts.gstatic.com/s/niramit/v10/I_uuMpWdvgLdNxVLbbRQkiCvs5Y.ttf",
  "italic": "http://fonts.gstatic.com/s/niramit/v10/I_usMpWdvgLdNxVLXbZalgKqo5bYbA.ttf",
  "500italic": "http://fonts.gstatic.com/s/niramit/v10/I_upMpWdvgLdNxVLXbZiYiuOq73EZZ_f6w.ttf",
  "600italic": "http://fonts.gstatic.com/s/niramit/v10/I_upMpWdvgLdNxVLXbZiTiyOq73EZZ_f6w.ttf",
  "700italic": "http://fonts.gstatic.com/s/niramit/v10/I_upMpWdvgLdNxVLXbZiKi2Oq73EZZ_f6w.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nixie One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/nixieone/v16/lW-8wjkKLXjg5y2o2uUoUOFzpS-yLw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nobile",
  "variants": [
  "regular",
  "italic",
  "500",
  "500italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/nobile/v17/m8JQjflSeaOVl1iOqo7zcJ5BZmqa3A.ttf",
  "700": "http://fonts.gstatic.com/s/nobile/v17/m8JQjflSeaOVl1iO4ojzcJ5BZmqa3A.ttf",
  "regular": "http://fonts.gstatic.com/s/nobile/v17/m8JTjflSeaOVl1i2XqfXeLVdbw.ttf",
  "italic": "http://fonts.gstatic.com/s/nobile/v17/m8JRjflSeaOVl1iGXK3TWrBNb3OD.ttf",
  "500italic": "http://fonts.gstatic.com/s/nobile/v17/m8JWjflSeaOVl1iGXJUnc5RFRG-K3Mud.ttf",
  "700italic": "http://fonts.gstatic.com/s/nobile/v17/m8JWjflSeaOVl1iGXJVvdZRFRG-K3Mud.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nokora",
  "variants": [
  "100",
  "300",
  "regular",
  "700",
  "900"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v30",
  "lastModified": "2022-05-10",
  "files": {
  "100": "http://fonts.gstatic.com/s/nokora/v30/~CgoKBk5va29yYRhkIAAqBAgBGAE=.ttf",
  "300": "http://fonts.gstatic.com/s/nokora/v30/~CgsKBk5va29yYRisAiAAKgQIARgB.ttf",
  "700": "http://fonts.gstatic.com/s/nokora/v30/~CgsKBk5va29yYRi8BSAAKgQIARgB.ttf",
  "900": "http://fonts.gstatic.com/s/nokora/v30/~CgsKBk5va29yYRiEByAAKgQIARgB.ttf",
  "regular": "http://fonts.gstatic.com/s/nokora/v30/~CggKBk5va29yYSAAKgQIARgB.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Norican",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/norican/v14/MwQ2bhXp1eSBqjkPGJJRtGs-lbA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nosifer",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/nosifer/v20/ZGjXol5JTp0g5bxZaC1RVDNdGDs.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Notable",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notable/v14/gNMEW3N_SIqx-WX9-HMoFIez5MI.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nothing You Could Do",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/nothingyoucoulddo/v15/oY1B8fbBpaP5OX3DtrRYf_Q2BPB1SnfZb0OJl1ol2Ymo.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noticia Text",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/noticiatext/v15/VuJpdNDF2Yv9qppOePKYRP1-3R59v2HRrDH0eA.ttf",
  "regular": "http://fonts.gstatic.com/s/noticiatext/v15/VuJ2dNDF2Yv9qppOePKYRP1GYTFZt0rNpQ.ttf",
  "italic": "http://fonts.gstatic.com/s/noticiatext/v15/VuJodNDF2Yv9qppOePKYRP12YztdlU_dpSjt.ttf",
  "700italic": "http://fonts.gstatic.com/s/noticiatext/v15/VuJrdNDF2Yv9qppOePKYRP12YwPhumvVjjTkeMnz.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Color Emoji",
  "variants": [
  "regular"
  ],
  "subsets": [
  "emoji"
  ],
  "version": "v24",
  "lastModified": "2022-09-26",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notocoloremoji/v24/Yq6P-KqIXTD0t4D9z1ESnKM3-HpFab5s79iz64w.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Emoji",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "emoji"
  ],
  "version": "v34",
  "lastModified": "2022-09-26",
  "files": {
  "300": "http://fonts.gstatic.com/s/notoemoji/v34/bMrnmSyK7YY-MEu6aWjPDs-ar6uWaGWuob_10jwvS-FGJCMY.ttf",
  "500": "http://fonts.gstatic.com/s/notoemoji/v34/bMrnmSyK7YY-MEu6aWjPDs-ar6uWaGWuob-Z0jwvS-FGJCMY.ttf",
  "600": "http://fonts.gstatic.com/s/notoemoji/v34/bMrnmSyK7YY-MEu6aWjPDs-ar6uWaGWuob911TwvS-FGJCMY.ttf",
  "700": "http://fonts.gstatic.com/s/notoemoji/v34/bMrnmSyK7YY-MEu6aWjPDs-ar6uWaGWuob9M1TwvS-FGJCMY.ttf",
  "regular": "http://fonts.gstatic.com/s/notoemoji/v34/bMrnmSyK7YY-MEu6aWjPDs-ar6uWaGWuob-r0jwvS-FGJCMY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Kufi Arabic",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "arabic"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notokufiarabic/v15/CSRp4ydQnPyaDxEXLFF6LZVLKrodhu8t57o1kDc5Wh5v3obPnLSmf5yD.ttf",
  "200": "http://fonts.gstatic.com/s/notokufiarabic/v15/CSRp4ydQnPyaDxEXLFF6LZVLKrodhu8t57o1kDc5Wh7v34bPnLSmf5yD.ttf",
  "300": "http://fonts.gstatic.com/s/notokufiarabic/v15/CSRp4ydQnPyaDxEXLFF6LZVLKrodhu8t57o1kDc5Wh4x34bPnLSmf5yD.ttf",
  "500": "http://fonts.gstatic.com/s/notokufiarabic/v15/CSRp4ydQnPyaDxEXLFF6LZVLKrodhu8t57o1kDc5Wh5d34bPnLSmf5yD.ttf",
  "600": "http://fonts.gstatic.com/s/notokufiarabic/v15/CSRp4ydQnPyaDxEXLFF6LZVLKrodhu8t57o1kDc5Wh6x2IbPnLSmf5yD.ttf",
  "700": "http://fonts.gstatic.com/s/notokufiarabic/v15/CSRp4ydQnPyaDxEXLFF6LZVLKrodhu8t57o1kDc5Wh6I2IbPnLSmf5yD.ttf",
  "800": "http://fonts.gstatic.com/s/notokufiarabic/v15/CSRp4ydQnPyaDxEXLFF6LZVLKrodhu8t57o1kDc5Wh7v2IbPnLSmf5yD.ttf",
  "900": "http://fonts.gstatic.com/s/notokufiarabic/v15/CSRp4ydQnPyaDxEXLFF6LZVLKrodhu8t57o1kDc5Wh7G2IbPnLSmf5yD.ttf",
  "regular": "http://fonts.gstatic.com/s/notokufiarabic/v15/CSRp4ydQnPyaDxEXLFF6LZVLKrodhu8t57o1kDc5Wh5v34bPnLSmf5yD.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Music",
  "variants": [
  "regular"
  ],
  "subsets": [
  "music"
  ],
  "version": "v14",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notomusic/v14/pe0rMIiSN5pO63htf1sxIteQB9Zra1U.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Naskh Arabic",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "arabic"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/notonaskharabic/v18/RrQ5bpV-9Dd1b1OAGA6M9PkyDuVBePeKNaxcsss0Y7bwj85krK0z9_Mnuw.ttf",
  "600": "http://fonts.gstatic.com/s/notonaskharabic/v18/RrQ5bpV-9Dd1b1OAGA6M9PkyDuVBePeKNaxcsss0Y7bwY8lkrK0z9_Mnuw.ttf",
  "700": "http://fonts.gstatic.com/s/notonaskharabic/v18/RrQ5bpV-9Dd1b1OAGA6M9PkyDuVBePeKNaxcsss0Y7bwWslkrK0z9_Mnuw.ttf",
  "regular": "http://fonts.gstatic.com/s/notonaskharabic/v18/RrQ5bpV-9Dd1b1OAGA6M9PkyDuVBePeKNaxcsss0Y7bwvc5krK0z9_Mnuw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Nastaliq Urdu",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-28",
  "files": {
  "500": "http://fonts.gstatic.com/s/notonastaliqurdu/v14/LhWNMUPbN-oZdNFcBy1-DJYsEoTq5pudQ9L940pGPkB3Qu3-DK2f2-_8mEw.ttf",
  "600": "http://fonts.gstatic.com/s/notonastaliqurdu/v14/LhWNMUPbN-oZdNFcBy1-DJYsEoTq5pudQ9L940pGPkB3QgH5DK2f2-_8mEw.ttf",
  "700": "http://fonts.gstatic.com/s/notonastaliqurdu/v14/LhWNMUPbN-oZdNFcBy1-DJYsEoTq5pudQ9L940pGPkB3Qjj5DK2f2-_8mEw.ttf",
  "regular": "http://fonts.gstatic.com/s/notonastaliqurdu/v14/LhWNMUPbN-oZdNFcBy1-DJYsEoTq5pudQ9L940pGPkB3Qt_-DK2f2-_8mEw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Rashi Hebrew",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notorashihebrew/v21/EJR_Qh82XsIK-QFmqXk4zvLwFVya0vFL-HlKM5e6C6HZB-DkRyq6Nf2pfA.ttf",
  "200": "http://fonts.gstatic.com/s/notorashihebrew/v21/EJR_Qh82XsIK-QFmqXk4zvLwFVya0vFL-HlKM5e6C6HZh-HkRyq6Nf2pfA.ttf",
  "300": "http://fonts.gstatic.com/s/notorashihebrew/v21/EJR_Qh82XsIK-QFmqXk4zvLwFVya0vFL-HlKM5e6C6HZWeHkRyq6Nf2pfA.ttf",
  "500": "http://fonts.gstatic.com/s/notorashihebrew/v21/EJR_Qh82XsIK-QFmqXk4zvLwFVya0vFL-HlKM5e6C6HZNeHkRyq6Nf2pfA.ttf",
  "600": "http://fonts.gstatic.com/s/notorashihebrew/v21/EJR_Qh82XsIK-QFmqXk4zvLwFVya0vFL-HlKM5e6C6HZ2ebkRyq6Nf2pfA.ttf",
  "700": "http://fonts.gstatic.com/s/notorashihebrew/v21/EJR_Qh82XsIK-QFmqXk4zvLwFVya0vFL-HlKM5e6C6HZ4ObkRyq6Nf2pfA.ttf",
  "800": "http://fonts.gstatic.com/s/notorashihebrew/v21/EJR_Qh82XsIK-QFmqXk4zvLwFVya0vFL-HlKM5e6C6HZh-bkRyq6Nf2pfA.ttf",
  "900": "http://fonts.gstatic.com/s/notorashihebrew/v21/EJR_Qh82XsIK-QFmqXk4zvLwFVya0vFL-HlKM5e6C6HZrubkRyq6Nf2pfA.ttf",
  "regular": "http://fonts.gstatic.com/s/notorashihebrew/v21/EJR_Qh82XsIK-QFmqXk4zvLwFVya0vFL-HlKM5e6C6HZB-HkRyq6Nf2pfA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "devanagari",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v27",
  "lastModified": "2022-05-10",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosans/v27/o-0OIpQlx3QUlC5A4PNjhjRFSfiM7HBj.ttf",
  "200": "http://fonts.gstatic.com/s/notosans/v27/o-0NIpQlx3QUlC5A4PNjKhVlY9aA5Wl6PQ.ttf",
  "300": "http://fonts.gstatic.com/s/notosans/v27/o-0NIpQlx3QUlC5A4PNjThZlY9aA5Wl6PQ.ttf",
  "500": "http://fonts.gstatic.com/s/notosans/v27/o-0NIpQlx3QUlC5A4PNjFhdlY9aA5Wl6PQ.ttf",
  "600": "http://fonts.gstatic.com/s/notosans/v27/o-0NIpQlx3QUlC5A4PNjOhBlY9aA5Wl6PQ.ttf",
  "700": "http://fonts.gstatic.com/s/notosans/v27/o-0NIpQlx3QUlC5A4PNjXhFlY9aA5Wl6PQ.ttf",
  "800": "http://fonts.gstatic.com/s/notosans/v27/o-0NIpQlx3QUlC5A4PNjQhJlY9aA5Wl6PQ.ttf",
  "900": "http://fonts.gstatic.com/s/notosans/v27/o-0NIpQlx3QUlC5A4PNjZhNlY9aA5Wl6PQ.ttf",
  "100italic": "http://fonts.gstatic.com/s/notosans/v27/o-0MIpQlx3QUlC5A4PNr4AwhQ_yu6WBjJLE.ttf",
  "200italic": "http://fonts.gstatic.com/s/notosans/v27/o-0TIpQlx3QUlC5A4PNr4AyNYtyEx2xqPaif.ttf",
  "300italic": "http://fonts.gstatic.com/s/notosans/v27/o-0TIpQlx3QUlC5A4PNr4AzpYdyEx2xqPaif.ttf",
  "regular": "http://fonts.gstatic.com/s/notosans/v27/o-0IIpQlx3QUlC5A4PNb4j5Ba_2c7A.ttf",
  "italic": "http://fonts.gstatic.com/s/notosans/v27/o-0OIpQlx3QUlC5A4PNr4DRFSfiM7HBj.ttf",
  "500italic": "http://fonts.gstatic.com/s/notosans/v27/o-0TIpQlx3QUlC5A4PNr4AyxYNyEx2xqPaif.ttf",
  "600italic": "http://fonts.gstatic.com/s/notosans/v27/o-0TIpQlx3QUlC5A4PNr4AydZ9yEx2xqPaif.ttf",
  "700italic": "http://fonts.gstatic.com/s/notosans/v27/o-0TIpQlx3QUlC5A4PNr4Az5ZtyEx2xqPaif.ttf",
  "800italic": "http://fonts.gstatic.com/s/notosans/v27/o-0TIpQlx3QUlC5A4PNr4AzlZdyEx2xqPaif.ttf",
  "900italic": "http://fonts.gstatic.com/s/notosans/v27/o-0TIpQlx3QUlC5A4PNr4AzBZNyEx2xqPaif.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Adlam",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "adlam",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosansadlam/v21/neIczCCpqp0s5pPusPamd81eMfjPonvqdbYxxpgufkn0TGnBZLwhuvk.ttf",
  "600": "http://fonts.gstatic.com/s/notosansadlam/v21/neIczCCpqp0s5pPusPamd81eMfjPonvqdbYxxpgufqXzTGnBZLwhuvk.ttf",
  "700": "http://fonts.gstatic.com/s/notosansadlam/v21/neIczCCpqp0s5pPusPamd81eMfjPonvqdbYxxpgufpzzTGnBZLwhuvk.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansadlam/v21/neIczCCpqp0s5pPusPamd81eMfjPonvqdbYxxpgufnv0TGnBZLwhuvk.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Adlam Unjoined",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "adlam",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosansadlamunjoined/v21/P5sszY2MYsLRsB5_ildkzPPDsLQXcOEmaFOqOGcaYrzFTIjsPam_Yd_5PMEe-E3slUg.ttf",
  "600": "http://fonts.gstatic.com/s/notosansadlamunjoined/v21/P5sszY2MYsLRsB5_ildkzPPDsLQXcOEmaFOqOGcaYrzFTIjsPam_YTP-PMEe-E3slUg.ttf",
  "700": "http://fonts.gstatic.com/s/notosansadlamunjoined/v21/P5sszY2MYsLRsB5_ildkzPPDsLQXcOEmaFOqOGcaYrzFTIjsPam_YQr-PMEe-E3slUg.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansadlamunjoined/v21/P5sszY2MYsLRsB5_ildkzPPDsLQXcOEmaFOqOGcaYrzFTIjsPam_Ye35PMEe-E3slUg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Anatolian Hieroglyphs",
  "variants": [
  "regular"
  ],
  "subsets": [
  "anatolian-hieroglyphs"
  ],
  "version": "v14",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansanatolianhieroglyphs/v14/ijw9s4roRME5LLRxjsRb8A0gKPSWq4BbDmHHu6j2pEtUJzZWXybIymc5QYo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Arabic",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "arabic"
  ],
  "version": "v18",
  "lastModified": "2022-06-01",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansarabic/v18/nwpxtLGrOAZMl5nJ_wfgRg3DrWFZWsnVBJ_sS6tlqHHFlhQ5l3sQWIHPqzCfyG2vu3CBFQLaig.ttf",
  "200": "http://fonts.gstatic.com/s/notosansarabic/v18/nwpxtLGrOAZMl5nJ_wfgRg3DrWFZWsnVBJ_sS6tlqHHFlhQ5l3sQWIHPqzCfSGyvu3CBFQLaig.ttf",
  "300": "http://fonts.gstatic.com/s/notosansarabic/v18/nwpxtLGrOAZMl5nJ_wfgRg3DrWFZWsnVBJ_sS6tlqHHFlhQ5l3sQWIHPqzCflmyvu3CBFQLaig.ttf",
  "500": "http://fonts.gstatic.com/s/notosansarabic/v18/nwpxtLGrOAZMl5nJ_wfgRg3DrWFZWsnVBJ_sS6tlqHHFlhQ5l3sQWIHPqzCf-myvu3CBFQLaig.ttf",
  "600": "http://fonts.gstatic.com/s/notosansarabic/v18/nwpxtLGrOAZMl5nJ_wfgRg3DrWFZWsnVBJ_sS6tlqHHFlhQ5l3sQWIHPqzCfFmuvu3CBFQLaig.ttf",
  "700": "http://fonts.gstatic.com/s/notosansarabic/v18/nwpxtLGrOAZMl5nJ_wfgRg3DrWFZWsnVBJ_sS6tlqHHFlhQ5l3sQWIHPqzCfL2uvu3CBFQLaig.ttf",
  "800": "http://fonts.gstatic.com/s/notosansarabic/v18/nwpxtLGrOAZMl5nJ_wfgRg3DrWFZWsnVBJ_sS6tlqHHFlhQ5l3sQWIHPqzCfSGuvu3CBFQLaig.ttf",
  "900": "http://fonts.gstatic.com/s/notosansarabic/v18/nwpxtLGrOAZMl5nJ_wfgRg3DrWFZWsnVBJ_sS6tlqHHFlhQ5l3sQWIHPqzCfYWuvu3CBFQLaig.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansarabic/v18/nwpxtLGrOAZMl5nJ_wfgRg3DrWFZWsnVBJ_sS6tlqHHFlhQ5l3sQWIHPqzCfyGyvu3CBFQLaig.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Armenian",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "armenian",
  "latin",
  "latin-ext"
  ],
  "version": "v39",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansarmenian/v39/ZgN0jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idb74R9UdM3y2nZLorxbq0iYy6zF3Eg.ttf",
  "200": "http://fonts.gstatic.com/s/notosansarmenian/v39/ZgN0jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idb74R9UdM3y2nZLopxb60iYy6zF3Eg.ttf",
  "300": "http://fonts.gstatic.com/s/notosansarmenian/v39/ZgN0jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idb74R9UdM3y2nZLoqvb60iYy6zF3Eg.ttf",
  "500": "http://fonts.gstatic.com/s/notosansarmenian/v39/ZgN0jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idb74R9UdM3y2nZLorDb60iYy6zF3Eg.ttf",
  "600": "http://fonts.gstatic.com/s/notosansarmenian/v39/ZgN0jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idb74R9UdM3y2nZLoovaK0iYy6zF3Eg.ttf",
  "700": "http://fonts.gstatic.com/s/notosansarmenian/v39/ZgN0jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idb74R9UdM3y2nZLooWaK0iYy6zF3Eg.ttf",
  "800": "http://fonts.gstatic.com/s/notosansarmenian/v39/ZgN0jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idb74R9UdM3y2nZLopxaK0iYy6zF3Eg.ttf",
  "900": "http://fonts.gstatic.com/s/notosansarmenian/v39/ZgN0jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idb74R9UdM3y2nZLopYaK0iYy6zF3Eg.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansarmenian/v39/ZgN0jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idb74R9UdM3y2nZLorxb60iYy6zF3Eg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Avestan",
  "variants": [
  "regular"
  ],
  "subsets": [
  "avestan",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansavestan/v17/bWti7ejKfBziStx7lIzKOLQZKhIJkyu9SASLji8U.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Balinese",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "balinese",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosansbalinese/v18/NaPwcYvSBuhTirw6IaFn6UrRDaqje-lpbbRtYf-Fwu2Ov4XdhE5Vd222PPY.ttf",
  "600": "http://fonts.gstatic.com/s/notosansbalinese/v18/NaPwcYvSBuhTirw6IaFn6UrRDaqje-lpbbRtYf-Fwu2Ov2nahE5Vd222PPY.ttf",
  "700": "http://fonts.gstatic.com/s/notosansbalinese/v18/NaPwcYvSBuhTirw6IaFn6UrRDaqje-lpbbRtYf-Fwu2Ov1DahE5Vd222PPY.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansbalinese/v18/NaPwcYvSBuhTirw6IaFn6UrRDaqje-lpbbRtYf-Fwu2Ov7fdhE5Vd222PPY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Bamum",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "bamum"
  ],
  "version": "v18",
  "lastModified": "2022-07-19",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosansbamum/v18/uk-0EGK3o6EruUbnwovcbBTkkklK_Ya_PBHfNGTPEeVO-_gLykxEkxA.ttf",
  "600": "http://fonts.gstatic.com/s/notosansbamum/v18/uk-0EGK3o6EruUbnwovcbBTkkklK_Ya_PBHfNGTPEQlJ-_gLykxEkxA.ttf",
  "700": "http://fonts.gstatic.com/s/notosansbamum/v18/uk-0EGK3o6EruUbnwovcbBTkkklK_Ya_PBHfNGTPETBJ-_gLykxEkxA.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansbamum/v18/uk-0EGK3o6EruUbnwovcbBTkkklK_Ya_PBHfNGTPEddO-_gLykxEkxA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Bassa Vah",
  "variants": [
  "regular"
  ],
  "subsets": [
  "bassa-vah"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansbassavah/v15/PN_sRee-r3f7LnqsD5sax12gjZn7mBpL_4c2VNUQptE.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Batak",
  "variants": [
  "regular"
  ],
  "subsets": [
  "batak",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansbatak/v16/gok2H6TwAEdtF9N8-mdTCQvT-Zdgo4_PHuk74A.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Bengali",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "bengali",
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansbengali/v20/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6KmsolKudCk8izI0lc.ttf",
  "200": "http://fonts.gstatic.com/s/notosansbengali/v20/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6KmsglLudCk8izI0lc.ttf",
  "300": "http://fonts.gstatic.com/s/notosansbengali/v20/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6KmstdLudCk8izI0lc.ttf",
  "500": "http://fonts.gstatic.com/s/notosansbengali/v20/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6KmsrtLudCk8izI0lc.ttf",
  "600": "http://fonts.gstatic.com/s/notosansbengali/v20/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6KmsldMudCk8izI0lc.ttf",
  "700": "http://fonts.gstatic.com/s/notosansbengali/v20/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6Kmsm5MudCk8izI0lc.ttf",
  "800": "http://fonts.gstatic.com/s/notosansbengali/v20/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6KmsglMudCk8izI0lc.ttf",
  "900": "http://fonts.gstatic.com/s/notosansbengali/v20/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6KmsiBMudCk8izI0lc.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansbengali/v20/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6KmsolLudCk8izI0lc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Bhaiksuki",
  "variants": [
  "regular"
  ],
  "subsets": [
  "bhaiksuki"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansbhaiksuki/v15/UcC63EosKniBH4iELXATsSBWdvUHXxhj8rLUdU4wh9U.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Brahmi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "brahmi"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansbrahmi/v15/vEFK2-VODB8RrNDvZSUmQQIIByV18tK1W77HtMo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Buginese",
  "variants": [
  "regular"
  ],
  "subsets": [
  "buginese"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansbuginese/v15/esDM30ldNv-KYGGJpKGk18phe_7Da6_gtfuEXLmNtw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Buhid",
  "variants": [
  "regular"
  ],
  "subsets": [
  "buhid",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansbuhid/v17/Dxxy8jiXMW75w3OmoDXVWJD7YwzAe6tgnaFoGA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Canadian Aboriginal",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "canadian-aboriginal",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanscanadianaboriginal/v21/4C_TLjTuEqPj-8J01CwaGkiZ9os0iGVkezM1mUT-j_Lmlzda6uH_nnX1bzigWLj_yAsg0q0uhQ.ttf",
  "200": "http://fonts.gstatic.com/s/notosanscanadianaboriginal/v21/4C_TLjTuEqPj-8J01CwaGkiZ9os0iGVkezM1mUT-j_Lmlzda6uH_nnX1bzig2Ln_yAsg0q0uhQ.ttf",
  "300": "http://fonts.gstatic.com/s/notosanscanadianaboriginal/v21/4C_TLjTuEqPj-8J01CwaGkiZ9os0iGVkezM1mUT-j_Lmlzda6uH_nnX1bzigBrn_yAsg0q0uhQ.ttf",
  "500": "http://fonts.gstatic.com/s/notosanscanadianaboriginal/v21/4C_TLjTuEqPj-8J01CwaGkiZ9os0iGVkezM1mUT-j_Lmlzda6uH_nnX1bzigarn_yAsg0q0uhQ.ttf",
  "600": "http://fonts.gstatic.com/s/notosanscanadianaboriginal/v21/4C_TLjTuEqPj-8J01CwaGkiZ9os0iGVkezM1mUT-j_Lmlzda6uH_nnX1bzighr7_yAsg0q0uhQ.ttf",
  "700": "http://fonts.gstatic.com/s/notosanscanadianaboriginal/v21/4C_TLjTuEqPj-8J01CwaGkiZ9os0iGVkezM1mUT-j_Lmlzda6uH_nnX1bzigv77_yAsg0q0uhQ.ttf",
  "800": "http://fonts.gstatic.com/s/notosanscanadianaboriginal/v21/4C_TLjTuEqPj-8J01CwaGkiZ9os0iGVkezM1mUT-j_Lmlzda6uH_nnX1bzig2L7_yAsg0q0uhQ.ttf",
  "900": "http://fonts.gstatic.com/s/notosanscanadianaboriginal/v21/4C_TLjTuEqPj-8J01CwaGkiZ9os0iGVkezM1mUT-j_Lmlzda6uH_nnX1bzig8b7_yAsg0q0uhQ.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanscanadianaboriginal/v21/4C_TLjTuEqPj-8J01CwaGkiZ9os0iGVkezM1mUT-j_Lmlzda6uH_nnX1bzigWLn_yAsg0q0uhQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Carian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "carian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanscarian/v15/LDIpaoiONgYwA9Yc6f0gUILeMIOgs7ob9yGLmfI.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Caucasian Albanian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "caucasian-albanian"
  ],
  "version": "v16",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanscaucasianalbanian/v16/nKKA-HM_FYFRJvXzVXaANsU0VzsAc46QGOkWytlTs-TXrYDmoVmRSZo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Chakma",
  "variants": [
  "regular"
  ],
  "subsets": [
  "chakma"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanschakma/v15/Y4GQYbJ8VTEp4t3MKJSMjg5OIzhi4JjTQhYBeYo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Cham",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cham",
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanscham/v23/pe06MIySN5pO62Z5YkFyQb_bbuRhe6D4yip43qfcER0cv7GykboaLg.ttf",
  "200": "http://fonts.gstatic.com/s/notosanscham/v23/pe06MIySN5pO62Z5YkFyQb_bbuRhe6D4yip43qfckRwcv7GykboaLg.ttf",
  "300": "http://fonts.gstatic.com/s/notosanscham/v23/pe06MIySN5pO62Z5YkFyQb_bbuRhe6D4yip43qfcTxwcv7GykboaLg.ttf",
  "500": "http://fonts.gstatic.com/s/notosanscham/v23/pe06MIySN5pO62Z5YkFyQb_bbuRhe6D4yip43qfcIxwcv7GykboaLg.ttf",
  "600": "http://fonts.gstatic.com/s/notosanscham/v23/pe06MIySN5pO62Z5YkFyQb_bbuRhe6D4yip43qfczxscv7GykboaLg.ttf",
  "700": "http://fonts.gstatic.com/s/notosanscham/v23/pe06MIySN5pO62Z5YkFyQb_bbuRhe6D4yip43qfc9hscv7GykboaLg.ttf",
  "800": "http://fonts.gstatic.com/s/notosanscham/v23/pe06MIySN5pO62Z5YkFyQb_bbuRhe6D4yip43qfckRscv7GykboaLg.ttf",
  "900": "http://fonts.gstatic.com/s/notosanscham/v23/pe06MIySN5pO62Z5YkFyQb_bbuRhe6D4yip43qfcuBscv7GykboaLg.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanscham/v23/pe06MIySN5pO62Z5YkFyQb_bbuRhe6D4yip43qfcERwcv7GykboaLg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Cherokee",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cherokee",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanscherokee/v19/KFOPCm6Yu8uF-29fiz9vQF9YWK6Z8O10cHNA0cSkZCHYWi5ODkm5rAffjl0.ttf",
  "200": "http://fonts.gstatic.com/s/notosanscherokee/v19/KFOPCm6Yu8uF-29fiz9vQF9YWK6Z8O10cHNA0cSkZCHYWq5PDkm5rAffjl0.ttf",
  "300": "http://fonts.gstatic.com/s/notosanscherokee/v19/KFOPCm6Yu8uF-29fiz9vQF9YWK6Z8O10cHNA0cSkZCHYWnBPDkm5rAffjl0.ttf",
  "500": "http://fonts.gstatic.com/s/notosanscherokee/v19/KFOPCm6Yu8uF-29fiz9vQF9YWK6Z8O10cHNA0cSkZCHYWhxPDkm5rAffjl0.ttf",
  "600": "http://fonts.gstatic.com/s/notosanscherokee/v19/KFOPCm6Yu8uF-29fiz9vQF9YWK6Z8O10cHNA0cSkZCHYWvBIDkm5rAffjl0.ttf",
  "700": "http://fonts.gstatic.com/s/notosanscherokee/v19/KFOPCm6Yu8uF-29fiz9vQF9YWK6Z8O10cHNA0cSkZCHYWslIDkm5rAffjl0.ttf",
  "800": "http://fonts.gstatic.com/s/notosanscherokee/v19/KFOPCm6Yu8uF-29fiz9vQF9YWK6Z8O10cHNA0cSkZCHYWq5IDkm5rAffjl0.ttf",
  "900": "http://fonts.gstatic.com/s/notosanscherokee/v19/KFOPCm6Yu8uF-29fiz9vQF9YWK6Z8O10cHNA0cSkZCHYWodIDkm5rAffjl0.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanscherokee/v19/KFOPCm6Yu8uF-29fiz9vQF9YWK6Z8O10cHNA0cSkZCHYWi5PDkm5rAffjl0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Coptic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "coptic",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanscoptic/v17/iJWfBWmUZi_OHPqn4wq6kgqumOEd78u_VG0xR4Y.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Cuneiform",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cuneiform"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanscuneiform/v15/bMrrmTWK7YY-MF22aHGGd7H8PhJtvBDWgb9JlRQueeQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Cypriot",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cypriot"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanscypriot/v15/8AtzGta9PYqQDjyp79a6f8Cj-3a3cxIsK5MPpahF.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Deseret",
  "variants": [
  "regular"
  ],
  "subsets": [
  "deseret"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansdeseret/v15/MwQsbgPp1eKH6QsAVuFb9AZM6MMr2Vq9ZnJSZtQG.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Devanagari",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansdevanagari/v19/TuGoUUFzXI5FBtUq5a8bjKYTZjtRU6Sgv3NaV_SNmI0b8QQCQmHn6B2OHjbL_08AlXQky-AzoFoW4Ow.ttf",
  "200": "http://fonts.gstatic.com/s/notosansdevanagari/v19/TuGoUUFzXI5FBtUq5a8bjKYTZjtRU6Sgv3NaV_SNmI0b8QQCQmHn6B2OHjbL_08AlfQly-AzoFoW4Ow.ttf",
  "300": "http://fonts.gstatic.com/s/notosansdevanagari/v19/TuGoUUFzXI5FBtUq5a8bjKYTZjtRU6Sgv3NaV_SNmI0b8QQCQmHn6B2OHjbL_08AlSoly-AzoFoW4Ow.ttf",
  "500": "http://fonts.gstatic.com/s/notosansdevanagari/v19/TuGoUUFzXI5FBtUq5a8bjKYTZjtRU6Sgv3NaV_SNmI0b8QQCQmHn6B2OHjbL_08AlUYly-AzoFoW4Ow.ttf",
  "600": "http://fonts.gstatic.com/s/notosansdevanagari/v19/TuGoUUFzXI5FBtUq5a8bjKYTZjtRU6Sgv3NaV_SNmI0b8QQCQmHn6B2OHjbL_08Alaoiy-AzoFoW4Ow.ttf",
  "700": "http://fonts.gstatic.com/s/notosansdevanagari/v19/TuGoUUFzXI5FBtUq5a8bjKYTZjtRU6Sgv3NaV_SNmI0b8QQCQmHn6B2OHjbL_08AlZMiy-AzoFoW4Ow.ttf",
  "800": "http://fonts.gstatic.com/s/notosansdevanagari/v19/TuGoUUFzXI5FBtUq5a8bjKYTZjtRU6Sgv3NaV_SNmI0b8QQCQmHn6B2OHjbL_08AlfQiy-AzoFoW4Ow.ttf",
  "900": "http://fonts.gstatic.com/s/notosansdevanagari/v19/TuGoUUFzXI5FBtUq5a8bjKYTZjtRU6Sgv3NaV_SNmI0b8QQCQmHn6B2OHjbL_08Ald0iy-AzoFoW4Ow.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansdevanagari/v19/TuGoUUFzXI5FBtUq5a8bjKYTZjtRU6Sgv3NaV_SNmI0b8QQCQmHn6B2OHjbL_08AlXQly-AzoFoW4Ow.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Display",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpbK4fy6r6tOBEJg0IAKzqdFZVZxpMkXJMhnB9XjO1o90LuV-PT4Doq_AKp_3cLVTGQ2iHrvWM.ttf",
  "200": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpbK4fy6r6tOBEJg0IAKzqdFZVZxpMkXJMhnB9XjO1o90LuV-PT4Doq_AKp__cKVTGQ2iHrvWM.ttf",
  "300": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpbK4fy6r6tOBEJg0IAKzqdFZVZxpMkXJMhnB9XjO1o90LuV-PT4Doq_AKp_ykKVTGQ2iHrvWM.ttf",
  "500": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpbK4fy6r6tOBEJg0IAKzqdFZVZxpMkXJMhnB9XjO1o90LuV-PT4Doq_AKp_0UKVTGQ2iHrvWM.ttf",
  "600": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpbK4fy6r6tOBEJg0IAKzqdFZVZxpMkXJMhnB9XjO1o90LuV-PT4Doq_AKp_6kNVTGQ2iHrvWM.ttf",
  "700": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpbK4fy6r6tOBEJg0IAKzqdFZVZxpMkXJMhnB9XjO1o90LuV-PT4Doq_AKp_5ANVTGQ2iHrvWM.ttf",
  "800": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpbK4fy6r6tOBEJg0IAKzqdFZVZxpMkXJMhnB9XjO1o90LuV-PT4Doq_AKp__cNVTGQ2iHrvWM.ttf",
  "900": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpbK4fy6r6tOBEJg0IAKzqdFZVZxpMkXJMhnB9XjO1o90LuV-PT4Doq_AKp_94NVTGQ2iHrvWM.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpbK4fy6r6tOBEJg0IAKzqdFZVZxpMkXJMhnB9XjO1o90LuV-PT4Doq_AKp_3cKVTGQ2iHrvWM.ttf",
  "100italic": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpZK4fy6r6tOBEJg0IAKzqdFZVZxrktbnDB5UzBIup9PwAcHtEsOFNBZqyu6r9JvXOa3gPurWM9uQ.ttf",
  "200italic": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpZK4fy6r6tOBEJg0IAKzqdFZVZxrktbnDB5UzBIup9PwAcHtEsOFNBZqyu6r9JPXKa3gPurWM9uQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpZK4fy6r6tOBEJg0IAKzqdFZVZxrktbnDB5UzBIup9PwAcHtEsOFNBZqyu6r9J43Ka3gPurWM9uQ.ttf",
  "italic": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpZK4fy6r6tOBEJg0IAKzqdFZVZxrktbnDB5UzBIup9PwAcHtEsOFNBZqyu6r9JvXKa3gPurWM9uQ.ttf",
  "500italic": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpZK4fy6r6tOBEJg0IAKzqdFZVZxrktbnDB5UzBIup9PwAcHtEsOFNBZqyu6r9Jj3Ka3gPurWM9uQ.ttf",
  "600italic": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpZK4fy6r6tOBEJg0IAKzqdFZVZxrktbnDB5UzBIup9PwAcHtEsOFNBZqyu6r9JY3Wa3gPurWM9uQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpZK4fy6r6tOBEJg0IAKzqdFZVZxrktbnDB5UzBIup9PwAcHtEsOFNBZqyu6r9JWnWa3gPurWM9uQ.ttf",
  "800italic": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpZK4fy6r6tOBEJg0IAKzqdFZVZxrktbnDB5UzBIup9PwAcHtEsOFNBZqyu6r9JPXWa3gPurWM9uQ.ttf",
  "900italic": "http://fonts.gstatic.com/s/notosansdisplay/v20/RLpZK4fy6r6tOBEJg0IAKzqdFZVZxrktbnDB5UzBIup9PwAcHtEsOFNBZqyu6r9JFHWa3gPurWM9uQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Duployan",
  "variants": [
  "regular"
  ],
  "subsets": [
  "duployan"
  ],
  "version": "v16",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansduployan/v16/gokzH7nwAEdtF9N8-mdTDx_X9JM5wsvrFsIn6WYDvA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Egyptian Hieroglyphs",
  "variants": [
  "regular"
  ],
  "subsets": [
  "egyptian-hieroglyphs"
  ],
  "version": "v26",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansegyptianhieroglyphs/v26/vEF42-tODB8RrNDvZSUmRhcQHzx1s7y_F9-j3qSzEcbEYindSVK8xRg7iw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Elbasan",
  "variants": [
  "regular"
  ],
  "subsets": [
  "elbasan"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanselbasan/v15/-F6rfiZqLzI2JPCgQBnw400qp1trvHdlre4dFcFh.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Elymaic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "elymaic"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanselymaic/v15/UqyKK9YTJW5liNMhTMqe9vUFP65ZD4AjWOT0zi2V.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Ethiopic",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "ethiopic",
  "latin",
  "latin-ext"
  ],
  "version": "v38",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansethiopic/v38/7cHPv50vjIepfJVOZZgcpQ5B9FBTH9KGNfhSTgtoow1KVnIvyBoMSzUMacb-T35OKqDjwmfeaY9u.ttf",
  "200": "http://fonts.gstatic.com/s/notosansethiopic/v38/7cHPv50vjIepfJVOZZgcpQ5B9FBTH9KGNfhSTgtoow1KVnIvyBoMSzUMacb-T37OK6DjwmfeaY9u.ttf",
  "300": "http://fonts.gstatic.com/s/notosansethiopic/v38/7cHPv50vjIepfJVOZZgcpQ5B9FBTH9KGNfhSTgtoow1KVnIvyBoMSzUMacb-T34QK6DjwmfeaY9u.ttf",
  "500": "http://fonts.gstatic.com/s/notosansethiopic/v38/7cHPv50vjIepfJVOZZgcpQ5B9FBTH9KGNfhSTgtoow1KVnIvyBoMSzUMacb-T358K6DjwmfeaY9u.ttf",
  "600": "http://fonts.gstatic.com/s/notosansethiopic/v38/7cHPv50vjIepfJVOZZgcpQ5B9FBTH9KGNfhSTgtoow1KVnIvyBoMSzUMacb-T36QLKDjwmfeaY9u.ttf",
  "700": "http://fonts.gstatic.com/s/notosansethiopic/v38/7cHPv50vjIepfJVOZZgcpQ5B9FBTH9KGNfhSTgtoow1KVnIvyBoMSzUMacb-T36pLKDjwmfeaY9u.ttf",
  "800": "http://fonts.gstatic.com/s/notosansethiopic/v38/7cHPv50vjIepfJVOZZgcpQ5B9FBTH9KGNfhSTgtoow1KVnIvyBoMSzUMacb-T37OLKDjwmfeaY9u.ttf",
  "900": "http://fonts.gstatic.com/s/notosansethiopic/v38/7cHPv50vjIepfJVOZZgcpQ5B9FBTH9KGNfhSTgtoow1KVnIvyBoMSzUMacb-T37nLKDjwmfeaY9u.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansethiopic/v38/7cHPv50vjIepfJVOZZgcpQ5B9FBTH9KGNfhSTgtoow1KVnIvyBoMSzUMacb-T35OK6DjwmfeaY9u.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Georgian",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "georgian",
  "latin",
  "latin-ext"
  ],
  "version": "v36",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansgeorgian/v36/PlIaFke5O6RzLfvNNVSitxkr76PRHBC4Ytyq-Gof7PUs4S7zWn-8YDB09HFNdpvnzVj-f5WK0OQV.ttf",
  "200": "http://fonts.gstatic.com/s/notosansgeorgian/v36/PlIaFke5O6RzLfvNNVSitxkr76PRHBC4Ytyq-Gof7PUs4S7zWn-8YDB09HFNdptnzFj-f5WK0OQV.ttf",
  "300": "http://fonts.gstatic.com/s/notosansgeorgian/v36/PlIaFke5O6RzLfvNNVSitxkr76PRHBC4Ytyq-Gof7PUs4S7zWn-8YDB09HFNdpu5zFj-f5WK0OQV.ttf",
  "500": "http://fonts.gstatic.com/s/notosansgeorgian/v36/PlIaFke5O6RzLfvNNVSitxkr76PRHBC4Ytyq-Gof7PUs4S7zWn-8YDB09HFNdpvVzFj-f5WK0OQV.ttf",
  "600": "http://fonts.gstatic.com/s/notosansgeorgian/v36/PlIaFke5O6RzLfvNNVSitxkr76PRHBC4Ytyq-Gof7PUs4S7zWn-8YDB09HFNdps5y1j-f5WK0OQV.ttf",
  "700": "http://fonts.gstatic.com/s/notosansgeorgian/v36/PlIaFke5O6RzLfvNNVSitxkr76PRHBC4Ytyq-Gof7PUs4S7zWn-8YDB09HFNdpsAy1j-f5WK0OQV.ttf",
  "800": "http://fonts.gstatic.com/s/notosansgeorgian/v36/PlIaFke5O6RzLfvNNVSitxkr76PRHBC4Ytyq-Gof7PUs4S7zWn-8YDB09HFNdptny1j-f5WK0OQV.ttf",
  "900": "http://fonts.gstatic.com/s/notosansgeorgian/v36/PlIaFke5O6RzLfvNNVSitxkr76PRHBC4Ytyq-Gof7PUs4S7zWn-8YDB09HFNdptOy1j-f5WK0OQV.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansgeorgian/v36/PlIaFke5O6RzLfvNNVSitxkr76PRHBC4Ytyq-Gof7PUs4S7zWn-8YDB09HFNdpvnzFj-f5WK0OQV.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Glagolitic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "glagolitic"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansglagolitic/v15/1q2ZY4-BBFBst88SU_tOj4J-4yuNF_HI4ERK4Amu7nM1.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Gothic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "gothic"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansgothic/v15/TuGKUUVzXI5FBtUq5a8bj6wRbzxTFMX40kFQRx0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Grantha",
  "variants": [
  "regular"
  ],
  "subsets": [
  "grantha",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansgrantha/v17/3y976akwcCjmsU8NDyrKo3IQfQ4o-r8cFeulHc6N.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Gujarati",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansgujarati/v19/wlpWgx_HC1ti5ViekvcxnhMlCVo3f5pv17ivlzsUB14gg1TMR2Gw4VceEl7MA_ypFgPM_OdiEH0s.ttf",
  "200": "http://fonts.gstatic.com/s/notosansgujarati/v19/wlpWgx_HC1ti5ViekvcxnhMlCVo3f5pv17ivlzsUB14gg1TMR2Gw4VceEl7MA_wpFwPM_OdiEH0s.ttf",
  "300": "http://fonts.gstatic.com/s/notosansgujarati/v19/wlpWgx_HC1ti5ViekvcxnhMlCVo3f5pv17ivlzsUB14gg1TMR2Gw4VceEl7MA_z3FwPM_OdiEH0s.ttf",
  "500": "http://fonts.gstatic.com/s/notosansgujarati/v19/wlpWgx_HC1ti5ViekvcxnhMlCVo3f5pv17ivlzsUB14gg1TMR2Gw4VceEl7MA_ybFwPM_OdiEH0s.ttf",
  "600": "http://fonts.gstatic.com/s/notosansgujarati/v19/wlpWgx_HC1ti5ViekvcxnhMlCVo3f5pv17ivlzsUB14gg1TMR2Gw4VceEl7MA_x3EAPM_OdiEH0s.ttf",
  "700": "http://fonts.gstatic.com/s/notosansgujarati/v19/wlpWgx_HC1ti5ViekvcxnhMlCVo3f5pv17ivlzsUB14gg1TMR2Gw4VceEl7MA_xOEAPM_OdiEH0s.ttf",
  "800": "http://fonts.gstatic.com/s/notosansgujarati/v19/wlpWgx_HC1ti5ViekvcxnhMlCVo3f5pv17ivlzsUB14gg1TMR2Gw4VceEl7MA_wpEAPM_OdiEH0s.ttf",
  "900": "http://fonts.gstatic.com/s/notosansgujarati/v19/wlpWgx_HC1ti5ViekvcxnhMlCVo3f5pv17ivlzsUB14gg1TMR2Gw4VceEl7MA_wAEAPM_OdiEH0s.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansgujarati/v19/wlpWgx_HC1ti5ViekvcxnhMlCVo3f5pv17ivlzsUB14gg1TMR2Gw4VceEl7MA_ypFwPM_OdiEH0s.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Gunjala Gondi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "gunjala-gondi"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansgunjalagondi/v15/bWto7e7KfBziStx7lIzKPrcSMwcEnCv6DW7n5hcVXYMTK4q1.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Gurmukhi",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "gurmukhi",
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansgurmukhi/v20/w8g9H3EvQP81sInb43inmyN9zZ7hb7ATbSWo4q8dJ74a3cVrYFQ_bogT0-gPeG1Oe3bxZ_trdp7h.ttf",
  "200": "http://fonts.gstatic.com/s/notosansgurmukhi/v20/w8g9H3EvQP81sInb43inmyN9zZ7hb7ATbSWo4q8dJ74a3cVrYFQ_bogT0-gPeG3OenbxZ_trdp7h.ttf",
  "300": "http://fonts.gstatic.com/s/notosansgurmukhi/v20/w8g9H3EvQP81sInb43inmyN9zZ7hb7ATbSWo4q8dJ74a3cVrYFQ_bogT0-gPeG0QenbxZ_trdp7h.ttf",
  "500": "http://fonts.gstatic.com/s/notosansgurmukhi/v20/w8g9H3EvQP81sInb43inmyN9zZ7hb7ATbSWo4q8dJ74a3cVrYFQ_bogT0-gPeG18enbxZ_trdp7h.ttf",
  "600": "http://fonts.gstatic.com/s/notosansgurmukhi/v20/w8g9H3EvQP81sInb43inmyN9zZ7hb7ATbSWo4q8dJ74a3cVrYFQ_bogT0-gPeG2QfXbxZ_trdp7h.ttf",
  "700": "http://fonts.gstatic.com/s/notosansgurmukhi/v20/w8g9H3EvQP81sInb43inmyN9zZ7hb7ATbSWo4q8dJ74a3cVrYFQ_bogT0-gPeG2pfXbxZ_trdp7h.ttf",
  "800": "http://fonts.gstatic.com/s/notosansgurmukhi/v20/w8g9H3EvQP81sInb43inmyN9zZ7hb7ATbSWo4q8dJ74a3cVrYFQ_bogT0-gPeG3OfXbxZ_trdp7h.ttf",
  "900": "http://fonts.gstatic.com/s/notosansgurmukhi/v20/w8g9H3EvQP81sInb43inmyN9zZ7hb7ATbSWo4q8dJ74a3cVrYFQ_bogT0-gPeG3nfXbxZ_trdp7h.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansgurmukhi/v20/w8g9H3EvQP81sInb43inmyN9zZ7hb7ATbSWo4q8dJ74a3cVrYFQ_bogT0-gPeG1OenbxZ_trdp7h.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans HK",
  "variants": [
  "100",
  "300",
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "chinese-hongkong",
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanshk/v21/nKKO-GM_FYFRJvXzVXaAPe9ZUHp1MOv2ObB7.otf",
  "300": "http://fonts.gstatic.com/s/notosanshk/v21/nKKP-GM_FYFRJvXzVXaAPe9ZmFhTHMX6MKliqQ.otf",
  "500": "http://fonts.gstatic.com/s/notosanshk/v21/nKKP-GM_FYFRJvXzVXaAPe9ZwFlTHMX6MKliqQ.otf",
  "700": "http://fonts.gstatic.com/s/notosanshk/v21/nKKP-GM_FYFRJvXzVXaAPe9ZiF9THMX6MKliqQ.otf",
  "900": "http://fonts.gstatic.com/s/notosanshk/v21/nKKP-GM_FYFRJvXzVXaAPe9ZsF1THMX6MKliqQ.otf",
  "regular": "http://fonts.gstatic.com/s/notosanshk/v21/nKKQ-GM_FYFRJvXzVXaAPe9hMnB3Eu7mOQ.otf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Hanifi Rohingya",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "hanifi-rohingya"
  ],
  "version": "v18",
  "lastModified": "2022-06-01",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosanshanifirohingya/v18/5h17iYsoOmIC3Yu3MDXLDw3UZCgghyOEBBY7hhLNyo3tiaiuSIAqrIYq4j6vvcudK8rN.ttf",
  "600": "http://fonts.gstatic.com/s/notosanshanifirohingya/v18/5h17iYsoOmIC3Yu3MDXLDw3UZCgghyOEBBY7hhLNyo3tiaiuSIAqrIbG5T6vvcudK8rN.ttf",
  "700": "http://fonts.gstatic.com/s/notosanshanifirohingya/v18/5h17iYsoOmIC3Yu3MDXLDw3UZCgghyOEBBY7hhLNyo3tiaiuSIAqrIb_5T6vvcudK8rN.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanshanifirohingya/v18/5h17iYsoOmIC3Yu3MDXLDw3UZCgghyOEBBY7hhLNyo3tiaiuSIAqrIYY4j6vvcudK8rN.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Hanunoo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "hanunoo"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanshanunoo/v15/f0Xs0fCv8dxkDWlZSoXOj6CphMloFsEsEpgL_ix2.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Hatran",
  "variants": [
  "regular"
  ],
  "subsets": [
  "hatran"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanshatran/v15/A2BBn4Ne0RgnVF3Lnko-0sOBIfL_mM83r1nwzDs.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Hebrew",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v38",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanshebrew/v38/or3HQ7v33eiDljA1IufXTtVf7V6RvEEdhQlk0LlGxCyaeNKYZC0sqk3xXGiXd4utoiJltutR2g.ttf",
  "200": "http://fonts.gstatic.com/s/notosanshebrew/v38/or3HQ7v33eiDljA1IufXTtVf7V6RvEEdhQlk0LlGxCyaeNKYZC0sqk3xXGiX94qtoiJltutR2g.ttf",
  "300": "http://fonts.gstatic.com/s/notosanshebrew/v38/or3HQ7v33eiDljA1IufXTtVf7V6RvEEdhQlk0LlGxCyaeNKYZC0sqk3xXGiXKYqtoiJltutR2g.ttf",
  "500": "http://fonts.gstatic.com/s/notosanshebrew/v38/or3HQ7v33eiDljA1IufXTtVf7V6RvEEdhQlk0LlGxCyaeNKYZC0sqk3xXGiXRYqtoiJltutR2g.ttf",
  "600": "http://fonts.gstatic.com/s/notosanshebrew/v38/or3HQ7v33eiDljA1IufXTtVf7V6RvEEdhQlk0LlGxCyaeNKYZC0sqk3xXGiXqY2toiJltutR2g.ttf",
  "700": "http://fonts.gstatic.com/s/notosanshebrew/v38/or3HQ7v33eiDljA1IufXTtVf7V6RvEEdhQlk0LlGxCyaeNKYZC0sqk3xXGiXkI2toiJltutR2g.ttf",
  "800": "http://fonts.gstatic.com/s/notosanshebrew/v38/or3HQ7v33eiDljA1IufXTtVf7V6RvEEdhQlk0LlGxCyaeNKYZC0sqk3xXGiX942toiJltutR2g.ttf",
  "900": "http://fonts.gstatic.com/s/notosanshebrew/v38/or3HQ7v33eiDljA1IufXTtVf7V6RvEEdhQlk0LlGxCyaeNKYZC0sqk3xXGiX3o2toiJltutR2g.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanshebrew/v38/or3HQ7v33eiDljA1IufXTtVf7V6RvEEdhQlk0LlGxCyaeNKYZC0sqk3xXGiXd4qtoiJltutR2g.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Imperial Aramaic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "imperial-aramaic"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansimperialaramaic/v15/a8IMNpjwKmHXpgXbMIsbTc_kvks91LlLetBr5itQrtdml3YfPNno.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Indic Siyaq Numbers",
  "variants": [
  "regular"
  ],
  "subsets": [
  "indic-siyaq-numbers"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansindicsiyaqnumbers/v15/6xK5dTJFKcWIu4bpRBjRZRpsIYHabOeZ8UZLubTzpXNHKx2WPOpVd5Iu.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Inscriptional Pahlavi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "inscriptional-pahlavi"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansinscriptionalpahlavi/v15/ll8UK3GaVDuxR-TEqFPIbsR79Xxz9WEKbwsjpz7VklYlC7FCVtqVOAYK0QA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Inscriptional Parthian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "inscriptional-parthian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansinscriptionalparthian/v15/k3k7o-IMPvpLmixcA63oYi-yStDkgXuXncL7dzfW3P4TAJ2yklBJ2jNkLlLr.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans JP",
  "variants": [
  "100",
  "300",
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "japanese",
  "latin"
  ],
  "version": "v42",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansjp/v42/-F6ofjtqLzI2JPCgQBnw7HFQoggM-FNthvIU.otf",
  "300": "http://fonts.gstatic.com/s/notosansjp/v42/-F6pfjtqLzI2JPCgQBnw7HFQaioq1H1hj-sNFQ.otf",
  "500": "http://fonts.gstatic.com/s/notosansjp/v42/-F6pfjtqLzI2JPCgQBnw7HFQMisq1H1hj-sNFQ.otf",
  "700": "http://fonts.gstatic.com/s/notosansjp/v42/-F6pfjtqLzI2JPCgQBnw7HFQei0q1H1hj-sNFQ.otf",
  "900": "http://fonts.gstatic.com/s/notosansjp/v42/-F6pfjtqLzI2JPCgQBnw7HFQQi8q1H1hj-sNFQ.otf",
  "regular": "http://fonts.gstatic.com/s/notosansjp/v42/-F62fjtqLzI2JPCgQBnw7HFowAIO2lZ9hg.otf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Javanese",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "javanese",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-28",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosansjavanese/v19/2V01KJkDAIA6Hp4zoSScDjV0Y-eoHAHT-Z3MngEefiidxKvkFFliZYWj4O8.ttf",
  "600": "http://fonts.gstatic.com/s/notosansjavanese/v19/2V01KJkDAIA6Hp4zoSScDjV0Y-eoHAHT-Z3MngEefiidxEfjFFliZYWj4O8.ttf",
  "700": "http://fonts.gstatic.com/s/notosansjavanese/v19/2V01KJkDAIA6Hp4zoSScDjV0Y-eoHAHT-Z3MngEefiidxH7jFFliZYWj4O8.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansjavanese/v19/2V01KJkDAIA6Hp4zoSScDjV0Y-eoHAHT-Z3MngEefiidxJnkFFliZYWj4O8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans KR",
  "variants": [
  "100",
  "300",
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v27",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanskr/v27/Pby6FmXiEBPT4ITbgNA5CgmOsn7uwpYcuH8y.otf",
  "300": "http://fonts.gstatic.com/s/notosanskr/v27/Pby7FmXiEBPT4ITbgNA5CgmOelzI7rgQsWYrzw.otf",
  "500": "http://fonts.gstatic.com/s/notosanskr/v27/Pby7FmXiEBPT4ITbgNA5CgmOIl3I7rgQsWYrzw.otf",
  "700": "http://fonts.gstatic.com/s/notosanskr/v27/Pby7FmXiEBPT4ITbgNA5CgmOalvI7rgQsWYrzw.otf",
  "900": "http://fonts.gstatic.com/s/notosanskr/v27/Pby7FmXiEBPT4ITbgNA5CgmOUlnI7rgQsWYrzw.otf",
  "regular": "http://fonts.gstatic.com/s/notosanskr/v27/PbykFmXiEBPT4ITbgNA5Cgm20HTs4JMMuA.otf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Kaithi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "kaithi"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanskaithi/v15/buEtppS9f8_vkXadMBJJu0tWjLwjQi0KdoZIKlo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Kannada",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "kannada",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanskannada/v21/8vIs7xs32H97qzQKnzfeXycxXZyUmySvZWItmf1fe6TVmgop9ndpS-BqHEyGrDvMzSIMLsPKrkY.ttf",
  "200": "http://fonts.gstatic.com/s/notosanskannada/v21/8vIs7xs32H97qzQKnzfeXycxXZyUmySvZWItmf1fe6TVmgop9ndpS-BqHEyGrLvNzSIMLsPKrkY.ttf",
  "300": "http://fonts.gstatic.com/s/notosanskannada/v21/8vIs7xs32H97qzQKnzfeXycxXZyUmySvZWItmf1fe6TVmgop9ndpS-BqHEyGrGXNzSIMLsPKrkY.ttf",
  "500": "http://fonts.gstatic.com/s/notosanskannada/v21/8vIs7xs32H97qzQKnzfeXycxXZyUmySvZWItmf1fe6TVmgop9ndpS-BqHEyGrAnNzSIMLsPKrkY.ttf",
  "600": "http://fonts.gstatic.com/s/notosanskannada/v21/8vIs7xs32H97qzQKnzfeXycxXZyUmySvZWItmf1fe6TVmgop9ndpS-BqHEyGrOXKzSIMLsPKrkY.ttf",
  "700": "http://fonts.gstatic.com/s/notosanskannada/v21/8vIs7xs32H97qzQKnzfeXycxXZyUmySvZWItmf1fe6TVmgop9ndpS-BqHEyGrNzKzSIMLsPKrkY.ttf",
  "800": "http://fonts.gstatic.com/s/notosanskannada/v21/8vIs7xs32H97qzQKnzfeXycxXZyUmySvZWItmf1fe6TVmgop9ndpS-BqHEyGrLvKzSIMLsPKrkY.ttf",
  "900": "http://fonts.gstatic.com/s/notosanskannada/v21/8vIs7xs32H97qzQKnzfeXycxXZyUmySvZWItmf1fe6TVmgop9ndpS-BqHEyGrJLKzSIMLsPKrkY.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanskannada/v21/8vIs7xs32H97qzQKnzfeXycxXZyUmySvZWItmf1fe6TVmgop9ndpS-BqHEyGrDvNzSIMLsPKrkY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Kayah Li",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "kayah-li"
  ],
  "version": "v18",
  "lastModified": "2022-06-01",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosanskayahli/v18/B50nF61OpWTRcGrhOVJJwOMXdca6Yecki3E06x2jVTX3WBU3CZH4EXLuKVM.ttf",
  "600": "http://fonts.gstatic.com/s/notosanskayahli/v18/B50nF61OpWTRcGrhOVJJwOMXdca6Yecki3E06x2jVTX3WPkwCZH4EXLuKVM.ttf",
  "700": "http://fonts.gstatic.com/s/notosanskayahli/v18/B50nF61OpWTRcGrhOVJJwOMXdca6Yecki3E06x2jVTX3WMAwCZH4EXLuKVM.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanskayahli/v18/B50nF61OpWTRcGrhOVJJwOMXdca6Yecki3E06x2jVTX3WCc3CZH4EXLuKVM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Kharoshthi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "kharoshthi"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanskharoshthi/v15/Fh4qPiLjKS30-P4-pGMMXCCfvkc5Vd7KE5z4rFyx5mR1.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Khmer",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "khmer",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanskhmer/v18/ijw3s5roRME5LLRxjsRb-gssOenAyendxrgV2c-Zw-9vbVUti_Z_dWgtWYuNAZz4kAbrddiA.ttf",
  "200": "http://fonts.gstatic.com/s/notosanskhmer/v18/ijw3s5roRME5LLRxjsRb-gssOenAyendxrgV2c-Zw-9vbVUti_Z_dWgtWYsNAJz4kAbrddiA.ttf",
  "300": "http://fonts.gstatic.com/s/notosanskhmer/v18/ijw3s5roRME5LLRxjsRb-gssOenAyendxrgV2c-Zw-9vbVUti_Z_dWgtWYvTAJz4kAbrddiA.ttf",
  "500": "http://fonts.gstatic.com/s/notosanskhmer/v18/ijw3s5roRME5LLRxjsRb-gssOenAyendxrgV2c-Zw-9vbVUti_Z_dWgtWYu_AJz4kAbrddiA.ttf",
  "600": "http://fonts.gstatic.com/s/notosanskhmer/v18/ijw3s5roRME5LLRxjsRb-gssOenAyendxrgV2c-Zw-9vbVUti_Z_dWgtWYtTB5z4kAbrddiA.ttf",
  "700": "http://fonts.gstatic.com/s/notosanskhmer/v18/ijw3s5roRME5LLRxjsRb-gssOenAyendxrgV2c-Zw-9vbVUti_Z_dWgtWYtqB5z4kAbrddiA.ttf",
  "800": "http://fonts.gstatic.com/s/notosanskhmer/v18/ijw3s5roRME5LLRxjsRb-gssOenAyendxrgV2c-Zw-9vbVUti_Z_dWgtWYsNB5z4kAbrddiA.ttf",
  "900": "http://fonts.gstatic.com/s/notosanskhmer/v18/ijw3s5roRME5LLRxjsRb-gssOenAyendxrgV2c-Zw-9vbVUti_Z_dWgtWYskB5z4kAbrddiA.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanskhmer/v18/ijw3s5roRME5LLRxjsRb-gssOenAyendxrgV2c-Zw-9vbVUti_Z_dWgtWYuNAJz4kAbrddiA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Khojki",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khojki"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanskhojki/v15/-nFnOHM29Oofr2wohFbTuPPKVWpmK_d709jy92k.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Khudawadi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khudawadi"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanskhudawadi/v15/fdNi9t6ZsWBZ2k5ltHN73zZ5hc8HANlHIjRnVVXz9MY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Lao",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "lao",
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanslao/v24/bx6lNx2Ol_ixgdYWLm9BwxM3NW6BOkuf763Clj73CiQ_J1Djx9pidOt4ccfdf5MK3riB2w.ttf",
  "200": "http://fonts.gstatic.com/s/notosanslao/v24/bx6lNx2Ol_ixgdYWLm9BwxM3NW6BOkuf763Clj73CiQ_J1Djx9pidOt48cbdf5MK3riB2w.ttf",
  "300": "http://fonts.gstatic.com/s/notosanslao/v24/bx6lNx2Ol_ixgdYWLm9BwxM3NW6BOkuf763Clj73CiQ_J1Djx9pidOt4L8bdf5MK3riB2w.ttf",
  "500": "http://fonts.gstatic.com/s/notosanslao/v24/bx6lNx2Ol_ixgdYWLm9BwxM3NW6BOkuf763Clj73CiQ_J1Djx9pidOt4Q8bdf5MK3riB2w.ttf",
  "600": "http://fonts.gstatic.com/s/notosanslao/v24/bx6lNx2Ol_ixgdYWLm9BwxM3NW6BOkuf763Clj73CiQ_J1Djx9pidOt4r8Hdf5MK3riB2w.ttf",
  "700": "http://fonts.gstatic.com/s/notosanslao/v24/bx6lNx2Ol_ixgdYWLm9BwxM3NW6BOkuf763Clj73CiQ_J1Djx9pidOt4lsHdf5MK3riB2w.ttf",
  "800": "http://fonts.gstatic.com/s/notosanslao/v24/bx6lNx2Ol_ixgdYWLm9BwxM3NW6BOkuf763Clj73CiQ_J1Djx9pidOt48cHdf5MK3riB2w.ttf",
  "900": "http://fonts.gstatic.com/s/notosanslao/v24/bx6lNx2Ol_ixgdYWLm9BwxM3NW6BOkuf763Clj73CiQ_J1Djx9pidOt42MHdf5MK3riB2w.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanslao/v24/bx6lNx2Ol_ixgdYWLm9BwxM3NW6BOkuf763Clj73CiQ_J1Djx9pidOt4ccbdf5MK3riB2w.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Lepcha",
  "variants": [
  "regular"
  ],
  "subsets": [
  "lepcha"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanslepcha/v15/0QI7MWlB_JWgA166SKhu05TekNS32AJstqBXgd4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Limbu",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "limbu"
  ],
  "version": "v17",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanslimbu/v17/3JnlSDv90Gmq2mrzckOBBRRoNJVj0MF3OHRDnA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Linear A",
  "variants": [
  "regular"
  ],
  "subsets": [
  "linear-a"
  ],
  "version": "v16",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanslineara/v16/oPWS_l16kP4jCuhpgEGmwJOiA18FZj22zmHQAGQicw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Linear B",
  "variants": [
  "regular"
  ],
  "subsets": [
  "linear-b"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanslinearb/v15/HhyJU4wt9vSgfHoORYOiXOckKNB737IV3BkFTq4EPw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Lisu",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "lisu"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosanslisu/v21/uk-3EGO3o6EruUbnwovcYhz6kh57_nqbcTdjJnHP61wt29IlxkVdig.ttf",
  "600": "http://fonts.gstatic.com/s/notosanslisu/v21/uk-3EGO3o6EruUbnwovcYhz6kh57_nqbcTdjJnHPB1st29IlxkVdig.ttf",
  "700": "http://fonts.gstatic.com/s/notosanslisu/v21/uk-3EGO3o6EruUbnwovcYhz6kh57_nqbcTdjJnHPPlst29IlxkVdig.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanslisu/v21/uk-3EGO3o6EruUbnwovcYhz6kh57_nqbcTdjJnHP2Vwt29IlxkVdig.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Lycian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "lycian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanslycian/v15/QldVNSNMqAsHtsJ7UmqxBQA9r8wA5_naCJwn00E.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Lydian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "lydian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanslydian/v15/c4m71mVzGN7s8FmIukZJ1v4ZlcPReUPXMoIjEQI.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Mahajani",
  "variants": [
  "regular"
  ],
  "subsets": [
  "mahajani"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmahajani/v15/-F6sfiVqLzI2JPCgQBnw60Agp0JrvD5Fh8ARHNh4zg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Malayalam",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "malayalam"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansmalayalam/v21/sJoi3K5XjsSdcnzn071rL37lpAOsUThnDZIfPdbeSNzVakglNM-Qw8EaeB8Nss-_RuH9BFzEr6HxEA.ttf",
  "200": "http://fonts.gstatic.com/s/notosansmalayalam/v21/sJoi3K5XjsSdcnzn071rL37lpAOsUThnDZIfPdbeSNzVakglNM-Qw8EaeB8Nss-_xuD9BFzEr6HxEA.ttf",
  "300": "http://fonts.gstatic.com/s/notosansmalayalam/v21/sJoi3K5XjsSdcnzn071rL37lpAOsUThnDZIfPdbeSNzVakglNM-Qw8EaeB8Nss-_GOD9BFzEr6HxEA.ttf",
  "500": "http://fonts.gstatic.com/s/notosansmalayalam/v21/sJoi3K5XjsSdcnzn071rL37lpAOsUThnDZIfPdbeSNzVakglNM-Qw8EaeB8Nss-_dOD9BFzEr6HxEA.ttf",
  "600": "http://fonts.gstatic.com/s/notosansmalayalam/v21/sJoi3K5XjsSdcnzn071rL37lpAOsUThnDZIfPdbeSNzVakglNM-Qw8EaeB8Nss-_mOf9BFzEr6HxEA.ttf",
  "700": "http://fonts.gstatic.com/s/notosansmalayalam/v21/sJoi3K5XjsSdcnzn071rL37lpAOsUThnDZIfPdbeSNzVakglNM-Qw8EaeB8Nss-_oef9BFzEr6HxEA.ttf",
  "800": "http://fonts.gstatic.com/s/notosansmalayalam/v21/sJoi3K5XjsSdcnzn071rL37lpAOsUThnDZIfPdbeSNzVakglNM-Qw8EaeB8Nss-_xuf9BFzEr6HxEA.ttf",
  "900": "http://fonts.gstatic.com/s/notosansmalayalam/v21/sJoi3K5XjsSdcnzn071rL37lpAOsUThnDZIfPdbeSNzVakglNM-Qw8EaeB8Nss-_7-f9BFzEr6HxEA.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansmalayalam/v21/sJoi3K5XjsSdcnzn071rL37lpAOsUThnDZIfPdbeSNzVakglNM-Qw8EaeB8Nss-_RuD9BFzEr6HxEA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Mandaic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "mandaic"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmandaic/v15/cIfnMbdWt1w_HgCcilqhKQBo_OsMI5_A_gMk0izH.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Manichaean",
  "variants": [
  "regular"
  ],
  "subsets": [
  "manichaean"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmanichaean/v15/taiVGntiC4--qtsfi4Jp9-_GkPZZCcrfekqCNTtFCtdX.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Marchen",
  "variants": [
  "regular"
  ],
  "subsets": [
  "marchen"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmarchen/v15/aFTO7OZ_Y282EP-WyG6QTOX_C8WZMHhPk652ZaHk.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Masaram Gondi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "masaram-gondi"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmasaramgondi/v15/6xK_dThFKcWIu4bpRBjRYRV7KZCbUq6n_1kPnuGe7RI9WSWX.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Math",
  "variants": [
  "regular"
  ],
  "subsets": [
  "math"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmath/v15/7Aump_cpkSecTWaHRlH2hyV5UHkG-V048PW0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Mayan Numerals",
  "variants": [
  "regular"
  ],
  "subsets": [
  "mayan-numerals"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmayannumerals/v15/PlIuFk25O6RzLfvNNVSivR09_KqYMwvvDKYjfIiE68oo6eepYQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Medefaidrin",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "medefaidrin"
  ],
  "version": "v19",
  "lastModified": "2022-06-01",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosansmedefaidrin/v19/WwkzxOq6Dk-wranENynkfeVsNbRZtbOIdLb1exeM4ZeuabBfmHjWlT318e5A3rw.ttf",
  "600": "http://fonts.gstatic.com/s/notosansmedefaidrin/v19/WwkzxOq6Dk-wranENynkfeVsNbRZtbOIdLb1exeM4ZeuabBfmJTRlT318e5A3rw.ttf",
  "700": "http://fonts.gstatic.com/s/notosansmedefaidrin/v19/WwkzxOq6Dk-wranENynkfeVsNbRZtbOIdLb1exeM4ZeuabBfmK3RlT318e5A3rw.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansmedefaidrin/v19/WwkzxOq6Dk-wranENynkfeVsNbRZtbOIdLb1exeM4ZeuabBfmErWlT318e5A3rw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Meetei Mayek",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "meetei-mayek"
  ],
  "version": "v14",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansmeeteimayek/v14/HTxAL3QyKieByqY9eZPFweO0be7M21uSphSdhqILnmrRfJ8t_1TJ__TW5PgeFYVa.ttf",
  "200": "http://fonts.gstatic.com/s/notosansmeeteimayek/v14/HTxAL3QyKieByqY9eZPFweO0be7M21uSphSdhqILnmrRfJ8t_1RJ_vTW5PgeFYVa.ttf",
  "300": "http://fonts.gstatic.com/s/notosansmeeteimayek/v14/HTxAL3QyKieByqY9eZPFweO0be7M21uSphSdhqILnmrRfJ8t_1SX_vTW5PgeFYVa.ttf",
  "500": "http://fonts.gstatic.com/s/notosansmeeteimayek/v14/HTxAL3QyKieByqY9eZPFweO0be7M21uSphSdhqILnmrRfJ8t_1T7_vTW5PgeFYVa.ttf",
  "600": "http://fonts.gstatic.com/s/notosansmeeteimayek/v14/HTxAL3QyKieByqY9eZPFweO0be7M21uSphSdhqILnmrRfJ8t_1QX-fTW5PgeFYVa.ttf",
  "700": "http://fonts.gstatic.com/s/notosansmeeteimayek/v14/HTxAL3QyKieByqY9eZPFweO0be7M21uSphSdhqILnmrRfJ8t_1Qu-fTW5PgeFYVa.ttf",
  "800": "http://fonts.gstatic.com/s/notosansmeeteimayek/v14/HTxAL3QyKieByqY9eZPFweO0be7M21uSphSdhqILnmrRfJ8t_1RJ-fTW5PgeFYVa.ttf",
  "900": "http://fonts.gstatic.com/s/notosansmeeteimayek/v14/HTxAL3QyKieByqY9eZPFweO0be7M21uSphSdhqILnmrRfJ8t_1Rg-fTW5PgeFYVa.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansmeeteimayek/v14/HTxAL3QyKieByqY9eZPFweO0be7M21uSphSdhqILnmrRfJ8t_1TJ_vTW5PgeFYVa.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Meroitic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "meroitic"
  ],
  "version": "v16",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmeroitic/v16/IFS5HfRJndhE3P4b5jnZ3ITPvC6i00UDgDhTiKY9KQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Miao",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "miao"
  ],
  "version": "v17",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmiao/v17/Dxxz8jmXMW75w3OmoDXVV4zyZUjgUYVslLhx.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Modi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "modi"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmodi/v15/pe03MIySN5pO62Z5YkFyT7jeav5qWVAgVol-.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Mongolian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "mongolian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmongolian/v15/VdGCAYADGIwE0EopZx8xQfHlgEAMsrToxLsg6-av1x0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Mono",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansmono/v21/BngrUXNETWXI6LwhGYvaxZikqZqK6fBq6kPvUce2oAZcdthSBUsYck4-_FNI49rXVEQQL8Y.ttf",
  "200": "http://fonts.gstatic.com/s/notosansmono/v21/BngrUXNETWXI6LwhGYvaxZikqZqK6fBq6kPvUce2oAZcdthSBUsYck4-_NNJ49rXVEQQL8Y.ttf",
  "300": "http://fonts.gstatic.com/s/notosansmono/v21/BngrUXNETWXI6LwhGYvaxZikqZqK6fBq6kPvUce2oAZcdthSBUsYck4-_A1J49rXVEQQL8Y.ttf",
  "500": "http://fonts.gstatic.com/s/notosansmono/v21/BngrUXNETWXI6LwhGYvaxZikqZqK6fBq6kPvUce2oAZcdthSBUsYck4-_GFJ49rXVEQQL8Y.ttf",
  "600": "http://fonts.gstatic.com/s/notosansmono/v21/BngrUXNETWXI6LwhGYvaxZikqZqK6fBq6kPvUce2oAZcdthSBUsYck4-_I1O49rXVEQQL8Y.ttf",
  "700": "http://fonts.gstatic.com/s/notosansmono/v21/BngrUXNETWXI6LwhGYvaxZikqZqK6fBq6kPvUce2oAZcdthSBUsYck4-_LRO49rXVEQQL8Y.ttf",
  "800": "http://fonts.gstatic.com/s/notosansmono/v21/BngrUXNETWXI6LwhGYvaxZikqZqK6fBq6kPvUce2oAZcdthSBUsYck4-_NNO49rXVEQQL8Y.ttf",
  "900": "http://fonts.gstatic.com/s/notosansmono/v21/BngrUXNETWXI6LwhGYvaxZikqZqK6fBq6kPvUce2oAZcdthSBUsYck4-_PpO49rXVEQQL8Y.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansmono/v21/BngrUXNETWXI6LwhGYvaxZikqZqK6fBq6kPvUce2oAZcdthSBUsYck4-_FNJ49rXVEQQL8Y.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Mro",
  "variants": [
  "regular"
  ],
  "subsets": [
  "mro"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmro/v15/qWcsB6--pZv9TqnUQMhe9b39WDzRtjkho4M.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Multani",
  "variants": [
  "regular"
  ],
  "subsets": [
  "multani"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansmultani/v15/9Bty3ClF38_RfOpe1gCaZ8p30BOFO1A0pfCs5Kos.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Myanmar",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "myanmar"
  ],
  "version": "v20",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansmyanmar/v20/AlZs_y1ZtY3ymOryg38hOCSdOnFq0HGS1uEapkAC3AY.ttf",
  "200": "http://fonts.gstatic.com/s/notosansmyanmar/v20/AlZv_y1ZtY3ymOryg38hOCSdOnFq0HE-98EwiEwLxR-r.ttf",
  "300": "http://fonts.gstatic.com/s/notosansmyanmar/v20/AlZv_y1ZtY3ymOryg38hOCSdOnFq0HFa9MEwiEwLxR-r.ttf",
  "500": "http://fonts.gstatic.com/s/notosansmyanmar/v20/AlZv_y1ZtY3ymOryg38hOCSdOnFq0HEC9cEwiEwLxR-r.ttf",
  "600": "http://fonts.gstatic.com/s/notosansmyanmar/v20/AlZv_y1ZtY3ymOryg38hOCSdOnFq0HEu8sEwiEwLxR-r.ttf",
  "700": "http://fonts.gstatic.com/s/notosansmyanmar/v20/AlZv_y1ZtY3ymOryg38hOCSdOnFq0HFK88EwiEwLxR-r.ttf",
  "800": "http://fonts.gstatic.com/s/notosansmyanmar/v20/AlZv_y1ZtY3ymOryg38hOCSdOnFq0HFW8MEwiEwLxR-r.ttf",
  "900": "http://fonts.gstatic.com/s/notosansmyanmar/v20/AlZv_y1ZtY3ymOryg38hOCSdOnFq0HFy8cEwiEwLxR-r.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansmyanmar/v20/AlZq_y1ZtY3ymOryg38hOCSdOnFq0En23OU4o1AC.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans N Ko",
  "variants": [
  "regular"
  ],
  "subsets": [
  "nko"
  ],
  "version": "v17",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansnko/v17/6NUP8FqDKBaKKjnr6P8v-sxPpvVBVNmme3gf.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Nabataean",
  "variants": [
  "regular"
  ],
  "subsets": [
  "nabataean"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansnabataean/v15/IFS4HfVJndhE3P4b5jnZ34DfsjO330dNoBJ9hK8kMK4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans New Tai Lue",
  "variants": [
  "regular"
  ],
  "subsets": [
  "new-tai-lue"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansnewtailue/v15/H4c5BW-Pl9DZ0Xe_nHUapt7PovLXAhAnY7wwY55O4AS32A.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Newa",
  "variants": [
  "regular"
  ],
  "subsets": [
  "newa"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansnewa/v15/7r3fqXp6utEsO9pI4f8ok8sWg8n_qN4R5lNU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Nushu",
  "variants": [
  "regular"
  ],
  "subsets": [
  "nushu"
  ],
  "version": "v18",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansnushu/v18/rnCw-xRQ3B7652emAbAe_Ai1IYaFWFAMArZKqQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Ogham",
  "variants": [
  "regular"
  ],
  "subsets": [
  "ogham"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansogham/v15/kmKlZqk1GBDGN0mY6k5lmEmww4hrt5laQxcoCA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Ol Chiki",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "ol-chiki"
  ],
  "version": "v17",
  "lastModified": "2022-07-19",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosansolchiki/v17/N0b92TJNOPt-eHmFZCdQbrL32r-4CvhzDzRwlxOQYuVALVs267I6gVrz5gQ.ttf",
  "600": "http://fonts.gstatic.com/s/notosansolchiki/v17/N0b92TJNOPt-eHmFZCdQbrL32r-4CvhzDzRwlxOQYuVALbcx67I6gVrz5gQ.ttf",
  "700": "http://fonts.gstatic.com/s/notosansolchiki/v17/N0b92TJNOPt-eHmFZCdQbrL32r-4CvhzDzRwlxOQYuVALY4x67I6gVrz5gQ.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansolchiki/v17/N0b92TJNOPt-eHmFZCdQbrL32r-4CvhzDzRwlxOQYuVALWk267I6gVrz5gQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Old Hungarian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "old-hungarian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansoldhungarian/v15/E213_cD6hP3GwCJPEUssHEM0KqLaHJXg2PiIgRfjbg5nCYXt.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Old Italic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "old-italic"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansolditalic/v15/TuGOUUFzXI5FBtUq5a8bh68BJxxEVam7tWlRdRhtCC4d.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Old North Arabian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "old-north-arabian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansoldnortharabian/v15/esDF30BdNv-KYGGJpKGk2tNiMt7Jar6olZDyNdr81zBQmUo_xw4ABw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Old Permic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "old-permic"
  ],
  "version": "v16",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansoldpermic/v16/snf1s1q1-dF8pli1TesqcbUY4Mr-ElrwKLdXgv_dKYB5.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Old Persian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "old-persian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansoldpersian/v15/wEOjEAbNnc5caQTFG18FHrZr9Bp6-8CmIJ_tqOlQfx9CjA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Old Sogdian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "old-sogdian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansoldsogdian/v15/3JnjSCH90Gmq2mrzckOBBhFhdrMst48aURt7neIqM-9uyg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Old South Arabian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "old-south-arabian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansoldsoutharabian/v15/3qT5oiOhnSyU8TNFIdhZTice3hB_HWKsEnF--0XCHiKx1OtDT9HwTA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Old Turkic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "old-turkic"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansoldturkic/v15/yMJNMJVya43H0SUF_WmcGEQVqoEMKDKbsE2RjEw-Vyws.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Oriya",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "oriya"
  ],
  "version": "v19",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansoriya/v19/AYCppXfzfccDCstK_hrjDyADv5e9748vhj3CJBLHIARtgD6TJQS0dJT5Ivj0fq_c6LhHBRe-.ttf",
  "200": "http://fonts.gstatic.com/s/notosansoriya/v19/AYCppXfzfccDCstK_hrjDyADv5e9748vhj3CJBLHIARtgD6TJQS0dJT5Ivh0f6_c6LhHBRe-.ttf",
  "300": "http://fonts.gstatic.com/s/notosansoriya/v19/AYCppXfzfccDCstK_hrjDyADv5e9748vhj3CJBLHIARtgD6TJQS0dJT5Iviqf6_c6LhHBRe-.ttf",
  "500": "http://fonts.gstatic.com/s/notosansoriya/v19/AYCppXfzfccDCstK_hrjDyADv5e9748vhj3CJBLHIARtgD6TJQS0dJT5IvjGf6_c6LhHBRe-.ttf",
  "600": "http://fonts.gstatic.com/s/notosansoriya/v19/AYCppXfzfccDCstK_hrjDyADv5e9748vhj3CJBLHIARtgD6TJQS0dJT5IvgqeK_c6LhHBRe-.ttf",
  "700": "http://fonts.gstatic.com/s/notosansoriya/v19/AYCppXfzfccDCstK_hrjDyADv5e9748vhj3CJBLHIARtgD6TJQS0dJT5IvgTeK_c6LhHBRe-.ttf",
  "800": "http://fonts.gstatic.com/s/notosansoriya/v19/AYCppXfzfccDCstK_hrjDyADv5e9748vhj3CJBLHIARtgD6TJQS0dJT5Ivh0eK_c6LhHBRe-.ttf",
  "900": "http://fonts.gstatic.com/s/notosansoriya/v19/AYCppXfzfccDCstK_hrjDyADv5e9748vhj3CJBLHIARtgD6TJQS0dJT5IvhdeK_c6LhHBRe-.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansoriya/v19/AYCppXfzfccDCstK_hrjDyADv5e9748vhj3CJBLHIARtgD6TJQS0dJT5Ivj0f6_c6LhHBRe-.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Osage",
  "variants": [
  "regular"
  ],
  "subsets": [
  "osage"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansosage/v15/oPWX_kB6kP4jCuhpgEGmw4mtAVtXRlaSxkrMCQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Osmanya",
  "variants": [
  "regular"
  ],
  "subsets": [
  "osmanya"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansosmanya/v15/8vIS7xs32H97qzQKnzfeWzUyUpOJmz6kR47NCV5Z.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Pahawh Hmong",
  "variants": [
  "regular"
  ],
  "subsets": [
  "pahawh-hmong"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanspahawhhmong/v15/bWtp7e_KfBziStx7lIzKKaMUOBEA3UPQDW7krzc_c48aMpM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Palmyrene",
  "variants": [
  "regular"
  ],
  "subsets": [
  "palmyrene"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanspalmyrene/v15/ZgNPjOdKPa7CHqq0h37c_ASCWvH93SFCPnK5ZpdNtcA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Pau Cin Hau",
  "variants": [
  "regular"
  ],
  "subsets": [
  "pau-cin-hau"
  ],
  "version": "v16",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanspaucinhau/v16/x3d-cl3IZKmUqiMg_9wBLLtzl22EayN7ehIdjEWqKMxsKw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Phags Pa",
  "variants": [
  "regular"
  ],
  "subsets": [
  "phags-pa"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansphagspa/v15/pxiZyoo6v8ZYyWh5WuPeJzMkd4SrGChkqkSsrvNXiA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Phoenician",
  "variants": [
  "regular"
  ],
  "subsets": [
  "phoenician"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansphoenician/v15/jizFRF9Ksm4Bt9PvcTaEkIHiTVtxmFtS5X7Jot-p5561.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Psalter Pahlavi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "psalter-pahlavi"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanspsalterpahlavi/v15/rP2Vp3K65FkAtHfwd-eISGznYihzggmsicPfud3w1G3KsUQBct4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Rejang",
  "variants": [
  "regular"
  ],
  "subsets": [
  "rejang"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansrejang/v15/Ktk2AKuMeZjqPnXgyqrib7DIogqwN4O3WYZB_sU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Runic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "runic"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansrunic/v15/H4c_BXWPl9DZ0Xe_nHUaus7W68WWaxpvHtgIYg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans SC",
  "variants": [
  "100",
  "300",
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "chinese-simplified",
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanssc/v26/k3kJo84MPvpLmixcA63oeALZTYKL2wv287Sb.otf",
  "300": "http://fonts.gstatic.com/s/notosanssc/v26/k3kIo84MPvpLmixcA63oeALZhaCt9yX6-q2CGg.otf",
  "500": "http://fonts.gstatic.com/s/notosanssc/v26/k3kIo84MPvpLmixcA63oeALZ3aGt9yX6-q2CGg.otf",
  "700": "http://fonts.gstatic.com/s/notosanssc/v26/k3kIo84MPvpLmixcA63oeALZlaet9yX6-q2CGg.otf",
  "900": "http://fonts.gstatic.com/s/notosanssc/v26/k3kIo84MPvpLmixcA63oeALZraWt9yX6-q2CGg.otf",
  "regular": "http://fonts.gstatic.com/s/notosanssc/v26/k3kXo84MPvpLmixcA63oeALhL4iJ-Q7m8w.otf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Samaritan",
  "variants": [
  "regular"
  ],
  "subsets": [
  "samaritan"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanssamaritan/v15/buEqppe9f8_vkXadMBJJo0tSmaYjFkxOUo5jNlOVMzQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Saurashtra",
  "variants": [
  "regular"
  ],
  "subsets": [
  "saurashtra"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanssaurashtra/v15/ea8GacQ0Wfz_XKWXe6OtoA8w8zvmYwTef9ndjhPTSIx9.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Sharada",
  "variants": [
  "regular"
  ],
  "subsets": [
  "sharada"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanssharada/v15/gok0H7rwAEdtF9N8-mdTGALG6p0kwoXLPOwr4H8a.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Shavian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "shavian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansshavian/v15/CHy5V_HZE0jxJBQlqAeCKjJvQBNF4EFQSplv2Cwg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Siddham",
  "variants": [
  "regular"
  ],
  "subsets": [
  "siddham"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanssiddham/v15/OZpZg-FwqiNLe9PELUikxTWDoCCeGqndk3Ic92ZH.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Sinhala",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "sinhala"
  ],
  "version": "v26",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanssinhala/v26/yMJ2MJBya43H0SUF_WmcBEEf4rQVO2P524V5N_MxQzQtb-tf5dJbC30Fu9zUwg2b5lgLpJwbQRM.ttf",
  "200": "http://fonts.gstatic.com/s/notosanssinhala/v26/yMJ2MJBya43H0SUF_WmcBEEf4rQVO2P524V5N_MxQzQtb-tf5dJbC30Fu9zUwo2a5lgLpJwbQRM.ttf",
  "300": "http://fonts.gstatic.com/s/notosanssinhala/v26/yMJ2MJBya43H0SUF_WmcBEEf4rQVO2P524V5N_MxQzQtb-tf5dJbC30Fu9zUwlOa5lgLpJwbQRM.ttf",
  "500": "http://fonts.gstatic.com/s/notosanssinhala/v26/yMJ2MJBya43H0SUF_WmcBEEf4rQVO2P524V5N_MxQzQtb-tf5dJbC30Fu9zUwj-a5lgLpJwbQRM.ttf",
  "600": "http://fonts.gstatic.com/s/notosanssinhala/v26/yMJ2MJBya43H0SUF_WmcBEEf4rQVO2P524V5N_MxQzQtb-tf5dJbC30Fu9zUwtOd5lgLpJwbQRM.ttf",
  "700": "http://fonts.gstatic.com/s/notosanssinhala/v26/yMJ2MJBya43H0SUF_WmcBEEf4rQVO2P524V5N_MxQzQtb-tf5dJbC30Fu9zUwuqd5lgLpJwbQRM.ttf",
  "800": "http://fonts.gstatic.com/s/notosanssinhala/v26/yMJ2MJBya43H0SUF_WmcBEEf4rQVO2P524V5N_MxQzQtb-tf5dJbC30Fu9zUwo2d5lgLpJwbQRM.ttf",
  "900": "http://fonts.gstatic.com/s/notosanssinhala/v26/yMJ2MJBya43H0SUF_WmcBEEf4rQVO2P524V5N_MxQzQtb-tf5dJbC30Fu9zUwqSd5lgLpJwbQRM.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanssinhala/v26/yMJ2MJBya43H0SUF_WmcBEEf4rQVO2P524V5N_MxQzQtb-tf5dJbC30Fu9zUwg2a5lgLpJwbQRM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Sogdian",
  "variants": [
  "regular"
  ],
  "subsets": [
  "sogdian"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanssogdian/v15/taiQGn5iC4--qtsfi4Jp6eHPnfxQBo--Pm6KHidM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Sora Sompeng",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "sora-sompeng"
  ],
  "version": "v17",
  "lastModified": "2022-07-19",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosanssorasompeng/v17/PlIRFkO5O6RzLfvNNVSioxM2_OTrEhPyDLolKvCsHzCxWuGkYHRO18DpZXJQd4Mu.ttf",
  "600": "http://fonts.gstatic.com/s/notosanssorasompeng/v17/PlIRFkO5O6RzLfvNNVSioxM2_OTrEhPyDLolKvCsHzCxWuGkYHSi0MDpZXJQd4Mu.ttf",
  "700": "http://fonts.gstatic.com/s/notosanssorasompeng/v17/PlIRFkO5O6RzLfvNNVSioxM2_OTrEhPyDLolKvCsHzCxWuGkYHSb0MDpZXJQd4Mu.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanssorasompeng/v17/PlIRFkO5O6RzLfvNNVSioxM2_OTrEhPyDLolKvCsHzCxWuGkYHR818DpZXJQd4Mu.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Soyombo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "soyombo"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanssoyombo/v15/RWmSoL-Y6-8q5LTtXs6MF6q7xsxgY0FrIFOcK25W.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Sundanese",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "sundanese"
  ],
  "version": "v17",
  "lastModified": "2022-07-19",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosanssundanese/v17/FwZw7_84xUkosG2xJo2gm7nFwSLQkdymq2mkz3Gz1_b6ctxbNNHCizv7fQES.ttf",
  "600": "http://fonts.gstatic.com/s/notosanssundanese/v17/FwZw7_84xUkosG2xJo2gm7nFwSLQkdymq2mkz3Gz1_b6cty3M9HCizv7fQES.ttf",
  "700": "http://fonts.gstatic.com/s/notosanssundanese/v17/FwZw7_84xUkosG2xJo2gm7nFwSLQkdymq2mkz3Gz1_b6ctyOM9HCizv7fQES.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanssundanese/v17/FwZw7_84xUkosG2xJo2gm7nFwSLQkdymq2mkz3Gz1_b6ctxpNNHCizv7fQES.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Syloti Nagri",
  "variants": [
  "regular"
  ],
  "subsets": [
  "syloti-nagri"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanssylotinagri/v15/uU9eCAQZ75uhfF9UoWDRiY3q7Sf_VFV3m4dGFVfxN87gsj0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Symbols",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "symbols"
  ],
  "version": "v36",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanssymbols/v36/rP2up3q65FkAtHfwd-eIS2brbDN6gxP34F9jRRCe4W3gfQ4gavVFRkzrbQ.ttf",
  "200": "http://fonts.gstatic.com/s/notosanssymbols/v36/rP2up3q65FkAtHfwd-eIS2brbDN6gxP34F9jRRCe4W3g_Q8gavVFRkzrbQ.ttf",
  "300": "http://fonts.gstatic.com/s/notosanssymbols/v36/rP2up3q65FkAtHfwd-eIS2brbDN6gxP34F9jRRCe4W3gIw8gavVFRkzrbQ.ttf",
  "500": "http://fonts.gstatic.com/s/notosanssymbols/v36/rP2up3q65FkAtHfwd-eIS2brbDN6gxP34F9jRRCe4W3gTw8gavVFRkzrbQ.ttf",
  "600": "http://fonts.gstatic.com/s/notosanssymbols/v36/rP2up3q65FkAtHfwd-eIS2brbDN6gxP34F9jRRCe4W3gowggavVFRkzrbQ.ttf",
  "700": "http://fonts.gstatic.com/s/notosanssymbols/v36/rP2up3q65FkAtHfwd-eIS2brbDN6gxP34F9jRRCe4W3gmgggavVFRkzrbQ.ttf",
  "800": "http://fonts.gstatic.com/s/notosanssymbols/v36/rP2up3q65FkAtHfwd-eIS2brbDN6gxP34F9jRRCe4W3g_QggavVFRkzrbQ.ttf",
  "900": "http://fonts.gstatic.com/s/notosanssymbols/v36/rP2up3q65FkAtHfwd-eIS2brbDN6gxP34F9jRRCe4W3g1AggavVFRkzrbQ.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanssymbols/v36/rP2up3q65FkAtHfwd-eIS2brbDN6gxP34F9jRRCe4W3gfQ8gavVFRkzrbQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Symbols 2",
  "variants": [
  "regular"
  ],
  "subsets": [
  "symbols"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanssymbols2/v15/I_uyMoGduATTei9eI8daxVHDyfisHr71ypPqfX71-AI.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Syriac",
  "variants": [
  "100",
  "regular",
  "900"
  ],
  "subsets": [
  "syriac"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanssyriac/v15/KtkwAKuMeZjqPnXgyqribqzQqgW0D-e9XaRE7sX5Cg.ttf",
  "900": "http://fonts.gstatic.com/s/notosanssyriac/v15/KtkxAKuMeZjqPnXgyqribqzQqgW0DweafY5q4szgE-Q.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanssyriac/v15/Ktk2AKuMeZjqPnXgyqribqzQqgW0N4O3WYZB_sU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans TC",
  "variants": [
  "100",
  "300",
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "chinese-traditional",
  "latin"
  ],
  "version": "v26",
  "lastModified": "2022-09-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanstc/v26/-nFlOG829Oofr2wohFbTp9i9WyEJIfNZ1sjy.otf",
  "300": "http://fonts.gstatic.com/s/notosanstc/v26/-nFkOG829Oofr2wohFbTp9i9kwMvDd1V39Hr7g.otf",
  "500": "http://fonts.gstatic.com/s/notosanstc/v26/-nFkOG829Oofr2wohFbTp9i9ywIvDd1V39Hr7g.otf",
  "700": "http://fonts.gstatic.com/s/notosanstc/v26/-nFkOG829Oofr2wohFbTp9i9gwQvDd1V39Hr7g.otf",
  "900": "http://fonts.gstatic.com/s/notosanstc/v26/-nFkOG829Oofr2wohFbTp9i9uwYvDd1V39Hr7g.otf",
  "regular": "http://fonts.gstatic.com/s/notosanstc/v26/-nF7OG829Oofr2wohFbTp9iFOSsLA_ZJ1g.otf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Tagalog",
  "variants": [
  "regular"
  ],
  "subsets": [
  "tagalog"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanstagalog/v15/J7aFnoNzCnFcV9ZI-sUYuvote1R0wwEAA8jHexnL.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Tagbanwa",
  "variants": [
  "regular"
  ],
  "subsets": [
  "tagbanwa"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanstagbanwa/v15/Y4GWYbB8VTEp4t3MKJSMmQdIKjRtt_nZRjQEaYpGoQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Tai Le",
  "variants": [
  "regular"
  ],
  "subsets": [
  "tai-le"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanstaile/v15/vEFK2-VODB8RrNDvZSUmVxEATwR58tK1W77HtMo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Tai Tham",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "tai-tham"
  ],
  "version": "v17",
  "lastModified": "2022-07-19",
  "files": {
  "500": "http://fonts.gstatic.com/s/notosanstaitham/v17/kJEbBv0U4hgtwxDUw2x9q7tbjLIfbPGHBoaVSAZ3MdLJBBcbPgquyaRGKMw.ttf",
  "600": "http://fonts.gstatic.com/s/notosanstaitham/v17/kJEbBv0U4hgtwxDUw2x9q7tbjLIfbPGHBoaVSAZ3MdLJBPscPgquyaRGKMw.ttf",
  "700": "http://fonts.gstatic.com/s/notosanstaitham/v17/kJEbBv0U4hgtwxDUw2x9q7tbjLIfbPGHBoaVSAZ3MdLJBMIcPgquyaRGKMw.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanstaitham/v17/kJEbBv0U4hgtwxDUw2x9q7tbjLIfbPGHBoaVSAZ3MdLJBCUbPgquyaRGKMw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Tai Viet",
  "variants": [
  "regular"
  ],
  "subsets": [
  "tai-viet"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanstaiviet/v15/8QIUdj3HhN_lv4jf9vsE-9GMOLsaSPZr644fWsRO9w.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Takri",
  "variants": [
  "regular"
  ],
  "subsets": [
  "takri"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanstakri/v15/TuGJUVpzXI5FBtUq5a8bnKIOdTwQNO_W3khJXg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Tamil",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanstamil/v21/ieVc2YdFI3GCY6SyQy1KfStzYKZgzN1z4LKDbeZce-0429tBManUktuex7vGor0RqKDt_EvT.ttf",
  "200": "http://fonts.gstatic.com/s/notosanstamil/v21/ieVc2YdFI3GCY6SyQy1KfStzYKZgzN1z4LKDbeZce-0429tBManUktuex7tGo70RqKDt_EvT.ttf",
  "300": "http://fonts.gstatic.com/s/notosanstamil/v21/ieVc2YdFI3GCY6SyQy1KfStzYKZgzN1z4LKDbeZce-0429tBManUktuex7uYo70RqKDt_EvT.ttf",
  "500": "http://fonts.gstatic.com/s/notosanstamil/v21/ieVc2YdFI3GCY6SyQy1KfStzYKZgzN1z4LKDbeZce-0429tBManUktuex7v0o70RqKDt_EvT.ttf",
  "600": "http://fonts.gstatic.com/s/notosanstamil/v21/ieVc2YdFI3GCY6SyQy1KfStzYKZgzN1z4LKDbeZce-0429tBManUktuex7sYpL0RqKDt_EvT.ttf",
  "700": "http://fonts.gstatic.com/s/notosanstamil/v21/ieVc2YdFI3GCY6SyQy1KfStzYKZgzN1z4LKDbeZce-0429tBManUktuex7shpL0RqKDt_EvT.ttf",
  "800": "http://fonts.gstatic.com/s/notosanstamil/v21/ieVc2YdFI3GCY6SyQy1KfStzYKZgzN1z4LKDbeZce-0429tBManUktuex7tGpL0RqKDt_EvT.ttf",
  "900": "http://fonts.gstatic.com/s/notosanstamil/v21/ieVc2YdFI3GCY6SyQy1KfStzYKZgzN1z4LKDbeZce-0429tBManUktuex7tvpL0RqKDt_EvT.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanstamil/v21/ieVc2YdFI3GCY6SyQy1KfStzYKZgzN1z4LKDbeZce-0429tBManUktuex7vGo70RqKDt_EvT.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Tamil Supplement",
  "variants": [
  "regular"
  ],
  "subsets": [
  "tamil-supplement"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanstamilsupplement/v19/DdTz78kEtnooLS5rXF1DaruiCd_bFp_Ph4sGcn7ax_vsAeMkeq1x.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Telugu",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "telugu"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosanstelugu/v19/0FlxVOGZlE2Rrtr-HmgkMWJNjJ5_RyT8o8c7fHkeg-esVC5dzHkHIJQqrEntezfqQUbf-3v37w.ttf",
  "200": "http://fonts.gstatic.com/s/notosanstelugu/v19/0FlxVOGZlE2Rrtr-HmgkMWJNjJ5_RyT8o8c7fHkeg-esVC5dzHkHIJQqrEnt-zbqQUbf-3v37w.ttf",
  "300": "http://fonts.gstatic.com/s/notosanstelugu/v19/0FlxVOGZlE2Rrtr-HmgkMWJNjJ5_RyT8o8c7fHkeg-esVC5dzHkHIJQqrEntJTbqQUbf-3v37w.ttf",
  "500": "http://fonts.gstatic.com/s/notosanstelugu/v19/0FlxVOGZlE2Rrtr-HmgkMWJNjJ5_RyT8o8c7fHkeg-esVC5dzHkHIJQqrEntSTbqQUbf-3v37w.ttf",
  "600": "http://fonts.gstatic.com/s/notosanstelugu/v19/0FlxVOGZlE2Rrtr-HmgkMWJNjJ5_RyT8o8c7fHkeg-esVC5dzHkHIJQqrEntpTHqQUbf-3v37w.ttf",
  "700": "http://fonts.gstatic.com/s/notosanstelugu/v19/0FlxVOGZlE2Rrtr-HmgkMWJNjJ5_RyT8o8c7fHkeg-esVC5dzHkHIJQqrEntnDHqQUbf-3v37w.ttf",
  "800": "http://fonts.gstatic.com/s/notosanstelugu/v19/0FlxVOGZlE2Rrtr-HmgkMWJNjJ5_RyT8o8c7fHkeg-esVC5dzHkHIJQqrEnt-zHqQUbf-3v37w.ttf",
  "900": "http://fonts.gstatic.com/s/notosanstelugu/v19/0FlxVOGZlE2Rrtr-HmgkMWJNjJ5_RyT8o8c7fHkeg-esVC5dzHkHIJQqrEnt0jHqQUbf-3v37w.ttf",
  "regular": "http://fonts.gstatic.com/s/notosanstelugu/v19/0FlxVOGZlE2Rrtr-HmgkMWJNjJ5_RyT8o8c7fHkeg-esVC5dzHkHIJQqrEntezbqQUbf-3v37w.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Thaana",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "thaana"
  ],
  "version": "v16",
  "lastModified": "2022-07-19",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansthaana/v16/C8c14dM-vnz-s-3jaEsxlxHkBH-WZOETXfoQrfQ9Y4XrbxLhnu4-tbNu.ttf",
  "200": "http://fonts.gstatic.com/s/notosansthaana/v16/C8c14dM-vnz-s-3jaEsxlxHkBH-WZOETXfoQrfQ9Y4VrbhLhnu4-tbNu.ttf",
  "300": "http://fonts.gstatic.com/s/notosansthaana/v16/C8c14dM-vnz-s-3jaEsxlxHkBH-WZOETXfoQrfQ9Y4W1bhLhnu4-tbNu.ttf",
  "500": "http://fonts.gstatic.com/s/notosansthaana/v16/C8c14dM-vnz-s-3jaEsxlxHkBH-WZOETXfoQrfQ9Y4XZbhLhnu4-tbNu.ttf",
  "600": "http://fonts.gstatic.com/s/notosansthaana/v16/C8c14dM-vnz-s-3jaEsxlxHkBH-WZOETXfoQrfQ9Y4U1aRLhnu4-tbNu.ttf",
  "700": "http://fonts.gstatic.com/s/notosansthaana/v16/C8c14dM-vnz-s-3jaEsxlxHkBH-WZOETXfoQrfQ9Y4UMaRLhnu4-tbNu.ttf",
  "800": "http://fonts.gstatic.com/s/notosansthaana/v16/C8c14dM-vnz-s-3jaEsxlxHkBH-WZOETXfoQrfQ9Y4VraRLhnu4-tbNu.ttf",
  "900": "http://fonts.gstatic.com/s/notosansthaana/v16/C8c14dM-vnz-s-3jaEsxlxHkBH-WZOETXfoQrfQ9Y4VCaRLhnu4-tbNu.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansthaana/v16/C8c14dM-vnz-s-3jaEsxlxHkBH-WZOETXfoQrfQ9Y4XrbhLhnu4-tbNu.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Thai",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansthai/v20/iJWnBXeUZi_OHPqn4wq6hQ2_hbJ1xyN9wd43SofNWcd1MKVQt_So_9CdU5RspzF-QRvzzXg.ttf",
  "200": "http://fonts.gstatic.com/s/notosansthai/v20/iJWnBXeUZi_OHPqn4wq6hQ2_hbJ1xyN9wd43SofNWcd1MKVQt_So_9CdUxRtpzF-QRvzzXg.ttf",
  "300": "http://fonts.gstatic.com/s/notosansthai/v20/iJWnBXeUZi_OHPqn4wq6hQ2_hbJ1xyN9wd43SofNWcd1MKVQt_So_9CdU8ptpzF-QRvzzXg.ttf",
  "500": "http://fonts.gstatic.com/s/notosansthai/v20/iJWnBXeUZi_OHPqn4wq6hQ2_hbJ1xyN9wd43SofNWcd1MKVQt_So_9CdU6ZtpzF-QRvzzXg.ttf",
  "600": "http://fonts.gstatic.com/s/notosansthai/v20/iJWnBXeUZi_OHPqn4wq6hQ2_hbJ1xyN9wd43SofNWcd1MKVQt_So_9CdU0pqpzF-QRvzzXg.ttf",
  "700": "http://fonts.gstatic.com/s/notosansthai/v20/iJWnBXeUZi_OHPqn4wq6hQ2_hbJ1xyN9wd43SofNWcd1MKVQt_So_9CdU3NqpzF-QRvzzXg.ttf",
  "800": "http://fonts.gstatic.com/s/notosansthai/v20/iJWnBXeUZi_OHPqn4wq6hQ2_hbJ1xyN9wd43SofNWcd1MKVQt_So_9CdUxRqpzF-QRvzzXg.ttf",
  "900": "http://fonts.gstatic.com/s/notosansthai/v20/iJWnBXeUZi_OHPqn4wq6hQ2_hbJ1xyN9wd43SofNWcd1MKVQt_So_9CdUz1qpzF-QRvzzXg.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansthai/v20/iJWnBXeUZi_OHPqn4wq6hQ2_hbJ1xyN9wd43SofNWcd1MKVQt_So_9CdU5RtpzF-QRvzzXg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Thai Looped",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "thai"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notosansthailooped/v12/B50fF6pOpWTRcGrhOVJJ3-oPfY7WQuFu5R3YX6AYeCT_Wfd1.ttf",
  "200": "http://fonts.gstatic.com/s/notosansthailooped/v12/B50cF6pOpWTRcGrhOVJJ3-oPfY7WQuFu5R3Y84E4UgrzUO5sKA.ttf",
  "300": "http://fonts.gstatic.com/s/notosansthailooped/v12/B50cF6pOpWTRcGrhOVJJ3-oPfY7WQuFu5R3Yl4I4UgrzUO5sKA.ttf",
  "500": "http://fonts.gstatic.com/s/notosansthailooped/v12/B50cF6pOpWTRcGrhOVJJ3-oPfY7WQuFu5R3Yz4M4UgrzUO5sKA.ttf",
  "600": "http://fonts.gstatic.com/s/notosansthailooped/v12/B50cF6pOpWTRcGrhOVJJ3-oPfY7WQuFu5R3Y44Q4UgrzUO5sKA.ttf",
  "700": "http://fonts.gstatic.com/s/notosansthailooped/v12/B50cF6pOpWTRcGrhOVJJ3-oPfY7WQuFu5R3Yh4U4UgrzUO5sKA.ttf",
  "800": "http://fonts.gstatic.com/s/notosansthailooped/v12/B50cF6pOpWTRcGrhOVJJ3-oPfY7WQuFu5R3Ym4Y4UgrzUO5sKA.ttf",
  "900": "http://fonts.gstatic.com/s/notosansthailooped/v12/B50cF6pOpWTRcGrhOVJJ3-oPfY7WQuFu5R3Yv4c4UgrzUO5sKA.ttf",
  "regular": "http://fonts.gstatic.com/s/notosansthailooped/v12/B50RF6pOpWTRcGrhOVJJ3-oPfY7WQuFu5R3gO6ocWiHvWQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Tifinagh",
  "variants": [
  "regular"
  ],
  "subsets": [
  "tifinagh"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanstifinagh/v15/I_uzMoCduATTei9eI8dawkHIwvmhCvbn6rnEcXfs4Q.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Tirhuta",
  "variants": [
  "regular"
  ],
  "subsets": [
  "tirhuta"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanstirhuta/v15/t5t6IQYRNJ6TWjahPR6X-M-apUyby7uGUBsTrn5P.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Ugaritic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "ugaritic"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansugaritic/v15/3qTwoiqhnSyU8TNFIdhZVCwbjCpkAXXkMhoIkiazfg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Vai",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vai"
  ],
  "version": "v17",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansvai/v17/NaPecZTSBuhTirw6IaFn_UrURMTsDIRSfr0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Wancho",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "wancho"
  ],
  "version": "v17",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanswancho/v17/zrf-0GXXyfn6Fs0lH9P4cUubP0GBqAPopiRfKp8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Warang Citi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "warang-citi"
  ],
  "version": "v17",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanswarangciti/v17/EYqtmb9SzL1YtsZSScyKDXIeOv3w-zgsNvKRpeVCCXzdgA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Yi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "yi"
  ],
  "version": "v16",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosansyi/v16/sJoD3LFXjsSdcnzn071rO3apxVDJNVgSNg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Sans Zanabazar Square",
  "variants": [
  "regular"
  ],
  "subsets": [
  "zanabazar-square"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notosanszanabazarsquare/v15/Cn-jJsuGWQxOjaGwMQ6fOicyxLBEMRfDtkzl4uagQtJxOCEgN0Gc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/notoserif/v21/ga6Law1J5X9T9RW6j9bNdOwzTRCUcM1IKoY.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserif/v21/ga6Iaw1J5X9T9RW6j9bNTFAcaRi_bMQ.ttf",
  "italic": "http://fonts.gstatic.com/s/notoserif/v21/ga6Kaw1J5X9T9RW6j9bNfFIWbTq6fMRRMw.ttf",
  "700italic": "http://fonts.gstatic.com/s/notoserif/v21/ga6Vaw1J5X9T9RW6j9bNfFIu0RWedO9NOoYIDg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Ahom",
  "variants": [
  "regular"
  ],
  "subsets": [
  "ahom",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notoserifahom/v17/FeVIS0hfp6cprmEUffAW_fUL_AN-wuYrPFiwaw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Armenian",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "armenian",
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifarmenian/v23/3XFMEqMt3YoFsciDRZxptyCUKJmytZ0kVU-XvF7QaZuL85rnQ_zDNzDe5xNnKxyZi8ObxvXagGdkbg.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifarmenian/v23/3XFMEqMt3YoFsciDRZxptyCUKJmytZ0kVU-XvF7QaZuL85rnQ_zDNzDe5xNnKxyZC8KbxvXagGdkbg.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifarmenian/v23/3XFMEqMt3YoFsciDRZxptyCUKJmytZ0kVU-XvF7QaZuL85rnQ_zDNzDe5xNnKxyZ1cKbxvXagGdkbg.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifarmenian/v23/3XFMEqMt3YoFsciDRZxptyCUKJmytZ0kVU-XvF7QaZuL85rnQ_zDNzDe5xNnKxyZucKbxvXagGdkbg.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifarmenian/v23/3XFMEqMt3YoFsciDRZxptyCUKJmytZ0kVU-XvF7QaZuL85rnQ_zDNzDe5xNnKxyZVcWbxvXagGdkbg.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifarmenian/v23/3XFMEqMt3YoFsciDRZxptyCUKJmytZ0kVU-XvF7QaZuL85rnQ_zDNzDe5xNnKxyZbMWbxvXagGdkbg.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifarmenian/v23/3XFMEqMt3YoFsciDRZxptyCUKJmytZ0kVU-XvF7QaZuL85rnQ_zDNzDe5xNnKxyZC8WbxvXagGdkbg.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifarmenian/v23/3XFMEqMt3YoFsciDRZxptyCUKJmytZ0kVU-XvF7QaZuL85rnQ_zDNzDe5xNnKxyZIsWbxvXagGdkbg.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifarmenian/v23/3XFMEqMt3YoFsciDRZxptyCUKJmytZ0kVU-XvF7QaZuL85rnQ_zDNzDe5xNnKxyZi8KbxvXagGdkbg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Balinese",
  "variants": [
  "regular"
  ],
  "subsets": [
  "balinese",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notoserifbalinese/v16/QdVKSS0-JginysQSRvuCmUMB_wVeQAxXRbgJdhapcUU.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Bengali",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "bengali",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifbengali/v19/hYkuPvggTvnzO14VSXltirUdnnkt1pwmWrprmO7RjE0a5BtdATYU1crFaM_5JfcAH3qn4LjQH8yD.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifbengali/v19/hYkuPvggTvnzO14VSXltirUdnnkt1pwmWrprmO7RjE0a5BtdATYU1crFaM_5JfeAHnqn4LjQH8yD.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifbengali/v19/hYkuPvggTvnzO14VSXltirUdnnkt1pwmWrprmO7RjE0a5BtdATYU1crFaM_5JfdeHnqn4LjQH8yD.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifbengali/v19/hYkuPvggTvnzO14VSXltirUdnnkt1pwmWrprmO7RjE0a5BtdATYU1crFaM_5JfcyHnqn4LjQH8yD.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifbengali/v19/hYkuPvggTvnzO14VSXltirUdnnkt1pwmWrprmO7RjE0a5BtdATYU1crFaM_5JffeGXqn4LjQH8yD.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifbengali/v19/hYkuPvggTvnzO14VSXltirUdnnkt1pwmWrprmO7RjE0a5BtdATYU1crFaM_5JffnGXqn4LjQH8yD.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifbengali/v19/hYkuPvggTvnzO14VSXltirUdnnkt1pwmWrprmO7RjE0a5BtdATYU1crFaM_5JfeAGXqn4LjQH8yD.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifbengali/v19/hYkuPvggTvnzO14VSXltirUdnnkt1pwmWrprmO7RjE0a5BtdATYU1crFaM_5JfepGXqn4LjQH8yD.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifbengali/v19/hYkuPvggTvnzO14VSXltirUdnnkt1pwmWrprmO7RjE0a5BtdATYU1crFaM_5JfcAHnqn4LjQH8yD.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Devanagari",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifdevanagari/v21/x3dYcl3IZKmUqiMk48ZHXJ5jwU-DZGRSaQ4Hh2dGyFzPLcQPVbnRNeFsw0xRWb6uxTA-og-HMUe1u_dv.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifdevanagari/v21/x3dYcl3IZKmUqiMk48ZHXJ5jwU-DZGRSaQ4Hh2dGyFzPLcQPVbnRNeFsw0xRWb6uxTC-ow-HMUe1u_dv.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifdevanagari/v21/x3dYcl3IZKmUqiMk48ZHXJ5jwU-DZGRSaQ4Hh2dGyFzPLcQPVbnRNeFsw0xRWb6uxTBgow-HMUe1u_dv.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifdevanagari/v21/x3dYcl3IZKmUqiMk48ZHXJ5jwU-DZGRSaQ4Hh2dGyFzPLcQPVbnRNeFsw0xRWb6uxTAMow-HMUe1u_dv.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifdevanagari/v21/x3dYcl3IZKmUqiMk48ZHXJ5jwU-DZGRSaQ4Hh2dGyFzPLcQPVbnRNeFsw0xRWb6uxTDgpA-HMUe1u_dv.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifdevanagari/v21/x3dYcl3IZKmUqiMk48ZHXJ5jwU-DZGRSaQ4Hh2dGyFzPLcQPVbnRNeFsw0xRWb6uxTDZpA-HMUe1u_dv.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifdevanagari/v21/x3dYcl3IZKmUqiMk48ZHXJ5jwU-DZGRSaQ4Hh2dGyFzPLcQPVbnRNeFsw0xRWb6uxTC-pA-HMUe1u_dv.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifdevanagari/v21/x3dYcl3IZKmUqiMk48ZHXJ5jwU-DZGRSaQ4Hh2dGyFzPLcQPVbnRNeFsw0xRWb6uxTCXpA-HMUe1u_dv.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifdevanagari/v21/x3dYcl3IZKmUqiMk48ZHXJ5jwU-DZGRSaQ4Hh2dGyFzPLcQPVbnRNeFsw0xRWb6uxTA-ow-HMUe1u_dv.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Display",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buERppa9f8_vkXaZLAgP0G5Wi6QmA1QaeYah2sovLCDq_ZgLyt3idQfktOG-PVpd49gKaDU9hvzC.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buERppa9f8_vkXaZLAgP0G5Wi6QmA1QaeYah2sovLCDq_ZgLyt3idQfktOG-PVrd4tgKaDU9hvzC.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buERppa9f8_vkXaZLAgP0G5Wi6QmA1QaeYah2sovLCDq_ZgLyt3idQfktOG-PVoD4tgKaDU9hvzC.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buERppa9f8_vkXaZLAgP0G5Wi6QmA1QaeYah2sovLCDq_ZgLyt3idQfktOG-PVpv4tgKaDU9hvzC.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buERppa9f8_vkXaZLAgP0G5Wi6QmA1QaeYah2sovLCDq_ZgLyt3idQfktOG-PVqD5dgKaDU9hvzC.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buERppa9f8_vkXaZLAgP0G5Wi6QmA1QaeYah2sovLCDq_ZgLyt3idQfktOG-PVq65dgKaDU9hvzC.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buERppa9f8_vkXaZLAgP0G5Wi6QmA1QaeYah2sovLCDq_ZgLyt3idQfktOG-PVrd5dgKaDU9hvzC.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buERppa9f8_vkXaZLAgP0G5Wi6QmA1QaeYah2sovLCDq_ZgLyt3idQfktOG-PVr05dgKaDU9hvzC.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buERppa9f8_vkXaZLAgP0G5Wi6QmA1QaeYah2sovLCDq_ZgLyt3idQfktOG-PVpd4tgKaDU9hvzC.ttf",
  "100italic": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buEPppa9f8_vkXaZLAgP0G5Wi6QmA1QwcLRCOrN8uo7t6FBJOJTQit-N33sQOk-VoTBIYjEfg-zCmf4.ttf",
  "200italic": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buEPppa9f8_vkXaZLAgP0G5Wi6QmA1QwcLRCOrN8uo7t6FBJOJTQit-N33sQOk-VobBJYjEfg-zCmf4.ttf",
  "300italic": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buEPppa9f8_vkXaZLAgP0G5Wi6QmA1QwcLRCOrN8uo7t6FBJOJTQit-N33sQOk-VoW5JYjEfg-zCmf4.ttf",
  "italic": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buEPppa9f8_vkXaZLAgP0G5Wi6QmA1QwcLRCOrN8uo7t6FBJOJTQit-N33sQOk-VoTBJYjEfg-zCmf4.ttf",
  "500italic": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buEPppa9f8_vkXaZLAgP0G5Wi6QmA1QwcLRCOrN8uo7t6FBJOJTQit-N33sQOk-VoQJJYjEfg-zCmf4.ttf",
  "600italic": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buEPppa9f8_vkXaZLAgP0G5Wi6QmA1QwcLRCOrN8uo7t6FBJOJTQit-N33sQOk-Voe5OYjEfg-zCmf4.ttf",
  "700italic": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buEPppa9f8_vkXaZLAgP0G5Wi6QmA1QwcLRCOrN8uo7t6FBJOJTQit-N33sQOk-VoddOYjEfg-zCmf4.ttf",
  "800italic": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buEPppa9f8_vkXaZLAgP0G5Wi6QmA1QwcLRCOrN8uo7t6FBJOJTQit-N33sQOk-VobBOYjEfg-zCmf4.ttf",
  "900italic": "http://fonts.gstatic.com/s/notoserifdisplay/v17/buEPppa9f8_vkXaZLAgP0G5Wi6QmA1QwcLRCOrN8uo7t6FBJOJTQit-N33sQOk-VoZlOYjEfg-zCmf4.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Dogra",
  "variants": [
  "regular"
  ],
  "subsets": [
  "dogra"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notoserifdogra/v15/MQpP-XquKMC7ROPP3QOOlm7xPu3fGy63IbPzkns.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Ethiopic",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "ethiopic",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifethiopic/v18/V8mjoR7-XjwJ8_Au3Ti5tXj5Rd83frpWLK4d-taxqWw2HMWjDxBAg5S_0QsrggxCzSQjkaO9UVLyiw.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifethiopic/v18/V8mjoR7-XjwJ8_Au3Ti5tXj5Rd83frpWLK4d-taxqWw2HMWjDxBAg5S_0QsrggxCTSUjkaO9UVLyiw.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifethiopic/v18/V8mjoR7-XjwJ8_Au3Ti5tXj5Rd83frpWLK4d-taxqWw2HMWjDxBAg5S_0QsrggxCkyUjkaO9UVLyiw.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifethiopic/v18/V8mjoR7-XjwJ8_Au3Ti5tXj5Rd83frpWLK4d-taxqWw2HMWjDxBAg5S_0QsrggxC_yUjkaO9UVLyiw.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifethiopic/v18/V8mjoR7-XjwJ8_Au3Ti5tXj5Rd83frpWLK4d-taxqWw2HMWjDxBAg5S_0QsrggxCEyIjkaO9UVLyiw.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifethiopic/v18/V8mjoR7-XjwJ8_Au3Ti5tXj5Rd83frpWLK4d-taxqWw2HMWjDxBAg5S_0QsrggxCKiIjkaO9UVLyiw.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifethiopic/v18/V8mjoR7-XjwJ8_Au3Ti5tXj5Rd83frpWLK4d-taxqWw2HMWjDxBAg5S_0QsrggxCTSIjkaO9UVLyiw.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifethiopic/v18/V8mjoR7-XjwJ8_Au3Ti5tXj5Rd83frpWLK4d-taxqWw2HMWjDxBAg5S_0QsrggxCZCIjkaO9UVLyiw.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifethiopic/v18/V8mjoR7-XjwJ8_Au3Ti5tXj5Rd83frpWLK4d-taxqWw2HMWjDxBAg5S_0QsrggxCzSUjkaO9UVLyiw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Georgian",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "georgian",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifgeorgian/v18/VEMXRpd8s4nv8hG_qOzL7HOAw4nt0Sl_XxyaEduNMvi7T6Y4etRnmGhyLop-R3aSTvsfdzTw-FgZxQ.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifgeorgian/v18/VEMXRpd8s4nv8hG_qOzL7HOAw4nt0Sl_XxyaEduNMvi7T6Y4etRnmGhyLop-R3aSzvofdzTw-FgZxQ.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifgeorgian/v18/VEMXRpd8s4nv8hG_qOzL7HOAw4nt0Sl_XxyaEduNMvi7T6Y4etRnmGhyLop-R3aSEPofdzTw-FgZxQ.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifgeorgian/v18/VEMXRpd8s4nv8hG_qOzL7HOAw4nt0Sl_XxyaEduNMvi7T6Y4etRnmGhyLop-R3aSfPofdzTw-FgZxQ.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifgeorgian/v18/VEMXRpd8s4nv8hG_qOzL7HOAw4nt0Sl_XxyaEduNMvi7T6Y4etRnmGhyLop-R3aSkP0fdzTw-FgZxQ.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifgeorgian/v18/VEMXRpd8s4nv8hG_qOzL7HOAw4nt0Sl_XxyaEduNMvi7T6Y4etRnmGhyLop-R3aSqf0fdzTw-FgZxQ.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifgeorgian/v18/VEMXRpd8s4nv8hG_qOzL7HOAw4nt0Sl_XxyaEduNMvi7T6Y4etRnmGhyLop-R3aSzv0fdzTw-FgZxQ.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifgeorgian/v18/VEMXRpd8s4nv8hG_qOzL7HOAw4nt0Sl_XxyaEduNMvi7T6Y4etRnmGhyLop-R3aS5_0fdzTw-FgZxQ.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifgeorgian/v18/VEMXRpd8s4nv8hG_qOzL7HOAw4nt0Sl_XxyaEduNMvi7T6Y4etRnmGhyLop-R3aSTvofdzTw-FgZxQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Grantha",
  "variants": [
  "regular"
  ],
  "subsets": [
  "grantha",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notoserifgrantha/v19/qkBIXuEH5NzDDvc3fLDYxPk9-Wq3WLiqFENLR7fHGw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Gujarati",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifgujarati/v21/hESa6WBlOixO-3OJ1FTmTsmqlBRUJBVkcgNLpdsspzP2HuYycYzuM1Kf-OJu.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifgujarati/v21/hESa6WBlOixO-3OJ1FTmTsmqlBRUJBVkcgNLpdsspzP2HuaycIzuM1Kf-OJu.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifgujarati/v21/hESa6WBlOixO-3OJ1FTmTsmqlBRUJBVkcgNLpdsspzP2HuZscIzuM1Kf-OJu.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifgujarati/v21/hESa6WBlOixO-3OJ1FTmTsmqlBRUJBVkcgNLpdsspzP2HuYAcIzuM1Kf-OJu.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifgujarati/v21/hESa6WBlOixO-3OJ1FTmTsmqlBRUJBVkcgNLpdsspzP2Hubsd4zuM1Kf-OJu.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifgujarati/v21/hESa6WBlOixO-3OJ1FTmTsmqlBRUJBVkcgNLpdsspzP2HubVd4zuM1Kf-OJu.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifgujarati/v21/hESa6WBlOixO-3OJ1FTmTsmqlBRUJBVkcgNLpdsspzP2Huayd4zuM1Kf-OJu.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifgujarati/v21/hESa6WBlOixO-3OJ1FTmTsmqlBRUJBVkcgNLpdsspzP2Huabd4zuM1Kf-OJu.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifgujarati/v21/hESa6WBlOixO-3OJ1FTmTsmqlBRUJBVkcgNLpdsspzP2HuYycIzuM1Kf-OJu.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Gurmukhi",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "gurmukhi",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifgurmukhi/v14/92z-tA9LNqsg7tCYlXdCV1VPnAEeDU0vLoYMbylXk0xTCr6-eBTNmqVU7y6l.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifgurmukhi/v14/92z-tA9LNqsg7tCYlXdCV1VPnAEeDU0vLoYMbylXk0xTCr4-eRTNmqVU7y6l.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifgurmukhi/v14/92z-tA9LNqsg7tCYlXdCV1VPnAEeDU0vLoYMbylXk0xTCr7geRTNmqVU7y6l.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifgurmukhi/v14/92z-tA9LNqsg7tCYlXdCV1VPnAEeDU0vLoYMbylXk0xTCr6MeRTNmqVU7y6l.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifgurmukhi/v14/92z-tA9LNqsg7tCYlXdCV1VPnAEeDU0vLoYMbylXk0xTCr5gfhTNmqVU7y6l.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifgurmukhi/v14/92z-tA9LNqsg7tCYlXdCV1VPnAEeDU0vLoYMbylXk0xTCr5ZfhTNmqVU7y6l.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifgurmukhi/v14/92z-tA9LNqsg7tCYlXdCV1VPnAEeDU0vLoYMbylXk0xTCr4-fhTNmqVU7y6l.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifgurmukhi/v14/92z-tA9LNqsg7tCYlXdCV1VPnAEeDU0vLoYMbylXk0xTCr4XfhTNmqVU7y6l.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifgurmukhi/v14/92z-tA9LNqsg7tCYlXdCV1VPnAEeDU0vLoYMbylXk0xTCr6-eRTNmqVU7y6l.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif HK",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "chinese-hongkong",
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-27",
  "files": {
  "200": "http://fonts.gstatic.com/s/notoserifhk/v2/BngdUXBETWXI6LwlBZGcqL-B_KuJFcgfwP_9RMf-K2RmV9Su1M6i.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifhk/v2/BngdUXBETWXI6LwlBZGcqL-B_KuJFcgfwP_9RMcgK2RmV9Su1M6i.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifhk/v2/BngdUXBETWXI6LwlBZGcqL-B_KuJFcgfwP_9RMdMK2RmV9Su1M6i.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifhk/v2/BngdUXBETWXI6LwlBZGcqL-B_KuJFcgfwP_9RMegLGRmV9Su1M6i.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifhk/v2/BngdUXBETWXI6LwlBZGcqL-B_KuJFcgfwP_9RMeZLGRmV9Su1M6i.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifhk/v2/BngdUXBETWXI6LwlBZGcqL-B_KuJFcgfwP_9RMf-LGRmV9Su1M6i.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifhk/v2/BngdUXBETWXI6LwlBZGcqL-B_KuJFcgfwP_9RMfXLGRmV9Su1M6i.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifhk/v2/BngdUXBETWXI6LwlBZGcqL-B_KuJFcgfwP_9RMd-K2RmV9Su1M6i.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Hebrew",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifhebrew/v20/k3k0o9MMPvpLmixYH7euCwmkS9DohjX1-kRyiqyBqIxnoLbp93i9IKrXKF_qVAwTAG8_vlQxz24.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifhebrew/v20/k3k0o9MMPvpLmixYH7euCwmkS9DohjX1-kRyiqyBqIxnoLbp93i9IKrXKF_qVIwSAG8_vlQxz24.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifhebrew/v20/k3k0o9MMPvpLmixYH7euCwmkS9DohjX1-kRyiqyBqIxnoLbp93i9IKrXKF_qVFISAG8_vlQxz24.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifhebrew/v20/k3k0o9MMPvpLmixYH7euCwmkS9DohjX1-kRyiqyBqIxnoLbp93i9IKrXKF_qVD4SAG8_vlQxz24.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifhebrew/v20/k3k0o9MMPvpLmixYH7euCwmkS9DohjX1-kRyiqyBqIxnoLbp93i9IKrXKF_qVNIVAG8_vlQxz24.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifhebrew/v20/k3k0o9MMPvpLmixYH7euCwmkS9DohjX1-kRyiqyBqIxnoLbp93i9IKrXKF_qVOsVAG8_vlQxz24.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifhebrew/v20/k3k0o9MMPvpLmixYH7euCwmkS9DohjX1-kRyiqyBqIxnoLbp93i9IKrXKF_qVIwVAG8_vlQxz24.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifhebrew/v20/k3k0o9MMPvpLmixYH7euCwmkS9DohjX1-kRyiqyBqIxnoLbp93i9IKrXKF_qVKUVAG8_vlQxz24.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifhebrew/v20/k3k0o9MMPvpLmixYH7euCwmkS9DohjX1-kRyiqyBqIxnoLbp93i9IKrXKF_qVAwSAG8_vlQxz24.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif JP",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "900"
  ],
  "subsets": [
  "japanese",
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-27",
  "files": {
  "200": "http://fonts.gstatic.com/s/notoserifjp/v21/xn77YHs72GKoTvER4Gn3b5eMZBaPRkgfU8fEwb0.otf",
  "300": "http://fonts.gstatic.com/s/notoserifjp/v21/xn77YHs72GKoTvER4Gn3b5eMZHKMRkgfU8fEwb0.otf",
  "500": "http://fonts.gstatic.com/s/notoserifjp/v21/xn77YHs72GKoTvER4Gn3b5eMZCqNRkgfU8fEwb0.otf",
  "600": "http://fonts.gstatic.com/s/notoserifjp/v21/xn77YHs72GKoTvER4Gn3b5eMZAaKRkgfU8fEwb0.otf",
  "700": "http://fonts.gstatic.com/s/notoserifjp/v21/xn77YHs72GKoTvER4Gn3b5eMZGKLRkgfU8fEwb0.otf",
  "900": "http://fonts.gstatic.com/s/notoserifjp/v21/xn77YHs72GKoTvER4Gn3b5eMZFqJRkgfU8fEwb0.otf",
  "regular": "http://fonts.gstatic.com/s/notoserifjp/v21/xn7mYHs72GKoTvER4Gn3b5eMXNikYkY0T84.otf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif KR",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "900"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-27",
  "files": {
  "200": "http://fonts.gstatic.com/s/notoserifkr/v20/3JnmSDn90Gmq2mr3blnHaTZXTihC8O1ZNH1ahck.otf",
  "300": "http://fonts.gstatic.com/s/notoserifkr/v20/3JnmSDn90Gmq2mr3blnHaTZXTkxB8O1ZNH1ahck.otf",
  "500": "http://fonts.gstatic.com/s/notoserifkr/v20/3JnmSDn90Gmq2mr3blnHaTZXThRA8O1ZNH1ahck.otf",
  "600": "http://fonts.gstatic.com/s/notoserifkr/v20/3JnmSDn90Gmq2mr3blnHaTZXTjhH8O1ZNH1ahck.otf",
  "700": "http://fonts.gstatic.com/s/notoserifkr/v20/3JnmSDn90Gmq2mr3blnHaTZXTlxG8O1ZNH1ahck.otf",
  "900": "http://fonts.gstatic.com/s/notoserifkr/v20/3JnmSDn90Gmq2mr3blnHaTZXTmRE8O1ZNH1ahck.otf",
  "regular": "http://fonts.gstatic.com/s/notoserifkr/v20/3Jn7SDn90Gmq2mr3blnHaTZXduZp1ONyKHQ.otf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Kannada",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "kannada",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifkannada/v21/v6-8GZHLJFKIhClqUYqXDiWqpxQxWSPoW6bz-l4hGHiNgcYCceRJ71svgcI.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifkannada/v21/v6-8GZHLJFKIhClqUYqXDiWqpxQxWSPoW6bz-l4hGHiNgUYDceRJ71svgcI.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifkannada/v21/v6-8GZHLJFKIhClqUYqXDiWqpxQxWSPoW6bz-l4hGHiNgZgDceRJ71svgcI.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifkannada/v21/v6-8GZHLJFKIhClqUYqXDiWqpxQxWSPoW6bz-l4hGHiNgfQDceRJ71svgcI.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifkannada/v21/v6-8GZHLJFKIhClqUYqXDiWqpxQxWSPoW6bz-l4hGHiNgRgEceRJ71svgcI.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifkannada/v21/v6-8GZHLJFKIhClqUYqXDiWqpxQxWSPoW6bz-l4hGHiNgSEEceRJ71svgcI.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifkannada/v21/v6-8GZHLJFKIhClqUYqXDiWqpxQxWSPoW6bz-l4hGHiNgUYEceRJ71svgcI.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifkannada/v21/v6-8GZHLJFKIhClqUYqXDiWqpxQxWSPoW6bz-l4hGHiNgW8EceRJ71svgcI.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifkannada/v21/v6-8GZHLJFKIhClqUYqXDiWqpxQxWSPoW6bz-l4hGHiNgcYDceRJ71svgcI.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Khmer",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "khmer",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifkhmer/v18/-F6UfidqLzI2JPCkXAO2hmogq0146FxtbwKEr951z5s6lI40sDRH_AVhUKdN6B4wXEZK9Xo4xg.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifkhmer/v18/-F6UfidqLzI2JPCkXAO2hmogq0146FxtbwKEr951z5s6lI40sDRH_AVhUKdNaB8wXEZK9Xo4xg.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifkhmer/v18/-F6UfidqLzI2JPCkXAO2hmogq0146FxtbwKEr951z5s6lI40sDRH_AVhUKdNth8wXEZK9Xo4xg.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifkhmer/v18/-F6UfidqLzI2JPCkXAO2hmogq0146FxtbwKEr951z5s6lI40sDRH_AVhUKdN2h8wXEZK9Xo4xg.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifkhmer/v18/-F6UfidqLzI2JPCkXAO2hmogq0146FxtbwKEr951z5s6lI40sDRH_AVhUKdNNhgwXEZK9Xo4xg.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifkhmer/v18/-F6UfidqLzI2JPCkXAO2hmogq0146FxtbwKEr951z5s6lI40sDRH_AVhUKdNDxgwXEZK9Xo4xg.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifkhmer/v18/-F6UfidqLzI2JPCkXAO2hmogq0146FxtbwKEr951z5s6lI40sDRH_AVhUKdNaBgwXEZK9Xo4xg.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifkhmer/v18/-F6UfidqLzI2JPCkXAO2hmogq0146FxtbwKEr951z5s6lI40sDRH_AVhUKdNQRgwXEZK9Xo4xg.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifkhmer/v18/-F6UfidqLzI2JPCkXAO2hmogq0146FxtbwKEr951z5s6lI40sDRH_AVhUKdN6B8wXEZK9Xo4xg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Lao",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "lao",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoseriflao/v18/3y9C6bYwcCjmsU8JEzCMxEwQfEBLk3f0rlSqCdaM_LlSNZ59oNw0BWH8VeMLrvOjlmyhHHQ.ttf",
  "200": "http://fonts.gstatic.com/s/notoseriflao/v18/3y9C6bYwcCjmsU8JEzCMxEwQfEBLk3f0rlSqCdaM_LlSNZ59oNw0BWH8VWMKrvOjlmyhHHQ.ttf",
  "300": "http://fonts.gstatic.com/s/notoseriflao/v18/3y9C6bYwcCjmsU8JEzCMxEwQfEBLk3f0rlSqCdaM_LlSNZ59oNw0BWH8Vb0KrvOjlmyhHHQ.ttf",
  "500": "http://fonts.gstatic.com/s/notoseriflao/v18/3y9C6bYwcCjmsU8JEzCMxEwQfEBLk3f0rlSqCdaM_LlSNZ59oNw0BWH8VdEKrvOjlmyhHHQ.ttf",
  "600": "http://fonts.gstatic.com/s/notoseriflao/v18/3y9C6bYwcCjmsU8JEzCMxEwQfEBLk3f0rlSqCdaM_LlSNZ59oNw0BWH8VT0NrvOjlmyhHHQ.ttf",
  "700": "http://fonts.gstatic.com/s/notoseriflao/v18/3y9C6bYwcCjmsU8JEzCMxEwQfEBLk3f0rlSqCdaM_LlSNZ59oNw0BWH8VQQNrvOjlmyhHHQ.ttf",
  "800": "http://fonts.gstatic.com/s/notoseriflao/v18/3y9C6bYwcCjmsU8JEzCMxEwQfEBLk3f0rlSqCdaM_LlSNZ59oNw0BWH8VWMNrvOjlmyhHHQ.ttf",
  "900": "http://fonts.gstatic.com/s/notoseriflao/v18/3y9C6bYwcCjmsU8JEzCMxEwQfEBLk3f0rlSqCdaM_LlSNZ59oNw0BWH8VUoNrvOjlmyhHHQ.ttf",
  "regular": "http://fonts.gstatic.com/s/notoseriflao/v18/3y9C6bYwcCjmsU8JEzCMxEwQfEBLk3f0rlSqCdaM_LlSNZ59oNw0BWH8VeMKrvOjlmyhHHQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Malayalam",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "malayalam"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifmalayalam/v20/JIAZUU5sdmdP_HMcVcZFcH7DeVBeGVgSMEk2cmVDq1ihUXL1t-1fnVwHpQVySg.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifmalayalam/v20/JIAZUU5sdmdP_HMcVcZFcH7DeVBeGVgSMEk2cmVDq1ihUXL1N-xfnVwHpQVySg.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifmalayalam/v20/JIAZUU5sdmdP_HMcVcZFcH7DeVBeGVgSMEk2cmVDq1ihUXL16exfnVwHpQVySg.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifmalayalam/v20/JIAZUU5sdmdP_HMcVcZFcH7DeVBeGVgSMEk2cmVDq1ihUXL1hexfnVwHpQVySg.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifmalayalam/v20/JIAZUU5sdmdP_HMcVcZFcH7DeVBeGVgSMEk2cmVDq1ihUXL1aetfnVwHpQVySg.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifmalayalam/v20/JIAZUU5sdmdP_HMcVcZFcH7DeVBeGVgSMEk2cmVDq1ihUXL1UOtfnVwHpQVySg.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifmalayalam/v20/JIAZUU5sdmdP_HMcVcZFcH7DeVBeGVgSMEk2cmVDq1ihUXL1N-tfnVwHpQVySg.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifmalayalam/v20/JIAZUU5sdmdP_HMcVcZFcH7DeVBeGVgSMEk2cmVDq1ihUXL1HutfnVwHpQVySg.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifmalayalam/v20/JIAZUU5sdmdP_HMcVcZFcH7DeVBeGVgSMEk2cmVDq1ihUXL1t-xfnVwHpQVySg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Myanmar",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "myanmar"
  ],
  "version": "v13",
  "lastModified": "2022-09-28",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifmyanmar/v13/VuJudM7F2Yv76aBKKs-bHMQfAHUw3jnNwBDsU9X6RPzQ.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifmyanmar/v13/VuJvdM7F2Yv76aBKKs-bHMQfAHUw3jnNbDHMefv2TeXJng.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifmyanmar/v13/VuJvdM7F2Yv76aBKKs-bHMQfAHUw3jnNCDLMefv2TeXJng.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifmyanmar/v13/VuJvdM7F2Yv76aBKKs-bHMQfAHUw3jnNUDPMefv2TeXJng.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifmyanmar/v13/VuJvdM7F2Yv76aBKKs-bHMQfAHUw3jnNfDTMefv2TeXJng.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifmyanmar/v13/VuJvdM7F2Yv76aBKKs-bHMQfAHUw3jnNGDXMefv2TeXJng.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifmyanmar/v13/VuJvdM7F2Yv76aBKKs-bHMQfAHUw3jnNBDbMefv2TeXJng.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifmyanmar/v13/VuJvdM7F2Yv76aBKKs-bHMQfAHUw3jnNIDfMefv2TeXJng.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifmyanmar/v13/VuJsdM7F2Yv76aBKKs-bHMQfAHUw3jn1pBrocdDqRA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Nyiakeng Puachue Hmong",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "nyiakeng-puachue-hmong"
  ],
  "version": "v16",
  "lastModified": "2022-07-19",
  "files": {
  "500": "http://fonts.gstatic.com/s/notoserifnyiakengpuachuehmong/v16/5h1jibMoOmIC3YuzLC-NZyLDZC8iwh-MTC8ggAjEhePFNRVcneAFp44kcYMUkNqVKiiPDFvbZkrZmb0.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifnyiakengpuachuehmong/v16/5h1jibMoOmIC3YuzLC-NZyLDZC8iwh-MTC8ggAjEhePFNRVcneAFp44kcYMUkNqVKsSIDFvbZkrZmb0.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifnyiakengpuachuehmong/v16/5h1jibMoOmIC3YuzLC-NZyLDZC8iwh-MTC8ggAjEhePFNRVcneAFp44kcYMUkNqVKv2IDFvbZkrZmb0.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifnyiakengpuachuehmong/v16/5h1jibMoOmIC3YuzLC-NZyLDZC8iwh-MTC8ggAjEhePFNRVcneAFp44kcYMUkNqVKhqPDFvbZkrZmb0.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif SC",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "900"
  ],
  "subsets": [
  "chinese-simplified",
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-27",
  "files": {
  "200": "http://fonts.gstatic.com/s/notoserifsc/v22/H4c8BXePl9DZ0Xe7gG9cyOj7mm63SzZBEtERe7U.otf",
  "300": "http://fonts.gstatic.com/s/notoserifsc/v22/H4c8BXePl9DZ0Xe7gG9cyOj7mgq0SzZBEtERe7U.otf",
  "500": "http://fonts.gstatic.com/s/notoserifsc/v22/H4c8BXePl9DZ0Xe7gG9cyOj7mlK1SzZBEtERe7U.otf",
  "600": "http://fonts.gstatic.com/s/notoserifsc/v22/H4c8BXePl9DZ0Xe7gG9cyOj7mn6ySzZBEtERe7U.otf",
  "700": "http://fonts.gstatic.com/s/notoserifsc/v22/H4c8BXePl9DZ0Xe7gG9cyOj7mhqzSzZBEtERe7U.otf",
  "900": "http://fonts.gstatic.com/s/notoserifsc/v22/H4c8BXePl9DZ0Xe7gG9cyOj7miKxSzZBEtERe7U.otf",
  "regular": "http://fonts.gstatic.com/s/notoserifsc/v22/H4chBXePl9DZ0Xe7gG9cyOj7oqCcbzhqDtg.otf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Sinhala",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "sinhala"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifsinhala/v18/DtVEJwinQqclnZE2CnsPug9lgGC3y2F2nehQ7Eg4EdBKWxPiDxMivFLgRXs_-pGxRlMsxaLRn3W-.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifsinhala/v18/DtVEJwinQqclnZE2CnsPug9lgGC3y2F2nehQ7Eg4EdBKWxPiDxMivFLgRXs_-pExR1MsxaLRn3W-.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifsinhala/v18/DtVEJwinQqclnZE2CnsPug9lgGC3y2F2nehQ7Eg4EdBKWxPiDxMivFLgRXs_-pHvR1MsxaLRn3W-.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifsinhala/v18/DtVEJwinQqclnZE2CnsPug9lgGC3y2F2nehQ7Eg4EdBKWxPiDxMivFLgRXs_-pGDR1MsxaLRn3W-.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifsinhala/v18/DtVEJwinQqclnZE2CnsPug9lgGC3y2F2nehQ7Eg4EdBKWxPiDxMivFLgRXs_-pFvQFMsxaLRn3W-.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifsinhala/v18/DtVEJwinQqclnZE2CnsPug9lgGC3y2F2nehQ7Eg4EdBKWxPiDxMivFLgRXs_-pFWQFMsxaLRn3W-.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifsinhala/v18/DtVEJwinQqclnZE2CnsPug9lgGC3y2F2nehQ7Eg4EdBKWxPiDxMivFLgRXs_-pExQFMsxaLRn3W-.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifsinhala/v18/DtVEJwinQqclnZE2CnsPug9lgGC3y2F2nehQ7Eg4EdBKWxPiDxMivFLgRXs_-pEYQFMsxaLRn3W-.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifsinhala/v18/DtVEJwinQqclnZE2CnsPug9lgGC3y2F2nehQ7Eg4EdBKWxPiDxMivFLgRXs_-pGxR1MsxaLRn3W-.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif TC",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "900"
  ],
  "subsets": [
  "chinese-traditional",
  "latin"
  ],
  "version": "v23",
  "lastModified": "2022-09-27",
  "files": {
  "200": "http://fonts.gstatic.com/s/notoseriftc/v23/XLY9IZb5bJNDGYxLBibeHZ0Bvr8vbX9GTsoOAX4.otf",
  "300": "http://fonts.gstatic.com/s/notoseriftc/v23/XLY9IZb5bJNDGYxLBibeHZ0BvtssbX9GTsoOAX4.otf",
  "500": "http://fonts.gstatic.com/s/notoseriftc/v23/XLY9IZb5bJNDGYxLBibeHZ0BvoMtbX9GTsoOAX4.otf",
  "600": "http://fonts.gstatic.com/s/notoseriftc/v23/XLY9IZb5bJNDGYxLBibeHZ0Bvq8qbX9GTsoOAX4.otf",
  "700": "http://fonts.gstatic.com/s/notoseriftc/v23/XLY9IZb5bJNDGYxLBibeHZ0BvssrbX9GTsoOAX4.otf",
  "900": "http://fonts.gstatic.com/s/notoseriftc/v23/XLY9IZb5bJNDGYxLBibeHZ0BvvMpbX9GTsoOAX4.otf",
  "regular": "http://fonts.gstatic.com/s/notoseriftc/v23/XLYgIZb5bJNDGYxLBibeHZ0BhnEESXFtUsM.otf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Tamil",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjndHr-klIgTfc40komjQ5OObazYp-6H94dBF-RX6nNRJfi-Gf55IgAecattN6R8Pz3v8Etew.ttf",
  "200": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjndHr-klIgTfc40komjQ5OObazYp-6H94dBF-RX6nNRJfi-Gf55IgAecatNN-R8Pz3v8Etew.ttf",
  "300": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjndHr-klIgTfc40komjQ5OObazYp-6H94dBF-RX6nNRJfi-Gf55IgAecat6t-R8Pz3v8Etew.ttf",
  "500": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjndHr-klIgTfc40komjQ5OObazYp-6H94dBF-RX6nNRJfi-Gf55IgAecatht-R8Pz3v8Etew.ttf",
  "600": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjndHr-klIgTfc40komjQ5OObazYp-6H94dBF-RX6nNRJfi-Gf55IgAecatatiR8Pz3v8Etew.ttf",
  "700": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjndHr-klIgTfc40komjQ5OObazYp-6H94dBF-RX6nNRJfi-Gf55IgAecatU9iR8Pz3v8Etew.ttf",
  "800": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjndHr-klIgTfc40komjQ5OObazYp-6H94dBF-RX6nNRJfi-Gf55IgAecatNNiR8Pz3v8Etew.ttf",
  "900": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjndHr-klIgTfc40komjQ5OObazYp-6H94dBF-RX6nNRJfi-Gf55IgAecatHdiR8Pz3v8Etew.ttf",
  "regular": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjndHr-klIgTfc40komjQ5OObazYp-6H94dBF-RX6nNRJfi-Gf55IgAecattN-R8Pz3v8Etew.ttf",
  "100italic": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjldHr-klIgTfc40komjQ5OObazSJaI_D5kV8k_WLwFBmWrypghjeOa18G4fJx5svbzncQ9e3wx.ttf",
  "200italic": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjldHr-klIgTfc40komjQ5OObazSJaI_D5kV8k_WLwFBmWrypghjeOa18G4fJz5s_bzncQ9e3wx.ttf",
  "300italic": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjldHr-klIgTfc40komjQ5OObazSJaI_D5kV8k_WLwFBmWrypghjeOa18G4fJwns_bzncQ9e3wx.ttf",
  "italic": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjldHr-klIgTfc40komjQ5OObazSJaI_D5kV8k_WLwFBmWrypghjeOa18G4fJx5s_bzncQ9e3wx.ttf",
  "500italic": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjldHr-klIgTfc40komjQ5OObazSJaI_D5kV8k_WLwFBmWrypghjeOa18G4fJxLs_bzncQ9e3wx.ttf",
  "600italic": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjldHr-klIgTfc40komjQ5OObazSJaI_D5kV8k_WLwFBmWrypghjeOa18G4fJyntPbzncQ9e3wx.ttf",
  "700italic": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjldHr-klIgTfc40komjQ5OObazSJaI_D5kV8k_WLwFBmWrypghjeOa18G4fJyetPbzncQ9e3wx.ttf",
  "800italic": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjldHr-klIgTfc40komjQ5OObazSJaI_D5kV8k_WLwFBmWrypghjeOa18G4fJz5tPbzncQ9e3wx.ttf",
  "900italic": "http://fonts.gstatic.com/s/notoseriftamil/v21/LYjldHr-klIgTfc40komjQ5OObazSJaI_D5kV8k_WLwFBmWrypghjeOa18G4fJzQtPbzncQ9e3wx.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Tangut",
  "variants": [
  "regular"
  ],
  "subsets": [
  "tangut"
  ],
  "version": "v15",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/notoseriftangut/v15/xn76YGc72GKoTvER4Gn3b4m9Ern7Em41fcvN2KT4.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Telugu",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "telugu"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoseriftelugu/v20/tDbl2pCbnkEKmXNVmt2M1q6f4HWbbj6MRbYEeav7Fe9D9TGwuY2fjgrZYA.ttf",
  "200": "http://fonts.gstatic.com/s/notoseriftelugu/v20/tDbl2pCbnkEKmXNVmt2M1q6f4HWbbj6MRbYEeav7Fe9DdTCwuY2fjgrZYA.ttf",
  "300": "http://fonts.gstatic.com/s/notoseriftelugu/v20/tDbl2pCbnkEKmXNVmt2M1q6f4HWbbj6MRbYEeav7Fe9DqzCwuY2fjgrZYA.ttf",
  "500": "http://fonts.gstatic.com/s/notoseriftelugu/v20/tDbl2pCbnkEKmXNVmt2M1q6f4HWbbj6MRbYEeav7Fe9DxzCwuY2fjgrZYA.ttf",
  "600": "http://fonts.gstatic.com/s/notoseriftelugu/v20/tDbl2pCbnkEKmXNVmt2M1q6f4HWbbj6MRbYEeav7Fe9DKzewuY2fjgrZYA.ttf",
  "700": "http://fonts.gstatic.com/s/notoseriftelugu/v20/tDbl2pCbnkEKmXNVmt2M1q6f4HWbbj6MRbYEeav7Fe9DEjewuY2fjgrZYA.ttf",
  "800": "http://fonts.gstatic.com/s/notoseriftelugu/v20/tDbl2pCbnkEKmXNVmt2M1q6f4HWbbj6MRbYEeav7Fe9DdTewuY2fjgrZYA.ttf",
  "900": "http://fonts.gstatic.com/s/notoseriftelugu/v20/tDbl2pCbnkEKmXNVmt2M1q6f4HWbbj6MRbYEeav7Fe9DXDewuY2fjgrZYA.ttf",
  "regular": "http://fonts.gstatic.com/s/notoseriftelugu/v20/tDbl2pCbnkEKmXNVmt2M1q6f4HWbbj6MRbYEeav7Fe9D9TCwuY2fjgrZYA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Thai",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoserifthai/v19/k3kyo80MPvpLmixYH7euCxWpSMu3-gcWGj0hHAKGvUQlUv_bCKDUSzB5L0oiFuRRCmsdu0Qx.ttf",
  "200": "http://fonts.gstatic.com/s/notoserifthai/v19/k3kyo80MPvpLmixYH7euCxWpSMu3-gcWGj0hHAKGvUQlUv_bCKDUSzB5L0qiF-RRCmsdu0Qx.ttf",
  "300": "http://fonts.gstatic.com/s/notoserifthai/v19/k3kyo80MPvpLmixYH7euCxWpSMu3-gcWGj0hHAKGvUQlUv_bCKDUSzB5L0p8F-RRCmsdu0Qx.ttf",
  "500": "http://fonts.gstatic.com/s/notoserifthai/v19/k3kyo80MPvpLmixYH7euCxWpSMu3-gcWGj0hHAKGvUQlUv_bCKDUSzB5L0oQF-RRCmsdu0Qx.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifthai/v19/k3kyo80MPvpLmixYH7euCxWpSMu3-gcWGj0hHAKGvUQlUv_bCKDUSzB5L0r8EORRCmsdu0Qx.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifthai/v19/k3kyo80MPvpLmixYH7euCxWpSMu3-gcWGj0hHAKGvUQlUv_bCKDUSzB5L0rFEORRCmsdu0Qx.ttf",
  "800": "http://fonts.gstatic.com/s/notoserifthai/v19/k3kyo80MPvpLmixYH7euCxWpSMu3-gcWGj0hHAKGvUQlUv_bCKDUSzB5L0qiEORRCmsdu0Qx.ttf",
  "900": "http://fonts.gstatic.com/s/notoserifthai/v19/k3kyo80MPvpLmixYH7euCxWpSMu3-gcWGj0hHAKGvUQlUv_bCKDUSzB5L0qLEORRCmsdu0Qx.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifthai/v19/k3kyo80MPvpLmixYH7euCxWpSMu3-gcWGj0hHAKGvUQlUv_bCKDUSzB5L0oiF-RRCmsdu0Qx.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Tibetan",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "tibetan"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/notoseriftibetan/v16/gokGH7nwAEdtF9N45n0Vaz7O-pk0wsvxHeDXMfqguoCmIrYdPS7rdSy_32c.ttf",
  "200": "http://fonts.gstatic.com/s/notoseriftibetan/v16/gokGH7nwAEdtF9N45n0Vaz7O-pk0wsvxHeDXMfqguoCmIjYcPS7rdSy_32c.ttf",
  "300": "http://fonts.gstatic.com/s/notoseriftibetan/v16/gokGH7nwAEdtF9N45n0Vaz7O-pk0wsvxHeDXMfqguoCmIugcPS7rdSy_32c.ttf",
  "500": "http://fonts.gstatic.com/s/notoseriftibetan/v16/gokGH7nwAEdtF9N45n0Vaz7O-pk0wsvxHeDXMfqguoCmIoQcPS7rdSy_32c.ttf",
  "600": "http://fonts.gstatic.com/s/notoseriftibetan/v16/gokGH7nwAEdtF9N45n0Vaz7O-pk0wsvxHeDXMfqguoCmImgbPS7rdSy_32c.ttf",
  "700": "http://fonts.gstatic.com/s/notoseriftibetan/v16/gokGH7nwAEdtF9N45n0Vaz7O-pk0wsvxHeDXMfqguoCmIlEbPS7rdSy_32c.ttf",
  "800": "http://fonts.gstatic.com/s/notoseriftibetan/v16/gokGH7nwAEdtF9N45n0Vaz7O-pk0wsvxHeDXMfqguoCmIjYbPS7rdSy_32c.ttf",
  "900": "http://fonts.gstatic.com/s/notoseriftibetan/v16/gokGH7nwAEdtF9N45n0Vaz7O-pk0wsvxHeDXMfqguoCmIh8bPS7rdSy_32c.ttf",
  "regular": "http://fonts.gstatic.com/s/notoseriftibetan/v16/gokGH7nwAEdtF9N45n0Vaz7O-pk0wsvxHeDXMfqguoCmIrYcPS7rdSy_32c.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Serif Yezidi",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "yezidi"
  ],
  "version": "v16",
  "lastModified": "2022-07-19",
  "files": {
  "500": "http://fonts.gstatic.com/s/notoserifyezidi/v16/XLYPIYr5bJNDGYxLBibeHZAn3B5KJENnQjbfhMSVZspD6SEkrlGJgmVCqg.ttf",
  "600": "http://fonts.gstatic.com/s/notoserifyezidi/v16/XLYPIYr5bJNDGYxLBibeHZAn3B5KJENnQjbfhMSVZspDBSYkrlGJgmVCqg.ttf",
  "700": "http://fonts.gstatic.com/s/notoserifyezidi/v16/XLYPIYr5bJNDGYxLBibeHZAn3B5KJENnQjbfhMSVZspDPCYkrlGJgmVCqg.ttf",
  "regular": "http://fonts.gstatic.com/s/notoserifyezidi/v16/XLYPIYr5bJNDGYxLBibeHZAn3B5KJENnQjbfhMSVZspD2yEkrlGJgmVCqg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Noto Traditional Nushu",
  "variants": [
  "regular"
  ],
  "subsets": [
  "nushu"
  ],
  "version": "v16",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/nototraditionalnushu/v16/SZco3EDkJ7q9FaoMPlmF4Su8hlIjoGh5aj67J011GNh6SYA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nova Cut",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/novacut/v24/KFOkCnSYu8mL-39LkWxPKTM1K9nz.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nova Flat",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/novaflat/v24/QdVUSTc-JgqpytEbVebEuStkm20oJA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nova Mono",
  "variants": [
  "regular"
  ],
  "subsets": [
  "greek",
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/novamono/v18/Cn-0JtiGWQ5Ajb--MRKfYGxYrdM9Sg.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nova Oval",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/novaoval/v24/jAnEgHdmANHvPenMaswCMY-h3cWkWg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nova Round",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/novaround/v21/flU9Rqquw5UhEnlwTJYTYYfeeetYEBc.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nova Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/novascript/v25/7Au7p_IpkSWSTWaFWkumvmQNEl0O0kEx.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nova Slim",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/novaslim/v24/Z9XUDmZNQAuem8jyZcn-yMOInrib9Q.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nova Square",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/novasquare/v20/RrQUbo9-9DV7b06QHgSWsZhARYMgGtWA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Numans",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/numans/v15/SlGRmQmGupYAfH8IYRggiHVqaQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nunito",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/nunito/v25/XRXI3I6Li01BKofiOc5wtlZ2di8HDDshRTM9jo7eTWk.ttf",
  "300": "http://fonts.gstatic.com/s/nunito/v25/XRXI3I6Li01BKofiOc5wtlZ2di8HDOUhRTM9jo7eTWk.ttf",
  "500": "http://fonts.gstatic.com/s/nunito/v25/XRXI3I6Li01BKofiOc5wtlZ2di8HDIkhRTM9jo7eTWk.ttf",
  "600": "http://fonts.gstatic.com/s/nunito/v25/XRXI3I6Li01BKofiOc5wtlZ2di8HDGUmRTM9jo7eTWk.ttf",
  "700": "http://fonts.gstatic.com/s/nunito/v25/XRXI3I6Li01BKofiOc5wtlZ2di8HDFwmRTM9jo7eTWk.ttf",
  "800": "http://fonts.gstatic.com/s/nunito/v25/XRXI3I6Li01BKofiOc5wtlZ2di8HDDsmRTM9jo7eTWk.ttf",
  "900": "http://fonts.gstatic.com/s/nunito/v25/XRXI3I6Li01BKofiOc5wtlZ2di8HDBImRTM9jo7eTWk.ttf",
  "regular": "http://fonts.gstatic.com/s/nunito/v25/XRXI3I6Li01BKofiOc5wtlZ2di8HDLshRTM9jo7eTWk.ttf",
  "200italic": "http://fonts.gstatic.com/s/nunito/v25/XRXK3I6Li01BKofIMPyPbj8d7IEAGXNiLXA3iqzbXWnoeg.ttf",
  "300italic": "http://fonts.gstatic.com/s/nunito/v25/XRXK3I6Li01BKofIMPyPbj8d7IEAGXNi83A3iqzbXWnoeg.ttf",
  "italic": "http://fonts.gstatic.com/s/nunito/v25/XRXK3I6Li01BKofIMPyPbj8d7IEAGXNirXA3iqzbXWnoeg.ttf",
  "500italic": "http://fonts.gstatic.com/s/nunito/v25/XRXK3I6Li01BKofIMPyPbj8d7IEAGXNin3A3iqzbXWnoeg.ttf",
  "600italic": "http://fonts.gstatic.com/s/nunito/v25/XRXK3I6Li01BKofIMPyPbj8d7IEAGXNic3c3iqzbXWnoeg.ttf",
  "700italic": "http://fonts.gstatic.com/s/nunito/v25/XRXK3I6Li01BKofIMPyPbj8d7IEAGXNiSnc3iqzbXWnoeg.ttf",
  "800italic": "http://fonts.gstatic.com/s/nunito/v25/XRXK3I6Li01BKofIMPyPbj8d7IEAGXNiLXc3iqzbXWnoeg.ttf",
  "900italic": "http://fonts.gstatic.com/s/nunito/v25/XRXK3I6Li01BKofIMPyPbj8d7IEAGXNiBHc3iqzbXWnoeg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nunito Sans",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/nunitosans/v12/pe03MImSLYBIv1o4X1M8cc9yAv5qWVAgVol-.ttf",
  "300": "http://fonts.gstatic.com/s/nunitosans/v12/pe03MImSLYBIv1o4X1M8cc8WAf5qWVAgVol-.ttf",
  "600": "http://fonts.gstatic.com/s/nunitosans/v12/pe03MImSLYBIv1o4X1M8cc9iB_5qWVAgVol-.ttf",
  "700": "http://fonts.gstatic.com/s/nunitosans/v12/pe03MImSLYBIv1o4X1M8cc8GBv5qWVAgVol-.ttf",
  "800": "http://fonts.gstatic.com/s/nunitosans/v12/pe03MImSLYBIv1o4X1M8cc8aBf5qWVAgVol-.ttf",
  "900": "http://fonts.gstatic.com/s/nunitosans/v12/pe03MImSLYBIv1o4X1M8cc8-BP5qWVAgVol-.ttf",
  "200italic": "http://fonts.gstatic.com/s/nunitosans/v12/pe01MImSLYBIv1o4X1M8cce4GxZrU1QCU5l-06Y.ttf",
  "300italic": "http://fonts.gstatic.com/s/nunitosans/v12/pe01MImSLYBIv1o4X1M8cce4G3JoU1QCU5l-06Y.ttf",
  "regular": "http://fonts.gstatic.com/s/nunitosans/v12/pe0qMImSLYBIv1o4X1M8cfe6Kdpickwp.ttf",
  "italic": "http://fonts.gstatic.com/s/nunitosans/v12/pe0oMImSLYBIv1o4X1M8cce4I95Ad1wpT5A.ttf",
  "600italic": "http://fonts.gstatic.com/s/nunitosans/v12/pe01MImSLYBIv1o4X1M8cce4GwZuU1QCU5l-06Y.ttf",
  "700italic": "http://fonts.gstatic.com/s/nunitosans/v12/pe01MImSLYBIv1o4X1M8cce4G2JvU1QCU5l-06Y.ttf",
  "800italic": "http://fonts.gstatic.com/s/nunitosans/v12/pe01MImSLYBIv1o4X1M8cce4G35sU1QCU5l-06Y.ttf",
  "900italic": "http://fonts.gstatic.com/s/nunitosans/v12/pe01MImSLYBIv1o4X1M8cce4G1ptU1QCU5l-06Y.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Nuosu SIL",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "yi"
  ],
  "version": "v2",
  "lastModified": "2022-09-28",
  "files": {
  "regular": "http://fonts.gstatic.com/s/nuosusil/v2/8vIK7wM3wmRn_kc4uAjeFGxbO_zo-w.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Odibee Sans",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/odibeesans/v14/neIPzCSooYAho6WvjeToRYkyepH9qGsf.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Odor Mean Chey",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v27",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/odormeanchey/v27/raxkHiKDttkTe1aOGcJMR1A_4mrY2zqUKafv.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Offside",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/offside/v20/HI_KiYMWKa9QrAykQ5HiRp-dhpQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "tamil",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/oi/v15/w8gXH2EuRqtaut6yjBOG.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Old Standard TT",
  "variants": [
  "regular",
  "italic",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/oldstandardtt/v18/MwQrbh3o1vLImiwAVvYawgcf2eVWEX-dTFxeb80flQ.ttf",
  "regular": "http://fonts.gstatic.com/s/oldstandardtt/v18/MwQubh3o1vLImiwAVvYawgcf2eVurVC5RHdCZg.ttf",
  "italic": "http://fonts.gstatic.com/s/oldstandardtt/v18/MwQsbh3o1vLImiwAVvYawgcf2eVer1q9ZnJSZtQG.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oldenburg",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/oldenburg/v20/fC1jPY5JYWzbywv7c4V6UU6oXyndrw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ole",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ole/v3/dFazZf6Z-rd89fw69qJ_ew.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oleo Script",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-05-10",
  "files": {
  "700": "http://fonts.gstatic.com/s/oleoscript/v14/raxkHieDvtMOe0iICsUccCDmnmrY2zqUKafv.ttf",
  "regular": "http://fonts.gstatic.com/s/oleoscript/v14/rax5HieDvtMOe0iICsUccBhasU7Q8Cad.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oleo Script Swash Caps",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-05-10",
  "files": {
  "700": "http://fonts.gstatic.com/s/oleoscriptswashcaps/v13/Noag6Vb-w5SFbTTAsZP_7JkCS08K-jCzDn_HCcaBbYUsn9T5dt0.ttf",
  "regular": "http://fonts.gstatic.com/s/oleoscriptswashcaps/v13/Noaj6Vb-w5SFbTTAsZP_7JkCS08K-jCzDn_HMXquSY0Hg90.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oooh Baby",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ooohbaby/v3/2sDcZGJWgJTT2Jf76xQDb2-4C7wFZQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Open Sans",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "hebrew",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v34",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/opensans/v34/memSYaGs126MiZpBA-UvWbX2vVnXBbObj2OVZyOOSr4dVJWUgsiH0C4nY1M2xLER.ttf",
  "500": "http://fonts.gstatic.com/s/opensans/v34/memSYaGs126MiZpBA-UvWbX2vVnXBbObj2OVZyOOSr4dVJWUgsjr0C4nY1M2xLER.ttf",
  "600": "http://fonts.gstatic.com/s/opensans/v34/memSYaGs126MiZpBA-UvWbX2vVnXBbObj2OVZyOOSr4dVJWUgsgH1y4nY1M2xLER.ttf",
  "700": "http://fonts.gstatic.com/s/opensans/v34/memSYaGs126MiZpBA-UvWbX2vVnXBbObj2OVZyOOSr4dVJWUgsg-1y4nY1M2xLER.ttf",
  "800": "http://fonts.gstatic.com/s/opensans/v34/memSYaGs126MiZpBA-UvWbX2vVnXBbObj2OVZyOOSr4dVJWUgshZ1y4nY1M2xLER.ttf",
  "regular": "http://fonts.gstatic.com/s/opensans/v34/memSYaGs126MiZpBA-UvWbX2vVnXBbObj2OVZyOOSr4dVJWUgsjZ0C4nY1M2xLER.ttf",
  "300italic": "http://fonts.gstatic.com/s/opensans/v34/memQYaGs126MiZpBA-UFUIcVXSCEkx2cmqvXlWq8tWZ0Pw86hd0Rk5hkaVcUwaERZjA.ttf",
  "italic": "http://fonts.gstatic.com/s/opensans/v34/memQYaGs126MiZpBA-UFUIcVXSCEkx2cmqvXlWq8tWZ0Pw86hd0Rk8ZkaVcUwaERZjA.ttf",
  "500italic": "http://fonts.gstatic.com/s/opensans/v34/memQYaGs126MiZpBA-UFUIcVXSCEkx2cmqvXlWq8tWZ0Pw86hd0Rk_RkaVcUwaERZjA.ttf",
  "600italic": "http://fonts.gstatic.com/s/opensans/v34/memQYaGs126MiZpBA-UFUIcVXSCEkx2cmqvXlWq8tWZ0Pw86hd0RkxhjaVcUwaERZjA.ttf",
  "700italic": "http://fonts.gstatic.com/s/opensans/v34/memQYaGs126MiZpBA-UFUIcVXSCEkx2cmqvXlWq8tWZ0Pw86hd0RkyFjaVcUwaERZjA.ttf",
  "800italic": "http://fonts.gstatic.com/s/opensans/v34/memQYaGs126MiZpBA-UFUIcVXSCEkx2cmqvXlWq8tWZ0Pw86hd0Rk0ZjaVcUwaERZjA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oranienbaum",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/oranienbaum/v15/OZpHg_txtzZKMuXLIVrx-3zn7kz3dpHc.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Orbitron",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/orbitron/v25/yMJMMIlzdpvBhQQL_SC3X9yhF25-T1nyKS6xpmIyXjU1pg.ttf",
  "600": "http://fonts.gstatic.com/s/orbitron/v25/yMJMMIlzdpvBhQQL_SC3X9yhF25-T1nyxSmxpmIyXjU1pg.ttf",
  "700": "http://fonts.gstatic.com/s/orbitron/v25/yMJMMIlzdpvBhQQL_SC3X9yhF25-T1ny_CmxpmIyXjU1pg.ttf",
  "800": "http://fonts.gstatic.com/s/orbitron/v25/yMJMMIlzdpvBhQQL_SC3X9yhF25-T1nymymxpmIyXjU1pg.ttf",
  "900": "http://fonts.gstatic.com/s/orbitron/v25/yMJMMIlzdpvBhQQL_SC3X9yhF25-T1nysimxpmIyXjU1pg.ttf",
  "regular": "http://fonts.gstatic.com/s/orbitron/v25/yMJMMIlzdpvBhQQL_SC3X9yhF25-T1nyGy6xpmIyXjU1pg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oregano",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/oregano/v13/If2IXTPxciS3H4S2kZffPznO3yM.ttf",
  "italic": "http://fonts.gstatic.com/s/oregano/v13/If2KXTPxciS3H4S2oZXVOxvLzyP_qw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Orelega One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/orelegaone/v10/3qTpojOggD2XtAdFb-QXZGt61EcYaQ7F.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Orienta",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/orienta/v13/PlI9FlK4Jrl5Y9zNeyeo9HRFhcU.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Original Surfer",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/originalsurfer/v18/RWmQoKGZ9vIirYntXJ3_MbekzNMiDEtvAlaMKw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oswald",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v49",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/oswald/v49/TK3_WkUHHAIjg75cFRf3bXL8LICs13FvgUFoZAaRliE.ttf",
  "300": "http://fonts.gstatic.com/s/oswald/v49/TK3_WkUHHAIjg75cFRf3bXL8LICs169vgUFoZAaRliE.ttf",
  "500": "http://fonts.gstatic.com/s/oswald/v49/TK3_WkUHHAIjg75cFRf3bXL8LICs18NvgUFoZAaRliE.ttf",
  "600": "http://fonts.gstatic.com/s/oswald/v49/TK3_WkUHHAIjg75cFRf3bXL8LICs1y9ogUFoZAaRliE.ttf",
  "700": "http://fonts.gstatic.com/s/oswald/v49/TK3_WkUHHAIjg75cFRf3bXL8LICs1xZogUFoZAaRliE.ttf",
  "regular": "http://fonts.gstatic.com/s/oswald/v49/TK3_WkUHHAIjg75cFRf3bXL8LICs1_FvgUFoZAaRliE.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Outfit",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v6",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/outfit/v6/QGYyz_MVcBeNP4NjuGObqx1XmO1I4TC0C4G-EiAou6Y.ttf",
  "200": "http://fonts.gstatic.com/s/outfit/v6/QGYyz_MVcBeNP4NjuGObqx1XmO1I4bC1C4G-EiAou6Y.ttf",
  "300": "http://fonts.gstatic.com/s/outfit/v6/QGYyz_MVcBeNP4NjuGObqx1XmO1I4W61C4G-EiAou6Y.ttf",
  "500": "http://fonts.gstatic.com/s/outfit/v6/QGYyz_MVcBeNP4NjuGObqx1XmO1I4QK1C4G-EiAou6Y.ttf",
  "600": "http://fonts.gstatic.com/s/outfit/v6/QGYyz_MVcBeNP4NjuGObqx1XmO1I4e6yC4G-EiAou6Y.ttf",
  "700": "http://fonts.gstatic.com/s/outfit/v6/QGYyz_MVcBeNP4NjuGObqx1XmO1I4deyC4G-EiAou6Y.ttf",
  "800": "http://fonts.gstatic.com/s/outfit/v6/QGYyz_MVcBeNP4NjuGObqx1XmO1I4bCyC4G-EiAou6Y.ttf",
  "900": "http://fonts.gstatic.com/s/outfit/v6/QGYyz_MVcBeNP4NjuGObqx1XmO1I4ZmyC4G-EiAou6Y.ttf",
  "regular": "http://fonts.gstatic.com/s/outfit/v6/QGYyz_MVcBeNP4NjuGObqx1XmO1I4TC1C4G-EiAou6Y.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Over the Rainbow",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/overtherainbow/v16/11haGoXG1k_HKhMLUWz7Mc7vvW5upvOm9NA2XG0.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Overlock",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/overlock/v15/Z9XSDmdMWRiN1_T9Z7xizcmMvL2L9TLT.ttf",
  "900": "http://fonts.gstatic.com/s/overlock/v15/Z9XSDmdMWRiN1_T9Z7xaz8mMvL2L9TLT.ttf",
  "regular": "http://fonts.gstatic.com/s/overlock/v15/Z9XVDmdMWRiN1_T9Z4Te4u2El6GC.ttf",
  "italic": "http://fonts.gstatic.com/s/overlock/v15/Z9XTDmdMWRiN1_T9Z7Tc6OmmkrGC7Cs.ttf",
  "700italic": "http://fonts.gstatic.com/s/overlock/v15/Z9XQDmdMWRiN1_T9Z7Tc0FWJtrmp8CLTlNs.ttf",
  "900italic": "http://fonts.gstatic.com/s/overlock/v15/Z9XQDmdMWRiN1_T9Z7Tc0G2Ltrmp8CLTlNs.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Overlock SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/overlocksc/v21/1cX3aUHKGZrstGAY8nwVzHGAq8Sk1PoH.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Overpass",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/overpass/v12/qFda35WCmI96Ajtm83upeyoaX6QPnlo6_PLrOZCLtce-og.ttf",
  "200": "http://fonts.gstatic.com/s/overpass/v12/qFda35WCmI96Ajtm83upeyoaX6QPnlo6fPPrOZCLtce-og.ttf",
  "300": "http://fonts.gstatic.com/s/overpass/v12/qFda35WCmI96Ajtm83upeyoaX6QPnlo6ovPrOZCLtce-og.ttf",
  "500": "http://fonts.gstatic.com/s/overpass/v12/qFda35WCmI96Ajtm83upeyoaX6QPnlo6zvPrOZCLtce-og.ttf",
  "600": "http://fonts.gstatic.com/s/overpass/v12/qFda35WCmI96Ajtm83upeyoaX6QPnlo6IvTrOZCLtce-og.ttf",
  "700": "http://fonts.gstatic.com/s/overpass/v12/qFda35WCmI96Ajtm83upeyoaX6QPnlo6G_TrOZCLtce-og.ttf",
  "800": "http://fonts.gstatic.com/s/overpass/v12/qFda35WCmI96Ajtm83upeyoaX6QPnlo6fPTrOZCLtce-og.ttf",
  "900": "http://fonts.gstatic.com/s/overpass/v12/qFda35WCmI96Ajtm83upeyoaX6QPnlo6VfTrOZCLtce-og.ttf",
  "regular": "http://fonts.gstatic.com/s/overpass/v12/qFda35WCmI96Ajtm83upeyoaX6QPnlo6_PPrOZCLtce-og.ttf",
  "100italic": "http://fonts.gstatic.com/s/overpass/v12/qFdU35WCmI96Ajtm81GgSdXCNs-VMF0vNLADe5qPl8Kuosgz.ttf",
  "200italic": "http://fonts.gstatic.com/s/overpass/v12/qFdU35WCmI96Ajtm81GgSdXCNs-VMF0vNLCDepqPl8Kuosgz.ttf",
  "300italic": "http://fonts.gstatic.com/s/overpass/v12/qFdU35WCmI96Ajtm81GgSdXCNs-VMF0vNLBdepqPl8Kuosgz.ttf",
  "italic": "http://fonts.gstatic.com/s/overpass/v12/qFdU35WCmI96Ajtm81GgSdXCNs-VMF0vNLADepqPl8Kuosgz.ttf",
  "500italic": "http://fonts.gstatic.com/s/overpass/v12/qFdU35WCmI96Ajtm81GgSdXCNs-VMF0vNLAxepqPl8Kuosgz.ttf",
  "600italic": "http://fonts.gstatic.com/s/overpass/v12/qFdU35WCmI96Ajtm81GgSdXCNs-VMF0vNLDdfZqPl8Kuosgz.ttf",
  "700italic": "http://fonts.gstatic.com/s/overpass/v12/qFdU35WCmI96Ajtm81GgSdXCNs-VMF0vNLDkfZqPl8Kuosgz.ttf",
  "800italic": "http://fonts.gstatic.com/s/overpass/v12/qFdU35WCmI96Ajtm81GgSdXCNs-VMF0vNLCDfZqPl8Kuosgz.ttf",
  "900italic": "http://fonts.gstatic.com/s/overpass/v12/qFdU35WCmI96Ajtm81GgSdXCNs-VMF0vNLCqfZqPl8Kuosgz.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Overpass Mono",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/overpassmono/v15/_Xm5-H86tzKDdAPa-KPQZ-AC_COcRycquHlL6EWKokzzXur-SmIr.ttf",
  "500": "http://fonts.gstatic.com/s/overpassmono/v15/_Xm5-H86tzKDdAPa-KPQZ-AC_COcRycquHlL6EXmokzzXur-SmIr.ttf",
  "600": "http://fonts.gstatic.com/s/overpassmono/v15/_Xm5-H86tzKDdAPa-KPQZ-AC_COcRycquHlL6EUKpUzzXur-SmIr.ttf",
  "700": "http://fonts.gstatic.com/s/overpassmono/v15/_Xm5-H86tzKDdAPa-KPQZ-AC_COcRycquHlL6EUzpUzzXur-SmIr.ttf",
  "regular": "http://fonts.gstatic.com/s/overpassmono/v15/_Xm5-H86tzKDdAPa-KPQZ-AC_COcRycquHlL6EXUokzzXur-SmIr.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ovo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ovo/v17/yYLl0h7Wyfzjy4Q5_3WVxA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oxanium",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/oxanium/v14/RrQPboN_4yJ0JmiMUW7sIGjd1IA9G83JfniMBXQ7d67x.ttf",
  "300": "http://fonts.gstatic.com/s/oxanium/v14/RrQPboN_4yJ0JmiMUW7sIGjd1IA9G80XfniMBXQ7d67x.ttf",
  "500": "http://fonts.gstatic.com/s/oxanium/v14/RrQPboN_4yJ0JmiMUW7sIGjd1IA9G817fniMBXQ7d67x.ttf",
  "600": "http://fonts.gstatic.com/s/oxanium/v14/RrQPboN_4yJ0JmiMUW7sIGjd1IA9G82XeXiMBXQ7d67x.ttf",
  "700": "http://fonts.gstatic.com/s/oxanium/v14/RrQPboN_4yJ0JmiMUW7sIGjd1IA9G82ueXiMBXQ7d67x.ttf",
  "800": "http://fonts.gstatic.com/s/oxanium/v14/RrQPboN_4yJ0JmiMUW7sIGjd1IA9G83JeXiMBXQ7d67x.ttf",
  "regular": "http://fonts.gstatic.com/s/oxanium/v14/RrQPboN_4yJ0JmiMUW7sIGjd1IA9G81JfniMBXQ7d67x.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oxygen",
  "variants": [
  "300",
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/oxygen/v15/2sDcZG1Wl4LcnbuCJW8Db2-4C7wFZQ.ttf",
  "700": "http://fonts.gstatic.com/s/oxygen/v15/2sDcZG1Wl4LcnbuCNWgDb2-4C7wFZQ.ttf",
  "regular": "http://fonts.gstatic.com/s/oxygen/v15/2sDfZG1Wl4Lcnbu6iUcnZ0SkAg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Oxygen Mono",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/oxygenmono/v13/h0GsssGg9FxgDgCjLeAd7ijfze-PPlUu.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "PT Mono",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ptmono/v13/9oRONYoBnWILk-9ArCg5MtPyAcg.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "PT Sans",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/ptsans/v17/jizfRExUiTo99u79B_mh4OmnLD0Z4zM.ttf",
  "regular": "http://fonts.gstatic.com/s/ptsans/v17/jizaRExUiTo99u79P0WOxOGMMDQ.ttf",
  "italic": "http://fonts.gstatic.com/s/ptsans/v17/jizYRExUiTo99u79D0eEwMOJIDQA-g.ttf",
  "700italic": "http://fonts.gstatic.com/s/ptsans/v17/jizdRExUiTo99u79D0e8fOytKB8c8zMrig.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "PT Sans Caption",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/ptsanscaption/v18/0FlJVP6Hrxmt7-fsUFhlFXNIlpcSwSrUSwWuz38Tgg.ttf",
  "regular": "http://fonts.gstatic.com/s/ptsanscaption/v18/0FlMVP6Hrxmt7-fsUFhlFXNIlpcqfQXwQy6yxg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "PT Sans Narrow",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/ptsansnarrow/v17/BngSUXNadjH0qYEzV7ab-oWlsbg95DiCUfzgRd-3.ttf",
  "regular": "http://fonts.gstatic.com/s/ptsansnarrow/v17/BngRUXNadjH0qYEzV7ab-oWlsYCByxyKeuDp.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "PT Serif",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/ptserif/v17/EJRSQgYoZZY2vCFuvAnt65qVXSr3pNNB.ttf",
  "regular": "http://fonts.gstatic.com/s/ptserif/v17/EJRVQgYoZZY2vCFuvDFRxL6ddjb-.ttf",
  "italic": "http://fonts.gstatic.com/s/ptserif/v17/EJRTQgYoZZY2vCFuvAFTzrq_cyb-vco.ttf",
  "700italic": "http://fonts.gstatic.com/s/ptserif/v17/EJRQQgYoZZY2vCFuvAFT9gaQVy7VocNB6Iw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "PT Serif Caption",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ptserifcaption/v17/ieVl2ZhbGCW-JoW6S34pSDpqYKU059WxDCs5cvI.ttf",
  "italic": "http://fonts.gstatic.com/s/ptserifcaption/v17/ieVj2ZhbGCW-JoW6S34pSDpqYKU019e7CAk8YvJEeg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pacifico",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pacifico/v22/FwZY7-Qmy14u9lezJ96A4sijpFu_.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Padauk",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "myanmar"
  ],
  "version": "v15",
  "lastModified": "2022-09-28",
  "files": {
  "700": "http://fonts.gstatic.com/s/padauk/v15/RrQSboJg-id7Onb512DE1JJEZ4YwGg.ttf",
  "regular": "http://fonts.gstatic.com/s/padauk/v15/RrQRboJg-id7OnbBa0_g3LlYbg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Palanquin",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/palanquin/v13/9XUhlJ90n1fBFg7ceXwUEltI7rWmZzTH.ttf",
  "200": "http://fonts.gstatic.com/s/palanquin/v13/9XUilJ90n1fBFg7ceXwUvnpoxJuqbi3ezg.ttf",
  "300": "http://fonts.gstatic.com/s/palanquin/v13/9XUilJ90n1fBFg7ceXwU2nloxJuqbi3ezg.ttf",
  "500": "http://fonts.gstatic.com/s/palanquin/v13/9XUilJ90n1fBFg7ceXwUgnhoxJuqbi3ezg.ttf",
  "600": "http://fonts.gstatic.com/s/palanquin/v13/9XUilJ90n1fBFg7ceXwUrn9oxJuqbi3ezg.ttf",
  "700": "http://fonts.gstatic.com/s/palanquin/v13/9XUilJ90n1fBFg7ceXwUyn5oxJuqbi3ezg.ttf",
  "regular": "http://fonts.gstatic.com/s/palanquin/v13/9XUnlJ90n1fBFg7ceXwsdlFMzLC2Zw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Palanquin Dark",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/palanquindark/v12/xn76YHgl1nqmANMB-26xC7yuF8Z6ZW41fcvN2KT4.ttf",
  "600": "http://fonts.gstatic.com/s/palanquindark/v12/xn76YHgl1nqmANMB-26xC7yuF8ZWYm41fcvN2KT4.ttf",
  "700": "http://fonts.gstatic.com/s/palanquindark/v12/xn76YHgl1nqmANMB-26xC7yuF8YyY241fcvN2KT4.ttf",
  "regular": "http://fonts.gstatic.com/s/palanquindark/v12/xn75YHgl1nqmANMB-26xC7yuF_6OTEo9VtfE.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pangolin",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pangolin/v11/cY9GfjGcW0FPpi-tWPfK5d3aiLBG.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Paprika",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/paprika/v21/8QIJdijZitv49rDfuIgOq7jkAOw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Parisienne",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/parisienne/v13/E21i_d3kivvAkxhLEVZpcy96DuKuavM.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Passero One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-05-10",
  "files": {
  "regular": "http://fonts.gstatic.com/s/passeroone/v24/JTUTjIko8DOq5FeaeEAjgE5B5Arr-s50.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Passion One",
  "variants": [
  "regular",
  "700",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/passionone/v16/Pby6FmL8HhTPqbjUzux3JEMq037owpYcuH8y.ttf",
  "900": "http://fonts.gstatic.com/s/passionone/v16/Pby6FmL8HhTPqbjUzux3JEMS0X7owpYcuH8y.ttf",
  "regular": "http://fonts.gstatic.com/s/passionone/v16/PbynFmL8HhTPqbjUzux3JHuW_Frg6YoV.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Passions Conflict",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/passionsconflict/v5/kmKnZrcrFhfafnWX9x0GuEC-zowow5NeYRI4CN2V.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pathway Gothic One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pathwaygothicone/v14/MwQrbgD32-KAvjkYGNUUxAtW7pEBwx-dTFxeb80flQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Patrick Hand",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/patrickhand/v19/LDI1apSQOAYtSuYWp8ZhfYeMWcjKm7sp8g.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Patrick Hand SC",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/patrickhandsc/v13/0nkwC9f7MfsBiWcLtY65AWDK873ViSi6JQc7Vg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pattaya",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pattaya/v12/ea8ZadcqV_zkHY-XNdCn92ZEmVs.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Patua One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/patuaone/v16/ZXuke1cDvLCKLDcimxBI5PNvNA9LuA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pavanam",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pavanam/v11/BXRrvF_aiezLh0xPDOtQ9Wf0QcE.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Paytone One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/paytoneone/v18/0nksC9P7MfYHj2oFtYm2CiTqivr9iBq_.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Peddana",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/peddana/v20/aFTU7PBhaX89UcKWhh2aBYyMcKw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Peralta",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/peralta/v17/hYkJPu0-RP_9d3kRGxAhrv956B8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Permanent Marker",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/permanentmarker/v16/Fh4uPib9Iyv2ucM6pGQMWimMp004HaqIfrT5nlk.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Petemoss",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/petemoss/v5/A2BZn5tA2xgtGWHZgxkesKb9UouQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Petit Formal Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/petitformalscript/v13/B50TF6xQr2TXJBnGOFME6u5OR83oRP5qoHnqP4gZSiE.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Petrona",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v28",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/petrona/v28/mtGl4_NXL7bZo9XXq35wRLONYyOjFk6NsARBH452Mvds.ttf",
  "200": "http://fonts.gstatic.com/s/petrona/v28/mtGl4_NXL7bZo9XXq35wRLONYyOjFk4NsQRBH452Mvds.ttf",
  "300": "http://fonts.gstatic.com/s/petrona/v28/mtGl4_NXL7bZo9XXq35wRLONYyOjFk7TsQRBH452Mvds.ttf",
  "500": "http://fonts.gstatic.com/s/petrona/v28/mtGl4_NXL7bZo9XXq35wRLONYyOjFk6_sQRBH452Mvds.ttf",
  "600": "http://fonts.gstatic.com/s/petrona/v28/mtGl4_NXL7bZo9XXq35wRLONYyOjFk5TtgRBH452Mvds.ttf",
  "700": "http://fonts.gstatic.com/s/petrona/v28/mtGl4_NXL7bZo9XXq35wRLONYyOjFk5qtgRBH452Mvds.ttf",
  "800": "http://fonts.gstatic.com/s/petrona/v28/mtGl4_NXL7bZo9XXq35wRLONYyOjFk4NtgRBH452Mvds.ttf",
  "900": "http://fonts.gstatic.com/s/petrona/v28/mtGl4_NXL7bZo9XXq35wRLONYyOjFk4ktgRBH452Mvds.ttf",
  "regular": "http://fonts.gstatic.com/s/petrona/v28/mtGl4_NXL7bZo9XXq35wRLONYyOjFk6NsQRBH452Mvds.ttf",
  "100italic": "http://fonts.gstatic.com/s/petrona/v28/mtGr4_NXL7bZo9XXgXdCu2vkCLkNEVtF8uwDFYpUN-dsIWs.ttf",
  "200italic": "http://fonts.gstatic.com/s/petrona/v28/mtGr4_NXL7bZo9XXgXdCu2vkCLkNEVtF8mwCFYpUN-dsIWs.ttf",
  "300italic": "http://fonts.gstatic.com/s/petrona/v28/mtGr4_NXL7bZo9XXgXdCu2vkCLkNEVtF8rICFYpUN-dsIWs.ttf",
  "italic": "http://fonts.gstatic.com/s/petrona/v28/mtGr4_NXL7bZo9XXgXdCu2vkCLkNEVtF8uwCFYpUN-dsIWs.ttf",
  "500italic": "http://fonts.gstatic.com/s/petrona/v28/mtGr4_NXL7bZo9XXgXdCu2vkCLkNEVtF8t4CFYpUN-dsIWs.ttf",
  "600italic": "http://fonts.gstatic.com/s/petrona/v28/mtGr4_NXL7bZo9XXgXdCu2vkCLkNEVtF8jIFFYpUN-dsIWs.ttf",
  "700italic": "http://fonts.gstatic.com/s/petrona/v28/mtGr4_NXL7bZo9XXgXdCu2vkCLkNEVtF8gsFFYpUN-dsIWs.ttf",
  "800italic": "http://fonts.gstatic.com/s/petrona/v28/mtGr4_NXL7bZo9XXgXdCu2vkCLkNEVtF8mwFFYpUN-dsIWs.ttf",
  "900italic": "http://fonts.gstatic.com/s/petrona/v28/mtGr4_NXL7bZo9XXgXdCu2vkCLkNEVtF8kUFFYpUN-dsIWs.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Philosopher",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "vietnamese"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/philosopher/v19/vEFI2_5QCwIS4_Dhez5jcWjVamgc-NaXXq7H.ttf",
  "regular": "http://fonts.gstatic.com/s/philosopher/v19/vEFV2_5QCwIS4_Dhez5jcVBpRUwU08qe.ttf",
  "italic": "http://fonts.gstatic.com/s/philosopher/v19/vEFX2_5QCwIS4_Dhez5jcWBrT0g21tqeR7c.ttf",
  "700italic": "http://fonts.gstatic.com/s/philosopher/v19/vEFK2_5QCwIS4_Dhez5jcWBrd_QZ8tK1W77HtMo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Piazzolla",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/piazzolla/v25/N0b52SlTPu5rIkWIZjVKKtYtfxYqZ4RJBFzFfYUjkSDdlqZgy7LYx3Ly1AHfAAy5.ttf",
  "200": "http://fonts.gstatic.com/s/piazzolla/v25/N0b52SlTPu5rIkWIZjVKKtYtfxYqZ4RJBFzFfYUjkSDdlqZgy7JYxnLy1AHfAAy5.ttf",
  "300": "http://fonts.gstatic.com/s/piazzolla/v25/N0b52SlTPu5rIkWIZjVKKtYtfxYqZ4RJBFzFfYUjkSDdlqZgy7KGxnLy1AHfAAy5.ttf",
  "500": "http://fonts.gstatic.com/s/piazzolla/v25/N0b52SlTPu5rIkWIZjVKKtYtfxYqZ4RJBFzFfYUjkSDdlqZgy7LqxnLy1AHfAAy5.ttf",
  "600": "http://fonts.gstatic.com/s/piazzolla/v25/N0b52SlTPu5rIkWIZjVKKtYtfxYqZ4RJBFzFfYUjkSDdlqZgy7IGwXLy1AHfAAy5.ttf",
  "700": "http://fonts.gstatic.com/s/piazzolla/v25/N0b52SlTPu5rIkWIZjVKKtYtfxYqZ4RJBFzFfYUjkSDdlqZgy7I_wXLy1AHfAAy5.ttf",
  "800": "http://fonts.gstatic.com/s/piazzolla/v25/N0b52SlTPu5rIkWIZjVKKtYtfxYqZ4RJBFzFfYUjkSDdlqZgy7JYwXLy1AHfAAy5.ttf",
  "900": "http://fonts.gstatic.com/s/piazzolla/v25/N0b52SlTPu5rIkWIZjVKKtYtfxYqZ4RJBFzFfYUjkSDdlqZgy7JxwXLy1AHfAAy5.ttf",
  "regular": "http://fonts.gstatic.com/s/piazzolla/v25/N0b52SlTPu5rIkWIZjVKKtYtfxYqZ4RJBFzFfYUjkSDdlqZgy7LYxnLy1AHfAAy5.ttf",
  "100italic": "http://fonts.gstatic.com/s/piazzolla/v25/N0b72SlTPu5rIkWIZjVgI-TckS03oGpPETyEJ88Rbvi0_TzOzKcQhZqw3gX9BRy5m5M.ttf",
  "200italic": "http://fonts.gstatic.com/s/piazzolla/v25/N0b72SlTPu5rIkWIZjVgI-TckS03oGpPETyEJ88Rbvi0_TzOzKcQhRqx3gX9BRy5m5M.ttf",
  "300italic": "http://fonts.gstatic.com/s/piazzolla/v25/N0b72SlTPu5rIkWIZjVgI-TckS03oGpPETyEJ88Rbvi0_TzOzKcQhcSx3gX9BRy5m5M.ttf",
  "italic": "http://fonts.gstatic.com/s/piazzolla/v25/N0b72SlTPu5rIkWIZjVgI-TckS03oGpPETyEJ88Rbvi0_TzOzKcQhZqx3gX9BRy5m5M.ttf",
  "500italic": "http://fonts.gstatic.com/s/piazzolla/v25/N0b72SlTPu5rIkWIZjVgI-TckS03oGpPETyEJ88Rbvi0_TzOzKcQhaix3gX9BRy5m5M.ttf",
  "600italic": "http://fonts.gstatic.com/s/piazzolla/v25/N0b72SlTPu5rIkWIZjVgI-TckS03oGpPETyEJ88Rbvi0_TzOzKcQhUS23gX9BRy5m5M.ttf",
  "700italic": "http://fonts.gstatic.com/s/piazzolla/v25/N0b72SlTPu5rIkWIZjVgI-TckS03oGpPETyEJ88Rbvi0_TzOzKcQhX223gX9BRy5m5M.ttf",
  "800italic": "http://fonts.gstatic.com/s/piazzolla/v25/N0b72SlTPu5rIkWIZjVgI-TckS03oGpPETyEJ88Rbvi0_TzOzKcQhRq23gX9BRy5m5M.ttf",
  "900italic": "http://fonts.gstatic.com/s/piazzolla/v25/N0b72SlTPu5rIkWIZjVgI-TckS03oGpPETyEJ88Rbvi0_TzOzKcQhTO23gX9BRy5m5M.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Piedra",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/piedra/v21/ke8kOg8aN0Bn7hTunEyHN_M3gA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pinyon Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pinyonscript/v17/6xKpdSJbL9-e9LuoeQiDRQR8aOLQO4bhiDY.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pirata One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pirataone/v22/I_urMpiDvgLdLh0fAtoftiiEr5_BdZ8.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Plaster",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/plaster/v24/DdTm79QatW80eRh4Ei5JOtLOeLI.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Play",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/play/v17/6ae84K2oVqwItm4TOpc423nTJTM.ttf",
  "regular": "http://fonts.gstatic.com/s/play/v17/6aez4K2oVqwIjtI8Hp8Tx3A.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Playball",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/playball/v16/TK3gWksYAxQ7jbsKcj8Dl-tPKo2t.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Playfair Display",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v30",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFvD-vYSZviVYUb_rj3ij__anPXJzDwcbmjWBN2PKd3vUDQZNLo_U2r.ttf",
  "600": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFvD-vYSZviVYUb_rj3ij__anPXJzDwcbmjWBN2PKebukDQZNLo_U2r.ttf",
  "700": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFvD-vYSZviVYUb_rj3ij__anPXJzDwcbmjWBN2PKeiukDQZNLo_U2r.ttf",
  "800": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFvD-vYSZviVYUb_rj3ij__anPXJzDwcbmjWBN2PKfFukDQZNLo_U2r.ttf",
  "900": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFvD-vYSZviVYUb_rj3ij__anPXJzDwcbmjWBN2PKfsukDQZNLo_U2r.ttf",
  "regular": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFvD-vYSZviVYUb_rj3ij__anPXJzDwcbmjWBN2PKdFvUDQZNLo_U2r.ttf",
  "italic": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFRD-vYSZviVYUb_rj3ij__anPXDTnCjmHKM4nYO7KN_qiTbtbK-F2rA0s.ttf",
  "500italic": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFRD-vYSZviVYUb_rj3ij__anPXDTnCjmHKM4nYO7KN_pqTbtbK-F2rA0s.ttf",
  "600italic": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFRD-vYSZviVYUb_rj3ij__anPXDTnCjmHKM4nYO7KN_naUbtbK-F2rA0s.ttf",
  "700italic": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFRD-vYSZviVYUb_rj3ij__anPXDTnCjmHKM4nYO7KN_k-UbtbK-F2rA0s.ttf",
  "800italic": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFRD-vYSZviVYUb_rj3ij__anPXDTnCjmHKM4nYO7KN_iiUbtbK-F2rA0s.ttf",
  "900italic": "http://fonts.gstatic.com/s/playfairdisplay/v30/nuFRD-vYSZviVYUb_rj3ij__anPXDTnCjmHKM4nYO7KN_gGUbtbK-F2rA0s.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Playfair Display SC",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/playfairdisplaysc/v15/ke80OhoaMkR6-hSn7kbHVoFf7ZfgMPr_nQIpNcsdL4IUMyE.ttf",
  "900": "http://fonts.gstatic.com/s/playfairdisplaysc/v15/ke80OhoaMkR6-hSn7kbHVoFf7ZfgMPr_nTorNcsdL4IUMyE.ttf",
  "regular": "http://fonts.gstatic.com/s/playfairdisplaysc/v15/ke85OhoaMkR6-hSn7kbHVoFf7ZfgMPr_pb4GEcM2M4s.ttf",
  "italic": "http://fonts.gstatic.com/s/playfairdisplaysc/v15/ke87OhoaMkR6-hSn7kbHVoFf7ZfgMPr_lbwMFeEzI4sNKg.ttf",
  "700italic": "http://fonts.gstatic.com/s/playfairdisplaysc/v15/ke82OhoaMkR6-hSn7kbHVoFf7ZfgMPr_lbw0qc4XK6ARIyH5IA.ttf",
  "900italic": "http://fonts.gstatic.com/s/playfairdisplaysc/v15/ke82OhoaMkR6-hSn7kbHVoFf7ZfgMPr_lbw0kcwXK6ARIyH5IA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Plus Jakarta Sans",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIbaomQNQcsA88c7O9yZ4KMCoOg4IA6-91aHEjcWuA_KU7NShXUEKi4Rw.ttf",
  "300": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIbaomQNQcsA88c7O9yZ4KMCoOg4IA6-91aHEjcWuA_907NShXUEKi4Rw.ttf",
  "500": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIbaomQNQcsA88c7O9yZ4KMCoOg4IA6-91aHEjcWuA_m07NShXUEKi4Rw.ttf",
  "600": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIbaomQNQcsA88c7O9yZ4KMCoOg4IA6-91aHEjcWuA_d0nNShXUEKi4Rw.ttf",
  "700": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIbaomQNQcsA88c7O9yZ4KMCoOg4IA6-91aHEjcWuA_TknNShXUEKi4Rw.ttf",
  "800": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIbaomQNQcsA88c7O9yZ4KMCoOg4IA6-91aHEjcWuA_KUnNShXUEKi4Rw.ttf",
  "regular": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIbaomQNQcsA88c7O9yZ4KMCoOg4IA6-91aHEjcWuA_qU7NShXUEKi4Rw.ttf",
  "200italic": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIZaomQNQcsA88c7O9yZ4KMCoOg4KozySKCdSNG9OcqYQ2lCR_QMq2oR82k.ttf",
  "300italic": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIZaomQNQcsA88c7O9yZ4KMCoOg4KozySKCdSNG9OcqYQ17CR_QMq2oR82k.ttf",
  "italic": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIZaomQNQcsA88c7O9yZ4KMCoOg4KozySKCdSNG9OcqYQ0lCR_QMq2oR82k.ttf",
  "500italic": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIZaomQNQcsA88c7O9yZ4KMCoOg4KozySKCdSNG9OcqYQ0XCR_QMq2oR82k.ttf",
  "600italic": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIZaomQNQcsA88c7O9yZ4KMCoOg4KozySKCdSNG9OcqYQ37Dh_QMq2oR82k.ttf",
  "700italic": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIZaomQNQcsA88c7O9yZ4KMCoOg4KozySKCdSNG9OcqYQ3CDh_QMq2oR82k.ttf",
  "800italic": "http://fonts.gstatic.com/s/plusjakartasans/v3/LDIZaomQNQcsA88c7O9yZ4KMCoOg4KozySKCdSNG9OcqYQ2lDh_QMq2oR82k.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Podkova",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v26",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/podkova/v26/K2FufZ1EmftJSV9VQpXb1lo9vC3nZWt3zcU4EoporSHH.ttf",
  "600": "http://fonts.gstatic.com/s/podkova/v26/K2FufZ1EmftJSV9VQpXb1lo9vC3nZWubysU4EoporSHH.ttf",
  "700": "http://fonts.gstatic.com/s/podkova/v26/K2FufZ1EmftJSV9VQpXb1lo9vC3nZWuiysU4EoporSHH.ttf",
  "800": "http://fonts.gstatic.com/s/podkova/v26/K2FufZ1EmftJSV9VQpXb1lo9vC3nZWvFysU4EoporSHH.ttf",
  "regular": "http://fonts.gstatic.com/s/podkova/v26/K2FufZ1EmftJSV9VQpXb1lo9vC3nZWtFzcU4EoporSHH.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Poiret One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/poiretone/v14/UqyVK80NJXN4zfRgbdfbk5lWVscxdKE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Poller One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pollerone/v19/ahccv82n0TN3gia5E4Bud-lbgUS5u0s.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Poly",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/poly/v16/MQpb-W6wKNitRLCAq2Lpris.ttf",
  "italic": "http://fonts.gstatic.com/s/poly/v16/MQpV-W6wKNitdLKKr0DsviuGWA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pompiere",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pompiere/v15/VEMyRoxis5Dwuyeov6Wt5jDtreOL.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pontano Sans",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pontanosans/v13/qFdD35GdgYR8EzR6oBLDHa3qwjUMg1siNQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Poor Story",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/poorstory/v20/jizfREFUsnUct9P6cDfd4OmnLD0Z4zM.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Poppins",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/poppins/v20/pxiGyp8kv8JHgFVrLPTed3FBGPaTSQ.ttf",
  "200": "http://fonts.gstatic.com/s/poppins/v20/pxiByp8kv8JHgFVrLFj_V1tvFP-KUEg.ttf",
  "300": "http://fonts.gstatic.com/s/poppins/v20/pxiByp8kv8JHgFVrLDz8V1tvFP-KUEg.ttf",
  "500": "http://fonts.gstatic.com/s/poppins/v20/pxiByp8kv8JHgFVrLGT9V1tvFP-KUEg.ttf",
  "600": "http://fonts.gstatic.com/s/poppins/v20/pxiByp8kv8JHgFVrLEj6V1tvFP-KUEg.ttf",
  "700": "http://fonts.gstatic.com/s/poppins/v20/pxiByp8kv8JHgFVrLCz7V1tvFP-KUEg.ttf",
  "800": "http://fonts.gstatic.com/s/poppins/v20/pxiByp8kv8JHgFVrLDD4V1tvFP-KUEg.ttf",
  "900": "http://fonts.gstatic.com/s/poppins/v20/pxiByp8kv8JHgFVrLBT5V1tvFP-KUEg.ttf",
  "100italic": "http://fonts.gstatic.com/s/poppins/v20/pxiAyp8kv8JHgFVrJJLmE3tFOvODSVFF.ttf",
  "200italic": "http://fonts.gstatic.com/s/poppins/v20/pxiDyp8kv8JHgFVrJJLmv1plEN2PQEhcqw.ttf",
  "300italic": "http://fonts.gstatic.com/s/poppins/v20/pxiDyp8kv8JHgFVrJJLm21llEN2PQEhcqw.ttf",
  "regular": "http://fonts.gstatic.com/s/poppins/v20/pxiEyp8kv8JHgFVrFJDUc1NECPY.ttf",
  "italic": "http://fonts.gstatic.com/s/poppins/v20/pxiGyp8kv8JHgFVrJJLed3FBGPaTSQ.ttf",
  "500italic": "http://fonts.gstatic.com/s/poppins/v20/pxiDyp8kv8JHgFVrJJLmg1hlEN2PQEhcqw.ttf",
  "600italic": "http://fonts.gstatic.com/s/poppins/v20/pxiDyp8kv8JHgFVrJJLmr19lEN2PQEhcqw.ttf",
  "700italic": "http://fonts.gstatic.com/s/poppins/v20/pxiDyp8kv8JHgFVrJJLmy15lEN2PQEhcqw.ttf",
  "800italic": "http://fonts.gstatic.com/s/poppins/v20/pxiDyp8kv8JHgFVrJJLm111lEN2PQEhcqw.ttf",
  "900italic": "http://fonts.gstatic.com/s/poppins/v20/pxiDyp8kv8JHgFVrJJLm81xlEN2PQEhcqw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Port Lligat Sans",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/portlligatsans/v18/kmKmZrYrGBbdN1aV7Vokow6Lw4s4l7N0Tx4xEcQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Port Lligat Slab",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/portlligatslab/v21/LDIpaoiQNgArA8kR7ulhZ8P_NYOss7ob9yGLmfI.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Potta One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pottaone/v16/FeVSS05Bp6cy7xI-YfxQ3Z5nm29Gww.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pragati Narrow",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/pragatinarrow/v13/vm8sdRf0T0bS1ffgsPB7WZ-mD2ZD5fd_GJMTlo_4.ttf",
  "regular": "http://fonts.gstatic.com/s/pragatinarrow/v13/vm8vdRf0T0bS1ffgsPB7WZ-mD17_ytN3M48a.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Praise",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/praise/v5/qkBUXvUZ-cnFXcFyDvO67L9XmQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Prata",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/prata/v18/6xKhdSpbNNCT-vWIAG_5LWwJ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Preahvihear",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v27",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/preahvihear/v27/6NUS8F-dNQeEYhzj7uluxswE49FJf8Wv.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Press Start 2P",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/pressstart2p/v14/e3t4euO8T-267oIAQAu6jDQyK0nSgPJE4580.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Pridi",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/pridi/v11/2sDdZG5JnZLfkc1SiE0jRUG0AqUc.ttf",
  "300": "http://fonts.gstatic.com/s/pridi/v11/2sDdZG5JnZLfkc02i00jRUG0AqUc.ttf",
  "500": "http://fonts.gstatic.com/s/pridi/v11/2sDdZG5JnZLfkc1uik0jRUG0AqUc.ttf",
  "600": "http://fonts.gstatic.com/s/pridi/v11/2sDdZG5JnZLfkc1CjU0jRUG0AqUc.ttf",
  "700": "http://fonts.gstatic.com/s/pridi/v11/2sDdZG5JnZLfkc0mjE0jRUG0AqUc.ttf",
  "regular": "http://fonts.gstatic.com/s/pridi/v11/2sDQZG5JnZLfkfWao2krbl29.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Princess Sofia",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/princesssofia/v21/qWczB6yguIb8DZ_GXZst16n7GRz7mDUoupoI.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Prociono",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/prociono/v22/r05YGLlR-KxAf9GGO8upyDYtStiJ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Prompt",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/prompt/v10/-W_9XJnvUD7dzB2CA9oYREcjeo0k.ttf",
  "200": "http://fonts.gstatic.com/s/prompt/v10/-W_8XJnvUD7dzB2Cr_s4bmkvc5Q9dw.ttf",
  "300": "http://fonts.gstatic.com/s/prompt/v10/-W_8XJnvUD7dzB2Cy_g4bmkvc5Q9dw.ttf",
  "500": "http://fonts.gstatic.com/s/prompt/v10/-W_8XJnvUD7dzB2Ck_k4bmkvc5Q9dw.ttf",
  "600": "http://fonts.gstatic.com/s/prompt/v10/-W_8XJnvUD7dzB2Cv_44bmkvc5Q9dw.ttf",
  "700": "http://fonts.gstatic.com/s/prompt/v10/-W_8XJnvUD7dzB2C2_84bmkvc5Q9dw.ttf",
  "800": "http://fonts.gstatic.com/s/prompt/v10/-W_8XJnvUD7dzB2Cx_w4bmkvc5Q9dw.ttf",
  "900": "http://fonts.gstatic.com/s/prompt/v10/-W_8XJnvUD7dzB2C4_04bmkvc5Q9dw.ttf",
  "100italic": "http://fonts.gstatic.com/s/prompt/v10/-W_7XJnvUD7dzB2KZeJ8TkMBf50kbiM.ttf",
  "200italic": "http://fonts.gstatic.com/s/prompt/v10/-W_6XJnvUD7dzB2KZeLQb2MrUZEtdzow.ttf",
  "300italic": "http://fonts.gstatic.com/s/prompt/v10/-W_6XJnvUD7dzB2KZeK0bGMrUZEtdzow.ttf",
  "regular": "http://fonts.gstatic.com/s/prompt/v10/-W__XJnvUD7dzB26Z9AcZkIzeg.ttf",
  "italic": "http://fonts.gstatic.com/s/prompt/v10/-W_9XJnvUD7dzB2KZdoYREcjeo0k.ttf",
  "500italic": "http://fonts.gstatic.com/s/prompt/v10/-W_6XJnvUD7dzB2KZeLsbWMrUZEtdzow.ttf",
  "600italic": "http://fonts.gstatic.com/s/prompt/v10/-W_6XJnvUD7dzB2KZeLAamMrUZEtdzow.ttf",
  "700italic": "http://fonts.gstatic.com/s/prompt/v10/-W_6XJnvUD7dzB2KZeKka2MrUZEtdzow.ttf",
  "800italic": "http://fonts.gstatic.com/s/prompt/v10/-W_6XJnvUD7dzB2KZeK4aGMrUZEtdzow.ttf",
  "900italic": "http://fonts.gstatic.com/s/prompt/v10/-W_6XJnvUD7dzB2KZeKcaWMrUZEtdzow.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Prosto One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/prostoone/v17/OpNJno4VhNfK-RgpwWWxpipfWhXD00c.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Proza Libre",
  "variants": [
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/prozalibre/v9/LYjbdGHgj0k1DIQRyUEyyELbV__fcpC69i6N.ttf",
  "600": "http://fonts.gstatic.com/s/prozalibre/v9/LYjbdGHgj0k1DIQRyUEyyEL3UP_fcpC69i6N.ttf",
  "700": "http://fonts.gstatic.com/s/prozalibre/v9/LYjbdGHgj0k1DIQRyUEyyEKTUf_fcpC69i6N.ttf",
  "800": "http://fonts.gstatic.com/s/prozalibre/v9/LYjbdGHgj0k1DIQRyUEyyEKPUv_fcpC69i6N.ttf",
  "regular": "http://fonts.gstatic.com/s/prozalibre/v9/LYjGdGHgj0k1DIQRyUEyyHovftvXWYyz.ttf",
  "italic": "http://fonts.gstatic.com/s/prozalibre/v9/LYjEdGHgj0k1DIQRyUEyyEotdN_1XJyz7zc.ttf",
  "500italic": "http://fonts.gstatic.com/s/prozalibre/v9/LYjZdGHgj0k1DIQRyUEyyEotTCvceJSY8z6Np1k.ttf",
  "600italic": "http://fonts.gstatic.com/s/prozalibre/v9/LYjZdGHgj0k1DIQRyUEyyEotTAfbeJSY8z6Np1k.ttf",
  "700italic": "http://fonts.gstatic.com/s/prozalibre/v9/LYjZdGHgj0k1DIQRyUEyyEotTGPaeJSY8z6Np1k.ttf",
  "800italic": "http://fonts.gstatic.com/s/prozalibre/v9/LYjZdGHgj0k1DIQRyUEyyEotTH_ZeJSY8z6Np1k.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Public Sans",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/publicsans/v14/ijwGs572Xtc6ZYQws9YVwllKVG8qX1oyOymuFpi5ww0pX189fg.ttf",
  "200": "http://fonts.gstatic.com/s/publicsans/v14/ijwGs572Xtc6ZYQws9YVwllKVG8qX1oyOymulpm5ww0pX189fg.ttf",
  "300": "http://fonts.gstatic.com/s/publicsans/v14/ijwGs572Xtc6ZYQws9YVwllKVG8qX1oyOymuSJm5ww0pX189fg.ttf",
  "500": "http://fonts.gstatic.com/s/publicsans/v14/ijwGs572Xtc6ZYQws9YVwllKVG8qX1oyOymuJJm5ww0pX189fg.ttf",
  "600": "http://fonts.gstatic.com/s/publicsans/v14/ijwGs572Xtc6ZYQws9YVwllKVG8qX1oyOymuyJ65ww0pX189fg.ttf",
  "700": "http://fonts.gstatic.com/s/publicsans/v14/ijwGs572Xtc6ZYQws9YVwllKVG8qX1oyOymu8Z65ww0pX189fg.ttf",
  "800": "http://fonts.gstatic.com/s/publicsans/v14/ijwGs572Xtc6ZYQws9YVwllKVG8qX1oyOymulp65ww0pX189fg.ttf",
  "900": "http://fonts.gstatic.com/s/publicsans/v14/ijwGs572Xtc6ZYQws9YVwllKVG8qX1oyOymuv565ww0pX189fg.ttf",
  "regular": "http://fonts.gstatic.com/s/publicsans/v14/ijwGs572Xtc6ZYQws9YVwllKVG8qX1oyOymuFpm5ww0pX189fg.ttf",
  "100italic": "http://fonts.gstatic.com/s/publicsans/v14/ijwAs572Xtc6ZYQws9YVwnNDZpDyNjGolS673tpRgQctfVotfj7j.ttf",
  "200italic": "http://fonts.gstatic.com/s/publicsans/v14/ijwAs572Xtc6ZYQws9YVwnNDZpDyNjGolS673trRgActfVotfj7j.ttf",
  "300italic": "http://fonts.gstatic.com/s/publicsans/v14/ijwAs572Xtc6ZYQws9YVwnNDZpDyNjGolS673toPgActfVotfj7j.ttf",
  "italic": "http://fonts.gstatic.com/s/publicsans/v14/ijwAs572Xtc6ZYQws9YVwnNDZpDyNjGolS673tpRgActfVotfj7j.ttf",
  "500italic": "http://fonts.gstatic.com/s/publicsans/v14/ijwAs572Xtc6ZYQws9YVwnNDZpDyNjGolS673tpjgActfVotfj7j.ttf",
  "600italic": "http://fonts.gstatic.com/s/publicsans/v14/ijwAs572Xtc6ZYQws9YVwnNDZpDyNjGolS673tqPhwctfVotfj7j.ttf",
  "700italic": "http://fonts.gstatic.com/s/publicsans/v14/ijwAs572Xtc6ZYQws9YVwnNDZpDyNjGolS673tq2hwctfVotfj7j.ttf",
  "800italic": "http://fonts.gstatic.com/s/publicsans/v14/ijwAs572Xtc6ZYQws9YVwnNDZpDyNjGolS673trRhwctfVotfj7j.ttf",
  "900italic": "http://fonts.gstatic.com/s/publicsans/v14/ijwAs572Xtc6ZYQws9YVwnNDZpDyNjGolS673tr4hwctfVotfj7j.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Puppies Play",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/puppiesplay/v5/wlp2gwHZEV99rG6M3NR9uB9vaAJSA_JN3Q.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Puritan",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/puritan/v24/845dNMgkAJ2VTtIozCbfYd6j-0rGRes.ttf",
  "regular": "http://fonts.gstatic.com/s/puritan/v24/845YNMgkAJ2VTtIo9JrwRdaI50M.ttf",
  "italic": "http://fonts.gstatic.com/s/puritan/v24/845aNMgkAJ2VTtIoxJj6QfSN90PfXA.ttf",
  "700italic": "http://fonts.gstatic.com/s/puritan/v24/845fNMgkAJ2VTtIoxJjC_dup_2jDVevnLQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Purple Purse",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/purplepurse/v21/qWctB66gv53iAp-Vfs4My6qyeBb_ujA4ug.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Qahiri",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin"
  ],
  "version": "v7",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/qahiri/v7/tsssAp1RZy0C_hGuU3Chrnmupw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Quando",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/quando/v14/xMQVuFNaVa6YuW0pC6WzKX_QmA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Quantico",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/quantico/v15/rax5HiSdp9cPL3KIF7TQARhasU7Q8Cad.ttf",
  "regular": "http://fonts.gstatic.com/s/quantico/v15/rax-HiSdp9cPL3KIF4xsLjxSmlLZ.ttf",
  "italic": "http://fonts.gstatic.com/s/quantico/v15/rax4HiSdp9cPL3KIF7xuJDhwn0LZ6T8.ttf",
  "700italic": "http://fonts.gstatic.com/s/quantico/v15/rax7HiSdp9cPL3KIF7xuHIRfu0ry9TadML4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Quattrocento",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/quattrocento/v17/OZpbg_xvsDZQL_LKIF7q4jP_eE3fd6PZsXcM9w.ttf",
  "regular": "http://fonts.gstatic.com/s/quattrocento/v17/OZpEg_xvsDZQL_LKIF7q4jPHxGL7f4jFuA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Quattrocento Sans",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/quattrocentosans/v18/va9Z4lja2NVIDdIAAoMR5MfuElaRB0RykmrWN33AiasJ.ttf",
  "regular": "http://fonts.gstatic.com/s/quattrocentosans/v18/va9c4lja2NVIDdIAAoMR5MfuElaRB3zOvU7eHGHJ.ttf",
  "italic": "http://fonts.gstatic.com/s/quattrocentosans/v18/va9a4lja2NVIDdIAAoMR5MfuElaRB0zMt0r8GXHJkLI.ttf",
  "700italic": "http://fonts.gstatic.com/s/quattrocentosans/v18/va9X4lja2NVIDdIAAoMR5MfuElaRB0zMj_bTPXnijLsJV7E.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Questrial",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/questrial/v18/QdVUSTchPBm7nuUeVf7EuStkm20oJA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Quicksand",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v30",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/quicksand/v30/6xK-dSZaM9iE8KbpRA_LJ3z8mH9BOJvgkKEo18G0wx40QDw.ttf",
  "500": "http://fonts.gstatic.com/s/quicksand/v30/6xK-dSZaM9iE8KbpRA_LJ3z8mH9BOJvgkM0o18G0wx40QDw.ttf",
  "600": "http://fonts.gstatic.com/s/quicksand/v30/6xK-dSZaM9iE8KbpRA_LJ3z8mH9BOJvgkCEv18G0wx40QDw.ttf",
  "700": "http://fonts.gstatic.com/s/quicksand/v30/6xK-dSZaM9iE8KbpRA_LJ3z8mH9BOJvgkBgv18G0wx40QDw.ttf",
  "regular": "http://fonts.gstatic.com/s/quicksand/v30/6xK-dSZaM9iE8KbpRA_LJ3z8mH9BOJvgkP8o18G0wx40QDw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Quintessential",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/quintessential/v20/fdNn9sOGq31Yjnh3qWU14DdtjY5wS7kmAyxM.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Qwigley",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/qwigley/v16/1cXzaU3UGJb5tGoCuVxsi1mBmcE.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Qwitcher Grypen",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/qwitchergrypen/v3/pxiZypclp9tDilN9RrC5BSI1dZmT9ExkqkSsrvNXiA.ttf",
  "regular": "http://fonts.gstatic.com/s/qwitchergrypen/v3/pxicypclp9tDilN9RrC5BSI1dZmrSGNAom-wpw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Racing Sans One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/racingsansone/v13/sykr-yRtm7EvTrXNxkv5jfKKyDCwL3rmWpIBtA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Radio Canada",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/radiocanada/v16/XRX13ISXn0dBMcibU6jlAqr3ejLv5OLZYiYXik6db2P4jxxlsls-0nESkQPIJOdSSfOT.ttf",
  "500": "http://fonts.gstatic.com/s/radiocanada/v16/XRX13ISXn0dBMcibU6jlAqr3ejLv5OLZYiYXik6db2P4jxxlsls-0nF-kQPIJOdSSfOT.ttf",
  "600": "http://fonts.gstatic.com/s/radiocanada/v16/XRX13ISXn0dBMcibU6jlAqr3ejLv5OLZYiYXik6db2P4jxxlsls-0nGSlgPIJOdSSfOT.ttf",
  "700": "http://fonts.gstatic.com/s/radiocanada/v16/XRX13ISXn0dBMcibU6jlAqr3ejLv5OLZYiYXik6db2P4jxxlsls-0nGrlgPIJOdSSfOT.ttf",
  "regular": "http://fonts.gstatic.com/s/radiocanada/v16/XRX13ISXn0dBMcibU6jlAqr3ejLv5OLZYiYXik6db2P4jxxlsls-0nFMkQPIJOdSSfOT.ttf",
  "300italic": "http://fonts.gstatic.com/s/radiocanada/v16/XRX33ISXn0dBMcibU6jlAqrdcwAMBJuK9IgQn4bfnSrKcMQM2cGQ1WSE0rWLLuNwTOOTa9k.ttf",
  "italic": "http://fonts.gstatic.com/s/radiocanada/v16/XRX33ISXn0dBMcibU6jlAqrdcwAMBJuK9IgQn4bfnSrKcMQM2cGQ1WSE0uuLLuNwTOOTa9k.ttf",
  "500italic": "http://fonts.gstatic.com/s/radiocanada/v16/XRX33ISXn0dBMcibU6jlAqrdcwAMBJuK9IgQn4bfnSrKcMQM2cGQ1WSE0tmLLuNwTOOTa9k.ttf",
  "600italic": "http://fonts.gstatic.com/s/radiocanada/v16/XRX33ISXn0dBMcibU6jlAqrdcwAMBJuK9IgQn4bfnSrKcMQM2cGQ1WSE0jWMLuNwTOOTa9k.ttf",
  "700italic": "http://fonts.gstatic.com/s/radiocanada/v16/XRX33ISXn0dBMcibU6jlAqrdcwAMBJuK9IgQn4bfnSrKcMQM2cGQ1WSE0gyMLuNwTOOTa9k.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Radley",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/radley/v20/LYjDdGzinEIjCN19oAlEpVs3VQ.ttf",
  "italic": "http://fonts.gstatic.com/s/radley/v20/LYjBdGzinEIjCN1NogNAh14nVcfe.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rajdhani",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/rajdhani/v15/LDI2apCSOBg7S-QT7pasEcOsc-bGkqIw.ttf",
  "500": "http://fonts.gstatic.com/s/rajdhani/v15/LDI2apCSOBg7S-QT7pb0EMOsc-bGkqIw.ttf",
  "600": "http://fonts.gstatic.com/s/rajdhani/v15/LDI2apCSOBg7S-QT7pbYF8Osc-bGkqIw.ttf",
  "700": "http://fonts.gstatic.com/s/rajdhani/v15/LDI2apCSOBg7S-QT7pa8FsOsc-bGkqIw.ttf",
  "regular": "http://fonts.gstatic.com/s/rajdhani/v15/LDIxapCSOBg7S-QT7q4AOeekWPrP.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rakkas",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rakkas/v17/Qw3cZQlNHiblL3j_lttPOeMcCw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Raleway",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v28",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/raleway/v28/1Ptxg8zYS_SKggPN4iEgvnHyvveLxVvao4CPNLA3JC9c.ttf",
  "200": "http://fonts.gstatic.com/s/raleway/v28/1Ptxg8zYS_SKggPN4iEgvnHyvveLxVtaooCPNLA3JC9c.ttf",
  "300": "http://fonts.gstatic.com/s/raleway/v28/1Ptxg8zYS_SKggPN4iEgvnHyvveLxVuEooCPNLA3JC9c.ttf",
  "500": "http://fonts.gstatic.com/s/raleway/v28/1Ptxg8zYS_SKggPN4iEgvnHyvveLxVvoooCPNLA3JC9c.ttf",
  "600": "http://fonts.gstatic.com/s/raleway/v28/1Ptxg8zYS_SKggPN4iEgvnHyvveLxVsEpYCPNLA3JC9c.ttf",
  "700": "http://fonts.gstatic.com/s/raleway/v28/1Ptxg8zYS_SKggPN4iEgvnHyvveLxVs9pYCPNLA3JC9c.ttf",
  "800": "http://fonts.gstatic.com/s/raleway/v28/1Ptxg8zYS_SKggPN4iEgvnHyvveLxVtapYCPNLA3JC9c.ttf",
  "900": "http://fonts.gstatic.com/s/raleway/v28/1Ptxg8zYS_SKggPN4iEgvnHyvveLxVtzpYCPNLA3JC9c.ttf",
  "regular": "http://fonts.gstatic.com/s/raleway/v28/1Ptxg8zYS_SKggPN4iEgvnHyvveLxVvaooCPNLA3JC9c.ttf",
  "100italic": "http://fonts.gstatic.com/s/raleway/v28/1Pt_g8zYS_SKggPNyCgSQamb1W0lwk4S4WjNPrQVIT9c2c8.ttf",
  "200italic": "http://fonts.gstatic.com/s/raleway/v28/1Pt_g8zYS_SKggPNyCgSQamb1W0lwk4S4ejMPrQVIT9c2c8.ttf",
  "300italic": "http://fonts.gstatic.com/s/raleway/v28/1Pt_g8zYS_SKggPNyCgSQamb1W0lwk4S4TbMPrQVIT9c2c8.ttf",
  "italic": "http://fonts.gstatic.com/s/raleway/v28/1Pt_g8zYS_SKggPNyCgSQamb1W0lwk4S4WjMPrQVIT9c2c8.ttf",
  "500italic": "http://fonts.gstatic.com/s/raleway/v28/1Pt_g8zYS_SKggPNyCgSQamb1W0lwk4S4VrMPrQVIT9c2c8.ttf",
  "600italic": "http://fonts.gstatic.com/s/raleway/v28/1Pt_g8zYS_SKggPNyCgSQamb1W0lwk4S4bbLPrQVIT9c2c8.ttf",
  "700italic": "http://fonts.gstatic.com/s/raleway/v28/1Pt_g8zYS_SKggPNyCgSQamb1W0lwk4S4Y_LPrQVIT9c2c8.ttf",
  "800italic": "http://fonts.gstatic.com/s/raleway/v28/1Pt_g8zYS_SKggPNyCgSQamb1W0lwk4S4ejLPrQVIT9c2c8.ttf",
  "900italic": "http://fonts.gstatic.com/s/raleway/v28/1Pt_g8zYS_SKggPNyCgSQamb1W0lwk4S4cHLPrQVIT9c2c8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Raleway Dots",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ralewaydots/v14/6NUR8FifJg6AfQvzpshgwJ8kyf9Fdty2ew.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ramabhadra",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v15",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ramabhadra/v15/EYq2maBOwqRW9P1SQ83LehNGX5uWw3o.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ramaraja",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ramaraja/v15/SlGTmQearpYAYG1CABIkqnB6aSQU.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rambla",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/rambla/v13/snfos0ip98hx6mrMn50qPvN4yJuDYQ.ttf",
  "regular": "http://fonts.gstatic.com/s/rambla/v13/snfrs0ip98hx6mr0I7IONthkwQ.ttf",
  "italic": "http://fonts.gstatic.com/s/rambla/v13/snfps0ip98hx6mrEIbgKFN10wYKa.ttf",
  "700italic": "http://fonts.gstatic.com/s/rambla/v13/snfus0ip98hx6mrEIYC2O_l86p6TYS-Y.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rammetto One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rammettoone/v14/LhWiMV3HOfMbMetJG3lQDpp9Mvuciu-_SQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rampart One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rampartone/v7/K2F1fZFGl_JSR1tAWNG9R6qgLS76ZHOM.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ranchers",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ranchers/v13/zrfm0H3Lx-P2Xvs2AoDYDC79XTHv.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rancho",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rancho/v17/46kulbzmXjLaqZRlbWXgd0RY1g.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ranga",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/ranga/v17/C8cg4cYisGb28qY-AxgR6X2NZAn2.ttf",
  "regular": "http://fonts.gstatic.com/s/ranga/v17/C8ct4cYisGb28p6CLDwZwmGE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rasa",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/rasa/v15/xn76YHIn1mWmVKl8ZtAM9NrJfN4YJW41fcvN2KT4.ttf",
  "500": "http://fonts.gstatic.com/s/rasa/v15/xn76YHIn1mWmVKl8ZtAM9NrJfN50JW41fcvN2KT4.ttf",
  "600": "http://fonts.gstatic.com/s/rasa/v15/xn76YHIn1mWmVKl8ZtAM9NrJfN6YIm41fcvN2KT4.ttf",
  "700": "http://fonts.gstatic.com/s/rasa/v15/xn76YHIn1mWmVKl8ZtAM9NrJfN6hIm41fcvN2KT4.ttf",
  "regular": "http://fonts.gstatic.com/s/rasa/v15/xn76YHIn1mWmVKl8ZtAM9NrJfN5GJW41fcvN2KT4.ttf",
  "300italic": "http://fonts.gstatic.com/s/rasa/v15/xn78YHIn1mWmfqBOmQhln0Bne8uOZth2d8_v3bT4Ycc.ttf",
  "italic": "http://fonts.gstatic.com/s/rasa/v15/xn78YHIn1mWmfqBOmQhln0Bne8uOZoZ2d8_v3bT4Ycc.ttf",
  "500italic": "http://fonts.gstatic.com/s/rasa/v15/xn78YHIn1mWmfqBOmQhln0Bne8uOZrR2d8_v3bT4Ycc.ttf",
  "600italic": "http://fonts.gstatic.com/s/rasa/v15/xn78YHIn1mWmfqBOmQhln0Bne8uOZlhxd8_v3bT4Ycc.ttf",
  "700italic": "http://fonts.gstatic.com/s/rasa/v15/xn78YHIn1mWmfqBOmQhln0Bne8uOZmFxd8_v3bT4Ycc.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rationale",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rationale/v24/9XUnlJ92n0_JFxHIfHcsdlFMzLC2Zw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ravi Prakash",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/raviprakash/v19/gokpH6fsDkVrF9Bv9X8SOAKHmNZEq6TTFw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Readex Pro",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/readexpro/v10/SLXYc1bJ7HE5YDoGPuzj_dh8na74KiwZQQzfm7w3bk38hTB8.ttf",
  "300": "http://fonts.gstatic.com/s/readexpro/v10/SLXYc1bJ7HE5YDoGPuzj_dh8na74KiwZQQwBm7w3bk38hTB8.ttf",
  "500": "http://fonts.gstatic.com/s/readexpro/v10/SLXYc1bJ7HE5YDoGPuzj_dh8na74KiwZQQxtm7w3bk38hTB8.ttf",
  "600": "http://fonts.gstatic.com/s/readexpro/v10/SLXYc1bJ7HE5YDoGPuzj_dh8na74KiwZQQyBnLw3bk38hTB8.ttf",
  "700": "http://fonts.gstatic.com/s/readexpro/v10/SLXYc1bJ7HE5YDoGPuzj_dh8na74KiwZQQy4nLw3bk38hTB8.ttf",
  "regular": "http://fonts.gstatic.com/s/readexpro/v10/SLXYc1bJ7HE5YDoGPuzj_dh8na74KiwZQQxfm7w3bk38hTB8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Recursive",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v35",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/recursive/v35/8vJN7wMr0mhh-RQChyHEH06TlXhq_gukbYrFMk1QuAIcyEwG_X-dpEfaE5YaERmK-CImKsvxvU-MXGX2fSqasNfUvz2xbXfn1uEQadDck018vwxjDJCL.ttf",
  "500": "http://fonts.gstatic.com/s/recursive/v35/8vJN7wMr0mhh-RQChyHEH06TlXhq_gukbYrFMk1QuAIcyEwG_X-dpEfaE5YaERmK-CImKsvxvU-MXGX2fSqasNfUvz2xbXfn1uEQadCwk018vwxjDJCL.ttf",
  "600": "http://fonts.gstatic.com/s/recursive/v35/8vJN7wMr0mhh-RQChyHEH06TlXhq_gukbYrFMk1QuAIcyEwG_X-dpEfaE5YaERmK-CImKsvxvU-MXGX2fSqasNfUvz2xbXfn1uEQadBclE18vwxjDJCL.ttf",
  "700": "http://fonts.gstatic.com/s/recursive/v35/8vJN7wMr0mhh-RQChyHEH06TlXhq_gukbYrFMk1QuAIcyEwG_X-dpEfaE5YaERmK-CImKsvxvU-MXGX2fSqasNfUvz2xbXfn1uEQadBllE18vwxjDJCL.ttf",
  "800": "http://fonts.gstatic.com/s/recursive/v35/8vJN7wMr0mhh-RQChyHEH06TlXhq_gukbYrFMk1QuAIcyEwG_X-dpEfaE5YaERmK-CImKsvxvU-MXGX2fSqasNfUvz2xbXfn1uEQadAClE18vwxjDJCL.ttf",
  "900": "http://fonts.gstatic.com/s/recursive/v35/8vJN7wMr0mhh-RQChyHEH06TlXhq_gukbYrFMk1QuAIcyEwG_X-dpEfaE5YaERmK-CImKsvxvU-MXGX2fSqasNfUvz2xbXfn1uEQadArlE18vwxjDJCL.ttf",
  "regular": "http://fonts.gstatic.com/s/recursive/v35/8vJN7wMr0mhh-RQChyHEH06TlXhq_gukbYrFMk1QuAIcyEwG_X-dpEfaE5YaERmK-CImKsvxvU-MXGX2fSqasNfUvz2xbXfn1uEQadCCk018vwxjDJCL.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Red Hat Display",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIf7wUr0m80wwYf0QCXZzYzUoTK8RZQvRd-D1NYbjKWckg5-Xecg3w.ttf",
  "500": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIf7wUr0m80wwYf0QCXZzYzUoTK8RZQvRd-D1NYbl6Wckg5-Xecg3w.ttf",
  "600": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIf7wUr0m80wwYf0QCXZzYzUoTK8RZQvRd-D1NYbrKRckg5-Xecg3w.ttf",
  "700": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIf7wUr0m80wwYf0QCXZzYzUoTK8RZQvRd-D1NYbouRckg5-Xecg3w.ttf",
  "800": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIf7wUr0m80wwYf0QCXZzYzUoTK8RZQvRd-D1NYbuyRckg5-Xecg3w.ttf",
  "900": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIf7wUr0m80wwYf0QCXZzYzUoTK8RZQvRd-D1NYbsWRckg5-Xecg3w.ttf",
  "regular": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIf7wUr0m80wwYf0QCXZzYzUoTK8RZQvRd-D1NYbmyWckg5-Xecg3w.ttf",
  "300italic": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIh7wUr0m80wwYf0QCXZzYzUoTg-CSvZX4Vlf1fe6TVxAsz_VWZk3zJGg.ttf",
  "italic": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIh7wUr0m80wwYf0QCXZzYzUoTg-CSvZX4Vlf1fe6TVmgsz_VWZk3zJGg.ttf",
  "500italic": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIh7wUr0m80wwYf0QCXZzYzUoTg-CSvZX4Vlf1fe6TVqAsz_VWZk3zJGg.ttf",
  "600italic": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIh7wUr0m80wwYf0QCXZzYzUoTg-CSvZX4Vlf1fe6TVRAwz_VWZk3zJGg.ttf",
  "700italic": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIh7wUr0m80wwYf0QCXZzYzUoTg-CSvZX4Vlf1fe6TVfQwz_VWZk3zJGg.ttf",
  "800italic": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIh7wUr0m80wwYf0QCXZzYzUoTg-CSvZX4Vlf1fe6TVGgwz_VWZk3zJGg.ttf",
  "900italic": "http://fonts.gstatic.com/s/redhatdisplay/v14/8vIh7wUr0m80wwYf0QCXZzYzUoTg-CSvZX4Vlf1fe6TVMwwz_VWZk3zJGg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Red Hat Mono",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/redhatmono/v10/jVyY7nDnA2uf2zVvFAhhzEs-VMSjJpBTfgjwQQPI-7HNuW4QuKI.ttf",
  "500": "http://fonts.gstatic.com/s/redhatmono/v10/jVyY7nDnA2uf2zVvFAhhzEs-VMSjJpBTfgjwQW_I-7HNuW4QuKI.ttf",
  "600": "http://fonts.gstatic.com/s/redhatmono/v10/jVyY7nDnA2uf2zVvFAhhzEs-VMSjJpBTfgjwQYPP-7HNuW4QuKI.ttf",
  "700": "http://fonts.gstatic.com/s/redhatmono/v10/jVyY7nDnA2uf2zVvFAhhzEs-VMSjJpBTfgjwQbrP-7HNuW4QuKI.ttf",
  "regular": "http://fonts.gstatic.com/s/redhatmono/v10/jVyY7nDnA2uf2zVvFAhhzEs-VMSjJpBTfgjwQV3I-7HNuW4QuKI.ttf",
  "300italic": "http://fonts.gstatic.com/s/redhatmono/v10/jVye7nDnA2uf2zVvFAhhzEsUXfZc_vk45Kb3VJWLTfLHvUwVqKIJuw.ttf",
  "italic": "http://fonts.gstatic.com/s/redhatmono/v10/jVye7nDnA2uf2zVvFAhhzEsUXfZc_vk45Kb3VJWLE_LHvUwVqKIJuw.ttf",
  "500italic": "http://fonts.gstatic.com/s/redhatmono/v10/jVye7nDnA2uf2zVvFAhhzEsUXfZc_vk45Kb3VJWLIfLHvUwVqKIJuw.ttf",
  "600italic": "http://fonts.gstatic.com/s/redhatmono/v10/jVye7nDnA2uf2zVvFAhhzEsUXfZc_vk45Kb3VJWLzfXHvUwVqKIJuw.ttf",
  "700italic": "http://fonts.gstatic.com/s/redhatmono/v10/jVye7nDnA2uf2zVvFAhhzEsUXfZc_vk45Kb3VJWL9PXHvUwVqKIJuw.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Red Hat Text",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/redhattext/v13/RrQCbohi_ic6B3yVSzGBrMx6ZI_cy1A6Ok2ML-ZwVrbacYVFtIY.ttf",
  "500": "http://fonts.gstatic.com/s/redhattext/v13/RrQCbohi_ic6B3yVSzGBrMx6ZI_cy1A6Ok2ML4pwVrbacYVFtIY.ttf",
  "600": "http://fonts.gstatic.com/s/redhattext/v13/RrQCbohi_ic6B3yVSzGBrMx6ZI_cy1A6Ok2ML2Z3VrbacYVFtIY.ttf",
  "700": "http://fonts.gstatic.com/s/redhattext/v13/RrQCbohi_ic6B3yVSzGBrMx6ZI_cy1A6Ok2ML193VrbacYVFtIY.ttf",
  "regular": "http://fonts.gstatic.com/s/redhattext/v13/RrQCbohi_ic6B3yVSzGBrMx6ZI_cy1A6Ok2ML7hwVrbacYVFtIY.ttf",
  "300italic": "http://fonts.gstatic.com/s/redhattext/v13/RrQEbohi_ic6B3yVSzGBrMxQbb0jEzlRoOOLOnAz4PXQdadApIYv_g.ttf",
  "italic": "http://fonts.gstatic.com/s/redhattext/v13/RrQEbohi_ic6B3yVSzGBrMxQbb0jEzlRoOOLOnAzvvXQdadApIYv_g.ttf",
  "500italic": "http://fonts.gstatic.com/s/redhattext/v13/RrQEbohi_ic6B3yVSzGBrMxQbb0jEzlRoOOLOnAzjPXQdadApIYv_g.ttf",
  "600italic": "http://fonts.gstatic.com/s/redhattext/v13/RrQEbohi_ic6B3yVSzGBrMxQbb0jEzlRoOOLOnAzYPLQdadApIYv_g.ttf",
  "700italic": "http://fonts.gstatic.com/s/redhattext/v13/RrQEbohi_ic6B3yVSzGBrMxQbb0jEzlRoOOLOnAzWfLQdadApIYv_g.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Red Rose",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/redrose/v14/QdVISTYiLBjouPgEUajvsfWwDtc3MH8y8_sDcjSsYUVUjg.ttf",
  "500": "http://fonts.gstatic.com/s/redrose/v14/QdVISTYiLBjouPgEUajvsfWwDtc3MH8yn_sDcjSsYUVUjg.ttf",
  "600": "http://fonts.gstatic.com/s/redrose/v14/QdVISTYiLBjouPgEUajvsfWwDtc3MH8yc_wDcjSsYUVUjg.ttf",
  "700": "http://fonts.gstatic.com/s/redrose/v14/QdVISTYiLBjouPgEUajvsfWwDtc3MH8ySvwDcjSsYUVUjg.ttf",
  "regular": "http://fonts.gstatic.com/s/redrose/v14/QdVISTYiLBjouPgEUajvsfWwDtc3MH8yrfsDcjSsYUVUjg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Redacted",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v6",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/redacted/v6/Z9XVDmdRShme2O_7aITe4u2El6GC.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Redacted Script",
  "variants": [
  "300",
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v6",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/redactedscript/v6/ypvEbXGRglhokR7dcC3d1-R6zmxqHUzVmbI397ldkg.ttf",
  "700": "http://fonts.gstatic.com/s/redactedscript/v6/ypvEbXGRglhokR7dcC3d1-R6zmxqDUvVmbI397ldkg.ttf",
  "regular": "http://fonts.gstatic.com/s/redactedscript/v6/ypvBbXGRglhokR7dcC3d1-R6zmxSsWTxkZkr_g.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Redressed",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/redressed/v25/x3dickHUbrmJ7wMy9MsBfPACvy_1BA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Reem Kufi",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/reemkufi/v18/2sDPZGJLip7W2J7v7wQZZE1I0yCmYzzQttRnEGGf3qGuvM4.ttf",
  "600": "http://fonts.gstatic.com/s/reemkufi/v18/2sDPZGJLip7W2J7v7wQZZE1I0yCmYzzQtjhgEGGf3qGuvM4.ttf",
  "700": "http://fonts.gstatic.com/s/reemkufi/v18/2sDPZGJLip7W2J7v7wQZZE1I0yCmYzzQtgFgEGGf3qGuvM4.ttf",
  "regular": "http://fonts.gstatic.com/s/reemkufi/v18/2sDPZGJLip7W2J7v7wQZZE1I0yCmYzzQtuZnEGGf3qGuvM4.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Reem Kufi Fun",
  "variants": [
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v4",
  "lastModified": "2022-09-14",
  "files": {
  "500": "http://fonts.gstatic.com/s/reemkufifun/v4/uK_m4rOFYukkmyUEbF43fIryZEk5qRZ8nrKChoYR3nCgrvqZzZXq.ttf",
  "600": "http://fonts.gstatic.com/s/reemkufifun/v4/uK_m4rOFYukkmyUEbF43fIryZEk5qRZ8nrKChob92XCgrvqZzZXq.ttf",
  "700": "http://fonts.gstatic.com/s/reemkufifun/v4/uK_m4rOFYukkmyUEbF43fIryZEk5qRZ8nrKChobE2XCgrvqZzZXq.ttf",
  "regular": "http://fonts.gstatic.com/s/reemkufifun/v4/uK_m4rOFYukkmyUEbF43fIryZEk5qRZ8nrKChoYj3nCgrvqZzZXq.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Reem Kufi Ink",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v4",
  "lastModified": "2022-09-14",
  "files": {
  "regular": "http://fonts.gstatic.com/s/reemkufiink/v4/oPWJ_kJmmu8hCvB9iFumxZSnRj5dQnSX1ko.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Reenie Beanie",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/reeniebeanie/v16/z7NSdR76eDkaJKZJFkkjuvWxbP2_qoOgf_w.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Reggae One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/reggaeone/v14/~CgwKClJlZ2dhZSBPbmUgACoECAEYAQ==.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Revalia",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/revalia/v20/WwkexPimBE2-4ZPEeVruNIgJSNM.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rhodium Libre",
  "variants": [
  "regular"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rhodiumlibre/v17/1q2AY5adA0tn_ukeHcQHqpx6pETLeo2gm2U.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ribeye",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ribeye/v21/L0x8DFMxk1MP9R3RvPCmRSlUig.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ribeye Marrow",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ribeyemarrow/v22/GFDsWApshnqMRO2JdtRZ2d0vEAwTVWgKdtw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Righteous",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/righteous/v13/1cXxaUPXBpj2rGoU7C9mj3uEicG01A.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Risque",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/risque/v20/VdGfAZUfHosahXxoCUYVBJ-T5g.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Road Rage",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/roadrage/v5/6NUU8F2fKAOBKjjr4ekvtMYAwdRZfw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Roboto",
  "variants": [
  "100",
  "100italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "700",
  "700italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v30",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/roboto/v30/KFOkCnqEu92Fr1MmgWxPKTM1K9nz.ttf",
  "300": "http://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmSU5vAx05IsDqlA.ttf",
  "500": "http://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmEU9vAx05IsDqlA.ttf",
  "700": "http://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmWUlvAx05IsDqlA.ttf",
  "900": "http://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmYUtvAx05IsDqlA.ttf",
  "100italic": "http://fonts.gstatic.com/s/roboto/v30/KFOiCnqEu92Fr1Mu51QrIzcXLsnzjYk.ttf",
  "300italic": "http://fonts.gstatic.com/s/roboto/v30/KFOjCnqEu92Fr1Mu51TjARc9AMX6lJBP.ttf",
  "regular": "http://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Me5WZLCzYlKw.ttf",
  "italic": "http://fonts.gstatic.com/s/roboto/v30/KFOkCnqEu92Fr1Mu52xPKTM1K9nz.ttf",
  "500italic": "http://fonts.gstatic.com/s/roboto/v30/KFOjCnqEu92Fr1Mu51S7ABc9AMX6lJBP.ttf",
  "700italic": "http://fonts.gstatic.com/s/roboto/v30/KFOjCnqEu92Fr1Mu51TzBhc9AMX6lJBP.ttf",
  "900italic": "http://fonts.gstatic.com/s/roboto/v30/KFOjCnqEu92Fr1Mu51TLBBc9AMX6lJBP.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Roboto Condensed",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v25",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/robotocondensed/v25/ieVi2ZhZI2eCN5jzbjEETS9weq8-33mZKCMSbvtdYyQ.ttf",
  "700": "http://fonts.gstatic.com/s/robotocondensed/v25/ieVi2ZhZI2eCN5jzbjEETS9weq8-32meKCMSbvtdYyQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/robotocondensed/v25/ieVg2ZhZI2eCN5jzbjEETS9weq8-19eDpCEYatlYcyRi4A.ttf",
  "regular": "http://fonts.gstatic.com/s/robotocondensed/v25/ieVl2ZhZI2eCN5jzbjEETS9weq8-59WxDCs5cvI.ttf",
  "italic": "http://fonts.gstatic.com/s/robotocondensed/v25/ieVj2ZhZI2eCN5jzbjEETS9weq8-19e7CAk8YvJEeg.ttf",
  "700italic": "http://fonts.gstatic.com/s/robotocondensed/v25/ieVg2ZhZI2eCN5jzbjEETS9weq8-19eDtCYYatlYcyRi4A.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Roboto Flex",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/robotoflex/v9/NaN4epOXO_NexZs0b5QrzlOHb8wCikXpYqmZsWI-__OGfttPZktqc2VdZ80KvCLZaPcSBZtOx2MifRuWR28sPJtUMbsFEK6cRrleUx9Xgbm3WLHa_F4Ep4Fm0PN19Ik5Dntczx0wZGzhPlL1YNMYKbv9_1IQXOw7AiUJVXpRJ6cXW4O8TNGoXjC79QRyaLshNDUf3e0O-gn5rrZCu20YNYG0EACUTNK-QKavMlxGIY8dxef0jQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Roboto Mono",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/robotomono/v22/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_3vuPQ--5Ip2sSQ.ttf",
  "200": "http://fonts.gstatic.com/s/robotomono/v22/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_XvqPQ--5Ip2sSQ.ttf",
  "300": "http://fonts.gstatic.com/s/robotomono/v22/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_gPqPQ--5Ip2sSQ.ttf",
  "500": "http://fonts.gstatic.com/s/robotomono/v22/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_7PqPQ--5Ip2sSQ.ttf",
  "600": "http://fonts.gstatic.com/s/robotomono/v22/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_AP2PQ--5Ip2sSQ.ttf",
  "700": "http://fonts.gstatic.com/s/robotomono/v22/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_Of2PQ--5Ip2sSQ.ttf",
  "regular": "http://fonts.gstatic.com/s/robotomono/v22/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_3vqPQ--5Ip2sSQ.ttf",
  "100italic": "http://fonts.gstatic.com/s/robotomono/v22/L0xoDF4xlVMF-BfR8bXMIjhOsXG-q2oeuFoqFrlnAeW9AJi8SZwt.ttf",
  "200italic": "http://fonts.gstatic.com/s/robotomono/v22/L0xoDF4xlVMF-BfR8bXMIjhOsXG-q2oeuFoqFrnnAOW9AJi8SZwt.ttf",
  "300italic": "http://fonts.gstatic.com/s/robotomono/v22/L0xoDF4xlVMF-BfR8bXMIjhOsXG-q2oeuFoqFrk5AOW9AJi8SZwt.ttf",
  "italic": "http://fonts.gstatic.com/s/robotomono/v22/L0xoDF4xlVMF-BfR8bXMIjhOsXG-q2oeuFoqFrlnAOW9AJi8SZwt.ttf",
  "500italic": "http://fonts.gstatic.com/s/robotomono/v22/L0xoDF4xlVMF-BfR8bXMIjhOsXG-q2oeuFoqFrlVAOW9AJi8SZwt.ttf",
  "600italic": "http://fonts.gstatic.com/s/robotomono/v22/L0xoDF4xlVMF-BfR8bXMIjhOsXG-q2oeuFoqFrm5B-W9AJi8SZwt.ttf",
  "700italic": "http://fonts.gstatic.com/s/robotomono/v22/L0xoDF4xlVMF-BfR8bXMIjhOsXG-q2oeuFoqFrmAB-W9AJi8SZwt.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Roboto Serif",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/robotoserif/v8/R71RjywflP6FLr3gZx7K8UyuXDs9zVwDmXCb8lxYgmuii32UGoVldX6UgfjL4-3sMM_kB_qXSEXTJQCFLH5-_bcEliosp6d2Af5fR4k.ttf",
  "200": "http://fonts.gstatic.com/s/robotoserif/v8/R71RjywflP6FLr3gZx7K8UyuXDs9zVwDmXCb8lxYgmuii32UGoVldX6UgfjL4-3sMM_kB_qXSEXTJQCFLH5-_bcElqotp6d2Af5fR4k.ttf",
  "300": "http://fonts.gstatic.com/s/robotoserif/v8/R71RjywflP6FLr3gZx7K8UyuXDs9zVwDmXCb8lxYgmuii32UGoVldX6UgfjL4-3sMM_kB_qXSEXTJQCFLH5-_bcElnQtp6d2Af5fR4k.ttf",
  "500": "http://fonts.gstatic.com/s/robotoserif/v8/R71RjywflP6FLr3gZx7K8UyuXDs9zVwDmXCb8lxYgmuii32UGoVldX6UgfjL4-3sMM_kB_qXSEXTJQCFLH5-_bcElhgtp6d2Af5fR4k.ttf",
  "600": "http://fonts.gstatic.com/s/robotoserif/v8/R71RjywflP6FLr3gZx7K8UyuXDs9zVwDmXCb8lxYgmuii32UGoVldX6UgfjL4-3sMM_kB_qXSEXTJQCFLH5-_bcElvQqp6d2Af5fR4k.ttf",
  "700": "http://fonts.gstatic.com/s/robotoserif/v8/R71RjywflP6FLr3gZx7K8UyuXDs9zVwDmXCb8lxYgmuii32UGoVldX6UgfjL4-3sMM_kB_qXSEXTJQCFLH5-_bcEls0qp6d2Af5fR4k.ttf",
  "800": "http://fonts.gstatic.com/s/robotoserif/v8/R71RjywflP6FLr3gZx7K8UyuXDs9zVwDmXCb8lxYgmuii32UGoVldX6UgfjL4-3sMM_kB_qXSEXTJQCFLH5-_bcElqoqp6d2Af5fR4k.ttf",
  "900": "http://fonts.gstatic.com/s/robotoserif/v8/R71RjywflP6FLr3gZx7K8UyuXDs9zVwDmXCb8lxYgmuii32UGoVldX6UgfjL4-3sMM_kB_qXSEXTJQCFLH5-_bcEloMqp6d2Af5fR4k.ttf",
  "regular": "http://fonts.gstatic.com/s/robotoserif/v8/R71RjywflP6FLr3gZx7K8UyuXDs9zVwDmXCb8lxYgmuii32UGoVldX6UgfjL4-3sMM_kB_qXSEXTJQCFLH5-_bcEliotp6d2Af5fR4k.ttf",
  "100italic": "http://fonts.gstatic.com/s/robotoserif/v8/R71XjywflP6FLr3gZx7K8UyEVQnyR1E7VN-f51xYuGCQepOvB0KLc2v0wKKB0Q4MSZxyqf2CgAchbDJ69BcVZxkDg-JuT-V8BdxaV4nUFw.ttf",
  "200italic": "http://fonts.gstatic.com/s/robotoserif/v8/R71XjywflP6FLr3gZx7K8UyEVQnyR1E7VN-f51xYuGCQepOvB0KLc2v0wKKB0Q4MSZxyqf2CgAchbDJ69BcVZxkDg-Juz-R8BdxaV4nUFw.ttf",
  "300italic": "http://fonts.gstatic.com/s/robotoserif/v8/R71XjywflP6FLr3gZx7K8UyEVQnyR1E7VN-f51xYuGCQepOvB0KLc2v0wKKB0Q4MSZxyqf2CgAchbDJ69BcVZxkDg-JuEeR8BdxaV4nUFw.ttf",
  "italic": "http://fonts.gstatic.com/s/robotoserif/v8/R71XjywflP6FLr3gZx7K8UyEVQnyR1E7VN-f51xYuGCQepOvB0KLc2v0wKKB0Q4MSZxyqf2CgAchbDJ69BcVZxkDg-JuT-R8BdxaV4nUFw.ttf",
  "500italic": "http://fonts.gstatic.com/s/robotoserif/v8/R71XjywflP6FLr3gZx7K8UyEVQnyR1E7VN-f51xYuGCQepOvB0KLc2v0wKKB0Q4MSZxyqf2CgAchbDJ69BcVZxkDg-JufeR8BdxaV4nUFw.ttf",
  "600italic": "http://fonts.gstatic.com/s/robotoserif/v8/R71XjywflP6FLr3gZx7K8UyEVQnyR1E7VN-f51xYuGCQepOvB0KLc2v0wKKB0Q4MSZxyqf2CgAchbDJ69BcVZxkDg-JukeN8BdxaV4nUFw.ttf",
  "700italic": "http://fonts.gstatic.com/s/robotoserif/v8/R71XjywflP6FLr3gZx7K8UyEVQnyR1E7VN-f51xYuGCQepOvB0KLc2v0wKKB0Q4MSZxyqf2CgAchbDJ69BcVZxkDg-JuqON8BdxaV4nUFw.ttf",
  "800italic": "http://fonts.gstatic.com/s/robotoserif/v8/R71XjywflP6FLr3gZx7K8UyEVQnyR1E7VN-f51xYuGCQepOvB0KLc2v0wKKB0Q4MSZxyqf2CgAchbDJ69BcVZxkDg-Juz-N8BdxaV4nUFw.ttf",
  "900italic": "http://fonts.gstatic.com/s/robotoserif/v8/R71XjywflP6FLr3gZx7K8UyEVQnyR1E7VN-f51xYuGCQepOvB0KLc2v0wKKB0Q4MSZxyqf2CgAchbDJ69BcVZxkDg-Ju5uN8BdxaV4nUFw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Roboto Slab",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/robotoslab/v24/BngbUXZYTXPIvIBgJJSb6s3BzlRRfKOFbvjojIWWaG5iddG-1A.ttf",
  "200": "http://fonts.gstatic.com/s/robotoslab/v24/BngbUXZYTXPIvIBgJJSb6s3BzlRRfKOFbvjoDISWaG5iddG-1A.ttf",
  "300": "http://fonts.gstatic.com/s/robotoslab/v24/BngbUXZYTXPIvIBgJJSb6s3BzlRRfKOFbvjo0oSWaG5iddG-1A.ttf",
  "500": "http://fonts.gstatic.com/s/robotoslab/v24/BngbUXZYTXPIvIBgJJSb6s3BzlRRfKOFbvjovoSWaG5iddG-1A.ttf",
  "600": "http://fonts.gstatic.com/s/robotoslab/v24/BngbUXZYTXPIvIBgJJSb6s3BzlRRfKOFbvjoUoOWaG5iddG-1A.ttf",
  "700": "http://fonts.gstatic.com/s/robotoslab/v24/BngbUXZYTXPIvIBgJJSb6s3BzlRRfKOFbvjoa4OWaG5iddG-1A.ttf",
  "800": "http://fonts.gstatic.com/s/robotoslab/v24/BngbUXZYTXPIvIBgJJSb6s3BzlRRfKOFbvjoDIOWaG5iddG-1A.ttf",
  "900": "http://fonts.gstatic.com/s/robotoslab/v24/BngbUXZYTXPIvIBgJJSb6s3BzlRRfKOFbvjoJYOWaG5iddG-1A.ttf",
  "regular": "http://fonts.gstatic.com/s/robotoslab/v24/BngbUXZYTXPIvIBgJJSb6s3BzlRRfKOFbvjojISWaG5iddG-1A.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rochester",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rochester/v18/6ae-4KCqVa4Zy6Fif-Uy31vWNTMwoQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rock Salt",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rocksalt/v18/MwQ0bhv11fWD6QsAVOZbsEk7hbBWrA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "RocknRoll One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rocknrollone/v10/kmK7ZqspGAfCeUiW6FFlmEC9guVhs7tfUxc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rokkitt",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v29",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/rokkitt/v29/qFdb35qfgYFjGy5hukqqhw5XeRgdi1rydpDLE76HvN6n.ttf",
  "200": "http://fonts.gstatic.com/s/rokkitt/v29/qFdb35qfgYFjGy5hukqqhw5XeRgdi1pyd5DLE76HvN6n.ttf",
  "300": "http://fonts.gstatic.com/s/rokkitt/v29/qFdb35qfgYFjGy5hukqqhw5XeRgdi1qsd5DLE76HvN6n.ttf",
  "500": "http://fonts.gstatic.com/s/rokkitt/v29/qFdb35qfgYFjGy5hukqqhw5XeRgdi1rAd5DLE76HvN6n.ttf",
  "600": "http://fonts.gstatic.com/s/rokkitt/v29/qFdb35qfgYFjGy5hukqqhw5XeRgdi1oscJDLE76HvN6n.ttf",
  "700": "http://fonts.gstatic.com/s/rokkitt/v29/qFdb35qfgYFjGy5hukqqhw5XeRgdi1oVcJDLE76HvN6n.ttf",
  "800": "http://fonts.gstatic.com/s/rokkitt/v29/qFdb35qfgYFjGy5hukqqhw5XeRgdi1pycJDLE76HvN6n.ttf",
  "900": "http://fonts.gstatic.com/s/rokkitt/v29/qFdb35qfgYFjGy5hukqqhw5XeRgdi1pbcJDLE76HvN6n.ttf",
  "regular": "http://fonts.gstatic.com/s/rokkitt/v29/qFdb35qfgYFjGy5hukqqhw5XeRgdi1ryd5DLE76HvN6n.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Romanesco",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/romanesco/v21/w8gYH2ozQOY7_r_J7mSn3HwLqOqSBg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ropa Sans",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ropasans/v15/EYqxmaNOzLlWtsZSScyKWjloU5KP2g.ttf",
  "italic": "http://fonts.gstatic.com/s/ropasans/v15/EYq3maNOzLlWtsZSScy6WDNscZef2mNE.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rosario",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v27",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/rosario/v27/xfuu0WDhWW_fOEoY8l_VPNZfB7jPM69GCWczd-YnOzUD.ttf",
  "500": "http://fonts.gstatic.com/s/rosario/v27/xfuu0WDhWW_fOEoY8l_VPNZfB7jPM68qCWczd-YnOzUD.ttf",
  "600": "http://fonts.gstatic.com/s/rosario/v27/xfuu0WDhWW_fOEoY8l_VPNZfB7jPM6_GDmczd-YnOzUD.ttf",
  "700": "http://fonts.gstatic.com/s/rosario/v27/xfuu0WDhWW_fOEoY8l_VPNZfB7jPM6__Dmczd-YnOzUD.ttf",
  "regular": "http://fonts.gstatic.com/s/rosario/v27/xfuu0WDhWW_fOEoY8l_VPNZfB7jPM68YCWczd-YnOzUD.ttf",
  "300italic": "http://fonts.gstatic.com/s/rosario/v27/xfug0WDhWW_fOEoY2Fbnww42bCJhNLrQStFwfeIFPiUDn08.ttf",
  "italic": "http://fonts.gstatic.com/s/rosario/v27/xfug0WDhWW_fOEoY2Fbnww42bCJhNLrQSo9wfeIFPiUDn08.ttf",
  "500italic": "http://fonts.gstatic.com/s/rosario/v27/xfug0WDhWW_fOEoY2Fbnww42bCJhNLrQSr1wfeIFPiUDn08.ttf",
  "600italic": "http://fonts.gstatic.com/s/rosario/v27/xfug0WDhWW_fOEoY2Fbnww42bCJhNLrQSlF3feIFPiUDn08.ttf",
  "700italic": "http://fonts.gstatic.com/s/rosario/v27/xfug0WDhWW_fOEoY2Fbnww42bCJhNLrQSmh3feIFPiUDn08.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rosarivo",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rosarivo/v20/PlI-Fl2lO6N9f8HaNAeC2nhMnNy5.ttf",
  "italic": "http://fonts.gstatic.com/s/rosarivo/v20/PlI4Fl2lO6N9f8HaNDeA0Hxumcy5ZX8.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rouge Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rougescript/v14/LYjFdGbiklMoCIQOw1Ep3S4PVPXbUJWq9g.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rowdies",
  "variants": [
  "300",
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/rowdies/v15/ptRMTieMYPNBAK219hth5O7yKQNute8.ttf",
  "700": "http://fonts.gstatic.com/s/rowdies/v15/ptRMTieMYPNBAK219gtm5O7yKQNute8.ttf",
  "regular": "http://fonts.gstatic.com/s/rowdies/v15/ptRJTieMYPNBAK21zrdJwObZNQo.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rozha One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rozhaone/v13/AlZy_zVFtYP12Zncg2khdXf4XB0Tow.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/rubik/v21/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-WYi1UE80V4bVkA.ttf",
  "500": "http://fonts.gstatic.com/s/rubik/v21/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-NYi1UE80V4bVkA.ttf",
  "600": "http://fonts.gstatic.com/s/rubik/v21/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-2Y-1UE80V4bVkA.ttf",
  "700": "http://fonts.gstatic.com/s/rubik/v21/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-4I-1UE80V4bVkA.ttf",
  "800": "http://fonts.gstatic.com/s/rubik/v21/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-h4-1UE80V4bVkA.ttf",
  "900": "http://fonts.gstatic.com/s/rubik/v21/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-ro-1UE80V4bVkA.ttf",
  "regular": "http://fonts.gstatic.com/s/rubik/v21/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-B4i1UE80V4bVkA.ttf",
  "300italic": "http://fonts.gstatic.com/s/rubik/v21/iJWbBXyIfDnIV7nEt3KSJbVDV49rz8sDE0UwdYPFkJ1O.ttf",
  "italic": "http://fonts.gstatic.com/s/rubik/v21/iJWbBXyIfDnIV7nEt3KSJbVDV49rz8tdE0UwdYPFkJ1O.ttf",
  "500italic": "http://fonts.gstatic.com/s/rubik/v21/iJWbBXyIfDnIV7nEt3KSJbVDV49rz8tvE0UwdYPFkJ1O.ttf",
  "600italic": "http://fonts.gstatic.com/s/rubik/v21/iJWbBXyIfDnIV7nEt3KSJbVDV49rz8uDFEUwdYPFkJ1O.ttf",
  "700italic": "http://fonts.gstatic.com/s/rubik/v21/iJWbBXyIfDnIV7nEt3KSJbVDV49rz8u6FEUwdYPFkJ1O.ttf",
  "800italic": "http://fonts.gstatic.com/s/rubik/v21/iJWbBXyIfDnIV7nEt3KSJbVDV49rz8vdFEUwdYPFkJ1O.ttf",
  "900italic": "http://fonts.gstatic.com/s/rubik/v21/iJWbBXyIfDnIV7nEt3KSJbVDV49rz8v0FEUwdYPFkJ1O.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Beastly",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikbeastly/v10/0QImMXRd5oOmSC2ZQ7o9653X07z8_ApHqqk.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Bubbles",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikbubbles/v2/JIA1UVdwbHFJtwA7Us1BPFbRNTENfDxyRXI.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Burned",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikburned/v1/Jqzk5TmOVOqQHihKqPpscqniHQuaCY5ZSg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Dirt",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikdirt/v1/DtVmJxC7WLEj1uIXEWAdulwm6gDXvwE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Distressed",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikdistressed/v1/GFDxWBdsmnqAVqjtUsZf2dcrQ2ldcWAhatVBaGM.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Glitch",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikglitch/v2/qkBSXv8b_srFRYQVYrDKh9ZvmC7HONiSFQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Iso",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikiso/v1/x3dickHUfr-S4VAI4sABfPACvy_1BA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Marker Hatch",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikmarkerhatch/v1/QldTNSFQsh0B_bFXXWv6LAt-jswapJHQDL4iw0H6zw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Maze",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikmaze/v1/xMQRuF9ZVa2ftiJEavXSAX7inS-bxV4.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Microbe",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikmicrobe/v2/UqyWK8oPP3hjw6ANS9rM3PsZcs8aaKgiauE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Mono One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikmonoone/v14/UqyJK8kPP3hjw6ANTdfRk9YSN-8wRqQrc_j9.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Moonrocks",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikmoonrocks/v2/845ANMAmAI2VUZMLu_W0M7HqlDHnXcD7JGy1Sw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Puddles",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikpuddles/v2/1Ptog8bYX_qGnkLkrU5MJsQcJfC0wVMT-aE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rubik Wet Paint",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rubikwetpaint/v2/HTx0L20uMDGHgdULcpTF3Oe4d_-F-zz313DuvQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ruda",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/ruda/v23/k3kKo8YQJOpFgHQ1mQ5VkEbUKaJ3si_-2KiSGg-H.ttf",
  "600": "http://fonts.gstatic.com/s/ruda/v23/k3kKo8YQJOpFgHQ1mQ5VkEbUKaKbtS_-2KiSGg-H.ttf",
  "700": "http://fonts.gstatic.com/s/ruda/v23/k3kKo8YQJOpFgHQ1mQ5VkEbUKaKitS_-2KiSGg-H.ttf",
  "800": "http://fonts.gstatic.com/s/ruda/v23/k3kKo8YQJOpFgHQ1mQ5VkEbUKaLFtS_-2KiSGg-H.ttf",
  "900": "http://fonts.gstatic.com/s/ruda/v23/k3kKo8YQJOpFgHQ1mQ5VkEbUKaLstS_-2KiSGg-H.ttf",
  "regular": "http://fonts.gstatic.com/s/ruda/v23/k3kKo8YQJOpFgHQ1mQ5VkEbUKaJFsi_-2KiSGg-H.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rufina",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/rufina/v13/Yq6W-LyURyLy-aKKHztAvMxenxE0SA.ttf",
  "regular": "http://fonts.gstatic.com/s/rufina/v13/Yq6V-LyURyLy-aKyoxRktOdClg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ruge Boogie",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rugeboogie/v24/JIA3UVFwbHRF_GIWSMhKNROiPzUveSxy.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ruluko",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ruluko/v21/xMQVuFNZVaODtm0pC6WzKX_QmA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rum Raisin",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rumraisin/v20/nwpRtKu3Ih8D5avB4h2uJ3-IywA7eMM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ruslan Display",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ruslandisplay/v22/Gw6jwczl81XcIZuckK_e3UpfdzxrldyFvm1n.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Russo One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/russoone/v14/Z9XUDmZRWg6M1LvRYsH-yMOInrib9Q.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ruthie",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ruthie/v24/gokvH63sGkdqXuU9lD53Q2u_mQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Rye",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/rye/v13/r05XGLJT86YDFpTsXOqx4w.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "STIX Two Text",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/stixtwotext/v10/YA9Gr02F12Xkf5whdwKf11l0jbKkeidMTtZ5YihS2SOYWxFMN1WD.ttf",
  "600": "http://fonts.gstatic.com/s/stixtwotext/v10/YA9Gr02F12Xkf5whdwKf11l0jbKkeidMTtZ5Yii-3iOYWxFMN1WD.ttf",
  "700": "http://fonts.gstatic.com/s/stixtwotext/v10/YA9Gr02F12Xkf5whdwKf11l0jbKkeidMTtZ5YiiH3iOYWxFMN1WD.ttf",
  "regular": "http://fonts.gstatic.com/s/stixtwotext/v10/YA9Gr02F12Xkf5whdwKf11l0jbKkeidMTtZ5Yihg2SOYWxFMN1WD.ttf",
  "italic": "http://fonts.gstatic.com/s/stixtwotext/v10/YA9Er02F12Xkf5whdwKf11l0p7uWhf8lJUzXZT2omsvbURVuMkWDmSo.ttf",
  "500italic": "http://fonts.gstatic.com/s/stixtwotext/v10/YA9Er02F12Xkf5whdwKf11l0p7uWhf8lJUzXZT2omvnbURVuMkWDmSo.ttf",
  "600italic": "http://fonts.gstatic.com/s/stixtwotext/v10/YA9Er02F12Xkf5whdwKf11l0p7uWhf8lJUzXZT2omhXcURVuMkWDmSo.ttf",
  "700italic": "http://fonts.gstatic.com/s/stixtwotext/v10/YA9Er02F12Xkf5whdwKf11l0p7uWhf8lJUzXZT2omizcURVuMkWDmSo.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sacramento",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sacramento/v13/buEzpo6gcdjy0EiZMBUG0CoV_NxLeiw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sahitya",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/sahitya/v17/6qLFKZkOuhnuqlJAUZsqGyQvEnvSexI.ttf",
  "regular": "http://fonts.gstatic.com/s/sahitya/v17/6qLAKZkOuhnuqlJAaScFPywEDnI.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sail",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sail/v16/DPEjYwiBxwYJFBTDADYAbvw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Saira",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/saira/v14/memWYa2wxmKQyPMrZX79wwYZQMhsyuShhKMjjbU9uXuA71rDosg7lwYmUVY.ttf",
  "200": "http://fonts.gstatic.com/s/saira/v14/memWYa2wxmKQyPMrZX79wwYZQMhsyuShhKMjjbU9uXuA79rCosg7lwYmUVY.ttf",
  "300": "http://fonts.gstatic.com/s/saira/v14/memWYa2wxmKQyPMrZX79wwYZQMhsyuShhKMjjbU9uXuA7wTCosg7lwYmUVY.ttf",
  "500": "http://fonts.gstatic.com/s/saira/v14/memWYa2wxmKQyPMrZX79wwYZQMhsyuShhKMjjbU9uXuA72jCosg7lwYmUVY.ttf",
  "600": "http://fonts.gstatic.com/s/saira/v14/memWYa2wxmKQyPMrZX79wwYZQMhsyuShhKMjjbU9uXuA74TFosg7lwYmUVY.ttf",
  "700": "http://fonts.gstatic.com/s/saira/v14/memWYa2wxmKQyPMrZX79wwYZQMhsyuShhKMjjbU9uXuA773Fosg7lwYmUVY.ttf",
  "800": "http://fonts.gstatic.com/s/saira/v14/memWYa2wxmKQyPMrZX79wwYZQMhsyuShhKMjjbU9uXuA79rFosg7lwYmUVY.ttf",
  "900": "http://fonts.gstatic.com/s/saira/v14/memWYa2wxmKQyPMrZX79wwYZQMhsyuShhKMjjbU9uXuA7_PFosg7lwYmUVY.ttf",
  "regular": "http://fonts.gstatic.com/s/saira/v14/memWYa2wxmKQyPMrZX79wwYZQMhsyuShhKMjjbU9uXuA71rCosg7lwYmUVY.ttf",
  "100italic": "http://fonts.gstatic.com/s/saira/v14/memUYa2wxmKQyNkiV50dulWP7s95AqZTzZHcVdxWI9WH-pKBSooxkyQjQVYmxA.ttf",
  "200italic": "http://fonts.gstatic.com/s/saira/v14/memUYa2wxmKQyNkiV50dulWP7s95AqZTzZHcVdxWI9WH-pKByosxkyQjQVYmxA.ttf",
  "300italic": "http://fonts.gstatic.com/s/saira/v14/memUYa2wxmKQyNkiV50dulWP7s95AqZTzZHcVdxWI9WH-pKBFIsxkyQjQVYmxA.ttf",
  "italic": "http://fonts.gstatic.com/s/saira/v14/memUYa2wxmKQyNkiV50dulWP7s95AqZTzZHcVdxWI9WH-pKBSosxkyQjQVYmxA.ttf",
  "500italic": "http://fonts.gstatic.com/s/saira/v14/memUYa2wxmKQyNkiV50dulWP7s95AqZTzZHcVdxWI9WH-pKBeIsxkyQjQVYmxA.ttf",
  "600italic": "http://fonts.gstatic.com/s/saira/v14/memUYa2wxmKQyNkiV50dulWP7s95AqZTzZHcVdxWI9WH-pKBlIwxkyQjQVYmxA.ttf",
  "700italic": "http://fonts.gstatic.com/s/saira/v14/memUYa2wxmKQyNkiV50dulWP7s95AqZTzZHcVdxWI9WH-pKBrYwxkyQjQVYmxA.ttf",
  "800italic": "http://fonts.gstatic.com/s/saira/v14/memUYa2wxmKQyNkiV50dulWP7s95AqZTzZHcVdxWI9WH-pKByowxkyQjQVYmxA.ttf",
  "900italic": "http://fonts.gstatic.com/s/saira/v14/memUYa2wxmKQyNkiV50dulWP7s95AqZTzZHcVdxWI9WH-pKB44wxkyQjQVYmxA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Saira Condensed",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/sairacondensed/v11/EJRMQgErUN8XuHNEtX81i9TmEkrnwetA2omSrzS8.ttf",
  "200": "http://fonts.gstatic.com/s/sairacondensed/v11/EJRLQgErUN8XuHNEtX81i9TmEkrnbcpg8Keepi2lHw.ttf",
  "300": "http://fonts.gstatic.com/s/sairacondensed/v11/EJRLQgErUN8XuHNEtX81i9TmEkrnCclg8Keepi2lHw.ttf",
  "500": "http://fonts.gstatic.com/s/sairacondensed/v11/EJRLQgErUN8XuHNEtX81i9TmEkrnUchg8Keepi2lHw.ttf",
  "600": "http://fonts.gstatic.com/s/sairacondensed/v11/EJRLQgErUN8XuHNEtX81i9TmEkrnfc9g8Keepi2lHw.ttf",
  "700": "http://fonts.gstatic.com/s/sairacondensed/v11/EJRLQgErUN8XuHNEtX81i9TmEkrnGc5g8Keepi2lHw.ttf",
  "800": "http://fonts.gstatic.com/s/sairacondensed/v11/EJRLQgErUN8XuHNEtX81i9TmEkrnBc1g8Keepi2lHw.ttf",
  "900": "http://fonts.gstatic.com/s/sairacondensed/v11/EJRLQgErUN8XuHNEtX81i9TmEkrnIcxg8Keepi2lHw.ttf",
  "regular": "http://fonts.gstatic.com/s/sairacondensed/v11/EJROQgErUN8XuHNEtX81i9TmEkrfpeFE-IyCrw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Saira Extra Condensed",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/sairaextracondensed/v11/-nFsOHYr-vcC7h8MklGBkrvmUG9rbpkisrTri0jx9i5ss3a3.ttf",
  "200": "http://fonts.gstatic.com/s/sairaextracondensed/v11/-nFvOHYr-vcC7h8MklGBkrvmUG9rbpkisrTrJ2nR3ABgum-uoQ.ttf",
  "300": "http://fonts.gstatic.com/s/sairaextracondensed/v11/-nFvOHYr-vcC7h8MklGBkrvmUG9rbpkisrTrQ2rR3ABgum-uoQ.ttf",
  "500": "http://fonts.gstatic.com/s/sairaextracondensed/v11/-nFvOHYr-vcC7h8MklGBkrvmUG9rbpkisrTrG2vR3ABgum-uoQ.ttf",
  "600": "http://fonts.gstatic.com/s/sairaextracondensed/v11/-nFvOHYr-vcC7h8MklGBkrvmUG9rbpkisrTrN2zR3ABgum-uoQ.ttf",
  "700": "http://fonts.gstatic.com/s/sairaextracondensed/v11/-nFvOHYr-vcC7h8MklGBkrvmUG9rbpkisrTrU23R3ABgum-uoQ.ttf",
  "800": "http://fonts.gstatic.com/s/sairaextracondensed/v11/-nFvOHYr-vcC7h8MklGBkrvmUG9rbpkisrTrT27R3ABgum-uoQ.ttf",
  "900": "http://fonts.gstatic.com/s/sairaextracondensed/v11/-nFvOHYr-vcC7h8MklGBkrvmUG9rbpkisrTra2_R3ABgum-uoQ.ttf",
  "regular": "http://fonts.gstatic.com/s/sairaextracondensed/v11/-nFiOHYr-vcC7h8MklGBkrvmUG9rbpkisrTT70L11Ct8sw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Saira Semi Condensed",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/sairasemicondensed/v11/U9MN6c-2-nnJkHxyCjRcnMHcWVWV1cWRRXdvaOM8rXT-8V8.ttf",
  "200": "http://fonts.gstatic.com/s/sairasemicondensed/v11/U9MM6c-2-nnJkHxyCjRcnMHcWVWV1cWRRXfDScMWg3j36Ebz.ttf",
  "300": "http://fonts.gstatic.com/s/sairasemicondensed/v11/U9MM6c-2-nnJkHxyCjRcnMHcWVWV1cWRRXenSsMWg3j36Ebz.ttf",
  "500": "http://fonts.gstatic.com/s/sairasemicondensed/v11/U9MM6c-2-nnJkHxyCjRcnMHcWVWV1cWRRXf_S8MWg3j36Ebz.ttf",
  "600": "http://fonts.gstatic.com/s/sairasemicondensed/v11/U9MM6c-2-nnJkHxyCjRcnMHcWVWV1cWRRXfTTMMWg3j36Ebz.ttf",
  "700": "http://fonts.gstatic.com/s/sairasemicondensed/v11/U9MM6c-2-nnJkHxyCjRcnMHcWVWV1cWRRXe3TcMWg3j36Ebz.ttf",
  "800": "http://fonts.gstatic.com/s/sairasemicondensed/v11/U9MM6c-2-nnJkHxyCjRcnMHcWVWV1cWRRXerTsMWg3j36Ebz.ttf",
  "900": "http://fonts.gstatic.com/s/sairasemicondensed/v11/U9MM6c-2-nnJkHxyCjRcnMHcWVWV1cWRRXePT8MWg3j36Ebz.ttf",
  "regular": "http://fonts.gstatic.com/s/sairasemicondensed/v11/U9MD6c-2-nnJkHxyCjRcnMHcWVWV1cWRRU8LYuceqGT-.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Saira Stencil One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sairastencilone/v14/SLXSc03I6HkvZGJ1GvvipLoYSTEL9AsMawif2YQ2.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Salsa",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/salsa/v17/gNMKW3FiRpKj-imY8ncKEZez.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sanchez",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sanchez/v13/Ycm2sZJORluHnXbITm5b_BwE1l0.ttf",
  "italic": "http://fonts.gstatic.com/s/sanchez/v13/Ycm0sZJORluHnXbIfmxR-D4Bxl3gkw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sancreek",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sancreek/v23/pxiHypAnsdxUm159X7D-XV9NEe-K.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sansita",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/sansita/v10/QldLNTRRphEb_-V7JKWUaXl0wqVv3_g.ttf",
  "800": "http://fonts.gstatic.com/s/sansita/v10/QldLNTRRphEb_-V7JLmXaXl0wqVv3_g.ttf",
  "900": "http://fonts.gstatic.com/s/sansita/v10/QldLNTRRphEb_-V7JJ2WaXl0wqVv3_g.ttf",
  "regular": "http://fonts.gstatic.com/s/sansita/v10/QldONTRRphEb_-V7HBm7TXFf3qw.ttf",
  "italic": "http://fonts.gstatic.com/s/sansita/v10/QldMNTRRphEb_-V7LBuxSVNazqx2xg.ttf",
  "700italic": "http://fonts.gstatic.com/s/sansita/v10/QldJNTRRphEb_-V7LBuJ9Xx-xodqz_joDQ.ttf",
  "800italic": "http://fonts.gstatic.com/s/sansita/v10/QldJNTRRphEb_-V7LBuJ6X9-xodqz_joDQ.ttf",
  "900italic": "http://fonts.gstatic.com/s/sansita/v10/QldJNTRRphEb_-V7LBuJzX5-xodqz_joDQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sansita Swashed",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/sansitaswashed/v17/BXR8vFfZifTZgFlDDLgNkBydPKTt3pVCeYWqJnZSW-ppbToVehmEa4Q.ttf",
  "500": "http://fonts.gstatic.com/s/sansitaswashed/v17/BXR8vFfZifTZgFlDDLgNkBydPKTt3pVCeYWqJnZSW4ZpbToVehmEa4Q.ttf",
  "600": "http://fonts.gstatic.com/s/sansitaswashed/v17/BXR8vFfZifTZgFlDDLgNkBydPKTt3pVCeYWqJnZSW2pubToVehmEa4Q.ttf",
  "700": "http://fonts.gstatic.com/s/sansitaswashed/v17/BXR8vFfZifTZgFlDDLgNkBydPKTt3pVCeYWqJnZSW1NubToVehmEa4Q.ttf",
  "800": "http://fonts.gstatic.com/s/sansitaswashed/v17/BXR8vFfZifTZgFlDDLgNkBydPKTt3pVCeYWqJnZSWzRubToVehmEa4Q.ttf",
  "900": "http://fonts.gstatic.com/s/sansitaswashed/v17/BXR8vFfZifTZgFlDDLgNkBydPKTt3pVCeYWqJnZSWx1ubToVehmEa4Q.ttf",
  "regular": "http://fonts.gstatic.com/s/sansitaswashed/v17/BXR8vFfZifTZgFlDDLgNkBydPKTt3pVCeYWqJnZSW7RpbToVehmEa4Q.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sarabun",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/sarabun/v13/DtVhJx26TKEr37c9YHZJmnYI5gnOpg.ttf",
  "200": "http://fonts.gstatic.com/s/sarabun/v13/DtVmJx26TKEr37c9YNpoulwm6gDXvwE.ttf",
  "300": "http://fonts.gstatic.com/s/sarabun/v13/DtVmJx26TKEr37c9YL5rulwm6gDXvwE.ttf",
  "500": "http://fonts.gstatic.com/s/sarabun/v13/DtVmJx26TKEr37c9YOZqulwm6gDXvwE.ttf",
  "600": "http://fonts.gstatic.com/s/sarabun/v13/DtVmJx26TKEr37c9YMptulwm6gDXvwE.ttf",
  "700": "http://fonts.gstatic.com/s/sarabun/v13/DtVmJx26TKEr37c9YK5sulwm6gDXvwE.ttf",
  "800": "http://fonts.gstatic.com/s/sarabun/v13/DtVmJx26TKEr37c9YLJvulwm6gDXvwE.ttf",
  "100italic": "http://fonts.gstatic.com/s/sarabun/v13/DtVnJx26TKEr37c9aBBx_nwMxAzephhN.ttf",
  "200italic": "http://fonts.gstatic.com/s/sarabun/v13/DtVkJx26TKEr37c9aBBxUl0s7iLSrwFUlw.ttf",
  "300italic": "http://fonts.gstatic.com/s/sarabun/v13/DtVkJx26TKEr37c9aBBxNl4s7iLSrwFUlw.ttf",
  "regular": "http://fonts.gstatic.com/s/sarabun/v13/DtVjJx26TKEr37c9WBJDnlQN9gk.ttf",
  "italic": "http://fonts.gstatic.com/s/sarabun/v13/DtVhJx26TKEr37c9aBBJmnYI5gnOpg.ttf",
  "500italic": "http://fonts.gstatic.com/s/sarabun/v13/DtVkJx26TKEr37c9aBBxbl8s7iLSrwFUlw.ttf",
  "600italic": "http://fonts.gstatic.com/s/sarabun/v13/DtVkJx26TKEr37c9aBBxQlgs7iLSrwFUlw.ttf",
  "700italic": "http://fonts.gstatic.com/s/sarabun/v13/DtVkJx26TKEr37c9aBBxJlks7iLSrwFUlw.ttf",
  "800italic": "http://fonts.gstatic.com/s/sarabun/v13/DtVkJx26TKEr37c9aBBxOlos7iLSrwFUlw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sarala",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/sarala/v10/uK_x4riEZv4o1w9ptjI3OtWYVkMpXA.ttf",
  "regular": "http://fonts.gstatic.com/s/sarala/v10/uK_y4riEZv4o1w9RCh0TMv6EXw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sarina",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sarina/v21/-F6wfjF3ITQwasLhLkDUriBQxw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sarpanch",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/sarpanch/v11/hES16Xt4NCpRuk6PziV0ba7f1HEuRHkM.ttf",
  "600": "http://fonts.gstatic.com/s/sarpanch/v11/hES16Xt4NCpRuk6PziVYaq7f1HEuRHkM.ttf",
  "700": "http://fonts.gstatic.com/s/sarpanch/v11/hES16Xt4NCpRuk6PziU8a67f1HEuRHkM.ttf",
  "800": "http://fonts.gstatic.com/s/sarpanch/v11/hES16Xt4NCpRuk6PziUgaK7f1HEuRHkM.ttf",
  "900": "http://fonts.gstatic.com/s/sarpanch/v11/hES16Xt4NCpRuk6PziUEaa7f1HEuRHkM.ttf",
  "regular": "http://fonts.gstatic.com/s/sarpanch/v11/hESy6Xt4NCpRuk6Pzh2ARIrX_20n.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sassy Frass",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sassyfrass/v5/LhWhMVrGOe0FLb97BjhsE99dGNWQg_am.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Satisfy",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/satisfy/v17/rP2Hp2yn6lkG50LoOZSCHBeHFl0.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sawarabi Gothic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sawarabigothic/v12/x3d4ckfVaqqa-BEj-I9mE65u3k3NBSk3E2YljQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sawarabi Mincho",
  "variants": [
  "regular"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sawarabimincho/v17/8QIRdiDaitzr7brc8ahpxt6GcIJTLahP46UDUw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Scada",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/scada/v14/RLp8K5Pv5qumeVrU6BEgRVfmZOE5.ttf",
  "regular": "http://fonts.gstatic.com/s/scada/v14/RLpxK5Pv5qumeWJoxzUobkvv.ttf",
  "italic": "http://fonts.gstatic.com/s/scada/v14/RLp_K5Pv5qumeVJqzTEKa1vvffg.ttf",
  "700italic": "http://fonts.gstatic.com/s/scada/v14/RLp6K5Pv5qumeVJq9Y0lT1PEYfE5p6g.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Scheherazade New",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/scheherazadenew/v12/4UaerFhTvxVnHDvUkUiHg8jprP4DM79DHlYC-IKnoSE.ttf",
  "regular": "http://fonts.gstatic.com/s/scheherazadenew/v12/4UaZrFhTvxVnHDvUkUiHg8jprP4DCwNsOl4p5Is.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Schoolbell",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/schoolbell/v18/92zQtBZWOrcgoe-fgnJIVxIQ6mRqfiQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Scope One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/scopeone/v14/WBLnrEXKYFlGHrOKmGD1W0_MJMGxiQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Seaweed Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/seaweedscript/v13/bx6cNx6Tne2pxOATYE8C_Rsoe0WJ-KcGVbLW.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Secular One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/secularone/v11/8QINdiTajsj_87rMuMdKypDlMul7LJpK.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sedgwick Ave",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sedgwickave/v12/uK_04rKEYuguzAcSYRdWTJq8Xmg1Vcf5JA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sedgwick Ave Display",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sedgwickavedisplay/v19/xfuu0XPgU3jZPUoUo3ScvmPi-NapQ8OxM2czd-YnOzUD.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sen",
  "variants": [
  "regular",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/sen/v7/6xKudSxYI9__J9CoKkH1JHUQSQ.ttf",
  "800": "http://fonts.gstatic.com/s/sen/v7/6xKudSxYI9__O9OoKkH1JHUQSQ.ttf",
  "regular": "http://fonts.gstatic.com/s/sen/v7/6xKjdSxYI9_Hm_-MImrpLQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Send Flowers",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sendflowers/v2/If2PXTjtZS-0Xqy13uCQSULvxwjjouU1iw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sevillana",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sevillana/v21/KFOlCnWFscmDt1Bfiy1vAx05IsDqlA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Seymour One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/seymourone/v20/4iCp6Khla9xbjQpoWGGd0myIPYBvgpUI.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Shadows Into Light",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/shadowsintolight/v15/UqyNK9UOIntux_czAvDQx_ZcHqZXBNQDcsr4xzSMYA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Shadows Into Light Two",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/shadowsintolighttwo/v13/4iC86LVlZsRSjQhpWGedwyOoW-0A6_kpsyNmlAvNGLNnIF0.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Shalimar",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/shalimar/v5/uU9MCBoE6I6iNWFUvTPx8PCOg0uX.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Shanti",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/shanti/v23/t5thIREMM4uSDgzgU0ezpKfwzA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Share",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/share/v16/i7dJIFliZjKNF63xM56-WkJUQUq7.ttf",
  "regular": "http://fonts.gstatic.com/s/share/v16/i7dEIFliZjKNF5VNHLq2cV5d.ttf",
  "italic": "http://fonts.gstatic.com/s/share/v16/i7dKIFliZjKNF6VPFr6UdE5dWFM.ttf",
  "700italic": "http://fonts.gstatic.com/s/share/v16/i7dPIFliZjKNF6VPLgK7UEZ2RFq7AwU.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Share Tech",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sharetech/v17/7cHtv4Uyi5K0OeZ7bohUwHoDmTcibrA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Share Tech Mono",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sharetechmono/v15/J7aHnp1uDWRBEqV98dVQztYldFc7pAsEIc3Xew.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Shippori Antique",
  "variants": [
  "regular"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v8",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/shipporiantique/v8/-F6qfid3KC8pdMyzR0qRyFUht11v8ldPg-IUDNg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Shippori Antique B1",
  "variants": [
  "regular"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v8",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/shipporiantiqueb1/v8/2Eb7L_JwClR7Zl_UAKZ0mUHw3oMKd40grRFCj9-5Y8Y.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Shippori Mincho",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-27",
  "files": {
  "500": "http://fonts.gstatic.com/s/shipporimincho/v14/VdGDAZweH5EbgHY6YExcZfDoj0B4L9am5JEO5--2zg.ttf",
  "600": "http://fonts.gstatic.com/s/shipporimincho/v14/VdGDAZweH5EbgHY6YExcZfDoj0B4A9Gm5JEO5--2zg.ttf",
  "700": "http://fonts.gstatic.com/s/shipporimincho/v14/VdGDAZweH5EbgHY6YExcZfDoj0B4Z9Cm5JEO5--2zg.ttf",
  "800": "http://fonts.gstatic.com/s/shipporimincho/v14/VdGDAZweH5EbgHY6YExcZfDoj0B4e9Om5JEO5--2zg.ttf",
  "regular": "http://fonts.gstatic.com/s/shipporimincho/v14/VdGGAZweH5EbgHY6YExcZfDoj0BA2_-C7LoS7g.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Shippori Mincho B1",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-27",
  "files": {
  "500": "http://fonts.gstatic.com/s/shipporiminchob1/v19/~ChcKElNoaXBwb3JpIE1pbmNobyBCMRj0AyAAKgQIARgB.ttf",
  "600": "http://fonts.gstatic.com/s/shipporiminchob1/v19/~ChcKElNoaXBwb3JpIE1pbmNobyBCMRjYBCAAKgQIARgB.ttf",
  "700": "http://fonts.gstatic.com/s/shipporiminchob1/v19/~ChcKElNoaXBwb3JpIE1pbmNobyBCMRi8BSAAKgQIARgB.ttf",
  "800": "http://fonts.gstatic.com/s/shipporiminchob1/v19/~ChcKElNoaXBwb3JpIE1pbmNobyBCMRigBiAAKgQIARgB.ttf",
  "regular": "http://fonts.gstatic.com/s/shipporiminchob1/v19/~ChQKElNoaXBwb3JpIE1pbmNobyBCMSAAKgQIARgB.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Shojumaru",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/shojumaru/v15/rax_HiWfutkLLnaKCtlMBBJek0vA8A.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Short Stack",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/shortstack/v15/bMrzmS2X6p0jZC6EcmPFX-SScX8D0nq6.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Shrikhand",
  "variants": [
  "regular"
  ],
  "subsets": [
  "gujarati",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/shrikhand/v11/a8IbNovtLWfR7T7bMJwbBIiQ0zhMtA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Siemreap",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/siemreap/v24/Gg82N5oFbgLvHAfNl2YbnA8DLXpe.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sigmar One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sigmarone/v16/co3DmWZ8kjZuErj9Ta3dk6Pjp3Di8U0.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Signika",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/signika/v20/vEFO2_JTCgwQ5ejvMV0O96D01E8J0tIJHJbGhs_cfKe1.ttf",
  "500": "http://fonts.gstatic.com/s/signika/v20/vEFO2_JTCgwQ5ejvMV0O96D01E8J0tJlHJbGhs_cfKe1.ttf",
  "600": "http://fonts.gstatic.com/s/signika/v20/vEFO2_JTCgwQ5ejvMV0O96D01E8J0tKJG5bGhs_cfKe1.ttf",
  "700": "http://fonts.gstatic.com/s/signika/v20/vEFO2_JTCgwQ5ejvMV0O96D01E8J0tKwG5bGhs_cfKe1.ttf",
  "regular": "http://fonts.gstatic.com/s/signika/v20/vEFO2_JTCgwQ5ejvMV0O96D01E8J0tJXHJbGhs_cfKe1.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Signika Negative",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/signikanegative/v20/E21x_cfngu7HiRpPX3ZpNE4kY5zKSPmJXkF0VDD2RAr5S73st9hiuEq8.ttf",
  "500": "http://fonts.gstatic.com/s/signikanegative/v20/E21x_cfngu7HiRpPX3ZpNE4kY5zKSPmJXkF0VDD2RAqVS73st9hiuEq8.ttf",
  "600": "http://fonts.gstatic.com/s/signikanegative/v20/E21x_cfngu7HiRpPX3ZpNE4kY5zKSPmJXkF0VDD2RAp5TL3st9hiuEq8.ttf",
  "700": "http://fonts.gstatic.com/s/signikanegative/v20/E21x_cfngu7HiRpPX3ZpNE4kY5zKSPmJXkF0VDD2RApATL3st9hiuEq8.ttf",
  "regular": "http://fonts.gstatic.com/s/signikanegative/v20/E21x_cfngu7HiRpPX3ZpNE4kY5zKSPmJXkF0VDD2RAqnS73st9hiuEq8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Silkscreen",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/silkscreen/v1/m8JUjfVPf62XiF7kO-i9aAhATmuo2dudFvc.ttf",
  "regular": "http://fonts.gstatic.com/s/silkscreen/v1/m8JXjfVPf62XiF7kO-i9ULRvamODxdI.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Simonetta",
  "variants": [
  "regular",
  "italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v23",
  "lastModified": "2022-04-27",
  "files": {
  "900": "http://fonts.gstatic.com/s/simonetta/v23/x3dnckHVYrCU5BU15c45-N0mtwTpDQIrGg.ttf",
  "regular": "http://fonts.gstatic.com/s/simonetta/v23/x3dickHVYrCU5BU15c4BfPACvy_1BA.ttf",
  "italic": "http://fonts.gstatic.com/s/simonetta/v23/x3dkckHVYrCU5BU15c4xfvoGnSrlBBsy.ttf",
  "900italic": "http://fonts.gstatic.com/s/simonetta/v23/x3d5ckHVYrCU5BU15c4xfsKCsA7tLwc7Gn88.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Single Day",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean"
  ],
  "version": "v15",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/singleday/v15/LYjHdGDjlEgoAcF95EI5jVoFUNfeQJU.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sintony",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/sintony/v13/XoHj2YDqR7-98cVUGYgIn9cDkjLp6C8.ttf",
  "regular": "http://fonts.gstatic.com/s/sintony/v13/XoHm2YDqR7-98cVUITQnu98ojjs.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sirin Stencil",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sirinstencil/v21/mem4YaWwznmLx-lzGfN7MdRydchGBq6al6o.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Six Caps",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sixcaps/v16/6ae_4KGrU7VR7bNmabcS9XXaPCop.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Skranji",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/skranji/v13/OZpGg_dtriVFNerMW4eBtlzNwED-b4g.ttf",
  "regular": "http://fonts.gstatic.com/s/skranji/v13/OZpDg_dtriVFNerMYzuuklTm3Ek.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Slabo 13px",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/slabo13px/v13/11hEGp_azEvXZUdSBzzRcKer2wkYnvI.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Slabo 27px",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/slabo27px/v12/mFT0WbgBwKPR_Z4hGN2qsxgJ1EJ7i90.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Slackey",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/slackey/v24/N0bV2SdQO-5yM0-dKlRaJdbWgdY.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Smokum",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/smokum/v24/TK3iWkUbAhopmrdGHjUHte5fKg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Smooch",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v5",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/smooch/v5/o-0LIps4xW8U1xUBjqp_6hVdYg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Smooch Sans",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v6",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/smoochsans/v6/c4mz1n5uGsXss2LJh1QH6b129FZvxPj6I4oiwUFodqIeNlzayg.ttf",
  "200": "http://fonts.gstatic.com/s/smoochsans/v6/c4mz1n5uGsXss2LJh1QH6b129FZvxPj6I4oiQUBodqIeNlzayg.ttf",
  "300": "http://fonts.gstatic.com/s/smoochsans/v6/c4mz1n5uGsXss2LJh1QH6b129FZvxPj6I4oin0BodqIeNlzayg.ttf",
  "500": "http://fonts.gstatic.com/s/smoochsans/v6/c4mz1n5uGsXss2LJh1QH6b129FZvxPj6I4oi80BodqIeNlzayg.ttf",
  "600": "http://fonts.gstatic.com/s/smoochsans/v6/c4mz1n5uGsXss2LJh1QH6b129FZvxPj6I4oiH0dodqIeNlzayg.ttf",
  "700": "http://fonts.gstatic.com/s/smoochsans/v6/c4mz1n5uGsXss2LJh1QH6b129FZvxPj6I4oiJkdodqIeNlzayg.ttf",
  "800": "http://fonts.gstatic.com/s/smoochsans/v6/c4mz1n5uGsXss2LJh1QH6b129FZvxPj6I4oiQUdodqIeNlzayg.ttf",
  "900": "http://fonts.gstatic.com/s/smoochsans/v6/c4mz1n5uGsXss2LJh1QH6b129FZvxPj6I4oiaEdodqIeNlzayg.ttf",
  "regular": "http://fonts.gstatic.com/s/smoochsans/v6/c4mz1n5uGsXss2LJh1QH6b129FZvxPj6I4oiwUBodqIeNlzayg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Smythe",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/smythe/v23/MwQ3bhT01--coT1BOLh_uGInjA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sniglet",
  "variants": [
  "regular",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "800": "http://fonts.gstatic.com/s/sniglet/v17/cIf4MaFLtkE3UjaJ_ImHRGEsnIJkWL4.ttf",
  "regular": "http://fonts.gstatic.com/s/sniglet/v17/cIf9MaFLtkE3UjaJxCmrYGkHgIs.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Snippet",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/snippet/v21/bWt47f7XfQH9Gupu2v_Afcp9QWc.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Snowburst One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/snowburstone/v20/MQpS-WezKdujBsXY3B7I-UT7eZ-UPyacPbo.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sofadi One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sofadione/v21/JIA2UVBxdnVBuElZaMFGcDOIETkmYDU.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sofia",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sofia/v14/8QIHdirahM3j_vu-sowsrqjk.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Solway",
  "variants": [
  "300",
  "regular",
  "500",
  "700",
  "800"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/solway/v15/AMOTz46Cs2uTAOCuLlgZms0QW3mqyg.ttf",
  "500": "http://fonts.gstatic.com/s/solway/v15/AMOTz46Cs2uTAOCudlkZms0QW3mqyg.ttf",
  "700": "http://fonts.gstatic.com/s/solway/v15/AMOTz46Cs2uTAOCuPl8Zms0QW3mqyg.ttf",
  "800": "http://fonts.gstatic.com/s/solway/v15/AMOTz46Cs2uTAOCuIlwZms0QW3mqyg.ttf",
  "regular": "http://fonts.gstatic.com/s/solway/v15/AMOQz46Cs2uTAOCWgnA9kuYMUg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Song Myung",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/songmyung/v20/1cX2aUDWAJH5-EIC7DIhr1GqhcitzeM.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sonsie One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sonsieone/v21/PbymFmP_EAnPqbKaoc18YVu80lbp8JM.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sora",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/sora/v11/xMQOuFFYT72X5wkB_18qmnndmSdSn3-KIwNhBti0.ttf",
  "200": "http://fonts.gstatic.com/s/sora/v11/xMQOuFFYT72X5wkB_18qmnndmSfSnn-KIwNhBti0.ttf",
  "300": "http://fonts.gstatic.com/s/sora/v11/xMQOuFFYT72X5wkB_18qmnndmScMnn-KIwNhBti0.ttf",
  "500": "http://fonts.gstatic.com/s/sora/v11/xMQOuFFYT72X5wkB_18qmnndmSdgnn-KIwNhBti0.ttf",
  "600": "http://fonts.gstatic.com/s/sora/v11/xMQOuFFYT72X5wkB_18qmnndmSeMmX-KIwNhBti0.ttf",
  "700": "http://fonts.gstatic.com/s/sora/v11/xMQOuFFYT72X5wkB_18qmnndmSe1mX-KIwNhBti0.ttf",
  "800": "http://fonts.gstatic.com/s/sora/v11/xMQOuFFYT72X5wkB_18qmnndmSfSmX-KIwNhBti0.ttf",
  "regular": "http://fonts.gstatic.com/s/sora/v11/xMQOuFFYT72X5wkB_18qmnndmSdSnn-KIwNhBti0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sorts Mill Goudy",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sortsmillgoudy/v15/Qw3GZR9MED_6PSuS_50nEaVrfzgEXH0OjpM75PE.ttf",
  "italic": "http://fonts.gstatic.com/s/sortsmillgoudy/v15/Qw3AZR9MED_6PSuS_50nEaVrfzgEbH8EirE-9PGLfQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Source Code Pro",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_diYsKILxRpg3hIP6sJ7fM7PqPMcMnZFqUwX28DEyQhM5hTXUcdJg.ttf",
  "300": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_diYsKILxRpg3hIP6sJ7fM7PqPMcMnZFqUwX28DJKQhM5hTXUcdJg.ttf",
  "500": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_diYsKILxRpg3hIP6sJ7fM7PqPMcMnZFqUwX28DP6QhM5hTXUcdJg.ttf",
  "600": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_diYsKILxRpg3hIP6sJ7fM7PqPMcMnZFqUwX28DBKXhM5hTXUcdJg.ttf",
  "700": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_diYsKILxRpg3hIP6sJ7fM7PqPMcMnZFqUwX28DCuXhM5hTXUcdJg.ttf",
  "800": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_diYsKILxRpg3hIP6sJ7fM7PqPMcMnZFqUwX28DEyXhM5hTXUcdJg.ttf",
  "900": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_diYsKILxRpg3hIP6sJ7fM7PqPMcMnZFqUwX28DGWXhM5hTXUcdJg.ttf",
  "regular": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_diYsKILxRpg3hIP6sJ7fM7PqPMcMnZFqUwX28DMyQhM5hTXUcdJg.ttf",
  "200italic": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_jiYsKILxRpg3hIP6sJ7fM7PqlOPHYvDP_W9O7GQTT7I1rSVcZZJiGpw.ttf",
  "300italic": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_jiYsKILxRpg3hIP6sJ7fM7PqlOPHYvDP_W9O7GQTTMo1rSVcZZJiGpw.ttf",
  "italic": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_jiYsKILxRpg3hIP6sJ7fM7PqlOPHYvDP_W9O7GQTTbI1rSVcZZJiGpw.ttf",
  "500italic": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_jiYsKILxRpg3hIP6sJ7fM7PqlOPHYvDP_W9O7GQTTXo1rSVcZZJiGpw.ttf",
  "600italic": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_jiYsKILxRpg3hIP6sJ7fM7PqlOPHYvDP_W9O7GQTTsoprSVcZZJiGpw.ttf",
  "700italic": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_jiYsKILxRpg3hIP6sJ7fM7PqlOPHYvDP_W9O7GQTTi4prSVcZZJiGpw.ttf",
  "800italic": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_jiYsKILxRpg3hIP6sJ7fM7PqlOPHYvDP_W9O7GQTT7IprSVcZZJiGpw.ttf",
  "900italic": "http://fonts.gstatic.com/s/sourcecodepro/v22/HI_jiYsKILxRpg3hIP6sJ7fM7PqlOPHYvDP_W9O7GQTTxYprSVcZZJiGpw.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Source Sans 3",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpBtKy2OAdR1K-IwhWudF-R9QMylBJAV3Bo8Kw461EN_io6npfB.ttf",
  "300": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpBtKy2OAdR1K-IwhWudF-R9QMylBJAV3Bo8Kzm61EN_io6npfB.ttf",
  "500": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpBtKy2OAdR1K-IwhWudF-R9QMylBJAV3Bo8KyK61EN_io6npfB.ttf",
  "600": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpBtKy2OAdR1K-IwhWudF-R9QMylBJAV3Bo8Kxm7FEN_io6npfB.ttf",
  "700": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpBtKy2OAdR1K-IwhWudF-R9QMylBJAV3Bo8Kxf7FEN_io6npfB.ttf",
  "800": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpBtKy2OAdR1K-IwhWudF-R9QMylBJAV3Bo8Kw47FEN_io6npfB.ttf",
  "900": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpBtKy2OAdR1K-IwhWudF-R9QMylBJAV3Bo8KwR7FEN_io6npfB.ttf",
  "regular": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpBtKy2OAdR1K-IwhWudF-R9QMylBJAV3Bo8Ky461EN_io6npfB.ttf",
  "200italic": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpDtKy2OAdR1K-IwhWudF-R3woAa8opPOrG97lwqDlO9C4Ym4fB3Ts.ttf",
  "300italic": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpDtKy2OAdR1K-IwhWudF-R3woAa8opPOrG97lwqOdO9C4Ym4fB3Ts.ttf",
  "italic": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpDtKy2OAdR1K-IwhWudF-R3woAa8opPOrG97lwqLlO9C4Ym4fB3Ts.ttf",
  "500italic": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpDtKy2OAdR1K-IwhWudF-R3woAa8opPOrG97lwqItO9C4Ym4fB3Ts.ttf",
  "600italic": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpDtKy2OAdR1K-IwhWudF-R3woAa8opPOrG97lwqGdJ9C4Ym4fB3Ts.ttf",
  "700italic": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpDtKy2OAdR1K-IwhWudF-R3woAa8opPOrG97lwqF5J9C4Ym4fB3Ts.ttf",
  "800italic": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpDtKy2OAdR1K-IwhWudF-R3woAa8opPOrG97lwqDlJ9C4Ym4fB3Ts.ttf",
  "900italic": "http://fonts.gstatic.com/s/sourcesans3/v8/nwpDtKy2OAdR1K-IwhWudF-R3woAa8opPOrG97lwqBBJ9C4Ym4fB3Ts.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Source Sans Pro",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xKydSBYKcSV-LCoeQqfX1RYOo3i94_AkB1v_8CGxg.ttf",
  "300": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xKydSBYKcSV-LCoeQqfX1RYOo3ik4zAkB1v_8CGxg.ttf",
  "600": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xKydSBYKcSV-LCoeQqfX1RYOo3i54rAkB1v_8CGxg.ttf",
  "700": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xKydSBYKcSV-LCoeQqfX1RYOo3ig4vAkB1v_8CGxg.ttf",
  "900": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xKydSBYKcSV-LCoeQqfX1RYOo3iu4nAkB1v_8CGxg.ttf",
  "200italic": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xKwdSBYKcSV-LCoeQqfX1RYOo3qPZYokRdr3cWWxg40.ttf",
  "300italic": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xKwdSBYKcSV-LCoeQqfX1RYOo3qPZZMkhdr3cWWxg40.ttf",
  "regular": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xK3dSBYKcSV-LCoeQqfX1RYOo3aP6TkmDZz9g.ttf",
  "italic": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xK1dSBYKcSV-LCoeQqfX1RYOo3qPa7gujNj9tmf.ttf",
  "600italic": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xKwdSBYKcSV-LCoeQqfX1RYOo3qPZY4lBdr3cWWxg40.ttf",
  "700italic": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xKwdSBYKcSV-LCoeQqfX1RYOo3qPZZclRdr3cWWxg40.ttf",
  "900italic": "http://fonts.gstatic.com/s/sourcesanspro/v21/6xKwdSBYKcSV-LCoeQqfX1RYOo3qPZZklxdr3cWWxg40.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Source Serif 4",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/sourceserif4/v7/vEFy2_tTDB4M7-auWDN0ahZJW3IX2ih5nk3AucvUHf6OAVIJmeUDygwjipdqrhxXD-wGvjU.ttf",
  "300": "http://fonts.gstatic.com/s/sourceserif4/v7/vEFy2_tTDB4M7-auWDN0ahZJW3IX2ih5nk3AucvUHf6OAVIJmeUDygwjiklqrhxXD-wGvjU.ttf",
  "500": "http://fonts.gstatic.com/s/sourceserif4/v7/vEFy2_tTDB4M7-auWDN0ahZJW3IX2ih5nk3AucvUHf6OAVIJmeUDygwjiiVqrhxXD-wGvjU.ttf",
  "600": "http://fonts.gstatic.com/s/sourceserif4/v7/vEFy2_tTDB4M7-auWDN0ahZJW3IX2ih5nk3AucvUHf6OAVIJmeUDygwjisltrhxXD-wGvjU.ttf",
  "700": "http://fonts.gstatic.com/s/sourceserif4/v7/vEFy2_tTDB4M7-auWDN0ahZJW3IX2ih5nk3AucvUHf6OAVIJmeUDygwjivBtrhxXD-wGvjU.ttf",
  "800": "http://fonts.gstatic.com/s/sourceserif4/v7/vEFy2_tTDB4M7-auWDN0ahZJW3IX2ih5nk3AucvUHf6OAVIJmeUDygwjipdtrhxXD-wGvjU.ttf",
  "900": "http://fonts.gstatic.com/s/sourceserif4/v7/vEFy2_tTDB4M7-auWDN0ahZJW3IX2ih5nk3AucvUHf6OAVIJmeUDygwjir5trhxXD-wGvjU.ttf",
  "regular": "http://fonts.gstatic.com/s/sourceserif4/v7/vEFy2_tTDB4M7-auWDN0ahZJW3IX2ih5nk3AucvUHf6OAVIJmeUDygwjihdqrhxXD-wGvjU.ttf",
  "200italic": "http://fonts.gstatic.com/s/sourceserif4/v7/vEF02_tTDB4M7-auWDN0ahZJW1ge6NmXpVAHV83Bfb_US2D2QYxoUKIkn98pxl9dC84DrjXEXw.ttf",
  "300italic": "http://fonts.gstatic.com/s/sourceserif4/v7/vEF02_tTDB4M7-auWDN0ahZJW1ge6NmXpVAHV83Bfb_US2D2QYxoUKIkn98pGF9dC84DrjXEXw.ttf",
  "italic": "http://fonts.gstatic.com/s/sourceserif4/v7/vEF02_tTDB4M7-auWDN0ahZJW1ge6NmXpVAHV83Bfb_US2D2QYxoUKIkn98pRl9dC84DrjXEXw.ttf",
  "500italic": "http://fonts.gstatic.com/s/sourceserif4/v7/vEF02_tTDB4M7-auWDN0ahZJW1ge6NmXpVAHV83Bfb_US2D2QYxoUKIkn98pdF9dC84DrjXEXw.ttf",
  "600italic": "http://fonts.gstatic.com/s/sourceserif4/v7/vEF02_tTDB4M7-auWDN0ahZJW1ge6NmXpVAHV83Bfb_US2D2QYxoUKIkn98pmFhdC84DrjXEXw.ttf",
  "700italic": "http://fonts.gstatic.com/s/sourceserif4/v7/vEF02_tTDB4M7-auWDN0ahZJW1ge6NmXpVAHV83Bfb_US2D2QYxoUKIkn98poVhdC84DrjXEXw.ttf",
  "800italic": "http://fonts.gstatic.com/s/sourceserif4/v7/vEF02_tTDB4M7-auWDN0ahZJW1ge6NmXpVAHV83Bfb_US2D2QYxoUKIkn98pxlhdC84DrjXEXw.ttf",
  "900italic": "http://fonts.gstatic.com/s/sourceserif4/v7/vEF02_tTDB4M7-auWDN0ahZJW1ge6NmXpVAHV83Bfb_US2D2QYxoUKIkn98p71hdC84DrjXEXw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Source Serif Pro",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIXzD-0qpwxpaWvjeD0X88SAOeasbsfhSugxYUvZrI.ttf",
  "300": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIXzD-0qpwxpaWvjeD0X88SAOeasd8chSugxYUvZrI.ttf",
  "600": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIXzD-0qpwxpaWvjeD0X88SAOeasasahSugxYUvZrI.ttf",
  "700": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIXzD-0qpwxpaWvjeD0X88SAOeasc8bhSugxYUvZrI.ttf",
  "900": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIXzD-0qpwxpaWvjeD0X88SAOeasfcZhSugxYUvZrI.ttf",
  "200italic": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIVzD-0qpwxpaWvjeD0X88SAOeauXEGbSqqwacqdrKvbQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIVzD-0qpwxpaWvjeD0X88SAOeauXEGCSmqwacqdrKvbQ.ttf",
  "regular": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIQzD-0qpwxpaWvjeD0X88SAOeaiXM0oSOL2Yw.ttf",
  "italic": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIWzD-0qpwxpaWvjeD0X88SAOeauXE-pQGOyYw2fw.ttf",
  "600italic": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIVzD-0qpwxpaWvjeD0X88SAOeauXEGfS-qwacqdrKvbQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIVzD-0qpwxpaWvjeD0X88SAOeauXEGGS6qwacqdrKvbQ.ttf",
  "900italic": "http://fonts.gstatic.com/s/sourceserifpro/v15/neIVzD-0qpwxpaWvjeD0X88SAOeauXEGISyqwacqdrKvbQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Space Grotesk",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/spacegrotesk/v13/V8mQoQDjQSkFtoMM3T6r8E7mF71Q-gOoraIAEj62UUsjNsFjTDJK.ttf",
  "500": "http://fonts.gstatic.com/s/spacegrotesk/v13/V8mQoQDjQSkFtoMM3T6r8E7mF71Q-gOoraIAEj7aUUsjNsFjTDJK.ttf",
  "600": "http://fonts.gstatic.com/s/spacegrotesk/v13/V8mQoQDjQSkFtoMM3T6r8E7mF71Q-gOoraIAEj42VksjNsFjTDJK.ttf",
  "700": "http://fonts.gstatic.com/s/spacegrotesk/v13/V8mQoQDjQSkFtoMM3T6r8E7mF71Q-gOoraIAEj4PVksjNsFjTDJK.ttf",
  "regular": "http://fonts.gstatic.com/s/spacegrotesk/v13/V8mQoQDjQSkFtoMM3T6r8E7mF71Q-gOoraIAEj7oUUsjNsFjTDJK.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Space Mono",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/spacemono/v12/i7dMIFZifjKcF5UAWdDRaPpZYFKQHwyVd3U.ttf",
  "regular": "http://fonts.gstatic.com/s/spacemono/v12/i7dPIFZifjKcF5UAWdDRUEZ2RFq7AwU.ttf",
  "italic": "http://fonts.gstatic.com/s/spacemono/v12/i7dNIFZifjKcF5UAWdDRYER8QHi-EwWMbg.ttf",
  "700italic": "http://fonts.gstatic.com/s/spacemono/v12/i7dSIFZifjKcF5UAWdDRYERE_FeaGy6QZ3WfYg.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Special Elite",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/specialelite/v18/XLYgIZbkc4JPUL5CVArUVL0nhncESXFtUsM.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Spectral",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/spectral/v13/rnCs-xNNww_2s0amA9v2s13GY_etWWIJ.ttf",
  "300": "http://fonts.gstatic.com/s/spectral/v13/rnCs-xNNww_2s0amA9uSsF3GY_etWWIJ.ttf",
  "500": "http://fonts.gstatic.com/s/spectral/v13/rnCs-xNNww_2s0amA9vKsV3GY_etWWIJ.ttf",
  "600": "http://fonts.gstatic.com/s/spectral/v13/rnCs-xNNww_2s0amA9vmtl3GY_etWWIJ.ttf",
  "700": "http://fonts.gstatic.com/s/spectral/v13/rnCs-xNNww_2s0amA9uCt13GY_etWWIJ.ttf",
  "800": "http://fonts.gstatic.com/s/spectral/v13/rnCs-xNNww_2s0amA9uetF3GY_etWWIJ.ttf",
  "200italic": "http://fonts.gstatic.com/s/spectral/v13/rnCu-xNNww_2s0amA9M8qrXHafOPXHIJErY.ttf",
  "300italic": "http://fonts.gstatic.com/s/spectral/v13/rnCu-xNNww_2s0amA9M8qtHEafOPXHIJErY.ttf",
  "regular": "http://fonts.gstatic.com/s/spectral/v13/rnCr-xNNww_2s0amA-M-mHnOSOuk.ttf",
  "italic": "http://fonts.gstatic.com/s/spectral/v13/rnCt-xNNww_2s0amA9M8kn3sTfukQHs.ttf",
  "500italic": "http://fonts.gstatic.com/s/spectral/v13/rnCu-xNNww_2s0amA9M8qonFafOPXHIJErY.ttf",
  "600italic": "http://fonts.gstatic.com/s/spectral/v13/rnCu-xNNww_2s0amA9M8qqXCafOPXHIJErY.ttf",
  "700italic": "http://fonts.gstatic.com/s/spectral/v13/rnCu-xNNww_2s0amA9M8qsHDafOPXHIJErY.ttf",
  "800italic": "http://fonts.gstatic.com/s/spectral/v13/rnCu-xNNww_2s0amA9M8qt3AafOPXHIJErY.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Spectral SC",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk0ALCRZonmalTgyPmRfs1qwkTXPYeVXJZB.ttf",
  "300": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk0ALCRZonmalTgyPmRfs0OwUTXPYeVXJZB.ttf",
  "500": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk0ALCRZonmalTgyPmRfs1WwETXPYeVXJZB.ttf",
  "600": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk0ALCRZonmalTgyPmRfs16x0TXPYeVXJZB.ttf",
  "700": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk0ALCRZonmalTgyPmRfs0exkTXPYeVXJZB.ttf",
  "800": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk0ALCRZonmalTgyPmRfs0CxUTXPYeVXJZB.ttf",
  "200italic": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk2ALCRZonmalTgyPmRfsWg26zWN4O3WYZB_sU.ttf",
  "300italic": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk2ALCRZonmalTgyPmRfsWg28jVN4O3WYZB_sU.ttf",
  "regular": "http://fonts.gstatic.com/s/spectralsc/v11/KtkpALCRZonmalTgyPmRfvWi6WDfFpuc.ttf",
  "italic": "http://fonts.gstatic.com/s/spectralsc/v11/KtkrALCRZonmalTgyPmRfsWg42T9E4ucRY8.ttf",
  "500italic": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk2ALCRZonmalTgyPmRfsWg25DUN4O3WYZB_sU.ttf",
  "600italic": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk2ALCRZonmalTgyPmRfsWg27zTN4O3WYZB_sU.ttf",
  "700italic": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk2ALCRZonmalTgyPmRfsWg29jSN4O3WYZB_sU.ttf",
  "800italic": "http://fonts.gstatic.com/s/spectralsc/v11/Ktk2ALCRZonmalTgyPmRfsWg28TRN4O3WYZB_sU.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Spicy Rice",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/spicyrice/v21/uK_24rSEd-Uqwk4jY1RyGv-2WkowRcc.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Spinnaker",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/spinnaker/v17/w8gYH2oyX-I0_rvR6Hmn3HwLqOqSBg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Spirax",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/spirax/v21/buE3poKgYNLy0F3cXktt-Csn-Q.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Splash",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/splash/v1/KtksAL2RZoDkbU6hpPPGNdS6wg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Spline Sans",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/splinesans/v8/_6_sED73Uf-2WfU2LzycEZousNzn1a1lKWRpZlnYEtvlUfE2kw.ttf",
  "500": "http://fonts.gstatic.com/s/splinesans/v8/_6_sED73Uf-2WfU2LzycEZousNzn1a1lKWRpClnYEtvlUfE2kw.ttf",
  "600": "http://fonts.gstatic.com/s/splinesans/v8/_6_sED73Uf-2WfU2LzycEZousNzn1a1lKWRp5l7YEtvlUfE2kw.ttf",
  "700": "http://fonts.gstatic.com/s/splinesans/v8/_6_sED73Uf-2WfU2LzycEZousNzn1a1lKWRp317YEtvlUfE2kw.ttf",
  "regular": "http://fonts.gstatic.com/s/splinesans/v8/_6_sED73Uf-2WfU2LzycEZousNzn1a1lKWRpOFnYEtvlUfE2kw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Spline Sans Mono",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/splinesansmono/v4/R70MjzAei_CDNLfgZxrW6wrZOF2WdZ6xabUGSVtNuGA8MrtVy4d4dGb1.ttf",
  "500": "http://fonts.gstatic.com/s/splinesansmono/v4/R70MjzAei_CDNLfgZxrW6wrZOF2WdZ6xabUGSVtNuGBQMrtVy4d4dGb1.ttf",
  "600": "http://fonts.gstatic.com/s/splinesansmono/v4/R70MjzAei_CDNLfgZxrW6wrZOF2WdZ6xabUGSVtNuGC8NbtVy4d4dGb1.ttf",
  "700": "http://fonts.gstatic.com/s/splinesansmono/v4/R70MjzAei_CDNLfgZxrW6wrZOF2WdZ6xabUGSVtNuGCFNbtVy4d4dGb1.ttf",
  "regular": "http://fonts.gstatic.com/s/splinesansmono/v4/R70MjzAei_CDNLfgZxrW6wrZOF2WdZ6xabUGSVtNuGBiMrtVy4d4dGb1.ttf",
  "300italic": "http://fonts.gstatic.com/s/splinesansmono/v4/R70yjzAei_CDNLfgZxrW6wrZOF2WX5eDlm1vIsHjv3WqcQ0WwYNacXb12MM.ttf",
  "italic": "http://fonts.gstatic.com/s/splinesansmono/v4/R70yjzAei_CDNLfgZxrW6wrZOF2WX5eDlm1vIsHjv3WqcVMWwYNacXb12MM.ttf",
  "500italic": "http://fonts.gstatic.com/s/splinesansmono/v4/R70yjzAei_CDNLfgZxrW6wrZOF2WX5eDlm1vIsHjv3WqcWEWwYNacXb12MM.ttf",
  "600italic": "http://fonts.gstatic.com/s/splinesansmono/v4/R70yjzAei_CDNLfgZxrW6wrZOF2WX5eDlm1vIsHjv3WqcY0RwYNacXb12MM.ttf",
  "700italic": "http://fonts.gstatic.com/s/splinesansmono/v4/R70yjzAei_CDNLfgZxrW6wrZOF2WX5eDlm1vIsHjv3WqcbQRwYNacXb12MM.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Squada One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/squadaone/v14/BCasqZ8XsOrx4mcOk6MtWaA8WDBkHgs.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Square Peg",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/squarepeg/v2/y83eW48Nzw6ZlUHc-phrBDHrHHfrFPE.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sree Krushnadevaraya",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sreekrushnadevaraya/v21/R70FjzQeifmPepmyQQjQ9kvwMkWYPfTA_EWb2FhQuXir.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sriracha",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sriracha/v10/0nkrC9D4IuYBgWcI9ObYRQDioeb0.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Srisakdi",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/srisakdi/v16/yMJWMIlvdpDbkB0A-gIAUghxoNFxW0Hz.ttf",
  "regular": "http://fonts.gstatic.com/s/srisakdi/v16/yMJRMIlvdpDbkB0A-jq8fSx5i814.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Staatliches",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/staatliches/v11/HI_OiY8KO6hCsQSoAPmtMbectJG9O9PS.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Stalemate",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/stalemate/v20/taiIGmZ_EJq97-UfkZRpuqSs8ZQpaQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Stalinist One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v54",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/stalinistone/v54/MQpS-WezM9W4Dd7D3B7I-UT7eZ-UPyacPbo.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Stardos Stencil",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/stardosstencil/v15/X7n44bcuGPC8hrvEOHXOgaKCc2TpU3tTvg-t29HSHw.ttf",
  "regular": "http://fonts.gstatic.com/s/stardosstencil/v15/X7n94bcuGPC8hrvEOHXOgaKCc2TR71R3tiSx0g.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Stick",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/stick/v15/Qw3TZQpMCyTtJSvfvPVDMPoF.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Stick No Bills",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "sinhala"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/sticknobills/v8/bWts7ffXZwHuAa9Uld-oEK4QKlxj9f9t_7uEmjcVP8Q7KriwKhcTKA.ttf",
  "300": "http://fonts.gstatic.com/s/sticknobills/v8/bWts7ffXZwHuAa9Uld-oEK4QKlxj9f9t_7uEmjcV4cQ7KriwKhcTKA.ttf",
  "500": "http://fonts.gstatic.com/s/sticknobills/v8/bWts7ffXZwHuAa9Uld-oEK4QKlxj9f9t_7uEmjcVjcQ7KriwKhcTKA.ttf",
  "600": "http://fonts.gstatic.com/s/sticknobills/v8/bWts7ffXZwHuAa9Uld-oEK4QKlxj9f9t_7uEmjcVYcM7KriwKhcTKA.ttf",
  "700": "http://fonts.gstatic.com/s/sticknobills/v8/bWts7ffXZwHuAa9Uld-oEK4QKlxj9f9t_7uEmjcVWMM7KriwKhcTKA.ttf",
  "800": "http://fonts.gstatic.com/s/sticknobills/v8/bWts7ffXZwHuAa9Uld-oEK4QKlxj9f9t_7uEmjcVP8M7KriwKhcTKA.ttf",
  "regular": "http://fonts.gstatic.com/s/sticknobills/v8/bWts7ffXZwHuAa9Uld-oEK4QKlxj9f9t_7uEmjcVv8Q7KriwKhcTKA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Stint Ultra Condensed",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/stintultracondensed/v21/-W_gXIrsVjjeyEnPC45qD2NoFPtBE0xCh2A-qhUO2cNvdg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Stint Ultra Expanded",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/stintultraexpanded/v20/CSRg4yNNh-GbW3o3JkwoDcdvMKMf0oBAd0qoATQkWwam.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Stoke",
  "variants": [
  "300",
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/stoke/v22/z7NXdRb7aTMfKNvFVgxC_pjcTeWU.ttf",
  "regular": "http://fonts.gstatic.com/s/stoke/v22/z7NadRb7aTMfKONpfihK1YTV.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Strait",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/strait/v13/DtViJxy6WaEr1LZzeDhtkl0U7w.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Style Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/stylescript/v7/vm8xdRX3SV7Z0aPa88xzW5npeFT76NZnMw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Stylish",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/stylish/v20/m8JSjfhPYriQkk7-fo35dLxEdmo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sue Ellen Francisco",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sueellenfrancisco/v16/wXK3E20CsoJ9j1DDkjHcQ5ZL8xRaxru9ropF2lqk9H4.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Suez One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/suezone/v11/taiJGmd_EZ6rqscQgNFJkIqg-I0w.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sulphur Point",
  "variants": [
  "300",
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/sulphurpoint/v14/RLpkK5vv8KaycDcazWFPBj2afVU6n6kFUHPIFaU.ttf",
  "700": "http://fonts.gstatic.com/s/sulphurpoint/v14/RLpkK5vv8KaycDcazWFPBj2afUU9n6kFUHPIFaU.ttf",
  "regular": "http://fonts.gstatic.com/s/sulphurpoint/v14/RLp5K5vv8KaycDcazWFPBj2aRfkSu6EuTHo.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sumana",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/sumana/v10/4UaArE5TqRBjGj--TDfG54fN6ppsKg.ttf",
  "regular": "http://fonts.gstatic.com/s/sumana/v10/4UaDrE5TqRBjGj-G8Bji76zR4w.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sunflower",
  "variants": [
  "300",
  "500",
  "700"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/sunflower/v14/RWmPoKeF8fUjqIj7Vc-06MfiqYsGBGBzCw.ttf",
  "500": "http://fonts.gstatic.com/s/sunflower/v14/RWmPoKeF8fUjqIj7Vc-0sMbiqYsGBGBzCw.ttf",
  "700": "http://fonts.gstatic.com/s/sunflower/v14/RWmPoKeF8fUjqIj7Vc-0-MDiqYsGBGBzCw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sunshiney",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/sunshiney/v24/LDIwapGTLBwsS-wT4vcgE8moUePWkg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Supermercado One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/supermercadoone/v22/OpNXnpQWg8jc_xps_Gi14kVVEXOn60b3MClBRTs.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Sura",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/sura/v15/SZc53FL5PbyzLUJ7fz3GkUrS8DI.ttf",
  "regular": "http://fonts.gstatic.com/s/sura/v15/SZc23FL5PbyzFf5UWzXtjUM.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Suranna",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v13",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/suranna/v13/gokuH6ztGkFjWe58tBRZT2KmgP0.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Suravaram",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/suravaram/v21/_gP61R_usiY7SCym4xIAi261Qv9roQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Suwannaphum",
  "variants": [
  "100",
  "300",
  "regular",
  "700",
  "900"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v29",
  "lastModified": "2022-04-27",
  "files": {
  "100": "http://fonts.gstatic.com/s/suwannaphum/v29/jAnAgHV7GtDvc8jbe8hXXL3B9cSWXx2VZmk.ttf",
  "300": "http://fonts.gstatic.com/s/suwannaphum/v29/jAnfgHV7GtDvc8jbe8hXXL0J1-S8cRGcf3Ai.ttf",
  "700": "http://fonts.gstatic.com/s/suwannaphum/v29/jAnfgHV7GtDvc8jbe8hXXL0Z0OS8cRGcf3Ai.ttf",
  "900": "http://fonts.gstatic.com/s/suwannaphum/v29/jAnfgHV7GtDvc8jbe8hXXL0h0uS8cRGcf3Ai.ttf",
  "regular": "http://fonts.gstatic.com/s/suwannaphum/v29/jAnCgHV7GtDvc8jbe8hXXIWl_8C0Wg2V.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Swanky and Moo Moo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/swankyandmoomoo/v22/flUlRrKz24IuWVI_WJYTYcqbEsMUZ3kUtbPkR64SYQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Syncopate",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/syncopate/v19/pe0pMIuPIYBCpEV5eFdKvtKaA_Rue1UwVg.ttf",
  "regular": "http://fonts.gstatic.com/s/syncopate/v19/pe0sMIuPIYBCpEV5eFdyAv2-C99ycg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Syne",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "greek",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/syne/v15/8vIS7w4qzmVxsWxjBZRjr0FKM_0KuT6kR47NCV5Z.ttf",
  "600": "http://fonts.gstatic.com/s/syne/v15/8vIS7w4qzmVxsWxjBZRjr0FKM_3mvj6kR47NCV5Z.ttf",
  "700": "http://fonts.gstatic.com/s/syne/v15/8vIS7w4qzmVxsWxjBZRjr0FKM_3fvj6kR47NCV5Z.ttf",
  "800": "http://fonts.gstatic.com/s/syne/v15/8vIS7w4qzmVxsWxjBZRjr0FKM_24vj6kR47NCV5Z.ttf",
  "regular": "http://fonts.gstatic.com/s/syne/v15/8vIS7w4qzmVxsWxjBZRjr0FKM_04uT6kR47NCV5Z.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Syne Mono",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/synemono/v15/K2FzfZNHj_FHBmRbFvHzIqCkDyvqZA.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Syne Tactile",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/synetactile/v15/11hGGpna2UTQKjMCVzjAPMKh3ysdjvKU8Q.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tai Heritage Pro",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tai-viet",
  "vietnamese"
  ],
  "version": "v1",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/taiheritagepro/v1/sZlYdQid-zgaNiNIYcUzJMU3IYyNmMB9NNRFMuhjCXY.ttf",
  "regular": "http://fonts.gstatic.com/s/taiheritagepro/v1/sZlfdQid-zgaNiNIYcUzJMU3IYyNoHxSENxuLuE.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tajawal",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "arabic",
  "latin"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/tajawal/v9/Iurf6YBj_oCad4k1l_6gLrZjiLlJ-G0.ttf",
  "300": "http://fonts.gstatic.com/s/tajawal/v9/Iurf6YBj_oCad4k1l5qjLrZjiLlJ-G0.ttf",
  "500": "http://fonts.gstatic.com/s/tajawal/v9/Iurf6YBj_oCad4k1l8KiLrZjiLlJ-G0.ttf",
  "700": "http://fonts.gstatic.com/s/tajawal/v9/Iurf6YBj_oCad4k1l4qkLrZjiLlJ-G0.ttf",
  "800": "http://fonts.gstatic.com/s/tajawal/v9/Iurf6YBj_oCad4k1l5anLrZjiLlJ-G0.ttf",
  "900": "http://fonts.gstatic.com/s/tajawal/v9/Iurf6YBj_oCad4k1l7KmLrZjiLlJ-G0.ttf",
  "regular": "http://fonts.gstatic.com/s/tajawal/v9/Iura6YBj_oCad4k1rzaLCr5IlLA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tangerine",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/tangerine/v17/Iurd6Y5j_oScZZow4VO5srNpjJtM6G0t9w.ttf",
  "regular": "http://fonts.gstatic.com/s/tangerine/v17/IurY6Y5j_oScZZow4VOBDpxNhLBQ4Q.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tapestry",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tapestry/v2/SlGTmQecrosEYXhaGBIkqnB6aSQU.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Taprom",
  "variants": [
  "regular"
  ],
  "subsets": [
  "khmer",
  "latin"
  ],
  "version": "v27",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/taprom/v27/UcCn3F82JHycULbFQyk3-0kvHg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tauri",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tauri/v16/TwMA-IISS0AM3IpVWHU_TBqO.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Taviraj",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/taviraj/v11/ahcbv8Cj3ylylTXzRIorV8N1jU2gog.ttf",
  "200": "http://fonts.gstatic.com/s/taviraj/v11/ahccv8Cj3ylylTXzRCYKd-lbgUS5u0s.ttf",
  "300": "http://fonts.gstatic.com/s/taviraj/v11/ahccv8Cj3ylylTXzREIJd-lbgUS5u0s.ttf",
  "500": "http://fonts.gstatic.com/s/taviraj/v11/ahccv8Cj3ylylTXzRBoId-lbgUS5u0s.ttf",
  "600": "http://fonts.gstatic.com/s/taviraj/v11/ahccv8Cj3ylylTXzRDYPd-lbgUS5u0s.ttf",
  "700": "http://fonts.gstatic.com/s/taviraj/v11/ahccv8Cj3ylylTXzRFIOd-lbgUS5u0s.ttf",
  "800": "http://fonts.gstatic.com/s/taviraj/v11/ahccv8Cj3ylylTXzRE4Nd-lbgUS5u0s.ttf",
  "900": "http://fonts.gstatic.com/s/taviraj/v11/ahccv8Cj3ylylTXzRGoMd-lbgUS5u0s.ttf",
  "100italic": "http://fonts.gstatic.com/s/taviraj/v11/ahcdv8Cj3ylylTXzTOwTM8lxr0iwolLl.ttf",
  "200italic": "http://fonts.gstatic.com/s/taviraj/v11/ahcev8Cj3ylylTXzTOwTn-hRhWa8q0v8ag.ttf",
  "300italic": "http://fonts.gstatic.com/s/taviraj/v11/ahcev8Cj3ylylTXzTOwT--tRhWa8q0v8ag.ttf",
  "regular": "http://fonts.gstatic.com/s/taviraj/v11/ahcZv8Cj3ylylTXzfO4hU-FwnU0.ttf",
  "italic": "http://fonts.gstatic.com/s/taviraj/v11/ahcbv8Cj3ylylTXzTOwrV8N1jU2gog.ttf",
  "500italic": "http://fonts.gstatic.com/s/taviraj/v11/ahcev8Cj3ylylTXzTOwTo-pRhWa8q0v8ag.ttf",
  "600italic": "http://fonts.gstatic.com/s/taviraj/v11/ahcev8Cj3ylylTXzTOwTj-1RhWa8q0v8ag.ttf",
  "700italic": "http://fonts.gstatic.com/s/taviraj/v11/ahcev8Cj3ylylTXzTOwT6-xRhWa8q0v8ag.ttf",
  "800italic": "http://fonts.gstatic.com/s/taviraj/v11/ahcev8Cj3ylylTXzTOwT9-9RhWa8q0v8ag.ttf",
  "900italic": "http://fonts.gstatic.com/s/taviraj/v11/ahcev8Cj3ylylTXzTOwT0-5RhWa8q0v8ag.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Teko",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/teko/v15/LYjCdG7kmE0gdQhfgCNqqVIuTN4.ttf",
  "500": "http://fonts.gstatic.com/s/teko/v15/LYjCdG7kmE0gdVBegCNqqVIuTN4.ttf",
  "600": "http://fonts.gstatic.com/s/teko/v15/LYjCdG7kmE0gdXxZgCNqqVIuTN4.ttf",
  "700": "http://fonts.gstatic.com/s/teko/v15/LYjCdG7kmE0gdRhYgCNqqVIuTN4.ttf",
  "regular": "http://fonts.gstatic.com/s/teko/v15/LYjNdG7kmE0gTaR3pCtBtVs.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Telex",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/telex/v14/ieVw2Y1fKWmIO9fTB1piKFIf.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tenali Ramakrishna",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tenaliramakrishna/v12/raxgHj6Yt9gAN3LLKs0BZVMo8jmwn1-8KJXqUFFvtA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tenor Sans",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tenorsans/v17/bx6ANxqUneKx06UkIXISr3JyC22IyqI.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Text Me One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/textmeone/v20/i7dOIFdlayuLUvgoFvHQFWZcalayGhyV.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Texturina",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/texturina/v21/c4mM1nxpEtL3pXiAulRTkY-HGmNEX1b9NspjMwhAgliHhVrXy2eYG_Ug25riW1OD.ttf",
  "200": "http://fonts.gstatic.com/s/texturina/v21/c4mM1nxpEtL3pXiAulRTkY-HGmNEX1b9NspjMwhAgliHhVrXy2cYGvUg25riW1OD.ttf",
  "300": "http://fonts.gstatic.com/s/texturina/v21/c4mM1nxpEtL3pXiAulRTkY-HGmNEX1b9NspjMwhAgliHhVrXy2fGGvUg25riW1OD.ttf",
  "500": "http://fonts.gstatic.com/s/texturina/v21/c4mM1nxpEtL3pXiAulRTkY-HGmNEX1b9NspjMwhAgliHhVrXy2eqGvUg25riW1OD.ttf",
  "600": "http://fonts.gstatic.com/s/texturina/v21/c4mM1nxpEtL3pXiAulRTkY-HGmNEX1b9NspjMwhAgliHhVrXy2dGHfUg25riW1OD.ttf",
  "700": "http://fonts.gstatic.com/s/texturina/v21/c4mM1nxpEtL3pXiAulRTkY-HGmNEX1b9NspjMwhAgliHhVrXy2d_HfUg25riW1OD.ttf",
  "800": "http://fonts.gstatic.com/s/texturina/v21/c4mM1nxpEtL3pXiAulRTkY-HGmNEX1b9NspjMwhAgliHhVrXy2cYHfUg25riW1OD.ttf",
  "900": "http://fonts.gstatic.com/s/texturina/v21/c4mM1nxpEtL3pXiAulRTkY-HGmNEX1b9NspjMwhAgliHhVrXy2cxHfUg25riW1OD.ttf",
  "regular": "http://fonts.gstatic.com/s/texturina/v21/c4mM1nxpEtL3pXiAulRTkY-HGmNEX1b9NspjMwhAgliHhVrXy2eYGvUg25riW1OD.ttf",
  "100italic": "http://fonts.gstatic.com/s/texturina/v21/c4mO1nxpEtL3pXiAulR5mL129FhZmLj7I4oiSUJyfYDu7sB5zHJQWR1i0Z7AXkODN94.ttf",
  "200italic": "http://fonts.gstatic.com/s/texturina/v21/c4mO1nxpEtL3pXiAulR5mL129FhZmLj7I4oiSUJyfYDu7sB5zHJQWZ1j0Z7AXkODN94.ttf",
  "300italic": "http://fonts.gstatic.com/s/texturina/v21/c4mO1nxpEtL3pXiAulR5mL129FhZmLj7I4oiSUJyfYDu7sB5zHJQWUNj0Z7AXkODN94.ttf",
  "italic": "http://fonts.gstatic.com/s/texturina/v21/c4mO1nxpEtL3pXiAulR5mL129FhZmLj7I4oiSUJyfYDu7sB5zHJQWR1j0Z7AXkODN94.ttf",
  "500italic": "http://fonts.gstatic.com/s/texturina/v21/c4mO1nxpEtL3pXiAulR5mL129FhZmLj7I4oiSUJyfYDu7sB5zHJQWS9j0Z7AXkODN94.ttf",
  "600italic": "http://fonts.gstatic.com/s/texturina/v21/c4mO1nxpEtL3pXiAulR5mL129FhZmLj7I4oiSUJyfYDu7sB5zHJQWcNk0Z7AXkODN94.ttf",
  "700italic": "http://fonts.gstatic.com/s/texturina/v21/c4mO1nxpEtL3pXiAulR5mL129FhZmLj7I4oiSUJyfYDu7sB5zHJQWfpk0Z7AXkODN94.ttf",
  "800italic": "http://fonts.gstatic.com/s/texturina/v21/c4mO1nxpEtL3pXiAulR5mL129FhZmLj7I4oiSUJyfYDu7sB5zHJQWZ1k0Z7AXkODN94.ttf",
  "900italic": "http://fonts.gstatic.com/s/texturina/v21/c4mO1nxpEtL3pXiAulR5mL129FhZmLj7I4oiSUJyfYDu7sB5zHJQWbRk0Z7AXkODN94.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Thasadith",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v9",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/thasadith/v9/mtG94_1TIqPYrd_f5R1gDGYw2A6yHk9d8w.ttf",
  "regular": "http://fonts.gstatic.com/s/thasadith/v9/mtG44_1TIqPYrd_f5R1YsEkU0CWuFw.ttf",
  "italic": "http://fonts.gstatic.com/s/thasadith/v9/mtG-4_1TIqPYrd_f5R1oskMQ8iC-F1ZE.ttf",
  "700italic": "http://fonts.gstatic.com/s/thasadith/v9/mtGj4_1TIqPYrd_f5R1osnus3QS2PEpN8zxA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "The Girl Next Door",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/thegirlnextdoor/v18/pe0zMJCIMIsBjFxqYBIcZ6_OI5oFHCYIV7t7w6bE2A.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "The Nautigal",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/thenautigal/v3/VdGGAZ8ZH51Lvng9fQV2bfKTWypA2_-C7LoS7g.ttf",
  "regular": "http://fonts.gstatic.com/s/thenautigal/v3/VdGZAZ8ZH51Lvng9fQV2bfKr5wVk09Se5Q.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tienne",
  "variants": [
  "regular",
  "700",
  "900"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/tienne/v20/AYCJpX7pe9YCRP0zLGzjQHhuzvef5Q.ttf",
  "900": "http://fonts.gstatic.com/s/tienne/v20/AYCJpX7pe9YCRP0zFG7jQHhuzvef5Q.ttf",
  "regular": "http://fonts.gstatic.com/s/tienne/v20/AYCKpX7pe9YCRP0LkEPHSFNyxw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tillana",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/tillana/v11/VuJ0dNvf35P4qJ1OQFL-HIlMZRNcp0o.ttf",
  "600": "http://fonts.gstatic.com/s/tillana/v11/VuJ0dNvf35P4qJ1OQH75HIlMZRNcp0o.ttf",
  "700": "http://fonts.gstatic.com/s/tillana/v11/VuJ0dNvf35P4qJ1OQBr4HIlMZRNcp0o.ttf",
  "800": "http://fonts.gstatic.com/s/tillana/v11/VuJ0dNvf35P4qJ1OQAb7HIlMZRNcp0o.ttf",
  "regular": "http://fonts.gstatic.com/s/tillana/v11/VuJxdNvf35P4qJ1OeKbXOIFneRo.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Timmana",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "telugu"
  ],
  "version": "v12",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/timmana/v12/6xKvdShfL9yK-rvpCmvbKHwJUOM.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tinos",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "hebrew",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/tinos/v24/buE1poGnedXvwj1AW0Fp2i43-cxL.ttf",
  "regular": "http://fonts.gstatic.com/s/tinos/v24/buE4poGnedXvwgX8dGVh8TI-.ttf",
  "italic": "http://fonts.gstatic.com/s/tinos/v24/buE2poGnedXvwjX-fmFD9CI-4NU.ttf",
  "700italic": "http://fonts.gstatic.com/s/tinos/v24/buEzpoGnedXvwjX-Rt1s0CoV_NxLeiw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tiro Bangla",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "bengali",
  "latin",
  "latin-ext"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tirobangla/v4/IFSgHe1Tm95E3O8b5i2V8MG9-UPeuz4i.ttf",
  "italic": "http://fonts.gstatic.com/s/tirobangla/v4/IFSiHe1Tm95E3O8b5i2V8PG_80f8vi4imBM.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tiro Devanagari Hindi",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tirodevanagarihindi/v3/55xyezN7P8T4e0_CfIJrwdodg9HoYw0i-M9fSOkOfG0Y3A.ttf",
  "italic": "http://fonts.gstatic.com/s/tirodevanagarihindi/v3/55x8ezN7P8T4e0_CfIJrwdodg9HoYw0i-M9vSuMKXmgI3F_o.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tiro Devanagari Marathi",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tirodevanagarimarathi/v3/fC1xPZBSZHrRhS3rd4M0MAPNJUHl4znXCxAkotDrDJYM2lAZ.ttf",
  "italic": "http://fonts.gstatic.com/s/tirodevanagarimarathi/v3/fC1zPZBSZHrRhS3rd4M0MAPNJUHl4znXCxAkouDpBpIu30AZbUY.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tiro Devanagari Sanskrit",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tirodevanagarisanskrit/v3/MCoAzBbr09vVUgVBM8FWu_yZdZkhkg-I0nUlb59pEoEqgtOh0w.ttf",
  "italic": "http://fonts.gstatic.com/s/tirodevanagarisanskrit/v3/MCoGzBbr09vVUgVBM8FWu_yZdZkhkg-I0nUlb59ZEIsuoNax06MM.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tiro Gurmukhi",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "gurmukhi",
  "latin",
  "latin-ext"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tirogurmukhi/v4/x3dmckXSYq-Uqjc048JUF7Jvly7HAQsyA2Y.ttf",
  "italic": "http://fonts.gstatic.com/s/tirogurmukhi/v4/x3d4ckXSYq-Uqjc048JUF7JvpyzNBSk3E2YljQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tiro Kannada",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "kannada",
  "latin",
  "latin-ext"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tirokannada/v4/CSR44ztKmvqaDxEDJFY7CIYKSPl6tOU9Eg.ttf",
  "italic": "http://fonts.gstatic.com/s/tirokannada/v4/CSRm4ztKmvqaDxEDJFY7CIY6SvN-luAtEnKp.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tiro Tamil",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "tamil"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tirotamil/v4/m8JXjfVIf7OT22n3M-S_ULRvamODxdI.ttf",
  "italic": "http://fonts.gstatic.com/s/tirotamil/v4/m8JVjfVIf7OT22n3M-S_YLZlbkGG1dKEDw.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tiro Telugu",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "telugu"
  ],
  "version": "v4",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tirotelugu/v4/aFTQ7PxlZWk2EPiSymjXdKSNQqn0X0BO.ttf",
  "italic": "http://fonts.gstatic.com/s/tirotelugu/v4/aFTS7PxlZWk2EPiSymjXdJSPSK3WWlBOoas.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Titan One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/titanone/v13/mFTzWbsGxbbS_J5cQcjykzIn2Etikg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Titillium Web",
  "variants": [
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPDcZTIAOhVxoMyOr9n_E7ffAzHKIx5YrSYqWM.ttf",
  "300": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPDcZTIAOhVxoMyOr9n_E7ffGjEKIx5YrSYqWM.ttf",
  "600": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPDcZTIAOhVxoMyOr9n_E7ffBzCKIx5YrSYqWM.ttf",
  "700": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPDcZTIAOhVxoMyOr9n_E7ffHjDKIx5YrSYqWM.ttf",
  "900": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPDcZTIAOhVxoMyOr9n_E7ffEDBKIx5YrSYqWM.ttf",
  "200italic": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPFcZTIAOhVxoMyOr9n_E7fdMbewI1zZpaduWMmxA.ttf",
  "300italic": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPFcZTIAOhVxoMyOr9n_E7fdMbepI5zZpaduWMmxA.ttf",
  "regular": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPecZTIAOhVxoMyOr9n_E7fRMTsDIRSfr0.ttf",
  "italic": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPAcZTIAOhVxoMyOr9n_E7fdMbmCKZXbr2BsA.ttf",
  "600italic": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPFcZTIAOhVxoMyOr9n_E7fdMbe0IhzZpaduWMmxA.ttf",
  "700italic": "http://fonts.gstatic.com/s/titilliumweb/v15/NaPFcZTIAOhVxoMyOr9n_E7fdMbetIlzZpaduWMmxA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tomorrow",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/tomorrow/v15/WBLgrETNbFtZCeGqgR2xe2XiKMiokE4.ttf",
  "200": "http://fonts.gstatic.com/s/tomorrow/v15/WBLhrETNbFtZCeGqgR0dWkXIBsShiVd4.ttf",
  "300": "http://fonts.gstatic.com/s/tomorrow/v15/WBLhrETNbFtZCeGqgR15WUXIBsShiVd4.ttf",
  "500": "http://fonts.gstatic.com/s/tomorrow/v15/WBLhrETNbFtZCeGqgR0hWEXIBsShiVd4.ttf",
  "600": "http://fonts.gstatic.com/s/tomorrow/v15/WBLhrETNbFtZCeGqgR0NX0XIBsShiVd4.ttf",
  "700": "http://fonts.gstatic.com/s/tomorrow/v15/WBLhrETNbFtZCeGqgR1pXkXIBsShiVd4.ttf",
  "800": "http://fonts.gstatic.com/s/tomorrow/v15/WBLhrETNbFtZCeGqgR11XUXIBsShiVd4.ttf",
  "900": "http://fonts.gstatic.com/s/tomorrow/v15/WBLhrETNbFtZCeGqgR1RXEXIBsShiVd4.ttf",
  "100italic": "http://fonts.gstatic.com/s/tomorrow/v15/WBLirETNbFtZCeGqgRXXQwHoLOqtgE5h0A.ttf",
  "200italic": "http://fonts.gstatic.com/s/tomorrow/v15/WBLjrETNbFtZCeGqgRXXQ63JDMCDjEd4yVY.ttf",
  "300italic": "http://fonts.gstatic.com/s/tomorrow/v15/WBLjrETNbFtZCeGqgRXXQ8nKDMCDjEd4yVY.ttf",
  "regular": "http://fonts.gstatic.com/s/tomorrow/v15/WBLmrETNbFtZCeGqgSXVcWHALdio.ttf",
  "italic": "http://fonts.gstatic.com/s/tomorrow/v15/WBLgrETNbFtZCeGqgRXXe2XiKMiokE4.ttf",
  "500italic": "http://fonts.gstatic.com/s/tomorrow/v15/WBLjrETNbFtZCeGqgRXXQ5HLDMCDjEd4yVY.ttf",
  "600italic": "http://fonts.gstatic.com/s/tomorrow/v15/WBLjrETNbFtZCeGqgRXXQ73MDMCDjEd4yVY.ttf",
  "700italic": "http://fonts.gstatic.com/s/tomorrow/v15/WBLjrETNbFtZCeGqgRXXQ9nNDMCDjEd4yVY.ttf",
  "800italic": "http://fonts.gstatic.com/s/tomorrow/v15/WBLjrETNbFtZCeGqgRXXQ8XODMCDjEd4yVY.ttf",
  "900italic": "http://fonts.gstatic.com/s/tomorrow/v15/WBLjrETNbFtZCeGqgRXXQ-HPDMCDjEd4yVY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tourney",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/tourney/v8/AlZa_ztDtYzv1tzq1wcJnbVt7xseomk-tNs7qrzTWbyt8n7GOQByZTp1I1LcGA.ttf",
  "200": "http://fonts.gstatic.com/s/tourney/v8/AlZa_ztDtYzv1tzq1wcJnbVt7xseomk-tNs7qrzTWbyt8n7GuQFyZTp1I1LcGA.ttf",
  "300": "http://fonts.gstatic.com/s/tourney/v8/AlZa_ztDtYzv1tzq1wcJnbVt7xseomk-tNs7qrzTWbyt8n7GZwFyZTp1I1LcGA.ttf",
  "500": "http://fonts.gstatic.com/s/tourney/v8/AlZa_ztDtYzv1tzq1wcJnbVt7xseomk-tNs7qrzTWbyt8n7GCwFyZTp1I1LcGA.ttf",
  "600": "http://fonts.gstatic.com/s/tourney/v8/AlZa_ztDtYzv1tzq1wcJnbVt7xseomk-tNs7qrzTWbyt8n7G5wZyZTp1I1LcGA.ttf",
  "700": "http://fonts.gstatic.com/s/tourney/v8/AlZa_ztDtYzv1tzq1wcJnbVt7xseomk-tNs7qrzTWbyt8n7G3gZyZTp1I1LcGA.ttf",
  "800": "http://fonts.gstatic.com/s/tourney/v8/AlZa_ztDtYzv1tzq1wcJnbVt7xseomk-tNs7qrzTWbyt8n7GuQZyZTp1I1LcGA.ttf",
  "900": "http://fonts.gstatic.com/s/tourney/v8/AlZa_ztDtYzv1tzq1wcJnbVt7xseomk-tNs7qrzTWbyt8n7GkAZyZTp1I1LcGA.ttf",
  "regular": "http://fonts.gstatic.com/s/tourney/v8/AlZa_ztDtYzv1tzq1wcJnbVt7xseomk-tNs7qrzTWbyt8n7GOQFyZTp1I1LcGA.ttf",
  "100italic": "http://fonts.gstatic.com/s/tourney/v8/AlZc_ztDtYzv1tzq_Q47flUUvI2wpXz29ilymEMLMNc3XHnT8UKaJzBxAVfMGOPb.ttf",
  "200italic": "http://fonts.gstatic.com/s/tourney/v8/AlZc_ztDtYzv1tzq_Q47flUUvI2wpXz29ilymEMLMNc3XHnT8UIaJjBxAVfMGOPb.ttf",
  "300italic": "http://fonts.gstatic.com/s/tourney/v8/AlZc_ztDtYzv1tzq_Q47flUUvI2wpXz29ilymEMLMNc3XHnT8ULEJjBxAVfMGOPb.ttf",
  "italic": "http://fonts.gstatic.com/s/tourney/v8/AlZc_ztDtYzv1tzq_Q47flUUvI2wpXz29ilymEMLMNc3XHnT8UKaJjBxAVfMGOPb.ttf",
  "500italic": "http://fonts.gstatic.com/s/tourney/v8/AlZc_ztDtYzv1tzq_Q47flUUvI2wpXz29ilymEMLMNc3XHnT8UKoJjBxAVfMGOPb.ttf",
  "600italic": "http://fonts.gstatic.com/s/tourney/v8/AlZc_ztDtYzv1tzq_Q47flUUvI2wpXz29ilymEMLMNc3XHnT8UJEITBxAVfMGOPb.ttf",
  "700italic": "http://fonts.gstatic.com/s/tourney/v8/AlZc_ztDtYzv1tzq_Q47flUUvI2wpXz29ilymEMLMNc3XHnT8UJ9ITBxAVfMGOPb.ttf",
  "800italic": "http://fonts.gstatic.com/s/tourney/v8/AlZc_ztDtYzv1tzq_Q47flUUvI2wpXz29ilymEMLMNc3XHnT8UIaITBxAVfMGOPb.ttf",
  "900italic": "http://fonts.gstatic.com/s/tourney/v8/AlZc_ztDtYzv1tzq_Q47flUUvI2wpXz29ilymEMLMNc3XHnT8UIzITBxAVfMGOPb.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Trade Winds",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tradewinds/v17/AYCPpXPpYNIIT7h8-QenM3Jq7PKP5Z_G.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Train One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/trainone/v13/gyB-hwkiNtc6KnxUVjWHOqbZRY7JVQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Trirong",
  "variants": [
  "100",
  "100italic",
  "200",
  "200italic",
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic",
  "800",
  "800italic",
  "900",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "thai",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/trirong/v11/7r3EqXNgp8wxdOdOl-go3YRl6ujngw.ttf",
  "200": "http://fonts.gstatic.com/s/trirong/v11/7r3DqXNgp8wxdOdOl0QJ_a5L5uH-mts.ttf",
  "300": "http://fonts.gstatic.com/s/trirong/v11/7r3DqXNgp8wxdOdOlyAK_a5L5uH-mts.ttf",
  "500": "http://fonts.gstatic.com/s/trirong/v11/7r3DqXNgp8wxdOdOl3gL_a5L5uH-mts.ttf",
  "600": "http://fonts.gstatic.com/s/trirong/v11/7r3DqXNgp8wxdOdOl1QM_a5L5uH-mts.ttf",
  "700": "http://fonts.gstatic.com/s/trirong/v11/7r3DqXNgp8wxdOdOlzAN_a5L5uH-mts.ttf",
  "800": "http://fonts.gstatic.com/s/trirong/v11/7r3DqXNgp8wxdOdOlywO_a5L5uH-mts.ttf",
  "900": "http://fonts.gstatic.com/s/trirong/v11/7r3DqXNgp8wxdOdOlwgP_a5L5uH-mts.ttf",
  "100italic": "http://fonts.gstatic.com/s/trirong/v11/7r3CqXNgp8wxdOdOn44QuY5hyO33g8IY.ttf",
  "200italic": "http://fonts.gstatic.com/s/trirong/v11/7r3BqXNgp8wxdOdOn44QFa9B4sP7itsB5g.ttf",
  "300italic": "http://fonts.gstatic.com/s/trirong/v11/7r3BqXNgp8wxdOdOn44QcaxB4sP7itsB5g.ttf",
  "regular": "http://fonts.gstatic.com/s/trirong/v11/7r3GqXNgp8wxdOdOr4wi2aZg-ug.ttf",
  "italic": "http://fonts.gstatic.com/s/trirong/v11/7r3EqXNgp8wxdOdOn44o3YRl6ujngw.ttf",
  "500italic": "http://fonts.gstatic.com/s/trirong/v11/7r3BqXNgp8wxdOdOn44QKa1B4sP7itsB5g.ttf",
  "600italic": "http://fonts.gstatic.com/s/trirong/v11/7r3BqXNgp8wxdOdOn44QBapB4sP7itsB5g.ttf",
  "700italic": "http://fonts.gstatic.com/s/trirong/v11/7r3BqXNgp8wxdOdOn44QYatB4sP7itsB5g.ttf",
  "800italic": "http://fonts.gstatic.com/s/trirong/v11/7r3BqXNgp8wxdOdOn44QfahB4sP7itsB5g.ttf",
  "900italic": "http://fonts.gstatic.com/s/trirong/v11/7r3BqXNgp8wxdOdOn44QWalB4sP7itsB5g.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Trispace",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/trispace/v18/Yq65-LKSQC3o56LxxgRrtA6yBqsrXL5GI5KI-IUZVGsxWFIlbH9qoQl0zHugpt0.ttf",
  "200": "http://fonts.gstatic.com/s/trispace/v18/Yq65-LKSQC3o56LxxgRrtA6yBqsrXL5GI5KI-IUZVGsxWFIlbP9roQl0zHugpt0.ttf",
  "300": "http://fonts.gstatic.com/s/trispace/v18/Yq65-LKSQC3o56LxxgRrtA6yBqsrXL5GI5KI-IUZVGsxWFIlbCFroQl0zHugpt0.ttf",
  "500": "http://fonts.gstatic.com/s/trispace/v18/Yq65-LKSQC3o56LxxgRrtA6yBqsrXL5GI5KI-IUZVGsxWFIlbE1roQl0zHugpt0.ttf",
  "600": "http://fonts.gstatic.com/s/trispace/v18/Yq65-LKSQC3o56LxxgRrtA6yBqsrXL5GI5KI-IUZVGsxWFIlbKFsoQl0zHugpt0.ttf",
  "700": "http://fonts.gstatic.com/s/trispace/v18/Yq65-LKSQC3o56LxxgRrtA6yBqsrXL5GI5KI-IUZVGsxWFIlbJhsoQl0zHugpt0.ttf",
  "800": "http://fonts.gstatic.com/s/trispace/v18/Yq65-LKSQC3o56LxxgRrtA6yBqsrXL5GI5KI-IUZVGsxWFIlbP9soQl0zHugpt0.ttf",
  "regular": "http://fonts.gstatic.com/s/trispace/v18/Yq65-LKSQC3o56LxxgRrtA6yBqsrXL5GI5KI-IUZVGsxWFIlbH9roQl0zHugpt0.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Trocchi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/trocchi/v14/qWcqB6WkuIDxDZLcDrtUvMeTYD0.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Trochut",
  "variants": [
  "regular",
  "italic",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/trochut/v20/CHymV-fDDlP9bDIw3sinWVokMnIllmA.ttf",
  "regular": "http://fonts.gstatic.com/s/trochut/v20/CHyjV-fDDlP9bDIw5nSIfVIPLns.ttf",
  "italic": "http://fonts.gstatic.com/s/trochut/v20/CHyhV-fDDlP9bDIw1naCeXAKPns8jw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Truculenta",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/truculenta/v18/LhWfMVvBKusVIfNYGi1-WvRVyDdZeeiySNppcu32Mb2f06y6Oa21F6XHi0VYDX_PzOupMlAjswcFHnJMMhg.ttf",
  "200": "http://fonts.gstatic.com/s/truculenta/v18/LhWfMVvBKusVIfNYGi1-WvRVyDdZeeiySNppcu32Mb2f06y6Oa21F6XHi0VYDX_PzOupMtAiswcFHnJMMhg.ttf",
  "300": "http://fonts.gstatic.com/s/truculenta/v18/LhWfMVvBKusVIfNYGi1-WvRVyDdZeeiySNppcu32Mb2f06y6Oa21F6XHi0VYDX_PzOupMg4iswcFHnJMMhg.ttf",
  "500": "http://fonts.gstatic.com/s/truculenta/v18/LhWfMVvBKusVIfNYGi1-WvRVyDdZeeiySNppcu32Mb2f06y6Oa21F6XHi0VYDX_PzOupMmIiswcFHnJMMhg.ttf",
  "600": "http://fonts.gstatic.com/s/truculenta/v18/LhWfMVvBKusVIfNYGi1-WvRVyDdZeeiySNppcu32Mb2f06y6Oa21F6XHi0VYDX_PzOupMo4lswcFHnJMMhg.ttf",
  "700": "http://fonts.gstatic.com/s/truculenta/v18/LhWfMVvBKusVIfNYGi1-WvRVyDdZeeiySNppcu32Mb2f06y6Oa21F6XHi0VYDX_PzOupMrclswcFHnJMMhg.ttf",
  "800": "http://fonts.gstatic.com/s/truculenta/v18/LhWfMVvBKusVIfNYGi1-WvRVyDdZeeiySNppcu32Mb2f06y6Oa21F6XHi0VYDX_PzOupMtAlswcFHnJMMhg.ttf",
  "900": "http://fonts.gstatic.com/s/truculenta/v18/LhWfMVvBKusVIfNYGi1-WvRVyDdZeeiySNppcu32Mb2f06y6Oa21F6XHi0VYDX_PzOupMvklswcFHnJMMhg.ttf",
  "regular": "http://fonts.gstatic.com/s/truculenta/v18/LhWfMVvBKusVIfNYGi1-WvRVyDdZeeiySNppcu32Mb2f06y6Oa21F6XHi0VYDX_PzOupMlAiswcFHnJMMhg.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Trykker",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/trykker/v21/KtktALyWZJXudUPzhNnoOd2j22U.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Tulpen One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/tulpenone/v21/dFa6ZfeC474skLgesc0CWj0w_HyIRlE.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Turret Road",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "700",
  "800"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/turretroad/v7/pxidypMgpcBFjE84Zv-fE0ONEdeLYk1Mq3ap.ttf",
  "300": "http://fonts.gstatic.com/s/turretroad/v7/pxidypMgpcBFjE84Zv-fE0PpEteLYk1Mq3ap.ttf",
  "500": "http://fonts.gstatic.com/s/turretroad/v7/pxidypMgpcBFjE84Zv-fE0OxE9eLYk1Mq3ap.ttf",
  "700": "http://fonts.gstatic.com/s/turretroad/v7/pxidypMgpcBFjE84Zv-fE0P5FdeLYk1Mq3ap.ttf",
  "800": "http://fonts.gstatic.com/s/turretroad/v7/pxidypMgpcBFjE84Zv-fE0PlFteLYk1Mq3ap.ttf",
  "regular": "http://fonts.gstatic.com/s/turretroad/v7/pxiAypMgpcBFjE84Zv-fE3tFOvODSVFF.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Twinkle Star",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/twinklestar/v3/pe0pMI6IL4dPoFl9LGEmY6WaA_Rue1UwVg.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ubuntu",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/ubuntu/v20/4iCv6KVjbNBYlgoC1CzTt2aMH4V_gg.ttf",
  "500": "http://fonts.gstatic.com/s/ubuntu/v20/4iCv6KVjbNBYlgoCjC3Tt2aMH4V_gg.ttf",
  "700": "http://fonts.gstatic.com/s/ubuntu/v20/4iCv6KVjbNBYlgoCxCvTt2aMH4V_gg.ttf",
  "300italic": "http://fonts.gstatic.com/s/ubuntu/v20/4iCp6KVjbNBYlgoKejZftWyIPYBvgpUI.ttf",
  "regular": "http://fonts.gstatic.com/s/ubuntu/v20/4iCs6KVjbNBYlgo6eAT3v02QFg.ttf",
  "italic": "http://fonts.gstatic.com/s/ubuntu/v20/4iCu6KVjbNBYlgoKeg7znUiAFpxm.ttf",
  "500italic": "http://fonts.gstatic.com/s/ubuntu/v20/4iCp6KVjbNBYlgoKejYHtGyIPYBvgpUI.ttf",
  "700italic": "http://fonts.gstatic.com/s/ubuntu/v20/4iCp6KVjbNBYlgoKejZPsmyIPYBvgpUI.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ubuntu Condensed",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ubuntucondensed/v16/u-4k0rCzjgs5J7oXnJcM_0kACGMtf-fVqvHoJXw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ubuntu Mono",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "greek-ext",
  "latin",
  "latin-ext"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/ubuntumono/v15/KFO-CneDtsqEr0keqCMhbC-BL-Hyv4xGemO1.ttf",
  "regular": "http://fonts.gstatic.com/s/ubuntumono/v15/KFOjCneDtsqEr0keqCMhbBc9AMX6lJBP.ttf",
  "italic": "http://fonts.gstatic.com/s/ubuntumono/v15/KFOhCneDtsqEr0keqCMhbCc_CsHYkYBPY3o.ttf",
  "700italic": "http://fonts.gstatic.com/s/ubuntumono/v15/KFO8CneDtsqEr0keqCMhbCc_Mn33tYhkf3O1GVg.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Uchen",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "tibetan"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/uchen/v7/nKKZ-GokGZ1baIaSEQGodLxA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Ultra",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/ultra/v19/zOLy4prXmrtY-tT6yLOD6NxF.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Uncial Antiqua",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/uncialantiqua/v20/N0bM2S5WOex4OUbESzoESK-i-PfRS5VBBSSF.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Underdog",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/underdog/v22/CHygV-jCElj7diMroVSiU14GN2Il.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Unica One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v13",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/unicaone/v13/DPEuYwWHyAYGVTSmalshdtffuEY7FA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "UnifrakturCook",
  "variants": [
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/unifrakturcook/v19/IurA6Yli8YOdcoky-0PTTdkm56n05Uw13ILXs-h6.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "UnifrakturMaguntia",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/unifrakturmaguntia/v16/WWXPlieVYwiGNomYU-ciRLRvEmK7oaVun2xNNgNa1A.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Unkempt",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/unkempt/v19/2EbiL-Z2DFZue0DScTow1zWzq_5uT84.ttf",
  "regular": "http://fonts.gstatic.com/s/unkempt/v19/2EbnL-Z2DFZue0DSSYYf8z2Yt_c.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Unlock",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/unlock/v22/7Au-p_8ykD-cDl7GKAjSwkUVOQ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Unna",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/unna/v21/AYCLpXzofN0NMiQusGnpRFpr3vc.ttf",
  "regular": "http://fonts.gstatic.com/s/unna/v21/AYCEpXzofN0NCpgBlGHCWFM.ttf",
  "italic": "http://fonts.gstatic.com/s/unna/v21/AYCKpXzofN0NOpoLkEPHSFNyxw.ttf",
  "700italic": "http://fonts.gstatic.com/s/unna/v21/AYCJpXzofN0NOpozLGzjQHhuzvef5Q.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Updock",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/updock/v2/nuF4D_3dVZ70UI9SjLK3602XBw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Urbanist",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/urbanist/v10/L0xjDF02iFML4hGCyOCpRdycFsGxSrqDyx8fFpOrS8SlKw.ttf",
  "200": "http://fonts.gstatic.com/s/urbanist/v10/L0xjDF02iFML4hGCyOCpRdycFsGxSrqDSx4fFpOrS8SlKw.ttf",
  "300": "http://fonts.gstatic.com/s/urbanist/v10/L0xjDF02iFML4hGCyOCpRdycFsGxSrqDlR4fFpOrS8SlKw.ttf",
  "500": "http://fonts.gstatic.com/s/urbanist/v10/L0xjDF02iFML4hGCyOCpRdycFsGxSrqD-R4fFpOrS8SlKw.ttf",
  "600": "http://fonts.gstatic.com/s/urbanist/v10/L0xjDF02iFML4hGCyOCpRdycFsGxSrqDFRkfFpOrS8SlKw.ttf",
  "700": "http://fonts.gstatic.com/s/urbanist/v10/L0xjDF02iFML4hGCyOCpRdycFsGxSrqDLBkfFpOrS8SlKw.ttf",
  "800": "http://fonts.gstatic.com/s/urbanist/v10/L0xjDF02iFML4hGCyOCpRdycFsGxSrqDSxkfFpOrS8SlKw.ttf",
  "900": "http://fonts.gstatic.com/s/urbanist/v10/L0xjDF02iFML4hGCyOCpRdycFsGxSrqDYhkfFpOrS8SlKw.ttf",
  "regular": "http://fonts.gstatic.com/s/urbanist/v10/L0xjDF02iFML4hGCyOCpRdycFsGxSrqDyx4fFpOrS8SlKw.ttf",
  "100italic": "http://fonts.gstatic.com/s/urbanist/v10/L0xtDF02iFML4hGCyMqgdyNEf6or5L2WA133VJmvacG1K4S1.ttf",
  "200italic": "http://fonts.gstatic.com/s/urbanist/v10/L0xtDF02iFML4hGCyMqgdyNEf6or5L2WA113VZmvacG1K4S1.ttf",
  "300italic": "http://fonts.gstatic.com/s/urbanist/v10/L0xtDF02iFML4hGCyMqgdyNEf6or5L2WA12pVZmvacG1K4S1.ttf",
  "italic": "http://fonts.gstatic.com/s/urbanist/v10/L0xtDF02iFML4hGCyMqgdyNEf6or5L2WA133VZmvacG1K4S1.ttf",
  "500italic": "http://fonts.gstatic.com/s/urbanist/v10/L0xtDF02iFML4hGCyMqgdyNEf6or5L2WA13FVZmvacG1K4S1.ttf",
  "600italic": "http://fonts.gstatic.com/s/urbanist/v10/L0xtDF02iFML4hGCyMqgdyNEf6or5L2WA10pUpmvacG1K4S1.ttf",
  "700italic": "http://fonts.gstatic.com/s/urbanist/v10/L0xtDF02iFML4hGCyMqgdyNEf6or5L2WA10QUpmvacG1K4S1.ttf",
  "800italic": "http://fonts.gstatic.com/s/urbanist/v10/L0xtDF02iFML4hGCyMqgdyNEf6or5L2WA113UpmvacG1K4S1.ttf",
  "900italic": "http://fonts.gstatic.com/s/urbanist/v10/L0xtDF02iFML4hGCyMqgdyNEf6or5L2WA11eUpmvacG1K4S1.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "VT323",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/vt323/v17/pxiKyp0ihIEF2hsYHpT2dkNE.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Vampiro One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v18",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/vampiroone/v18/gokqH6DoDl5yXvJytFsdLkqnsvhIor3K.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Varela",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/varela/v16/DPEtYwqExx0AWHXJBBQFfvzDsQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Varela Round",
  "variants": [
  "regular"
  ],
  "subsets": [
  "hebrew",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/varelaround/v19/w8gdH283Tvk__Lua32TysjIvoMGOD9gxZw.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Varta",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/varta/v17/Qw3AZQpJHj_6LzHUngWbrFkDH1x96j4EirE-9PGLfQ.ttf",
  "500": "http://fonts.gstatic.com/s/varta/v17/Qw3AZQpJHj_6LzHUngWbrFkDH1x9hj4EirE-9PGLfQ.ttf",
  "600": "http://fonts.gstatic.com/s/varta/v17/Qw3AZQpJHj_6LzHUngWbrFkDH1x9ajkEirE-9PGLfQ.ttf",
  "700": "http://fonts.gstatic.com/s/varta/v17/Qw3AZQpJHj_6LzHUngWbrFkDH1x9UzkEirE-9PGLfQ.ttf",
  "regular": "http://fonts.gstatic.com/s/varta/v17/Qw3AZQpJHj_6LzHUngWbrFkDH1x9tD4EirE-9PGLfQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Vast Shadow",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/vastshadow/v15/pe0qMImKOZ1V62ZwbVY9dfe6Kdpickwp.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Vazirmatn",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900"
  ],
  "subsets": [
  "arabic",
  "latin",
  "latin-ext"
  ],
  "version": "v6",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/vazirmatn/v6/Dxx78j6PP2D_kU2muijPEe1n2vVbfJRklWgyOReZ72DF_QY.ttf",
  "200": "http://fonts.gstatic.com/s/vazirmatn/v6/Dxx78j6PP2D_kU2muijPEe1n2vVbfJRklegzOReZ72DF_QY.ttf",
  "300": "http://fonts.gstatic.com/s/vazirmatn/v6/Dxx78j6PP2D_kU2muijPEe1n2vVbfJRklTYzOReZ72DF_QY.ttf",
  "500": "http://fonts.gstatic.com/s/vazirmatn/v6/Dxx78j6PP2D_kU2muijPEe1n2vVbfJRklVozOReZ72DF_QY.ttf",
  "600": "http://fonts.gstatic.com/s/vazirmatn/v6/Dxx78j6PP2D_kU2muijPEe1n2vVbfJRklbY0OReZ72DF_QY.ttf",
  "700": "http://fonts.gstatic.com/s/vazirmatn/v6/Dxx78j6PP2D_kU2muijPEe1n2vVbfJRklY80OReZ72DF_QY.ttf",
  "800": "http://fonts.gstatic.com/s/vazirmatn/v6/Dxx78j6PP2D_kU2muijPEe1n2vVbfJRkleg0OReZ72DF_QY.ttf",
  "900": "http://fonts.gstatic.com/s/vazirmatn/v6/Dxx78j6PP2D_kU2muijPEe1n2vVbfJRklcE0OReZ72DF_QY.ttf",
  "regular": "http://fonts.gstatic.com/s/vazirmatn/v6/Dxx78j6PP2D_kU2muijPEe1n2vVbfJRklWgzOReZ72DF_QY.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Vesper Libre",
  "variants": [
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/vesperlibre/v19/bx6dNxyWnf-uxPdXDHUD_RdA-2ap0okKXKvPlw.ttf",
  "700": "http://fonts.gstatic.com/s/vesperlibre/v19/bx6dNxyWnf-uxPdXDHUD_RdAs2Cp0okKXKvPlw.ttf",
  "900": "http://fonts.gstatic.com/s/vesperlibre/v19/bx6dNxyWnf-uxPdXDHUD_RdAi2Kp0okKXKvPlw.ttf",
  "regular": "http://fonts.gstatic.com/s/vesperlibre/v19/bx6CNxyWnf-uxPdXDHUD_Rd4D0-N2qIWVQ.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Viaoda Libre",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/viaodalibre/v15/vEFW2_lWCgoR6OKuRz9kcRVJb2IY2tOHXg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Vibes",
  "variants": [
  "regular"
  ],
  "subsets": [
  "arabic",
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/vibes/v14/QdVYSTsmIB6tmbd3HpbsuBlh.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Vibur",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v23",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/vibur/v23/DPEiYwmEzw0QRjTpLjoJd-Xa.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Vidaloka",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/vidaloka/v18/7cHrv4c3ipenMKlEass8yn4hnCci.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Viga",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/viga/v14/xMQbuFFdSaiX_QIjD4e2OX8.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Voces",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/voces/v20/-F6_fjJyLyU8d4PBBG7YpzlJ.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Volkhov",
  "variants": [
  "regular",
  "italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-04-27",
  "files": {
  "700": "http://fonts.gstatic.com/s/volkhov/v17/SlGVmQieoJcKemNeeY4hoHRYbDQUego.ttf",
  "regular": "http://fonts.gstatic.com/s/volkhov/v17/SlGQmQieoJcKemNeQTIOhHxzcD0.ttf",
  "italic": "http://fonts.gstatic.com/s/volkhov/v17/SlGSmQieoJcKemNecTAEgF52YD0NYw.ttf",
  "700italic": "http://fonts.gstatic.com/s/volkhov/v17/SlGXmQieoJcKemNecTA8PHFSaBYRagrQrA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Vollkorn",
  "variants": [
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "greek",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v21",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/vollkorn/v21/0ybgGDoxxrvAnPhYGzMlQLzuMasz6Df2AnGuGWOdEbD63w.ttf",
  "600": "http://fonts.gstatic.com/s/vollkorn/v21/0ybgGDoxxrvAnPhYGzMlQLzuMasz6Df27nauGWOdEbD63w.ttf",
  "700": "http://fonts.gstatic.com/s/vollkorn/v21/0ybgGDoxxrvAnPhYGzMlQLzuMasz6Df213auGWOdEbD63w.ttf",
  "800": "http://fonts.gstatic.com/s/vollkorn/v21/0ybgGDoxxrvAnPhYGzMlQLzuMasz6Df2sHauGWOdEbD63w.ttf",
  "900": "http://fonts.gstatic.com/s/vollkorn/v21/0ybgGDoxxrvAnPhYGzMlQLzuMasz6Df2mXauGWOdEbD63w.ttf",
  "regular": "http://fonts.gstatic.com/s/vollkorn/v21/0ybgGDoxxrvAnPhYGzMlQLzuMasz6Df2MHGuGWOdEbD63w.ttf",
  "italic": "http://fonts.gstatic.com/s/vollkorn/v21/0ybuGDoxxrvAnPhYGxksckM2WMCpRjDj-DJGWmmZM7Xq34g9.ttf",
  "500italic": "http://fonts.gstatic.com/s/vollkorn/v21/0ybuGDoxxrvAnPhYGxksckM2WMCpRjDj-DJ0WmmZM7Xq34g9.ttf",
  "600italic": "http://fonts.gstatic.com/s/vollkorn/v21/0ybuGDoxxrvAnPhYGxksckM2WMCpRjDj-DKYXWmZM7Xq34g9.ttf",
  "700italic": "http://fonts.gstatic.com/s/vollkorn/v21/0ybuGDoxxrvAnPhYGxksckM2WMCpRjDj-DKhXWmZM7Xq34g9.ttf",
  "800italic": "http://fonts.gstatic.com/s/vollkorn/v21/0ybuGDoxxrvAnPhYGxksckM2WMCpRjDj-DLGXWmZM7Xq34g9.ttf",
  "900italic": "http://fonts.gstatic.com/s/vollkorn/v21/0ybuGDoxxrvAnPhYGxksckM2WMCpRjDj-DLvXWmZM7Xq34g9.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Vollkorn SC",
  "variants": [
  "regular",
  "600",
  "700",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "600": "http://fonts.gstatic.com/s/vollkornsc/v11/j8_y6-zQ3rXpceZj9cqnVimhGluqYbPN5Yjn.ttf",
  "700": "http://fonts.gstatic.com/s/vollkornsc/v11/j8_y6-zQ3rXpceZj9cqnVinFG1uqYbPN5Yjn.ttf",
  "900": "http://fonts.gstatic.com/s/vollkornsc/v11/j8_y6-zQ3rXpceZj9cqnVin9GVuqYbPN5Yjn.ttf",
  "regular": "http://fonts.gstatic.com/s/vollkornsc/v11/j8_v6-zQ3rXpceZj9cqnVhF5NH-iSq_E.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Voltaire",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/voltaire/v15/1Pttg8PcRfSblAvGvQooYKVnBOif.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Vujahday Script",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/vujahdayscript/v3/RWmQoKGA8fEkrIPtSZ3_J7er2dUiDEtvAlaMKw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Waiting for the Sunrise",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/waitingforthesunrise/v16/WBL1rFvOYl9CEv2i1mO6KUW8RKWJ2zoXoz5JsYZQ9h_ZYk5J.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Wallpoet",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v16",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/wallpoet/v16/f0X10em2_8RnXVVdUNbu7cXP8L8G.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Walter Turncoat",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v19",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/walterturncoat/v19/snfys0Gs98ln43n0d-14ULoToe67YB2dQ5ZPqQ.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Warnes",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v22",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/warnes/v22/pONn1hc0GsW6sW5OpiC2o6Lkqg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Water Brush",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/waterbrush/v2/AYCPpXPqc8cJWLhp4hywKHJq7PKP5Z_G.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Waterfall",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v3",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/waterfall/v3/MCoRzAfo293fACdFKcwY2rH8D_EZwA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Wellfleet",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/wellfleet/v20/nuF7D_LfQJb3VYgX6eyT42aLDhO2HA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Wendy One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-04-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/wendyone/v14/2sDcZGJOipXfgfXV5wgDb2-4C7wFZQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Whisper",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v2",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/whisper/v2/q5uHsoqtKftx74K9milCBxxdmYU.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "WindSong",
  "variants": [
  "regular",
  "500"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "500": "http://fonts.gstatic.com/s/windsong/v7/KR1RBsyu-P-GFEW57oeNNPWylS3-jVXm.ttf",
  "regular": "http://fonts.gstatic.com/s/windsong/v7/KR1WBsyu-P-GFEW57r95HdG6vjH3.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Wire One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/wireone/v24/qFdH35Wah5htUhV75WGiWdrCwwcJ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Work Sans",
  "variants": [
  "100",
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700",
  "800",
  "900",
  "100italic",
  "200italic",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic",
  "800italic",
  "900italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/worksans/v18/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K0nWNigDp6_cOyA.ttf",
  "200": "http://fonts.gstatic.com/s/worksans/v18/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K8nXNigDp6_cOyA.ttf",
  "300": "http://fonts.gstatic.com/s/worksans/v18/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32KxfXNigDp6_cOyA.ttf",
  "500": "http://fonts.gstatic.com/s/worksans/v18/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K3vXNigDp6_cOyA.ttf",
  "600": "http://fonts.gstatic.com/s/worksans/v18/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K5fQNigDp6_cOyA.ttf",
  "700": "http://fonts.gstatic.com/s/worksans/v18/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K67QNigDp6_cOyA.ttf",
  "800": "http://fonts.gstatic.com/s/worksans/v18/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K8nQNigDp6_cOyA.ttf",
  "900": "http://fonts.gstatic.com/s/worksans/v18/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K-DQNigDp6_cOyA.ttf",
  "regular": "http://fonts.gstatic.com/s/worksans/v18/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K0nXNigDp6_cOyA.ttf",
  "100italic": "http://fonts.gstatic.com/s/worksans/v18/QGY9z_wNahGAdqQ43Rh_ebrnlwyYfEPxPoGU3moJo43ZKyDSQQ.ttf",
  "200italic": "http://fonts.gstatic.com/s/worksans/v18/QGY9z_wNahGAdqQ43Rh_ebrnlwyYfEPxPoGUXmsJo43ZKyDSQQ.ttf",
  "300italic": "http://fonts.gstatic.com/s/worksans/v18/QGY9z_wNahGAdqQ43Rh_ebrnlwyYfEPxPoGUgGsJo43ZKyDSQQ.ttf",
  "italic": "http://fonts.gstatic.com/s/worksans/v18/QGY9z_wNahGAdqQ43Rh_ebrnlwyYfEPxPoGU3msJo43ZKyDSQQ.ttf",
  "500italic": "http://fonts.gstatic.com/s/worksans/v18/QGY9z_wNahGAdqQ43Rh_ebrnlwyYfEPxPoGU7GsJo43ZKyDSQQ.ttf",
  "600italic": "http://fonts.gstatic.com/s/worksans/v18/QGY9z_wNahGAdqQ43Rh_ebrnlwyYfEPxPoGUAGwJo43ZKyDSQQ.ttf",
  "700italic": "http://fonts.gstatic.com/s/worksans/v18/QGY9z_wNahGAdqQ43Rh_ebrnlwyYfEPxPoGUOWwJo43ZKyDSQQ.ttf",
  "800italic": "http://fonts.gstatic.com/s/worksans/v18/QGY9z_wNahGAdqQ43Rh_ebrnlwyYfEPxPoGUXmwJo43ZKyDSQQ.ttf",
  "900italic": "http://fonts.gstatic.com/s/worksans/v18/QGY9z_wNahGAdqQ43Rh_ebrnlwyYfEPxPoGUd2wJo43ZKyDSQQ.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Xanh Mono",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/xanhmono/v17/R70YjykVmvKCep-vWhSYmACQXzLhTg.ttf",
  "italic": "http://fonts.gstatic.com/s/xanhmono/v17/R70ejykVmvKCep-vWhSomgqUfTfxTo24.ttf"
  },
  "category": "monospace",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yaldevi",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "sinhala"
  ],
  "version": "v8",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/yaldevi/v8/cY9afj6VW0NMrDWtDNzCOwlPMq9SLpfxJzvobxLCBJkS.ttf",
  "300": "http://fonts.gstatic.com/s/yaldevi/v8/cY9afj6VW0NMrDWtDNzCOwlPMq9SLpcvJzvobxLCBJkS.ttf",
  "500": "http://fonts.gstatic.com/s/yaldevi/v8/cY9afj6VW0NMrDWtDNzCOwlPMq9SLpdDJzvobxLCBJkS.ttf",
  "600": "http://fonts.gstatic.com/s/yaldevi/v8/cY9afj6VW0NMrDWtDNzCOwlPMq9SLpevIDvobxLCBJkS.ttf",
  "700": "http://fonts.gstatic.com/s/yaldevi/v8/cY9afj6VW0NMrDWtDNzCOwlPMq9SLpeWIDvobxLCBJkS.ttf",
  "regular": "http://fonts.gstatic.com/s/yaldevi/v8/cY9afj6VW0NMrDWtDNzCOwlPMq9SLpdxJzvobxLCBJkS.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yanone Kaffeesatz",
  "variants": [
  "200",
  "300",
  "regular",
  "500",
  "600",
  "700"
  ],
  "subsets": [
  "cyrillic",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v24",
  "lastModified": "2022-09-22",
  "files": {
  "200": "http://fonts.gstatic.com/s/yanonekaffeesatz/v24/3y9I6aknfjLm_3lMKjiMgmUUYBs04aUXNxt9gW2LIftodtWpcGuLCnXkVA.ttf",
  "300": "http://fonts.gstatic.com/s/yanonekaffeesatz/v24/3y9I6aknfjLm_3lMKjiMgmUUYBs04aUXNxt9gW2LIftoqNWpcGuLCnXkVA.ttf",
  "500": "http://fonts.gstatic.com/s/yanonekaffeesatz/v24/3y9I6aknfjLm_3lMKjiMgmUUYBs04aUXNxt9gW2LIftoxNWpcGuLCnXkVA.ttf",
  "600": "http://fonts.gstatic.com/s/yanonekaffeesatz/v24/3y9I6aknfjLm_3lMKjiMgmUUYBs04aUXNxt9gW2LIftoKNKpcGuLCnXkVA.ttf",
  "700": "http://fonts.gstatic.com/s/yanonekaffeesatz/v24/3y9I6aknfjLm_3lMKjiMgmUUYBs04aUXNxt9gW2LIftoEdKpcGuLCnXkVA.ttf",
  "regular": "http://fonts.gstatic.com/s/yanonekaffeesatz/v24/3y9I6aknfjLm_3lMKjiMgmUUYBs04aUXNxt9gW2LIfto9tWpcGuLCnXkVA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yantramanav",
  "variants": [
  "100",
  "300",
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "100": "http://fonts.gstatic.com/s/yantramanav/v11/flU-Rqu5zY00QEpyWJYWN5-QXeNzDB41rZg.ttf",
  "300": "http://fonts.gstatic.com/s/yantramanav/v11/flUhRqu5zY00QEpyWJYWN59Yf8NZIhI8tIHh.ttf",
  "500": "http://fonts.gstatic.com/s/yantramanav/v11/flUhRqu5zY00QEpyWJYWN58AfsNZIhI8tIHh.ttf",
  "700": "http://fonts.gstatic.com/s/yantramanav/v11/flUhRqu5zY00QEpyWJYWN59IeMNZIhI8tIHh.ttf",
  "900": "http://fonts.gstatic.com/s/yantramanav/v11/flUhRqu5zY00QEpyWJYWN59wesNZIhI8tIHh.ttf",
  "regular": "http://fonts.gstatic.com/s/yantramanav/v11/flU8Rqu5zY00QEpyWJYWN6f0V-dRCQ41.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yatra One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "devanagari",
  "latin",
  "latin-ext"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/yatraone/v14/C8ch4copsHzj8p7NaF0xw1OBbRDvXw.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yellowtail",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v18",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/yellowtail/v18/OZpGg_pnoDtINPfRIlLotlzNwED-b4g.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yeon Sung",
  "variants": [
  "regular"
  ],
  "subsets": [
  "korean",
  "latin"
  ],
  "version": "v20",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/yeonsung/v20/QldMNTpbohAGtsJvUn6xSVNazqx2xg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yeseva One",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "cyrillic-ext",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v20",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/yesevaone/v20/OpNJno4ck8vc-xYpwWWxpipfWhXD00c.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yesteryear",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v14",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/yesteryear/v14/dg4g_p78rroaKl8kRKo1r7wHTwonmyw.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yomogi",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v8",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/yomogi/v8/VuJwdNrS2ZL7rpoPWIz5NIh-YA.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yrsa",
  "variants": [
  "300",
  "regular",
  "500",
  "600",
  "700",
  "300italic",
  "italic",
  "500italic",
  "600italic",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext",
  "vietnamese"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/yrsa/v15/wlprgwnQFlxs_wD3CFSMYmFaaCjASNNV9rRPfrKu.ttf",
  "500": "http://fonts.gstatic.com/s/yrsa/v15/wlprgwnQFlxs_wD3CFSMYmFaaCisSNNV9rRPfrKu.ttf",
  "600": "http://fonts.gstatic.com/s/yrsa/v15/wlprgwnQFlxs_wD3CFSMYmFaaChAT9NV9rRPfrKu.ttf",
  "700": "http://fonts.gstatic.com/s/yrsa/v15/wlprgwnQFlxs_wD3CFSMYmFaaCh5T9NV9rRPfrKu.ttf",
  "regular": "http://fonts.gstatic.com/s/yrsa/v15/wlprgwnQFlxs_wD3CFSMYmFaaCieSNNV9rRPfrKu.ttf",
  "300italic": "http://fonts.gstatic.com/s/yrsa/v15/wlptgwnQFlxs1QnF94zlCfv0bz1WC2UW_LBte6KuGEo.ttf",
  "italic": "http://fonts.gstatic.com/s/yrsa/v15/wlptgwnQFlxs1QnF94zlCfv0bz1WCzsW_LBte6KuGEo.ttf",
  "500italic": "http://fonts.gstatic.com/s/yrsa/v15/wlptgwnQFlxs1QnF94zlCfv0bz1WCwkW_LBte6KuGEo.ttf",
  "600italic": "http://fonts.gstatic.com/s/yrsa/v15/wlptgwnQFlxs1QnF94zlCfv0bz1WC-UR_LBte6KuGEo.ttf",
  "700italic": "http://fonts.gstatic.com/s/yrsa/v15/wlptgwnQFlxs1QnF94zlCfv0bz1WC9wR_LBte6KuGEo.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yuji Boku",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v5",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/yujiboku/v5/P5sAzZybeNzXsA9xj1Fkjb2r2dgvJA.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yuji Mai",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v5",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/yujimai/v5/ZgNQjPxdJ7DEHrS0gC38hmHmNpCO.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yuji Syuku",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v5",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/yujisyuku/v5/BngNUXdTV3vO6Lw5ApOPqPfgwqiA-Rk.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Yusei Magic",
  "variants": [
  "regular"
  ],
  "subsets": [
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/yuseimagic/v11/yYLt0hbAyuCmoo5wlhPkpjHR-tdfcIT_.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "ZCOOL KuaiLe",
  "variants": [
  "regular"
  ],
  "subsets": [
  "chinese-simplified",
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zcoolkuaile/v17/tssqApdaRQokwFjFJjvM6h2WpozzoXhC2g.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "ZCOOL QingKe HuangYou",
  "variants": [
  "regular"
  ],
  "subsets": [
  "chinese-simplified",
  "latin"
  ],
  "version": "v13",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zcoolqingkehuangyou/v13/2Eb5L_R5IXJEWhD3AOhSvFC554MOOahI4mRIi_28c8bHWA.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "ZCOOL XiaoWei",
  "variants": [
  "regular"
  ],
  "subsets": [
  "chinese-simplified",
  "latin"
  ],
  "version": "v10",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zcoolxiaowei/v10/i7dMIFFrTRywPpUVX9_RJyM1YFKQHwyVd3U.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zen Antique",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "greek",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zenantique/v10/AYCPpXPnd91Ma_Zf-Ri2JXJq7PKP5Z_G.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zen Antique Soft",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "greek",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zenantiquesoft/v10/DtV4JwqzSL1q_KwnEWMc_3xfgW6ihwBmkui5HNg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zen Dots",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zendots/v10/XRXX3ICfm00IGoesQeaETM_FcCIG.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zen Kaku Gothic Antique",
  "variants": [
  "300",
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-27",
  "files": {
  "300": "http://fonts.gstatic.com/s/zenkakugothicantique/v11/6qLVKYkHvh-nlUpKPAdoVFBtfxDzIn1eCzpB22cM9TarWJtyZyGU.ttf",
  "500": "http://fonts.gstatic.com/s/zenkakugothicantique/v11/6qLVKYkHvh-nlUpKPAdoVFBtfxDzIn1eCzpB22dU9DarWJtyZyGU.ttf",
  "700": "http://fonts.gstatic.com/s/zenkakugothicantique/v11/6qLVKYkHvh-nlUpKPAdoVFBtfxDzIn1eCzpB22cc8jarWJtyZyGU.ttf",
  "900": "http://fonts.gstatic.com/s/zenkakugothicantique/v11/6qLVKYkHvh-nlUpKPAdoVFBtfxDzIn1eCzpB22ck8DarWJtyZyGU.ttf",
  "regular": "http://fonts.gstatic.com/s/zenkakugothicantique/v11/6qLQKYkHvh-nlUpKPAdoVFBtfxDzIn1eCzpB21-g3RKjc4d7.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zen Kaku Gothic New",
  "variants": [
  "300",
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-27",
  "files": {
  "300": "http://fonts.gstatic.com/s/zenkakugothicnew/v11/gNMVW2drQpDw0GjzrVNFf_valaDBcznOqpdKaWTSTGlMyd8.ttf",
  "500": "http://fonts.gstatic.com/s/zenkakugothicnew/v11/gNMVW2drQpDw0GjzrVNFf_valaDBcznOqs9LaWTSTGlMyd8.ttf",
  "700": "http://fonts.gstatic.com/s/zenkakugothicnew/v11/gNMVW2drQpDw0GjzrVNFf_valaDBcznOqodNaWTSTGlMyd8.ttf",
  "900": "http://fonts.gstatic.com/s/zenkakugothicnew/v11/gNMVW2drQpDw0GjzrVNFf_valaDBcznOqr9PaWTSTGlMyd8.ttf",
  "regular": "http://fonts.gstatic.com/s/zenkakugothicnew/v11/gNMYW2drQpDw0GjzrVNFf_valaDBcznOkjtiTWz5UGA.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zen Kurenaido",
  "variants": [
  "regular"
  ],
  "subsets": [
  "cyrillic",
  "greek",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zenkurenaido/v10/3XFsEr0515BK2u6UUptu_gWJZfz22PRLd0U.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zen Loop",
  "variants": [
  "regular",
  "italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zenloop/v7/h0GrssK16UsnJwHsEK9zqwzX5vOG.ttf",
  "italic": "http://fonts.gstatic.com/s/zenloop/v7/h0GtssK16UsnJwHsEJ9xoQj14-OGJ0w.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zen Maru Gothic",
  "variants": [
  "300",
  "regular",
  "500",
  "700",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "greek",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v10",
  "lastModified": "2022-09-27",
  "files": {
  "300": "http://fonts.gstatic.com/s/zenmarugothic/v10/o-0XIpIxzW5b-RxT-6A8jWAtCp-cQWpCPJqa_ajlvw.ttf",
  "500": "http://fonts.gstatic.com/s/zenmarugothic/v10/o-0XIpIxzW5b-RxT-6A8jWAtCp-cGWtCPJqa_ajlvw.ttf",
  "700": "http://fonts.gstatic.com/s/zenmarugothic/v10/o-0XIpIxzW5b-RxT-6A8jWAtCp-cUW1CPJqa_ajlvw.ttf",
  "900": "http://fonts.gstatic.com/s/zenmarugothic/v10/o-0XIpIxzW5b-RxT-6A8jWAtCp-caW9CPJqa_ajlvw.ttf",
  "regular": "http://fonts.gstatic.com/s/zenmarugothic/v10/o-0SIpIxzW5b-RxT-6A8jWAtCp-k7UJmNLGG9A.ttf"
  },
  "category": "sans-serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zen Old Mincho",
  "variants": [
  "regular",
  "700",
  "900"
  ],
  "subsets": [
  "cyrillic",
  "greek",
  "japanese",
  "latin",
  "latin-ext"
  ],
  "version": "v9",
  "lastModified": "2022-09-27",
  "files": {
  "700": "http://fonts.gstatic.com/s/zenoldmincho/v9/tss3ApVaYytLwxTqcxfMyBveyb5LrFla8dMgPgBu.ttf",
  "900": "http://fonts.gstatic.com/s/zenoldmincho/v9/tss3ApVaYytLwxTqcxfMyBveyb5zrlla8dMgPgBu.ttf",
  "regular": "http://fonts.gstatic.com/s/zenoldmincho/v9/tss0ApVaYytLwxTqcxfMyBveyYb3g31S2s8p.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zen Tokyo Zoo",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v7",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zentokyozoo/v7/NGSyv5ffC0J_BK6aFNtr6sRv8a1uRWe9amg.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zeyada",
  "variants": [
  "regular"
  ],
  "subsets": [
  "latin"
  ],
  "version": "v15",
  "lastModified": "2022-09-22",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zeyada/v15/11hAGpPTxVPUbgZDNGatWKaZ3g.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zhi Mang Xing",
  "variants": [
  "regular"
  ],
  "subsets": [
  "chinese-simplified",
  "latin"
  ],
  "version": "v17",
  "lastModified": "2022-09-27",
  "files": {
  "regular": "http://fonts.gstatic.com/s/zhimangxing/v17/f0Xw0ey79sErYFtWQ9a2rq-g0actfektIJ0.ttf"
  },
  "category": "handwriting",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zilla Slab",
  "variants": [
  "300",
  "300italic",
  "regular",
  "italic",
  "500",
  "500italic",
  "600",
  "600italic",
  "700",
  "700italic"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v11",
  "lastModified": "2022-09-22",
  "files": {
  "300": "http://fonts.gstatic.com/s/zillaslab/v11/dFa5ZfeM_74wlPZtksIFYpEY2HSjWlhzbaw.ttf",
  "500": "http://fonts.gstatic.com/s/zillaslab/v11/dFa5ZfeM_74wlPZtksIFYskZ2HSjWlhzbaw.ttf",
  "600": "http://fonts.gstatic.com/s/zillaslab/v11/dFa5ZfeM_74wlPZtksIFYuUe2HSjWlhzbaw.ttf",
  "700": "http://fonts.gstatic.com/s/zillaslab/v11/dFa5ZfeM_74wlPZtksIFYoEf2HSjWlhzbaw.ttf",
  "300italic": "http://fonts.gstatic.com/s/zillaslab/v11/dFanZfeM_74wlPZtksIFaj8CVHapXnp2fazkfg.ttf",
  "regular": "http://fonts.gstatic.com/s/zillaslab/v11/dFa6ZfeM_74wlPZtksIFWj0w_HyIRlE.ttf",
  "italic": "http://fonts.gstatic.com/s/zillaslab/v11/dFa4ZfeM_74wlPZtksIFaj86-F6NVlFqdA.ttf",
  "500italic": "http://fonts.gstatic.com/s/zillaslab/v11/dFanZfeM_74wlPZtksIFaj8CDHepXnp2fazkfg.ttf",
  "600italic": "http://fonts.gstatic.com/s/zillaslab/v11/dFanZfeM_74wlPZtksIFaj8CIHCpXnp2fazkfg.ttf",
  "700italic": "http://fonts.gstatic.com/s/zillaslab/v11/dFanZfeM_74wlPZtksIFaj8CRHGpXnp2fazkfg.ttf"
  },
  "category": "serif",
  "kind": "webfonts#webfont"
  },
  {
  "family": "Zilla Slab Highlight",
  "variants": [
  "regular",
  "700"
  ],
  "subsets": [
  "latin",
  "latin-ext"
  ],
  "version": "v17",
  "lastModified": "2022-09-22",
  "files": {
  "700": "http://fonts.gstatic.com/s/zillaslabhighlight/v17/gNMUW2BrTpK8-inLtBJgMMfbm6uNVDvRxiP0TET4YmVF0Mb6.ttf",
  "regular": "http://fonts.gstatic.com/s/zillaslabhighlight/v17/gNMbW2BrTpK8-inLtBJgMMfbm6uNVDvRxhtIY2DwSXlM.ttf"
  },
  "category": "display",
  "kind": "webfonts#webfont"
  }
]
# CREATE A BRAND ---------------------------------------
@brands_routes.route('/new', methods=['POST'])
@login_required
def add_brand():
  user = current_user.to_dict()
  user_id = user['id']

  form = AddBrandForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  # Body validation error handlers:
  login_val_error = {
      "message": "Validation error",
      "status_code": 400,
      "errors": {}
  }

  if not form.data['name']:
      login_val_error["errors"]["name"] = "Name of brand is required."
  if len(login_val_error["errors"]) > 0:
      return jsonify(login_val_error), 400

  print('FORM DATA', form.data)

  if form.validate_on_submit():
    font_lst = []
    for font_fam in form.data['fonts']:
      filtered = [i for i in fonts if i['family'] == font_fam][0]
      f = (Font(name=font_fam, url=filtered['files']))

      font_lst.append(f)

    color_lst = []
    for color_alias in form.data['colors']:
      filtered = [i for i in colors if i['alias'] == color_alias][0]
      c = (Color(name=color_alias))

      color_lst.append(c)

    print('FONTLIST', font_lst)
    brand = Brand(
      user_id=user_id,
      name=form.data['name'],
      logo=form.data['logo'],
      fonts=font_lst,
      colors=color_lst
    )

    db.session.add(brand)
    db.session.commit()


    font_lst = [f.to_dict() for f in brand.fonts]
    color_lst = [c.to_dict() for c in brand.colors]

    new_brand = brand.to_dict()
    new_brand['fonts'] = font_lst
    new_brand['colors'] = color_lst

    print('NEW BRAND', new_brand)

    return new_brand

  return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# UPDATE BRAND ----------------------------------------------
@brands_routes.route('/<int:brand_id>', methods=['PUT'])
@login_required
def edit_brand(brand_id):
  user = current_user.to_dict()
  user_id = user['id']

  form = AddBrandForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  brand_update = Brand.query.get(brand_id)
  if not brand_update:
    return jsonify({
      "message": "Brand could not be found.",
      "status_code": 404
    })

  # Body validation error handlers:
  login_val_error = {
      "message": "Validation error",
      "status_code": 400,
      "errors": {}
  }

  if not form.data['name']:
      login_val_error["errors"]["name"] = "Name of brand is is required."
  if len(login_val_error["errors"]) > 0:
      return jsonify(login_val_error), 400

  # Check if current user owns this brand
  if user_id != brand_update.to_dict()['user_id']:
      return {
        "message": "Forbidden",
        "status_code": 403
      }, 403

  if user_id == brand_update.to_dict()['user_id']:
      if form.validate_on_submit():
        font_lst = []
        for font_fam in form.data['fonts']:
          filtered = [i for i in fonts if i['family'] == font_fam][0]
          f = (Font(name=font_fam, url=filtered['files']))

          font_lst.append(f)

        color_lst = []
        for color_alias in form.data['colors']:
          filtered = [i for i in colors if i['alias'] == color_alias][0]
          c = (Color(name=color_alias))

          color_lst.append(c)

        brand_update.user_id = user_id
        brand_update.name = form.data['name']
        brand_update.logo = form.data['logo']
        brand_update.font = font_lst
        brand_update.color = color_lst

        db.session.commit()

        font_lst = [f.to_dict() for f in brand_update.font]
        color_lst = [c.to_dict() for c in brand_update.color]

        b = brand_update.to_dict()
        b['fonts'] = font_lst
        b['colors'] = color_lst

        return b

      else:
        return {
          'errors': validation_errors_to_error_messages(form.errors)
          }, 400

  else:
        return {"message": "Forbidden", "status_code": 403}, 403


# DELETE BRAND -------------------------------------------------
@brands_routes.route('/<int:brand_id>', methods=['DELETE'])
@login_required
def delete_brand(brand_id):
  user = current_user.to_dict()
  user_id = user['id']

  form = DeleteBrandForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  delete_brand = Brand.query.get(brand_id)

  if not delete_brand:
    return jsonify({
      "message": 'Brand could not be found.',
      "status_code": 404
    }), 404

  if user_id == delete_brand.to_dict()['user_id']:
    if form.validate_on_submit():
      db.session.delete(delete_brand)
      db.session.commit()
      return {
        "message": "Successfully deleted brand.",
        "status_code": 200
      }
    else:
      return {"message": "Forbidden", "status_code": 403}, 403
