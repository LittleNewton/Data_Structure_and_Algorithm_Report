# 1.5.1 Information Passing

def count(data,target):
    n = 0
    data = []
    for item in data:
        if item == target:      # found a match
            n += 1
    return n

def scale(data,factor):
    for j in range(len(data)):
        data[j] *= factor

def compute_gpa(grades,points={'A+':4.0,'A':4.0,'A-':3.67,'B+':3.33,\
                               'B':3.0,'B-':2.67,'C+':2.33,'C':2.0,\
                               'C-':1.67,'D+':1.33,'D':1.0,'F':0.00}):
    num_courses = 0
    total_points = 0
    for g in grades:
        if g in points:         # a recognizable grade
            num_courses += 1
            total_points += points[g]
    return total_points / num_courses


grades = ['A','B','C','A','A','B']
print('1: ',count(grades,'A'))
print('2: ',grades)
liupeng = [1,2,3,4,5,6,7,8,9]
scale(liupeng,2)
print('3: ',liupeng)