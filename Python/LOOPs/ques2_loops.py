# write a program to show student are pass or not conditions total percentage 40 % per subject 33 % asume 3 subject 
Subject1=int(input("Enter your makrs "))
Subject2=int(input("Enter your makrs "))
Subject3=int(input("Enter your makrs "))
total_percentage = (100*(Subject1 + Subject2 + Subject3)) / 300
if(total_percentage>=40 and Subject1>=33 and Subject2>=33 and Subject3>=33 ):
  print("You are pass with percentage:", total_percentage)
else:
  print("Your are fail with percentage:" ,total_percentage)
