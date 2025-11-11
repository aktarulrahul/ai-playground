def basic_examples():
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    
    person = {"name": "John", "age": 25}
    
    for i, num in enumerate(numbers):
        print(f"Number {i}: {num}")

def simple_function(name="User"):
    return f"Hello, {name}!"

def generator_example(n):
    for i in range(n):
        yield i * 2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    @property
    def is_adult(self):
        return self.age >= 18

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

if __name__ == "__main__":
    basic_examples()
    
    result = simple_function("Alice")
    print(result)
    
    for value in generator_example(5):
        print(f"Generated: {value}")
    
    person = Person("Bob", 20)
    print(person.introduce())
    print(f"Is adult: {person.is_adult}")
    
    student = Student("Charlie", 19, "STU123")
    print(student.introduce()) 