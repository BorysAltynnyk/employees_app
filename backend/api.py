from flask import Blueprint, jsonify, redirect, request
from .models import Department, Employee
from .database import db

blueprint = Blueprint('api', __name__)


@blueprint.route('/api/departments', methods=(['GET']))
def get_departments():
    res = Department.query.all()
    return jsonify(json_list=[i.serialize for i in res])


@blueprint.route('/api/departments/<int:id>', methods=(['DELETE']))
def delete_department(id):
    dep_to_delete = Department.query.get_or_404(id)
    db.session.delete(dep_to_delete)
    db.session.commit()
    return jsonify({"message": "OK"})


@blueprint.route('/api/employees/<int:id>', methods=(['DELETE']))
def delete_employee(id):
    empl_to_delete = Employee.query.get_or_404(id)
    db.session.delete(empl_to_delete)
    db.session.commit()
    return jsonify({"message": "OK"})
