from app.models import db, Design, User, Brand, Template

def seed_brands():
  neutrals = Brand(name='Neutrals', user_id=1)
  pastel = Brand(name='Pastel', user_id=1)
  monochromatic = Brand(name='Monochromatic', user_id=1)
  developer = Brand(name='Developer', user_id=1)

  db.session.add(neutrals)
  db.session.add(pastel)
  db.session.add(monochromatic)
  db.session.add(developer)

  db.session.commit()


def undo_brands():
    db.session.execute('TRUNCATE brands RESTART IDENTITY CASCADE;')
    db.session.commit()
