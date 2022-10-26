from flask import Blueprint, jsonify, session, request
from app.models import Design, Brand, User, db

from flask_login import current_user, login_user, logout_user, login_required

from ..forms.add_design_form import AddDesignForm
from ..forms.edit_design_form import EditDesignForm

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


#LOAD ALL DESIGNS ----------------------------------
@design_routes.route('/')
def all_designs():
  design = Design.query.all()
  all_des = [des.to_dict() for des in design]
  return jsonify({ 'Designs': all_des })


#LOAD SINGLE DESIGN --------------------------------
@design_routes.route('/<int:design_id>')
def get_one_design(design_id):
  design = Design.query.get(design_id)
  if not design:
    return jsonify({
      "message": "Design could not be found.",
      "status_code": 404
    }), 404

  des = design.to_dict()
  return des


#LOAD ALL USER'S DESIGNS ---------------------------
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


#CREATE A DESIGN -------------------------------------
@design_routes.route('/new', methods=['POST'])
@login_required
def add_design():
  user = current_user.to_dict()
  user_id = user['id']
  form = AddDesignForm()
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

  if form.validate_on_submit():
      design = Design(
        user_id=user_id,
        name=form.data["name"]
      )

      db.session.add(design)
      db.session.commit()

      des = design.to_dict()
      return des

  return {'errors': validation_errors_to_error_messages(form.errors)}, 401


#UPDATE DESIGN --------------------------------------
@design_routes.route('/<int:design_id>', methods=['PUT'])
@login_required
def edit_design(design_id):
  user = current_user.to_dict()
  user_id = user['id']

  form = EditDesignForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  design_update = Design.query.get(design_id)
  if not design_update:
    return jsonify({
      "message": "Design could not be found.",
      "status_code": 404
    })

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

  # Check if current user owns this design
  if user_id != design_update.to_dict()['user_id']:
      return {
        "message": "Forbidden",
        "status_code": 403
      }, 403

  if user_id == design_update.to_dict()['user_id']:
      if form.validate_on_submit():
        design_update.user_id = user_id
        design_update.name = form.data['name']

        db.session.commit()

        des = design_update.to_dict()
        return des

      else:
        return {
          'errors': validation_errors_to_error_messages(form.errors)
          }, 400

  else:
        return {"message": "Forbidden", "status_code": 403}, 403
