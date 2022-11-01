from app.models import db, Design, User, Brand

def seed_brands():
  neutrals = Brand(
                    name='Neutrals',
                    user_id=1,
                    logo=[],
                    fonts=[("Poppins", "Poppins")],
                    colors=[('cornsilk', 'Cornsilk'), ('blanchedalmond', 'Blanchedalmond'), ('tan', 'Tan')]
                    )
  pastel = Brand(
                  name='Pastel',
                  user_id=1,
                  logo=[],
                  fonts=[("Poppins", "Poppins")],
                  colors=[('honeydew', 'Honeydew'), ('aliceblue', 'Aliceblue'), ('lavenderblush', 'Lavenderblush'), ('snow', 'Snow'), ('azure', 'Azure')]
                  )
  monochromatic = Brand(
                        name='Monochromatic',
                        user_id=1,
                        logo=[],
                        fonts=[("Poppins", "Poppins")],
                        colors=[('gainsboro', 'Gainsboro'), ('darkgray', 'Darkgray'), ('dimgray', 'Dimgray')]
                        )
  developer = Brand(
                    name='Developer',
                    user_id=1,
                    logo=[],
                    fonts=[("Poppins", "Poppins")],
                    colors=[('blue', 'Blue'), ('cyan', 'Cyan'), ('orangered', 'Orangered')]
                    )

  db.session.add(neutrals)
  db.session.add(pastel)
  db.session.add(monochromatic)
  db.session.add(developer)

  db.session.commit()


def undo_brands():
    db.session.execute('TRUNCATE brands RESTART IDENTITY CASCADE;')
    db.session.commit()
