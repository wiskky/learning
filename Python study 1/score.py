#Program that get user's number grade and prints a letter grade
#if input is 90 the output will be A, 100-85 is A
#84-70 is B, 69-60 is C, 50-59 is D anything below 50 is F.

userGrade = input("Enter your score: ")
userGrade = int(userGrade)

if (userGrade < 50):
    print("You get F")
elif(userGrade >= 50) and (userGrade <= 59):
    print("You get D")
elif(userGrade >= 60) and (userGrade <= 69):
    print("You get C")
elif(userGrade >= 70) and (userGrade <= 85):
    print("You get B")
else:
    print("You get A")
