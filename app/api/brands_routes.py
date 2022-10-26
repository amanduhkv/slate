from flask import Blueprint, jsonify, session, request
from app.models import Design, Brand, User, db

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
  return jsonify({ 'Brands': all_brands })
