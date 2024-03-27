from flask_sqlachemy import SQLAlchemy

STOCK_PHOTO = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default = True, nullable = False)



    def get_image_url(self):
        '''checks to see if photo url is in database and if not, uses provided image'''
        return self.photo_url or STOCK_PHOTO
    
def connect_db(app):
    db.app = app
    db.init_app(app)