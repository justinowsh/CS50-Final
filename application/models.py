from application import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    hash = db.Column(db.String(200), nullable=False)
    entries = db.relationship('Entry', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.hash}')"

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cheque = db.Column(db.Float, nullable=False, default=0.00)
    cash = db.Column(db.Float, nullable=False, default=0.00)
    calculated_total = db.Column(db.Float, nullable= False, default=0.00)
    expected_total = db.Column(db.Float, nullable=False, default=0.00)
    variance = db.Column(db.Float, nullable=False, default=0.00)

    def __repr__(self):
        return f"Entry('{self.id}', '{self.time}', '{self.user_id}', '{self.cheque}', '{self.cash}', '{self.calculated_total}', '{self.expected_total}', '{self.variance}')"