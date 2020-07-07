from flask import Blueprint, render_template, request

from app.posts.forms import Posts_Form

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='static')


@posts.route('/')
def indexx():
    return render_template('posts/indexx.html')


@posts.route('/new/', methods=['POST', 'GET'])
def new_page():
    form = Posts_Form()
    name = ''
    mail = ''
    if request.method == 'POST':
        print(f'this is req {dict(request.form)}')
        name = request.form['naaame']
        mail = request.form['mail']
    return render_template('posts/new_post.html', name=name, mail=mail, form=form)
