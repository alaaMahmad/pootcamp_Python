class Person:
    def pay_bill(self):
        raise NotImplementedError("pay_bill method it must implemented in the son class")
    
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!") 
        
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?") 

class Doctor(Person):
    pass # لم نكتب دالة pay_bill هنا!

# إنشاء الكائنات
rich_guy = Millionaire()
poor_student = GradStudent()

people = [rich_guy, poor_student]

for person in people:
    person.pay_bill()  

doc = Doctor()
doc.pay_bill() 
