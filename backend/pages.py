import sys

from flask import Blueprint, render_template, redirect, request, url_for
from .models import Department, Employee
from .database import db


blueprint = Blueprint('views', __name__)


@blueprint.route('/', methods=(['GET']))
def index():
    departments = Department.query.all()
    return render_template('index.html', departments=departments)


@blueprint.route('/departments', methods=(['POST']))
def create_department():
    dep_name = request.form['dep_name']
    new_dep = Department(name=dep_name)

    try:
        db.session.add(new_dep)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue adding your department'

@blueprint.route('/departments/<int:id>', methods=(['POST']))
def create_employee(id):
    empl_name = request.form['name']
    empl_salary = request.form['salary']
    empl_birth_date = request.form['birth_date']
    new_empl = Employee(name=empl_name,
                        salary=empl_salary,
                        birth_date=empl_birth_date,
                        department_id=id)
    try:
        db.session.add(new_empl)
        db.session.commit()
        return redirect('/departments/'+str(id))
    except:
        x = sys.exc_info()
        return 'There was a problem adding this employee'



@blueprint.route('/departments/<int:id>', methods=(['GET']))
def department_employees(id):
    employees = Employee.query.filter(Employee.department_id == id)
    department = Department.query.get_or_404(id)
    return render_template('department.html', employees=employees, department=department)
