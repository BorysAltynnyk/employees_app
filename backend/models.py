from .database import db
Model = db.Model


class Department(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    employees = db.relationship("Employee")

class Employee(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    department_id = db.Column(db.ForeignKey("department.id"))
