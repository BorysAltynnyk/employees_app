from flask import Blueprint, render_template
from .models import Department, Employee

blueprint = Blueprint('api', __name__)


@blueprint.route('/', methods=(['GET']))
def index_page():
    # Render index html with departments
    # get all departments
    # pass to render template
    # inside template iterate over each department
    # return jsonify(res)
    # Use https://github.com/BorysAltynnyk/employees_app/tree/5c79c2f1ad7066e5f2a78dd8291d74853cef74da as reference
    res = Department.query.all()
    return render_template('index.html', deps=res)

@blueprint.route('/departments/1', methods=(['GET']))
def department_page():
    # Render department html with departments
    # return jsonify(res)
