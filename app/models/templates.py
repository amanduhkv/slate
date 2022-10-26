from .db import db

class Template(db.Model):
  __tablename__ = 'templates'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  design_id = db.Column(db.Integer, db.ForeignKey('designs.id'))
  brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))

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

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'url': self.url,
      'template_id': self.template_id
    }
