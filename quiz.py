print("Hello, Welcome to my quiz game!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0;


answer = input("what does CPU stand for? ")

if answer.lower() == "central processing unit" :
    print("correct!")
    score +=1
else:
    print ("Incorrect")


answer = input("what does GPU stand for? ")

if answer.lower() == "graphic processing unit" :
    print("correct!")
    score +=1
else:
    print ("Incorrect")


answer = input("what does RAM stand for? ")

if answer.lower() == "random access memory" :
    print("correct!")
    score +=1
else:
    print ("Incorrect")

print( "You got " + str(score) + " questions correct")
print( "You got " + str((score/3) *100) + "%")