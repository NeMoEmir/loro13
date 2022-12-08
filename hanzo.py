class Student:
    def __init__(self, name, second_name):
        self.name = name
        self.second_name = second_name
        self._hello = 'hello'
        self.__is_student = True
    
    def get_is_student(self):
        return self.__is_student
    
    def set_is_student(self):
        res = True if self.__is_student == False else False
    
    def __say_goodbye(self):
        print('Good bye')
    
    def say_hello(self):
        print(f'Hello {self.name}')
    
s = Student('Human', 'Alive')
s.say_hello()