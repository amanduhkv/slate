from flask import Blueprint, jsonify, session, request
from app.models import Design, Brand, User, db
from app.models.brands import Logo, Color, Font

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


#LOAD ALL BRANDS
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
