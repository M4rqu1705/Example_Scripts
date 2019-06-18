from time import sleep
import re

# FUNCTIONS -- FUNCTIONS -- FUNCTIONS -- FUNCTIONS -- FUNCTIONS 

def get_serving(text):
  # Display the string variable "text" as you wait for user input
  serving = input(text)
  sleep(sleep_time)

  # While the answer is not a number, keep asking for the serving
  while not bool(re.search("^\d+$", serving.strip())):
    print("\nI'm sorry. I didn't get that.")
    # Request user input once more
    serving = input(text)
    sleep(sleep_time)
  
  # Return the serving as an integer
  return int(serving)

def calculate_facts(fact, servings = []):
  # Make sure servings and facts have the correct data types
  servings, fact = list(servings), str(fact)

  # Calculate the requested fact taking into account the amount of servings
  bread_nutrition = servings[0] * bread[fact] 
  ham_nutrition = servings[1] * ham[fact] 
  cheese_nutrition = servings[2] * cheese[fact] 
  peanut_butter_nutrition = servings[3] * peanut_butter[fact]

  # Add the requested nutritional fact for each component
  return int(bread_nutrition + cheese_nutrition + ham_nutrition + peanut_butter_nutrition)

# DICTIONARIES -- DICTIONARIES -- DICTIONARIES -- DICTIONARIES
bread = {
  "Calories":80, "Calories from Fat": 5, "Total Fat": 1,
  "Saturated Fat":0, "Trans Fat": 0, "Cholesterol": 0,
  "Sodium": 160, "Carbohydrates":17, "Dietary Fiber":2,
  "Sugars": 2, "Protein": 3, "Vitamin A": 0,
  "Vitamin C": 0, "Calcium": 2, "Iron":6 }
ham = {
  "Calories":30, "Calories from Fat": 0, "Total Fat": 0,
  "Saturated Fat":0, "Trans Fat": 0, "Cholesterol": 10,
  "Sodium": 250, "Carbohydrates":1, "Dietary Fiber":0,
  "Sugars": 1, "Protein": 5, "Vitamin A": 0,
  "Vitamin C": 0, "Calcium": 0, "Iron":0 }
cheese = {
  "Calories":40, "Calories from Fat": 15, "Total Fat": 1.5,
  "Saturated Fat":1, "Trans Fat": 0, "Cholesterol": 5,
  "Sodium": 280, "Carbohydrates":3, "Dietary Fiber":0,
  "Sugars": 2, "Protein": 3, "Vitamin A": 2,
  "Vitamin C": 0, "Calcium": 10, "Iron":0 }
peanut_butter = {
  "Calories":180, "Calories from Fat": 110, "Total Fat": 12,
  "Saturated Fat":2, "Trans Fat": 0, "Cholesterol": 0,
  "Sodium": 160, "Carbohydrates":14, "Dietary Fiber":2,
  "Sugars": 4, "Protein": 7, "Vitamin A": 0,
  "Vitamin C": 0, "Calcium": 0, "Iron":2 }

if __name__ == "__main__":
  sleep_time, servings = 1, [0, 0, 0, 0]
  thin_line, thick_line = str("-" * 80), str("=" * 80)

  # Introduction to the program
  print("\n"+thick_line)
  print("\nWelcome to the Sandwich Nutritional Facts Calculator!")
  sleep(sleep_time)
  print("\nWith this application you can see the nutritional facts of a")
  sleep(sleep_time)
  print("peanut butter, ham, and cheese sandwich according to")
  sleep(sleep_time)
  print("your serving size")
  sleep(sleep_time)

  # User input
  print("")
  servings[0] = get_serving("How many servings of bread did you have?\n << ")
  print("")
  servings[1] = get_serving("How many servings of ham did you have?\n << ")
  print("")
  servings[2] = get_serving("How many servings of cheese did you have?\n << ")
  print("")
  servings[3] = get_serving("How many servings of peanut butter did you have?\n << ")

  # Print out nicely-formatted nutrition facts
  print("\n" + thick_line + "\n")
  print("Nutrition Facts")
  sleep(sleep_time)

  msg = "Calories {}\tCalories from Fat {}".format(calculate_facts("Calories", servings), calculate_facts("Calories from Fat", servings))
  print(msg)
  print(thin_line)
  sleep(sleep_time)

  msg = "Total Fat {}g".format(calculate_facts("Total Fat", servings))
  print(msg)
  sleep(sleep_time)

  msg = "   Saturated Fat {}g".format(calculate_facts("Saturated Fat", servings))
  print(msg)
  sleep(sleep_time)

  msg = "   Trans Fat {}g".format(calculate_facts("Trans Fat", servings))
  print(msg)
  sleep(sleep_time)

  msg = "Cholesterol {}mg".format(calculate_facts("Cholesterol", servings))
  print(msg)
  sleep(sleep_time)

  msg = "Sodium {}mg".format(calculate_facts("Sodium", servings))
  print(msg)
  sleep(sleep_time)

  msg = "Total Carbohydrates {}g".format(calculate_facts("Carbohydrates", servings))
  print(msg)
  sleep(sleep_time)

  msg = "  Dietary Fiber {}g".format(calculate_facts("Dietary Fiber", servings))
  print(msg)
  sleep(sleep_time)

  msg = "  Sugars {}g".format(calculate_facts("Sugars", servings))
  print(msg)
  sleep(sleep_time)

  msg = "Protein {}g".format(calculate_facts("Protein", servings))
  print(msg)
  print(thin_line)
  sleep(sleep_time)

  msg = "Vitamin A {}%".format(calculate_facts("Vitamin A", servings))
  print(msg)
  sleep(sleep_time)

  msg = "Vitamin C {}%".format(calculate_facts("Vitamin C", servings))
  print(msg)
  sleep(sleep_time)

  msg = "Calcium {}%".format(calculate_facts("Calcium", servings))
  print(msg)
  sleep(sleep_time)

  msg = "Iron {}%".format(calculate_facts("Iron", servings))
  print(msg)
  sleep(sleep_time)

  print("\n" + thick_line + "\n")