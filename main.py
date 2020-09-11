# Author: Kyle Hamlet kjh6064@psu.edu
# Solo
# Section: 5
def getLetterGrade (gradevalue): 
  if gradevalue >= 93.0:
    return "A"
  elif gradevalue >= 90.0:
    return "A-"
  elif gradevalue >= 87.0:
    return "B+"
  elif gradevalue >= 83.0:
    return "B"
  elif gradevalue >= 80.0:
    return "B-"
  elif gradevalue >= 77.0:
    return "C+"
  elif gradevalue >= 70.0:
    return "C"
  elif gradevalue >= 60.0:
    return "D"
  else:
    return "F"
  
def run():
  gradevalue = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(gradevalue)}.")

if __name__ == "__main__":
  run()
