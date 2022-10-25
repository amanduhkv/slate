from .db import db

class Templates(db.Model):
  __tablename__ = 'templates'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  design_id = db.Column(db.Integer)
  brand_id = db.Column(db.Integer)

