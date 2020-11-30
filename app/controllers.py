from flask import Blueprint, jsonify
from .models import Department, Employee
blueprint = Blueprint('api', __name__)

@blueprint.route('/api/departments', methods=('GET'))
def get_articles():
    res = Department.query.all()
    return jsonify(res)

@blueprint.route('/api/employees', methods=('GET'))
def get_articles():
    res = Employee.query.all()
    return jsonify(res)