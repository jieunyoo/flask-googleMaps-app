from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length
from .models import Post

class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])
