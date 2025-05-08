class Student:
    def __init__(self, name, major):
        self._name = name
        self._major = major
        self._total_grades = 0.0
        self._num_courses = 0

    def getName(self):
        return self._name
    
    def getMajor(self):
        return self._major
    
    def getGPA(self):
        if self._num_courses == 0:
            return 0.0
        return self._total_grades / self._num_courses
    
    def addGrade(self, grade):
        self._total_grades += grade
        self._num_courses += 1
    
    def getNumCourses(self):
        return self._num_courses
    
    def __eq__(self, other):
        return self._name == other._name and self._major == other._major
    
    def __lt__(self, other):
        return self.getGPA() < other.getGPA()
    
    def __str__(self):
        return f'Name: {self._name}, Major: {self._major}, GPA: {round(self.getGPA(), 2)}'
    

