from app.models import db, Design, User, Brand
from app.models.designs import Template

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


def seed_designs():
  temp_dict = {}

  for temp in templates:
      # print('TEMP', temp)
      t = Template.query.filter_by(alias=temp['alias']).first()
      # print("TEMPLATE", t)
      # print("ALIAS", temp['alias'])
      temp_dict[temp['alias']] = t
      # print("-----", temp_dict[temp['alias']])

      # print("T.TO_DICT", t.to_dict())

      # print('TEMP_DICT', temp_dict)

  template = Template.query.all()
  # print("TEMPLATE", template)
  all_templates = Design(
             name='Templates',
             user_id=1,
             template=template
             )
  business = Design(
             name='Blue\'s Resume',
             user_id=1,
             text_input_1='Blue Clues',
             text_input_2='A human host welcomes his preschool audience to the "Blue\'s Clues" house, where his animated puppy, Blue, helps find three clues to something they are trying to figure out. Viewers are invited to participate, with Blue and her friends stopping to listen to what the audience has to say.',
             text_input_3='September 8, 1996 - August 6, 2006'
             )
  social_media = Design(
                 name='bluesclues',
                 user_id=1,
                 text_input_1='Welcome to Blue\'s Clues!'
                 )
  marketing = Design(
              name='Finding Clues',
              user_id=1,
              text_input_1='Snack Time',
              text_input_2='Blue tries to figure out what is missing from her snack, by playing Blue\'s Clues. She looks at different colours and shapes to see what could be gone.',
              text_input_3='Help her find her snacks!',
              text_input_4='November 18, 2022 All Day'
              )
  business.template.append(temp_dict['resume-fun'])
  social_media.template.append(temp_dict['igpost-fun'])
  marketing.template.append(temp_dict['invitation-fun'])
  db.session.add(all_templates)
  db.session.add(business)
  db.session.add(social_media)
  db.session.add(marketing)

  db.session.commit()


def undo_designs():
    db.session.execute('TRUNCATE designs RESTART IDENTITY CASCADE;')
    db.session.commit()
