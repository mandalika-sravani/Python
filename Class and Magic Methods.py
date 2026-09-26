# Class Methods --- Allow operations related to the class itself
# Magic Methods --- They are automaticaly called by many of Python's built-in operations. Allows customize the behaviour of objects

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students : {cls.count}"

    @classmethod
    def get_gpa(cls):
        return f"Total GPA of students : {cls.total_gpa}"


st1 = Student("Malini", 6.4)
st2 = Student("Pallavi", 7.9)
print(Student.get_count())
print(Student.get_gpa())

# Magic methods

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by '{self.author}'"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title" :
            return self.title
        elif key == "author" :
            return self.author
        elif key == "num_pages" :
            return self.num_pages
        else: 
            return f"Key {key} was not found"

b1 = Book("The Hobbit", "J.R.R Tolkein", 300)
b2 = Book("Harry Potter and The Philosopher's Stone", "J.K Rowling", 450)

print(b2)
print(b1 == b2)
print(b1 + b2)
print("The" in b1 and "and" in b2)
print("Tolkein" in b1)

print(b1['author'])
print(b2['num_pages'])

print(b2['audio'])