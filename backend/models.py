from .database import db
Model = db.Model


class Department(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    employees = db.relationship("Employee")


    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id': self.id,
           # This is an example how to deal with Many2Many relations
           'name': self.name,
           'avr_salary': self.avr_salary
       }
    @property
    def salary(self):
        employees = self.employees
        if len(employees) == 0:
            return 0
        sum = 0
        for e in employees:
            sum += e.salary
        return sum/len(employees)




class Employee(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    department_id = db.Column(db.ForeignKey("department.id"))

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id': self.id,
           'name': self.name,
           'salary': self.salary,
           'birth date': self.birth_date,
           'departament': self.department_id
       }
