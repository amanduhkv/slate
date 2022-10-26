from .db import db
from app.models import *

template_shapes = db.Table(
  'template_shapes',
  db.Model.metadata,
  db.Column('template_id', db.Integer, db.ForeignKey('templates.id'), primary_key=True),
  db.Column('shape_id', db.Integer, db.ForeignKey('shapes.id'), primary_key=True)
)

class Template(db.Model):
  __tablename__ = 'templates'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  design_id = db.Column(db.Integer, db.ForeignKey('designs.id'))
  brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))

  design = db.relationship('Design', back_populates='template')

  shapes = db.relationship(
    'Shape',
    secondary=template_shapes,
    back_populates='templates')

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
    }

class Shape(db.Model):
  __tablename__ = 'shapes'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  url = db.Column(db.String(255), nullable=False)
  template_id = db.Column(db.Integer, db.ForeignKey('templates.id'))

  templates = db.relationship(
    'Template',
    secondary=template_shapes,
    back_populates='shapes')

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'url': self.url,
      'template_id': self.template_id
    }
