from main import db, ma

class student(db.Model):
   id = db.Column('students.id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200)) 
   pin = db.Column(db.String(10))

   def __init__(self, name, city, addr,pin):
      self.name = name
      self.city = city
      self.addr = addr
      self.pin = pin


#student schema
class studentSchema(ma.Schema):
   class Meta:
      fields = ('id', 'name', 'city', 'addr', 'pin')

#init schema
student_schema = studentSchema()
students_schema = studentSchema(many=True)