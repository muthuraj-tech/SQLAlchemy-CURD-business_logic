from flask import Flask, request, jsonify
from main import app
from models import student, studentSchema
from models import student_schema, students_schema
from main import db, ma


@app.route('/', methods = ['GET', 'POST'])
def show_all():
   # create student
   if request.method == 'POST':

      name = request.json['name']
      city = request.json['city']
      addr = request.json['addr']
      pin = request.json['pin']
      new_student = student(name, city, addr, pin)
      db.session.add(new_student)
      db.session.commit()
      return student_schema.jsonify(new_student)

   # get all student
   if request.method == 'GET':
      all_students = student.query.all()
      result = students_schema.dump(all_students).data
      return jsonify(result)


@app.route('/operation/<id>', methods = ['GET', 'PUT', 'DELETE'])
def operation(id):

   # get student by id
   if request.method == 'GET':
      stu = student.query.get(id)
      return student_schema.jsonify(stu)

   # update student by id
   if request.method == 'PUT':
      stu = student.query.get(id)
      name = request.json['name']
      city = request.json['city']
      addr = request.json['addr']
      pin = request.json['pin']
      stu.name=name
      stu.city=city
      stu.addr=addr
      stu.pin=pin
      db.session.commit()
      return student_schema.jsonify(stu)

   # delete student by id
   if request.method == 'DELETE':

      std = student.query.get(id)
      db.session.delete(std)
      db.session.commit()
      return student_schema.jsonify(std)