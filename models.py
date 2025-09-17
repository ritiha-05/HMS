from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
db = SQLAlchemy()

class Admin(db.Model):
    __tablename__="admins"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return f"Admin: {self.username}" 

class Department(db.Model):
    __tablename__="departments" 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    doctors = db.relationship("Doctor", backref="department", lazy=True)
    def __repr(self):
        return f"Department: {self.name}"
    
class Doctor(db.Model):
    __tablename__="doctors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    specialization_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    appointments = db.relationship("Appointment", backref="doctor", lazy=True) 
    def __refr__(self):
        return f"Doctor: {self.name}" 

class Patient(db.Model):
    __tablename__="patients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    appointments = db.relationship("Appointment", backref="patient", lazy=True)
    def __refr__(self):
        return f"Patient: {self.name}"
    
class Appointment(db.Model):
    __tablename__="appointments"
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), default="Scheduled")
    treatments = db.relationship("Treatment", backref="appointment", lazy=True)
    def __refr__(self):
        return f"Appointment: {self.id} - Patient: {self.patient_id} with Doctor {self.doctor_id}"

class Treatment(db.Model):
    __tablename__="treatments"
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey("appointments.id"), nullable=False)
    description = db.Column(db.Text, nullable = False)
    medicine_prescribed = db.Column(db.String(200))
    follow_up_date = db.Column(db.DateTime)
    def __refr__(self):
        return f"Treatment: {self.id} for {self.appointment_id}" 
    