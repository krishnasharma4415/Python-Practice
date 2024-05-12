start = int(input("Enter the Start value\n"))
end = int(input("Enter the End value\n"))
check = 0
for i in range(start, end+1):
    check = 0
    for j in range(1, i):
        if i % j == 0:
            check = check + 1
    if check < 2:
        print(i)
    