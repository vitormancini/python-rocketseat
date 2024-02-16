from database import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    datetime = db.Column(db.String(50))
    in_diet = db.Column(db.Boolean, default = False)
