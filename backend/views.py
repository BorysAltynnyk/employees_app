from flask import Blueprint, render_template, redirect, request, url_for
from .models import Department, Employee
from .database import db

blueprint = Blueprint('views', __name__)


# Render index html with departments
    # get all departments
    # pass to render template
    # inside template iterate over each department
    # return jsonify(res)
    #https://github.com/BorysAltynnyk/employees_app/tree/5c79c2f1ad7066e5f2a78dd8291d74853cef74da as reference
@blueprint.route('/', methods=(['GET', 'POST']))
def index_page():
    if request.method == 'POST':
        dep_name = request.form['dep_name']
        new_dep = Department(name=dep_name)

        try:
            db.session.add(new_dep)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        res = Department.query.all()
        return render_template('index.html', deps=res)


@blueprint.route('/departments/<int:id>', methods=(['GET']))
def department_page(id):
    res = Employee.query.filter(Employee.department_id == id)
    if res.count() == 0:
        res = 0
    return render_template('department.html', empls=res, depid=id)
    # Render department html with departments
    # return jsonify(res)


@blueprint.route('/employees', methods=(['GET']))
def employees_page():
    res = Employee.query.all()
    return render_template('employees.html', empls=res)







