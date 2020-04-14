from flask import Blueprint, render_template, request, redirect

from hoti_utils import get_hotties, create_hoti, get_hoti_by_id

bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/hotties'
)


@bp.route('/')
def list():
    return render_template('hoti_list.html', hotties=get_hotties())


@bp.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        title = request.form.get('hoti_title')
        content = request.form.get('hoti_content')

        hoti = create_hoti(title=title, content=content)

        return redirect('/hotties/view/' + hoti['id'])

    return render_template('hoti_edit.html')


@bp.route('/view/<hoti_id>')
def view(hoti_id):
    return render_template('hoti_view.html', hoti=get_hoti_by_id(hoti_id))
