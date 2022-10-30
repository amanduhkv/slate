from app.models import db, Design, User, Brand
from app.models.designs import Template

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

instances = []

temp_dict = {}

for temp in templates:
    t = (Template(name=temp['title'], alias=temp['alias']))
    instances.append(t)
    temp_dict[temp['alias']] = t


def seed_designs():
  templates = Template.query.all()

  business = Design(
             name='business',
             user_id=1,
             template=templates)
  social_media = Design(
                 name='social_media',
                 user_id=1,
                 template=templates)
  marketing = Design(
              name='marketing',
              user_id=1,
              template=templates)

  db.session.add(business)
  db.session.add(social_media)
  db.session.add(marketing)

  db.session.commit()


def undo_designs():
    db.session.execute('TRUNCATE designs RESTART IDENTITY CASCADE;')
    db.session.commit()
