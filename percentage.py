# finding average of all subjects

student_marks = {}
n = int((input()))

for x in range(n):
    name, *line = input().split()
    scores = list(map(float,line))
    avg =   (scores[0]+scores[1]+scores[2])/3
# finding value upto 2 decimal places if needed
    student_marks[name] = '%.2f' % avg
# without this more precision not possible
# "/" division se round off float value ati hai upto 1 decimal place

query_name = input()

print(student_marks[query_name])


