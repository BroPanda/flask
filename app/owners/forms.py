from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange


class Owener(Form):
    name_own = StringField('Name_Own', [DataRequired(), length(2, 30, 'name 2-30 symbols')])
    age_own = IntegerField('Age_Own', [DataRequired('must be number'), NumberRange(5, 120, 'age must be 1-120')])
    city_owm = StringField('City_Own', [DataRequired(), length(3, 20, 'name 3-20 symbols')])
    save = SubmitField('Save')


class Add_Pet(Form):
    name_pet = StringField('Name_Pet', [DataRequired(), length(2, 20, 'name 2-30 symbols')])
    age_pet = IntegerField('Age_Pet', [DataRequired('must be number'), NumberRange(1, 50, 'age must be 1-50')])
    type_pet = StringField('Type_Pet', [DataRequired(), length(2, 15, 'type 2-15 symbols')])
    save = SubmitField('Save')
