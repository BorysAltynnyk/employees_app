from flask import Blueprint, jsonify, redirect, request
from .models import Department, Employee
from .database import db


blueprint = Blueprint('api', __name__)

@blueprint.route('/api/employees', methods=(['GET']))
def get_employees():
    res = Employee.query.all()
    return jsonify(json_list=[i.serialize for i in res])


@blueprint.route('/api/departments', methods=(['GET']))
def get_departments():
    res = Department.query.all()
    return jsonify(json_list=[i.serialize for i in res])


@blueprint.route('/departments/<int:id>', methods=(['POST']))
def add_employee(id):
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
        return 'There was a problem adding this employee'


@blueprint.route('/delete/<int:id>', methods=(['GET']))
def delete_department(id):
    dep_to_delete = Department.query.get_or_404(id)

    try:
        db.session.delete(dep_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting this task'


@blueprint.route('/employees/<int:id>', methods=(['DELETE']))
def delete_employee(id):
    empl_to_delete = Employee.query.get_or_404(id)

    return render_template('employees.html', empls=res)

