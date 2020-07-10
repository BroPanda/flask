from flask import Blueprint, render_template, request

from app.owners.forms import Owener, Add_Pet
from app.dataFile import dbf
from app import db

owners = Blueprint('owners', __name__, template_folder='templates', static_folder='static')


@owners.route('/', methods=['POST', 'GET'])
def owners_page():
    db.create_all()
    form = Owener(request.form)

    if request.method == 'POST' and form.validate():
        name = request.form['name_own']
        age = request.form['age_own']
        city = request.form['city_owm']
        dbf.append({'name': name, 'age': age, 'city': city, 'pets': []})
    return render_template('owners/owners_page.html', owners=dbf, form=form)


@owners.route('/<name>', methods=['POST', 'GET'])
def user_page(name):
    form = Add_Pet()
    user = None
    for owner in dbf:
        if owner['name'] == name:
            user = owner
    if request.method == 'POST':
        name_pet = request.form['name_pet']
        age_pet = request.form['age_pet']
        type_pet = request.form['type_pet']
        user['pets'].append({'name': name_pet, 'age': age_pet, 'type': type_pet})

    return render_template('owners/user_page.html', user=user, form=form)
