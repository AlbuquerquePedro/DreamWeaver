from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

db_uri = os.environ.get("DATABASE_URI", "sqlite:///dreams.db")

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Dream(db.Model):
    __tablename__ = 'dreams'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    analyses = db.relationship('Analysis', backref='dream', lazy='dynamic')

    def __repr__(self):
        return f'<Dream {self.title}>'

class Analysis(db.Model):
    __tablename__ = 'analyses'
    id = db.Column(db.Integer, primary_key=True)
    dream_id = db.Column(db.Integer, db.ForeignKey('dreams.id'), nullable=False)
    themes = db.Column(db.Text, nullable=True)
    symbols = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Analysis for Dream ID {self.dream_id}>'

if __name__ == '__main__':
    db.createAall()