class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
    
    def get_name(self):
        return self._name
    
    def get_surname(self):
        return self._surname
    
    @property
    def fullname(self):
        return f"{self._name} {self._surname}"


    @fullname.setter
    def fullname(self,a):
        self._name, self._surname = a.split()


    

person = Person('Джон', 'Маккарти') 
person.fullname = 'Алан Тьюринг' 

print(person.get_name()) 
print(person.get_surname())