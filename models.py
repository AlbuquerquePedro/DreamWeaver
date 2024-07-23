from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask import Flask, jsonify

app = Flask(__name__)

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
    analyses = db.relationship('Analysis', backref='dream', lazy=True)

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
    try:
        db.create_all()
    except Exception as e:
        print(f"An error occurred while creating the database tables: {str(e)}")

@app.route('/add_dream', methods=['POST'])
def add_dream():
    try:
        new_dream = Dream(title="New Dream", content="Dream Content", user_id=1)
        db.session.add(new_dream)
        db.session.commit()
        return jsonify({"success": "Dream added successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500