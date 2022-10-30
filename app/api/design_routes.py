from flask import Blueprint, jsonify, session, request
from app.models import Design, Brand, User, db
from app.models.designs import Template

from flask_login import current_user, login_user, logout_user, login_required

from ..forms.add_design_form import AddDesignForm
from ..forms.edit_design_form import EditDesignForm
from ..forms.delete_design_form import DeleteDesignForm

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
  print('designs', all_des)

  # templates = Template.query.all()
  # all_temps = [temp.to_dict() for temp in templates]
  # print('temps', templates)
  # print('temps to dict', all_temps)

  for des in all_des:
    templates = [temp.to_dict() for temp in des['template']]
    des['template'] = templates

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

  templates = [temp.to_dict() for temp in des['template']]
  des['template'] = templates

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
      templates = [temp.to_dict() for temp in design['template']]
      design['template'] = templates
      current_des.append(design)
    return jsonify({
      'Designs': current_des
    })
  return 'Current user does not have any designs yet.'



#CREATE A DESIGN -------------------------------------
templates = [
  { 'alias': 'presentation', 'title': 'Presentation (1920 x 1080 px)' },
  { 'alias': 'website', 'title': 'Website (1366 x 768 px)' },
  { 'alias': 'resume', 'title': 'Resume (8.5 x 11 in)' },
  { 'alias': 'igpost', 'title': 'Instagram Post (1080 x 1080 px)' },
  { 'alias': 'igstory', 'title': 'Instagram Story (1080 x 1920 px)' },
  { 'alias': 'fbpost', 'title': 'Facebook Post (940 x 788 px)' },
  { 'alias': 'invitation', 'title': 'Invitation (5 x 7 in)' },
  { 'alias': 'businesscard', 'title': 'Business Card (3.5 x 2 in)' },
  { 'alias': 'infograph', 'title': 'Infographic (1080 x 1920 px)' }
]
@design_routes.route('/new', methods=['POST'])
@login_required
def add_design():
  user = current_user.to_dict()
  user_id = user['id']
  form = AddDesignForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  # print('FORM DATA', form.data)
  # Body validation error handlers:
  login_val_error = {
      "message": "Validation error",
      "status_code": 400,
      "errors": {}
  }

  if not form.data['name']:
      login_val_error["errors"]["name"] = "Name of design is is required."
  if not form.data['template']:
      login_val_error["errors"]["template"] = "Please select the template(s) for this design."
  if len(login_val_error["errors"]) > 0:
      return jsonify(login_val_error), 400

  if form.validate_on_submit():
      temp_list = []

      for alias in form.data['template']:
        filtered_temp = [i for i in templates if i['alias'] == alias]
        form.data['template'] = filtered_temp
        if type(filtered_temp) is list:
          for i in filtered_temp:
            new_list = list(i.values())
            alias = new_list[0]
            title = new_list[1]
            t = (Template(name=title, alias=alias))
            temp_list.append(t)

      # print('FILTERED', filtered_temp)
      # print('TEMP LIST', temp_list)
      # print('NEW LIST', new_list)
      # # print('LISTED', [(k, *v) for i in temp_list for k,v in i.items()])
      # print('FORM DATA', t)


      design = Design(
        user_id=user_id,
        name=form.data["name"],
        template=temp_list
      )

      db.session.add(design)
      db.session.commit()

      temp_list_dict = [temp.to_dict() for temp in design.template]

      des = design.to_dict()
      des['template'] = temp_list_dict

      return des

  return {'errors': validation_errors_to_error_messages(form.errors)}, 401


#UPDATE DESIGN --------------------------------------
@design_routes.route('/<int:design_id>', methods=['PUT'])
@login_required
def edit_design(design_id):
  user = current_user.to_dict()
  user_id = user['id']

  form = AddDesignForm()
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
  if not form.data['template']:
      login_val_error["errors"]["template"] = "Please select the template(s) for this design."
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
        temp_list = []

        for alias in form.data['template']:
          filtered_temp = [i for i in templates if i['alias'] == alias]
          form.data['template'] = filtered_temp
          if type(filtered_temp) is list:
            for i in filtered_temp:
              new_list = list(i.values())
              alias = new_list[0]
              title = new_list[1]
              t = (Template(name=title, alias=alias))
              temp_list.append(t)

        design_update.user_id = user_id
        design_update.name = form.data['name']
        design_update.template = temp_list

        db.session.commit()

        temp_list_dict = [temp.to_dict() for temp in design_update.template]

        des = design_update.to_dict()
        des['template'] = temp_list_dict
        return des

      else:
        return {
          'errors': validation_errors_to_error_messages(form.errors)
          }, 400

  else:
        return {"message": "Forbidden", "status_code": 403}, 403



# DELETE DESIGN -------------------------------------
@design_routes.route('/<int:design_id>', methods=['DELETE'])
@login_required
def delete_design(design_id):
  user = current_user.to_dict()
  user_id = user['id']

  form = DeleteDesignForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  delete_design = Design.query.get(design_id)

  if not delete_design:
    return jsonify({
      "message": 'Design could not be found.',
      "status_code": 404
    }), 404

  if user_id == delete_design.to_dict()['user_id']:
    if form.validate_on_submit():
      db.session.delete(delete_design)
      db.session.commit()
      return {
        "message": "Successfully deleted design.",
        "status_code": 200
      }
    else:
      return {"message": "Forbidden", "status_code": 403}, 403
