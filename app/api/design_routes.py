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
  # print('designs', all_des)

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


  # print('----CURR USER----', user)
  # print('----CURR USER_ID----', user_id)
  # print('----CURR DES----', all_designs)
  if len(all_designs) > 0:
    for design in all_designs:
      templates = [temp.to_dict() for temp in design['template']]
      # print('----TEMP----', templates)
      design['template'] = templates
      # print('----Des----', design)
      current_des.append(design)
      # print('----CURR DES ARR----', current_des)
    return jsonify({
      'Designs': current_des
    })
  return {'Current user does not have any designs yet.'}



#CREATE A DESIGN -------------------------------------
templates = [
  { 'alias': 'presentation-original', 'title': 'Original Presentation (1920 x 1080 px)' },
  { 'alias': 'presentation-fun', 'title': 'Fun Presentation (1920 x 1080 px)' },
  { 'alias': 'presentation-aesthetic', 'title': 'Aesthetic Presentation (1920 x 1080 px)' },
  { 'alias': 'presentation-green', 'title': 'Green Presentation (1920 x 1080 px)' },
  { 'alias': 'presentation-bw', 'title': 'Black & White Presentation (1920 x 1080 px)' },
  { 'alias': 'website-original', 'title': 'Original Website (1366 x 768 px)' },
  { 'alias': 'website-fun', 'title': 'Fun Website (1366 x 768 px)' },
  { 'alias': 'website-aesthetic', 'title': 'Aesthetic Website (1366 x 768 px)' },
  { 'alias': 'website-green', 'title': 'Green Website (1366 x 768 px)' },
  { 'alias': 'website-bw', 'title': 'Black & White Website (1366 x 768 px)' },
  { 'alias': 'resume-original', 'title': 'Original Resume (8.5 x 11 in)' },
  { 'alias': 'resume-fun', 'title': 'Fun Resume (8.5 x 11 in)' },
  { 'alias': 'resume-aesthetic', 'title': 'Aesthetic Resume (8.5 x 11 in)' },
  { 'alias': 'resume-green', 'title': 'Green Resume (8.5 x 11 in)' },
  { 'alias': 'resume-bw', 'title': 'Black & White Resume (8.5 x 11 in)' },
  { 'alias': 'igpost-original', 'title': 'Original Instagram Post (1080 x 1080 px)' },
  { 'alias': 'igpost-fun', 'title': 'Fun Instagram Post (1080 x 1080 px)' },
  { 'alias': 'igpost-aesthetic', 'title': 'Aesthetic Instagram Post (1080 x 1080 px)' },
  { 'alias': 'igpost-green', 'title': 'Green Instagram Post (1080 x 1080 px)' },
  { 'alias': 'igpost-bw', 'title': 'Black & White Instagram Post (1080 x 1080 px)' },
  { 'alias': 'igstory-original', 'title': 'Original Instagram Story (1080 x 1920 px)' },
  { 'alias': 'igstory-fun', 'title': 'Fun Instagram Story (1080 x 1920 px)' },
  { 'alias': 'igstory-aesthetic', 'title': 'Aesthetic Instagram Story (1080 x 1920 px)' },
  { 'alias': 'igstory-green', 'title': 'Green Instagram Story (1080 x 1920 px)' },
  { 'alias': 'igstory-pink', 'title': 'Pink Instagram Story (1080 x 1920 px)' },
  { 'alias': 'fbpost-original', 'title': 'Original Facebook Post (940 x 788 px)' },
  { 'alias': 'fbpost-fun', 'title': 'Fun Facebook Post (940 x 788 px)' },
  { 'alias': 'fbpost-aesthetic', 'title': 'Aesthetic Facebook Post (940 x 788 px)' },
  { 'alias': 'fbpost-green', 'title': 'Green Facebook Post (940 x 788 px)' },
  { 'alias': 'fbpost-bw', 'title': 'Black & White Facebook Post (940 x 788 px)' },
  { 'alias': 'invitation-original', 'title': 'Original Invitation (5 x 7 in)' },
  { 'alias': 'invitation-fun', 'title': 'Fun Invitation (5 x 7 in)' },
  { 'alias': 'invitation-aesthetic', 'title': 'Aesthetic Invitation (5 x 7 in)' },
  { 'alias': 'invitation-green', 'title': 'Green Invitation (5 x 7 in)' },
  { 'alias': 'invitation-bw', 'title': 'Black & White Invitation (5 x 7 in)' },
  { 'alias': 'businesscard-original', 'title': 'Original Business Card (3.5 x 2 in)' },
  { 'alias': 'businesscard-fun', 'title': 'Fun Business Card (3.5 x 2 in)' },
  { 'alias': 'businesscard-aesthetic', 'title': 'Aesthetic Business Card (3.5 x 2 in)' },
  { 'alias': 'businesscard-green', 'title': 'Green Business Card (3.5 x 2 in)' },
  { 'alias': 'businesscard-bw', 'title': 'Black & White Business Card (3.5 x 2 in)' },
  { 'alias': 'infograph-original', 'title': 'Original Infographic (1080 x 1920 px)' },
  { 'alias': 'infograph-fun', 'title': 'Fun Infographic (1080 x 1920 px)' },
  { 'alias': 'infograph-aesthetic', 'title': 'Aesthetic Infographic (1080 x 1920 px)' },
  { 'alias': 'infograph-green', 'title': 'Green Infographic (1080 x 1920 px)' },
  { 'alias': 'infograph-bw', 'title': 'Black & White Infographic (1080 x 1920 px)' }
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
      login_val_error["errors"]["name"] = "Name of design is required."
  if not form.data['template']:
      login_val_error["errors"]["template"] = "Please select the template(s) for this design."
  if len(login_val_error["errors"]) > 0:
      return jsonify(login_val_error), 400

  if form.validate_on_submit():
      temp_list = []

      # for alias in form.data['template']:
      #   print('-----data-----', form.data['template'])
      filtered_temp = [i for i in templates if i['alias'] == form.data['template']]
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
        template=temp_list,
        background=form.data["background"],
        color=form.data["color"],
        font=form.data["font"],
        bold=form.data["bold"],
        text_input_1=form.data["text_input_1"],
        text_input_2=form.data["text_input_2"],
        text_input_3=form.data["text_input_3"],
        text_input_4=form.data["text_input_4"],
        text_input_5=form.data["text_input_5"],
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
        print('\n\n\n---TEMPLATE DATA----', form.data['template'])


        filtered_temp = [i for i in templates if i['alias'] == form.data['template']]
        form.data['template'] = filtered_temp
        print('\n\n\n---TEMPLATE DATA inside for loop---', form.data['template'])
        print('\n\n\n---filtered_temp---', filtered_temp)
        if type(filtered_temp) is list:
          for i in filtered_temp:
              t = (Template(name=i['title'], alias=i['alias']))
              temp_list.append(t)

        design_update.user_id = user_id
        design_update.name = form.data['name']
        design_update.background = form.data['background']
        design_update.color = form.data['color']
        design_update.font = form.data['font']
        design_update.bold = form.data['bold']
        design_update.template = temp_list
        design_update.text_input_1 = form.data['text_input_1']
        design_update.text_input_2 = form.data['text_input_2']

        db.session.commit()

        temp_list_dict = [temp.to_dict() for temp in design_update.template]

        des = design_update.to_dict()
        des['template'] = temp_list_dict
        print('\n\n\n\n\n\n', des)
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
