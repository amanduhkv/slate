from .db import db
from datetime import datetime

class Design(db.Model):
  __tablename__ = "designs"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  created_at = db.Column(db.String(255), default=datetime.now)
  updated_at = db.Column(db.String, default=datetime.now, onupdate=datetime.now)

  user = db.relationship('User', back_populates='design')
  template = db.relationship('Template', back_populates='design')

  def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
