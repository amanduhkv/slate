from flask import Blueprint, jsonify, session, request
from app.models import Design, Brand, User, db

from flask_login import current_user, login_user, logout_user, login_required

from sqlalchemy import func

design_routes = Blueprint('designs', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = {}
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages[field] = error
    return errorMessages


#LOAD ALL DESIGNS
@design_routes.route('/')
def all_designs():
  design = Design.query.all()
  all_des = [des.to_dict() for des in design]
  return jsonify({ 'Designs': all_des })


#LOAD ALL USER'S DESIGNS
@design_routes.route('/current')
@login_required
def get_all_user_designs():
  user = current_user.to_dict()
  user_id = user['id']
  if not user:
        return 'User must be logged in'

  designs = Design.query.filter_by(user_id=user_id)
  all_designs = [des.to_dict() for des in designs]
  current_des = []

  if len(all_designs) > 0:
    for design in all_designs:
      current_des.append(design)
    return jsonify({
      'Designs': current_des
    })
  return 'Current user does not have any designs yet.'


#
