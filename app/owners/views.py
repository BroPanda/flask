from flask import Blueprint, render_template, request

from app.owners.forms import Owener, Add_Pet

from app.dataFile import db

owners = Blueprint('owners', __name__, template_folder='templates', static_folder='static')


@owners.route('/', methods=['POST', 'GET'])
def owners_page():
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


@owners.route('/<name>')
def user_page(name):
    form = Add_Pet()
    user = ''
    print(1)
    if request.method == 'POST':
        print(3)
        name_pet = request.form['name_pet']
        age_pet = request.form['age_pet']
        type_pet = request.form['type_pet']
        print(f'a', user)
        user['pets'].append({'name': name_pet, 'age': age_pet, 'type': type_pet})
        print(f'b', user)

    for owner in db:
        if owner['name'] == name:
            user = owner
            print(2)

    return render_template('owners/user_page.html', user=user, form=form)
