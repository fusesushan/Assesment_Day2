'''
[**kwargs] Create a function create_student_report that takes the student's
name as the first argument, the student's age as the second argument, and an
arbitrary number of keyword arguments for the subjects and their respective
scores. The function should return a dictionary with the student's information and a
list of subjects along with their scores.

'''

def create_student_report(name, age, **kwargs):
    '''Function that takes the student's name, age and list of subjects with marks obtained and
    return a dictionary with all those info'''
    student_info = {
        'Name': name,
        'Age': age,
        'Subjects': []
    }
    for subject, score in kwargs.items():
        student_info['Subjects'].append({"sub":subject ,"score": score})
    return student_info

print(create_student_report.__doc__)

report1 = create_student_report('Sushan', 24, math=95, science=88, history=75)
print(report1)

report2 = create_student_report('Kattel', 25, physics=92, chemistry=85)
print(report2)
