from app.models import Design, db
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
