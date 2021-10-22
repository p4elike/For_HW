class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def __set__(self):
        res = (f'Имя: = {self.name} \n Фамилия: = {self.surname} \n Средняя оценка за домашние задания: = {self.grades} \n'
               f'Курсы в процессе изучения: = {self.courses_in_progress} \n Завершенные курсы: = {self.finished_courses} \n')
        return res
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']




class Lecturer(Mentor):
    def __init__(self, read_lectures, get_rate):
        self.read_lectures = read_lectures
        self.read_lectures = []
        self.get_rate = []
    def __set__(self):
        res = (f'Имя: = {self.name} \n Фамилия: = {self.surname} \n Средняя оценка за лекции: = {self.get_rate}')
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
        self.check_homework = []
        self.rating_hw = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __set__(self):
        res = (f'Имя: = {self.name} \n Фамилия: = {self.surname} \n ')
        return res


