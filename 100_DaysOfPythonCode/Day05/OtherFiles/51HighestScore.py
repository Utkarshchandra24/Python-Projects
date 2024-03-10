# 78 65 89 86 55 91 64 89

student_scores = input("Input a list of student scores ").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# print("Highest score =",max(student_scores))
# print("Lowest score =",min(student_scores))

lowest = student_scores[0]
for num in range(1,len(student_scores)):
    num = student_scores[num]                   #65
    if lowest > num:
        lowest = num
    else:
        continue

print("Lowest number in the list =",lowest)

highest = student_scores[0]
for num in range(1,len(student_scores)):
    num = student_scores[num]
    if highest < num:
        highest = num
    else:
        continue

print("Highest number in the list =",highest)
print()
print("The highest score in the class is:",highest)