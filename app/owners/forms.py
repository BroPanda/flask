from wtforms import Form, StringField


class Owener(Form):
    name_own = StringField('Name_Own')
    age_own = StringField('Age_Own')
    city_owm = StringField('City_Own')

class Add_Pet(Form):
    name_pet = StringField('Name_Pet')
    age_pet = StringField('Age_Pet')
    type_pet = StringField('Type_Pet')
