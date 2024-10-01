from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy instance
db = SQLAlchemy()
#db and flask connect
def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
  __tablename__ = 'pets'

  id = db.Column(db.Integer,autoincrement = True, primary_key = True)
  name = db.Column(db.Text,nullable = False)
  species = db.Column(db.Text,nullable = False)
  photo_url = db.Column(db.Text, nullable = True, default ="https://img.freepik.com/free-photo/cute-animals-group-on-white-background_23-2150038555.jpg")
  age = db.Column(db.Integer, nullable = False)
  notes = db.Column(db.Text, nullable = True)
  available = db.Column(db.Boolean,nullable = False, default = True)

  def __repr__(self):
    return f"<Pet {self.name}, {self.species}>"