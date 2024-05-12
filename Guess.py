secret_word = "giraffe"
guess = ""
count = 0
flag = 0
while guess != secret_word:
    if count <= 3:
        guess = input("Enter guess : ")
        count = count + 1
    else:
        flag = 1
if flag == 0:
    print("YOU WIN !!!")
else:
    print("OUT OF GUESSES")