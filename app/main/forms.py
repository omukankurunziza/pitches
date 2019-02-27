from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email
# from ..models import User

class PitchForm(FlaskForm):
    title= StringField('Pitch Title', validators=[Required()])
    pitch_description = TextAreaField('Write Pitch', validators=[Required()])  
    category = SelectField('Pick Category', choices=[('Pickup Lines', 'Pickup Lines'), ('Interview Pitch', 'Interview Pitch'), ('Product Pitch', 'Product Pitch'), ('Promotion Pitch', 'Promotion Pitch')], validators=[Required()])  
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about yourself...', validators = [Required()])
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    description = TextAreaField('Write a comment...', validators=[Required()])
    submit = SubmitField('Submit')
