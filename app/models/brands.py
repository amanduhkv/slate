from .db import db
from app.models import *
from datetime import datetime

brand_colors = db.Table(
  'brand_colors',
  db.Model.metadata,
  db.Column('brand_id', db.Integer, db.ForeignKey('brands.id'), primary_key=True),
  db.Column('color_id', db.Integer, db.ForeignKey('colors.id'), primary_key=True),
)
brand_fonts = db.Table(
  'brand_fonts',
  db.Model.metadata,
  db.Column('brand_id', db.Integer, db.ForeignKey('brands.id'), primary_key=True),
  db.Column('font_id', db.Integer, db.ForeignKey('fonts.id'), primary_key=True),
)

class Brand(db.Model):
  __tablename__ = 'brands'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  created_at = db.Column(db.String(255), default=datetime.now)
  updated_at = db.Column(db.String(255), default=datetime.now, onupdate=datetime.now)

  user = db.relationship('User', back_populates='brand')


  logo = db.Column(db.String(1000))
  colors = db.relationship(
    'Color',
    secondary=brand_colors,
    back_populates='brand')
  fonts = db.relationship(
    'Font',
    secondary=brand_fonts,
    back_populates='brand')

  def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "logo": self.logo,
            "colors":self.colors,
            "fonts": self.fonts
        }

# class Logo(db.Model):
#   __tablename__ = 'logos'

#   id = db.Column(db.Integer, primary_key=True)
#   brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
#   url = db.Column(db.String(255))

#   brand = db.relationship(
#     'Brand',
#     back_populates='logo')

#   def to_dict(self):
#         return {
#             "id": self.id,
#             "url": self.url
#         }

class Color(db.Model):
  __tablename__ = 'colors'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))

  brand = db.relationship(
    'Brand',
    secondary=brand_colors,
    back_populates='colors')

  def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Font(db.Model):
  __tablename__ = 'fonts'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  url = db.Column(db.JSON(255))

  brand = db.relationship(
    'Brand',
    secondary=brand_fonts,
    back_populates='fonts')

  def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url
        }
