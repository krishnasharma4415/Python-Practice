marks = [80, 90, 85, 70, 75]
for i in range(0,5):
    print(marks[i])
print(marks[0:3])

marks.append(99)
marks.insert(3, 95)

print(95 in marks)
print(60 in marks)
print(len(marks))

marks.clear()
print(marks)