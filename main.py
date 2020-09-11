# Author: Kyle Hamlet kjh6064@psu.edu
# Section: 5
def getLetterGrade ():
  gradevalue = int(input("Enter your CMPSC 131 grade: "))
  if gradevalue >= 93.0:
    gradevalue = "A"
  elif gradevalue >= 90.0:
    gradevalue = "A-"
  elif gradevalue >= 87.0:
    gradevalue = "B+"
  elif gradevalue >= 83.0:
    gradevalue = "B"
  elif gradevalue >= 80.0:
    gradevalue = "B-"
  elif gradevalue >= 77.0:
    gradevalue = "C+"
  elif gradevalue >= 70.0:
    gradevalue = "C"
  elif gradevalue >= 60.0:
    gradevalue = "D"
  else:
    gradevalue = "F"
  print(f"Your letter grade for CMPSC 131 is {gradevalue}.\n")