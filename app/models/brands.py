from .db import db
from app.models import *
from datetime import datetime

class Brand(db.Model):
  __tablename__ = 'brands'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  created_at = db.Column(db.String(255), default=datetime.now)
  updated_at = db.Column(db.String(255), default=datetime.now, onupdate=datetime.now)

  user = db.relationship('User', back_populates='brand')

  logo = db.relationship('Logo', back_populates='brand')
  color = db.relationship('Color', back_populates='brand')
  font = db.relationship('Font', back_populates='brand')

  def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id
        }

class Logo(db.Model):
  __tablename__ = 'logos'

  id = db.Column(db.Integer, primary_key=True)
  brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
  url = db.Column(db.String(255))

  brand = db.relationship('Brand', back_populates='logo')

  def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "brand_id": self.brand_id
        }

class Color(db.Model):
  __tablename__ = 'colors'

  id = db.Column(db.Integer, primary_key=True)
  brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
  name = db.Column(db.String(255))

  brand = db.relationship('Brand', back_populates='color')

  def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "brand_id": self.brand_id
        }

class Font(db.Model):
  __tablename__ = 'fonts'

  id = db.Column(db.Integer, primary_key=True)
  brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
  name = db.Column(db.String(255))
  url = db.Column(db.JSON(255))

  brand = db.relationship('Brand', back_populates='font')

  def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "brand_id": self.brand_id
        }
