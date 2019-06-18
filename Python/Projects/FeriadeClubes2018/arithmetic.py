import random
import re

user_name = str(input('= + '*20 + "\n [!] Please enter your name to continue: "))
print("[*] Welcome {}. With this application you will be able to practice arithmetic\n".format(user_name))


temp = str(input(" [!] How many exercises do you want?: "))
while not re.match("^\d+$", temp):
    print("[*] Error! Input was either empty, not a number, or the number was not an integer")
    
    temp = input(" [!] How many exercises do you want?: ")
iterations = int(temp)

type_of_exercises = str(input(" [!] What kind of arithmetic operation do you want to practice? (Addition, Substraction, Multiplication, Division, or empty for random) "))
  
  
correct_counter, incorrect_counter = 0, 0

for exercise in range(iterations):
  result, user_response = 0, 0;
  
  if type_of_exercises.lower() in ["add", "addition", "sum", "summing", "suma", "adicion"]:
    a, b = random.randint(1,50), random.randint(1,50)
    user_response = float(input(" [{}] What is {} + {}?".format(exercise+1,a,b)))
    result = float(a + b)
    
  elif type_of_exercises.lower() in ["substract", "subs", "resta", "substraccion"]:
    a, b = random.randint(1,50), random.randint(1,50)
    user_response = float(input(" [{}] What is {} - {}?".format(exercise+1,a,b)))
    result = float(a - b)
    
  elif type_of_exercises.lower() in ["mult", "mul", "multiplication", "multiplicacion"]:
    a, b = random.randint(0,12), random.randint(0,12)
    user_response = float(input(" [{}] What is {} × {}?".format(exercise+1,a,b)))
    result = float(a * b)
    
  elif type_of_exercises.lower() in ["div", "division"]:
    a, b = random.randint(0,12), random.randint(1,12)
    a = a*b
    user_response = float(input(" [{}] What is {} ÷ {}?".format(exercise+1,a,b)))
    result = float(a / b)
  
  else:
    operation = random.randint(0,3)
    if operation == 1:
      a, b = random.randint(1,50), random.randint(1,50)
      user_response = float(input(" [{}] What is {} + {}?".format(exercise+1,a,b)))
      result = float(a + b)
      
    elif operation == 2:
      a, b = random.randint(1,50), random.randint(1,50)
      user_response = float(input(" [{}] What is {} - {}?".format(exercise+1,a,b)))
      result = float(a - b)
    
    elif operation == 3:
      a, b = random.randint(0,12), random.randint(0,12)
      user_response = float(input(" [{}] What is {} × {}?".format(exercise+1,a,b)))
      result = float(a * b)
    
    elif operation == 4:
      a, b = random.randint(0,12), random.randint(1,12)
      a = a*b
      user_response = float(input(" [{}] What is {} ÷ {}?".format(exercise+1,a,b)))
      result = float(a / b)
      
  
  if result == user_response:
    print("[*] Correct!")
    correct_counter += 1
  else:
    print("[*] Wrong! The result was {}".format(int(result)))
    incorrect_counter += 1
    
if correct_counter / iterations >= 0.8:
  print("[*] You had {} correct and {} incorrect. Good job!".format(correct_counter, incorrect_counter))
else:
  print("[*] You had {} correct and {} incorrect. Better luck next time!".format(correct_counter, incorrect_counter))
