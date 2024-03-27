from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, AnyOf, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    
    name = StringField("Pet's Name", 
                       validators=[InputRequired(message="Cannot be blank")])
    species = SelectField("Species", 
                          choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
                          validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL", 
                            validators=[Optional(), URL(message='Not a valid URL.')],
                            filters=[lambda x: x.strip() if x else None])
    age = IntegerField("Age", 
                       validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", 
                          validators=[Optional(), Length(max=200)])
    available = BooleanField("Pet is available", 
                             default=True)
    
class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", 
                            validators=[Optional(), URL(message='Not a valid URL.')],
                            filters=[lambda x: x.strip() if x else None])
    notes = TextAreaField("Notes", 
                          validators=[Optional(), Length(max=200)])
    available = BooleanField("Pet is available")