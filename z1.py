class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def mean_grades(self):
        grades_list = list(self.grades.values())
        for m_grades in grades_list:
            grades = sum(m_grades) / len(m_grades)
        return grades
    def __str__(self):
        res = (
f'''Имя: = {self.name} 
Фамилия: = {self.surname}
Средняя оценка за домашние задания: = {self.mean_grades()} 
Курсы в процессе изучения: = {", ".join(self.courses_in_progress)} 
Завершенные курсы: = {", ".join(self.finished_courses)} '''
)
        return res

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.read_lectures:
            if course in lecturer.rate:
                lecturer.rate[course] += [rate]
            else:
                lecturer.rate[course] = [rate]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return print('Not Student')
        return self.mean_grades() < other.mean_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.read_lectures = []
        self.rate = {}


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return print('Not Lecturer')
        return other.mean_rate() > self.mean_rate()

    def mean_rate(self):
        rate_list = list(self.rate.values())
        for m_rate in rate_list:
            res = sum(m_rate) / len(m_rate)
        return res
    def __str__(self):
        res = (f'''
Имя: = {self.name} 
Фамилия: = {self.surname} 
Cредняя оценка за лекции: = {self.mean_rate()}'''
)
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.check_homework = []


    def rating_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.check_homework and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (
        f'''
Имя: = {self.name} 
Фамилия: = {self.surname}
        ''')
        return res

#Students
Sasha_Vasin = Student('Sasha', 'Vasin', 'boy')
Sasha_Vasin.courses_in_progress.append('Python')
Sasha_Vasin.courses_in_progress.append('Git')


Natasha_Ivanova = Student('Natasha', 'Ivanova', 'girl')
Natasha_Ivanova.courses_in_progress.append('Python')
Natasha_Ivanova.finished_courses.append('Git')


#Oleg_Bulygin = Mentor('Oleg', 'Bulygin')
#Ilnaz_Gilyazov = Mentor('Ilnaz', 'Gilyazov')
#Elena_Nikitina = Mentor('Elena', 'Nikitina')


#Lecturers
Oleg_Bulygin = Lecturer('Oleg', 'Bulygin')
Oleg_Bulygin.read_lectures.append('Python')

Ilnaz_Gilyazov = Lecturer('Ilnaz', 'Gilyazov')
Ilnaz_Gilyazov.read_lectures.append('Git')

#Reviewers
Alyona_Batitskaya = Reviewer('Alyona', 'Batitskaya')
Alyona_Batitskaya.check_homework.append('Git')


Alexander_Bardin = Reviewer('Alexander', 'Bardin')
Alexander_Bardin.check_homework.append('Python')

#Rating_hw
Alexander_Bardin.rating_hw(Natasha_Ivanova, 'Python', 8)
Alexander_Bardin.rating_hw(Natasha_Ivanova, 'Python', 8)
Alexander_Bardin.rating_hw(Natasha_Ivanova, 'Python', 8)
Alexander_Bardin.rating_hw(Sasha_Vasin, 'Python', 9)
Alexander_Bardin.rating_hw(Sasha_Vasin, 'Python', 9)
Alyona_Batitskaya.rating_hw(Natasha_Ivanova, 'Git', 8)
Alyona_Batitskaya.rating_hw(Natasha_Ivanova, 'Git', 8)
Alyona_Batitskaya.rating_hw(Natasha_Ivanova, 'Git', 9)
Alyona_Batitskaya.rating_hw(Sasha_Vasin, 'Git', 9)
Alyona_Batitskaya.rating_hw(Sasha_Vasin, 'Git', 10)


#Rate Lecturers
Sasha_Vasin.rate_lecturer(Oleg_Bulygin, 'Python', 10 )
Sasha_Vasin.rate_lecturer(Oleg_Bulygin, 'Python', 10 )
Sasha_Vasin.rate_lecturer(Oleg_Bulygin, 'Python', 10 )
Sasha_Vasin.rate_lecturer(Oleg_Bulygin, 'Python', 10 )
Sasha_Vasin.rate_lecturer(Ilnaz_Gilyazov, 'Git', 10 )
Sasha_Vasin.rate_lecturer(Ilnaz_Gilyazov, 'Git', 10 )
Sasha_Vasin.rate_lecturer(Ilnaz_Gilyazov, 'Git', 10 )

Natasha_Ivanova.rate_lecturer(Oleg_Bulygin, 'Python', 7)
Natasha_Ivanova.rate_lecturer(Oleg_Bulygin, 'Python', 8)
Natasha_Ivanova.rate_lecturer(Oleg_Bulygin, 'Python', 6)
Natasha_Ivanova.rate_lecturer(Oleg_Bulygin, 'Python', 7)
Natasha_Ivanova.rate_lecturer(Ilnaz_Gilyazov, 'Git', 6 )
Natasha_Ivanova.rate_lecturer(Ilnaz_Gilyazov, 'Git', 6 )
Natasha_Ivanova.rate_lecturer(Ilnaz_Gilyazov, 'Git', 5 )


student_list = []
student_list.append(Natasha_Ivanova)
student_list.append(Sasha_Vasin)

def mean_grade(list, course):
    result = []
    mean_grade_course = 0
    amount = 0
    for student in list:
        amount += 1
        if course in student.grades.keys():
            result.extend(student.grades[course])
        mean_grade_course += sum(result) / len(result)
    print('Средняя оценка студентов: ', mean_grade_course/amount)
mean_grade(student_list, 'Python')

lectures_list=[]
lectures_list.append(Oleg_Bulygin)
lectures_list.append(Ilnaz_Gilyazov)

def mean_rate(list, course):
    result = []
    amount = 0
    mean_rate_course = 0
    for lectures in list:
        amount += 1
        if course in lectures.rate.keys():
            result.extend(lectures.rate[course])
        mean_rate_course += sum(result) / len(result)
    print('Средний рейтинг лекторов: ', mean_rate_course / amount)
mean_rate(lectures_list, 'Python')