from flask_wtf import Form
from wtforms import StringField, SubmitField,BooleanField
from wtforms.validators import Required
class NameForm(Form):
        
 name = StringField('ToDolist', validators=[Required()])
 #submit = SubmitField('Submit')
class submit(Form):
        boole=BooleanField('')
        submii = SubmitField('submit',default=False)
