student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

# print("Length = ", len(student_heights))      #Do not use len function
# print("sum = ",sum(student_heights))          #Do not use sum function

cnt = 0
for i in student_heights:
    cnt+=1

print("Length =",cnt)
no_of_students = cnt

sum=0
for i in student_heights:
    sum+=i

print("Sum =",sum)
total_height = sum

average_height = round(total_height/no_of_students)

print("Average height =",average_height)




