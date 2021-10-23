class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.rate_lecturer = {}

    def __set__(self):
        res = (
            f'Имя: = {self.name} \n Фамилия: = {self.surname} \n Средняя оценка за домашние задания: = {self.grades} \n'
            f'Курсы в процессе изучения: = {self.courses_in_progress} \n Завершенные курсы: = {self.finished_courses} \n')
        return res

    def rate_lecturer(self, lecturer, lesson, rate):
        if isinstance(lecturer, Lecturer) and lesson in Lecturer.read_lectures:
            if lesson in lecturer.rate:
                lecturer.rate[lesson] += [rate]
            else:
                lecturer.rate[lesson] = [rate]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return print('Not Student')
        return self.grades < other.grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, read_lectures):
        super().__init__(name, surname)
        self.read_lectures = []
        self.get_rate = {}


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return print('Not Lecturer')
        return self.get_rate < other.get_rate

    def rate(self):
        for rate in Student.rate_lecturer():
            midlle_rate += rate
            midlle_rate = rate / len(rate)
        return midlle_rate
    def __set__(self):
        res = (f'Имя: = {self.name} \n Фамилия: = {self.surname} \n Средняя оценка за лекции: = {self.get_rate}')
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname, check_homework):
        super().__init__(self, name, surname)
        self.check_homework = []
        self.rating_hw = []

    def rating_hw(self, student, course, grade):
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


Sasha_Vasin = Student('Sasha', 'Vasin', 'boy')
Natasha_Ivanova = Student('Natasha', 'Ivanova', 'girl')

Oleg_Bulygin = Lecturer('Oleg', 'Bulygin', 'Phython')
Ilnaz_Gilyazov = Lecturer('Ilnaz', 'Gilyazov', 'Git')

Alyona_Batitskaya = Reviewer('Alyona', 'Batitskaya', 'Git')
Oleg_Bulygin1 = Lecturer('Oleg1', 'Bulygin1', 'Phython')


