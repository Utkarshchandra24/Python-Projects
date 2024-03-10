#Exercise : Add even numbers from 1 to 100

total=0
for num in range(2,101,2):                  #it will skip in the number range(start,end,skip)
     total += num

print("Sum of even numbers from 1 to 100 =",total)

print()
total2 = 0
for number in range(1,101):
    if number%2 == 0:
        total2 += number

print("Sum of even numbers =",total2)