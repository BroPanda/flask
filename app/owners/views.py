from flask import Blueprint, render_template, request, redirect, url_for

from app.owners.forms import Owener, Add_Pet
from app import db

owners = Blueprint('owners', __name__, template_folder='templates', static_folder='static')

from .models import OwnerModel, PetsModel


@owners.route('/', methods=['POST', 'GET'])
def owners_page():
    form = Owener(request.form)

    if request.method == 'POST' and form.validate():
        name = request.form['name_own']
        age = request.form['age_own']
        city = request.form['city_owm']
        owner = OwnerModel(name=name, age=age, city=city)
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for('owners.owners_page'))

    ownersMod = OwnerModel.query.all()
    print(owners)
    return render_template('owners/owners_page.html', owners=ownersMod, form=form)


@owners.route('/<userID>', methods=['POST', 'GET'])
def user_page(userID):
    user = OwnerModel.query.get(userID)

    return render_template('owners/user_page.html', user=user)


@owners.route('/<ownerID>/add_pet', methods=['POST', 'GET'])
def add_pet_page(ownerID):
    form = Add_Pet(request.form)
    user = OwnerModel.query.get(ownerID)
    # pets = PetsModel.query.filter_by(ownerID=ownerID)

    if request.method == 'POST' and form.validate():
        name_pet = request.form['name_pet']
        age_pet = request.form['age_pet']
        type_pet = request.form['type_pet']

        pet = PetsModel(name=name_pet, age=age_pet, type_pet=type_pet)
        user.pets.append(pet)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('owners.add_pet_page', ownerID=ownerID))
    return render_template('owners/add_pet_page.html', form=form, user=user)


@owners.route('/delete_owner/<int:id>')
def delete_owner(id):
    OwnerModel.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('owners.owners_page'))


@owners.route('/delete_pet/<int:id_pet>/<int:owner_id>')
def delete_pet(id_pet, owner_id):
    PetsModel.query.filter_by(id=id_pet).delete()
    db.session.commit()
    return redirect(url_for('owners.add_pet_page', ownerID=owner_id))
