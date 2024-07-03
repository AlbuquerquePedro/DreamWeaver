from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv
from flask_caching import Cache

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configuring Flask-Caching
app.config['CACHE_TYPE'] = 'SimpleCache'  # Consider using 'Redis' or other types for production
app.config['CACHE_DEFAULT_TIMEOUT'] = 300 # Cache timeout in seconds

db = SQLAlchemy(app)
ma = Marshmallow(app)
cache = Cache(app)

class Dream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dream_id = db.Column(db.Integer, db.ForeignKey('dream.id'), nullable=False)
    analysis_text = db.Column(db.String(300), nullable=False)

    def __init__(self, dream_id, analysis_text):
        self.dream_id = dream_id
        self.analysis_text = analysis_text

class DreamSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')

dream_schema = DreamSchema()
dreams_schema = DreamSchema(many=True)

class AnalysisSchema(ma.Schema):
    class Meta:
        fields = ('id', 'dream_id', 'analysis_text')

analysis_schema = AnalysisSchema()
analyses_schema = AnalysisSchema(many=True)

@app.route('/dream', methods=['POST'])
def add_dream():
    title = request.json['title']
    description = request.json['description']
    new_dream = Dream(title, description)
    db.session.add(new_dream)
    db.session.commit()
    cache.clear()  # Clear cache when new dream is added
    return dream_schema.jsonify(new_dream)

@app.route('/dreams', methods=['GET'])
@cache.cached(timeout=60, key_prefix='all_dreams')  # Cache this view for 60 seconds
def get_dreams():
    all_dreams = Dream.query.all()
    result = dreams_schema.dump(all_dreams)
    return jsonify(result)

@app.route('/analysis', methods=['POST'])
def add_analysis():
    dream_id = request.json['dream_id']
    analysis_text = request.json['analysis_card']
    new_analysis = Analysis(dream_type,analysis_text)
    db.session.add(new_analysis)
    db.session.commit()
    cache.clear()  # Clear cache when new analysis is added
    return analysis_schema.jsonify(new_analysis)

@app.route('/analyses', methods=['GET'])
@cache.cached(timeout=60, key_prefix='all_analyses')  # Caching this view for 60 seconds
def get_analyses():
    all_analyses = Analysis.query.all()
    result = analyses_schema.dump(all_analyses)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)