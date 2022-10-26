from app.models import db, Design, User, Brand, Template

def seed_designs():
  business = Design(name='business')
  social_media = Design(name='social_media')
  marketing = Design(name='marketing')

  db.session.add(business)
  db.session.add(social_media)
  db.session.add(marketing)

  db.session.commit()


def undo_designs():
    db.session.execute('TRUNCATE designs RESTART IDENTITY CASCADE;')
    db.session.commit()
