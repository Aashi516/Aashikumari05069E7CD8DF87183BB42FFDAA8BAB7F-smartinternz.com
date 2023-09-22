class student:
  
 def __init__(self,name,roll_number, cgpa):
   self.name = name 
   self.roll_number = roll_number 
   self.cgpa = cgpa


def sort_students(student_list):
  
  sorted_students = sorted(student_list,
    key=lambda student:student.cgpa,
                       reverse=True)
  return sorted_students



students = [
  student("sumitha","A123",7.8),
  student("raji","A124",8.9),
  student("harini","A125", 9.1),
  student("swetha","A126",9.9),
]

sorted_student = sort_students(students)


for student in sorted_student:
  print("Name: {}, Roll number:{}, CGPA: {}".format(student.name,
student.roll_number,
student.cgpa))