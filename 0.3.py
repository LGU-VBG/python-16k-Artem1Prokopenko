class User:
    def __init__(self,name,age):
        self.error_name(name)
        self.error_age(age)
        self._name=name
        self._age=age
    
    def error_name(self,name):
        if not isinstance(name, str) or not name or not name.isalpha():
            raise ValueError("Некорректное имя")
    
    
    def error_age(self,age):
        if not isinstance(age, int) or age < 0 or age >100:
            raise ValueError("Некорректное возраст")
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        self.error_name(new_name)
        self._name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,new_age):
        self.error_age(new_age)
        self._age=new_age
        
try:
    user = User('Гвидо', 101) 
except Exception as e:
    print(e)

user.name = 'Тимур' 
user.age = 30 
print(user.name) 
print(user.age)