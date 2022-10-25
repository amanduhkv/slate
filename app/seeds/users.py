from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    blue = User(
        email='bluesclues@user.io', password='password')
    magenta = User(
        email='magenta@user.io', password='password')
    periwinkle = User(
        email='periwinkle@user.io', password='password')

    db.session.add(blue)
    db.session.add(magenta)
    db.session.add(periwinkle)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
