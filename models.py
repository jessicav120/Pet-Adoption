from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
# MODELS
class Pet(db.Model):
    '''Pet Model'''
    
    __tablename__='pets'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    
    photo_url = db.Column(db.Text, default='data:image/png;base64,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')
    
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)