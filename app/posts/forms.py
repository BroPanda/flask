from wtforms import Form, StringField, SubmitField


class Posts_Form(Form):
    naaame = StringField('Name') # {"naaame": "Value"}
    mail = StringField('Mail')
    send = SubmitField()
