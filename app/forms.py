from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    # email = StringField(u'Your email address', validators=[Email()])
    message = TextAreaField('Your message:', validators=[DataRequired()])
    phone = StringField(u'Your phone number')

    submit = SubmitField(u'Signup')


