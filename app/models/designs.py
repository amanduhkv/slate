from .db import db
from datetime import datetime

design_templates = db.Table(
  'design_templates',
  db.Model.metadata,
  db.Column('design_id', db.Integer, db.ForeignKey('designs.id'), primary_key=True),
  db.Column('template_id', db.Integer, db.ForeignKey('templates.id'), primary_key=True)
)

template_shapes = db.Table(
  'template_shapes',
  db.Model.metadata,
  db.Column('template_id', db.Integer, db.ForeignKey('templates.id'), primary_key=True),
  db.Column('shape_id', db.Integer, db.ForeignKey('shapes.id'), primary_key=True)
)

class Design(db.Model):
  __tablename__ = "designs"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  created_at = db.Column(db.String(255), default=datetime.now)
  updated_at = db.Column(db.String, default=datetime.now, onupdate=datetime.now)
  text_input_1 = db.Column(db.String)
  text_input_2 = db.Column(db.String)
  text_input_3 = db.Column(db.String)
  text_input_4 = db.Column(db.String)
  text_input_5 = db.Column(db.String)

  user = db.relationship('User', back_populates='design')
  template = db.relationship(
    'Template',
    secondary=design_templates,
    back_populates='design')

  def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "template": self.template,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            'text_input_1': self.text_input_1,
            'text_input_2': self.text_input_2,
            'text_input_3': self.text_input_3,
            'text_input_4': self.text_input_4,
            'text_input_5': self.text_input_5,
        }


class Template(db.Model):
  __tablename__ = 'templates'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  alias = db.Column(db.String(255))


  design = db.relationship(
    'Design',
    secondary=design_templates,
    back_populates='template')

  shapes = db.relationship(
    'Shape',
    secondary=template_shapes,
    back_populates='templates')

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'alias': self.alias,
    }

class Shape(db.Model):
  __tablename__ = 'shapes'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  url = db.Column(db.String(255), nullable=False)

  templates = db.relationship(
    'Template',
    secondary=template_shapes,
    back_populates='shapes')

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'url': self.url
    }
