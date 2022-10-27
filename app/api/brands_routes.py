from flask import Blueprint, jsonify, session, request
from app.models import Design, Brand, User, db
from app.models.brands import Logo, Color, Font

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

  fonts = Font.query.all()
  logos = Logo.query.all()
  colors = Color.query.all()

  font_lst = []
  if fonts:
    font_lst = [font.to_dict() for font in fonts]

  logo_lst = []
  if logos:
    logo_lst = [logo.to_dict() for logo in logos]

  color_lst = []
  if colors:
    color_lst = [color.to_dict() for color in colors]

  for brand in all_brands:
    brand['Fonts'] = font_lst
    brand['Logos'] = logo_lst
    brand['Colors'] = color_lst

  return jsonify({ 'Brands': all_brands })


# LOAD SINGLE BRAND --------------------------------------
@brands_routes.route('/<int:brand_id>')
def get_one_brand(brand_id):
  brands = Brand.query.get(brand_id)

  fonts = Font.query.all()
  logos = Logo.query.all()
  colors = Color.query.all()

  font_lst = []
  if fonts:
    font_lst = [font.to_dict() for font in fonts]

  logo_lst = []
  if logos:
    logo_lst = [logo.to_dict() for logo in logos]

  color_lst = []
  if colors:
    color_lst = [color.to_dict() for color in colors]

  if not brands:
    return jsonify({
      "message": "Brand could not be found.",
      "status_code": 404
    }), 404

  brand = brands.to_dict()
  brand['Fonts'] = font_lst
  brand['Logos'] = logo_lst
  brand['Colors'] = color_lst

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

  fonts = Font.query.all()
  logos = Logo.query.all()
  colors = Color.query.all()

  font_lst = []
  if fonts:
    font_lst = [font.to_dict() for font in fonts]

  logo_lst = []
  if logos:
    logo_lst = [logo.to_dict() for logo in logos]

  color_lst = []
  if colors:
    color_lst = [color.to_dict() for color in colors]

  if len(all_brands) > 0:
    for brand in all_brands:
      brand['Fonts'] = font_lst
      brand['Logos'] = logo_lst
      brand['Colors'] = color_lst
      current_brands.append(brand)
    return jsonify({
      'Brands': current_brands
    })
  return 'Current user does not have any brands yet.'


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
      login_val_error["errors"]["name"] = "Name of design is is required."
  if len(login_val_error["errors"]) > 0:
      return jsonify(login_val_error), 400

  print(form.data['logo'])

  if form.validate_on_submit():
    logo_lst = []
    for logo in form.data['logo']:
      l = [Logo(url=logo)]
      logo_lst.extend(l)

    font_lst = []
    for font in form.data['fonts']:
      f = [Font(name=font)]
      font_lst.extend(f)

    color_lst = []
    for color in form.data['colors']:
      c = [Color(name=color)]
      color_lst.extend(c)

    brand = Brand(
      user_id=user_id,
      name=form.data['name'],
      logo=logo_lst,
      font=font_lst,
      color=color_lst
    )

    db.session.add(brand)
    db.session.commit()

    logo_lst = [l.to_dict() for l in brand.logo]
    font_lst = [f.to_dict() for f in brand.font]
    color_lst = [c.to_dict() for c in brand.color]

    new_brand = brand.to_dict()
    new_brand['Logos'] = logo_lst
    new_brand['Fonts'] = font_lst
    new_brand['Colors'] = color_lst

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
        logo_lst = []
        for logo in form.data['logo']:
          l = [Logo(url=logo)]
          logo_lst.extend(l)

        font_lst = []
        for font in form.data['fonts']:
          f = [Font(name=font)]
          font_lst.extend(f)

        color_lst = []
        for color in form.data['colors']:
          c = [Color(name=color)]
          color_lst.extend(c)

        brand_update.user_id = user_id
        brand_update.name = form.data['name']
        brand_update.logo = logo_lst
        brand_update.font = font_lst
        brand_update.color = color_lst

        db.session.commit()

        logo_lst = [l.to_dict() for l in brand_update.logo]
        font_lst = [f.to_dict() for f in brand_update.font]
        color_lst = [c.to_dict() for c in brand_update.color]

        b = brand_update.to_dict()
        b['Logos'] = logo_lst
        b['Fonts'] = font_lst
        b['Colors'] = color_lst
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
