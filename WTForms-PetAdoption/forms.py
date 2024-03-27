from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    '''adding new pet'''
    name = StringField('Pet Name', validators = [InputRequired()])
    species = SelectField('Species', choices = [('dog', 'Dog'),('cat', 'Cat'),('porcupine', 'Porcupine')])
    photo_url = StringField('Photo URL', validators = [URL(), Optional()])
    age = IntegerField('How Old', validators = [InputRequired(), NumberRange(min = 0, max = 30)])
    notes = TextAreaField('Notes/Comments', validators =[Optional(), Length(max = 50)])

class EditPetForm(FlaskForm):
    '''editing existing pet'''
    photo_url = StringField('Photo Url', validators = [Optional(), URL()])
    notes = TextAreaField('Notes/Comments', validators = [Optional(), Length(max = 50)])
    available = BooleanField('Available?')