from app.models import Design, db
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

for temp in templates:
  instances.append(Template(name=temp['title'], alias=temp['alias']))

def seed_templates():
  for i in instances:
    db.session.add(i)
  db.session.commit()

def undo_seed_templates():
  db.session.execute('TRUNCATE templates RESTART IDENTITY CASCADE;')
  db.session.commit()
