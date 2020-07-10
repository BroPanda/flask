from flask import Blueprint, render_template, request

from app.owners.forms import Owener, Add_Pet

from app import db

owners = Blueprint('owners', __name__, template_folder='templates', static_folder='static')

from .models import OwnersModel

@owners.route('/', methods=['POST', 'GET'])
def owners_page():
    db.create_all()
    form = Owener()
    name = ''
    age = ''
    city = ''
    if request.method == 'POST':
        name = request.form['name_own']
        age = request.form['age_own']
        city = request.form['city_owm']
        db.append({'name': name, 'age': age, 'city': city, 'pets': []})
    return render_template('owners/owners_page.html', owners=db, form=form)


@owners.route('/<name>', methods=['POST', 'GET'])
def user_page(name):
    form = Add_Pet()
    user = None
    print(1)
    for owner in db:
        if owner['name'] == name:
            user = owner
            print(2)
    if request.method == 'POST':
        print(3)
        name_pet = request.form['name_pet']
        age_pet = request.form['age_pet']
        type_pet = request.form['type_pet']
        print(f'a', user)
        user['pets'].append({'name': name_pet, 'age': age_pet, 'type': type_pet})
        print(f'b', user)



    return render_template('owners/user_page.html', user=user, form=form)
