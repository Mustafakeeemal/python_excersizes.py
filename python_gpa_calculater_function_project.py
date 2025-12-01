"""

💻 PYTHON CODING PROJECT

1-)Write a Python function named calculate_weighted_average(mt1, mt2, f).
2-)This function takes three exam scores (scores entered will be out of 100) and calculates the weighted average.
3-)The weights for the exams are given as 20%, 35%, and 45% respectively.Print the calculated average to the screen.
4-)Additionally, if the average score is less than 50 or  the final exam score is less than 20 (regardless of the midterm scores), 
print the message "You failed and are eligible for the makeup exam" (or a similar appropriate phrase like "You are eligible for the supplementary exam"). 
Otherwise, print "You passed".

"""

print("lets calculate your average!!!")

def calculate_weighted_average():
    m1=int(input("Midterm1: "))
    m2=int(input("Midterm2: "))
    f=int(input("Final: "))
    average= ( m1* 0.2 )+( m2 * 0.35 ) + (f * 0.45)

    if average < 50 or f < 20:
        print("You failed and are eligible for the makeup exam :( ")
    else: 
        print(f"You passed with : {average} ")

calculate_weighted_average()


