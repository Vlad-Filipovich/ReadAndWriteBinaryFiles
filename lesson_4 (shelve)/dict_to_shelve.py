import shelve

university = shelve.open('university_file')
# university['schedules'] = {
#         'monday_schedule': ['Math', 'English language', 'System programming', 'Python'],
#         'tuesday_schedule': ['English language', 'HTML', 'Python', 'Football'],
#         'wednesday_schedule': ['Physics', 'English language', 'Python'],
#         'thursday_schedule': ['Math', 'Chemistry', 'Java'],
#         'friday_schedule': ['Running', 'Math', 'Python']
#     }
# university['tutors'] = {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['Jane Smith', 'Will Brown']
#     }

print(university['schedules']['thursday_schedule'])
print(university['tutors']['Python'])

university.close()