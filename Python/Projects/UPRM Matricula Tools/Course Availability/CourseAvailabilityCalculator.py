import json

# Main variables - Change these to change program behavior
course_interest = "INEL"

# Retrieve JSON data
data = []
with open("data.json", "r+") as fp:
    data = json.load(fp)
sections = data['items']

# Extract data of interest: courses, capacity and amount of sections
output, courses = list(), set()
capacities, amount_sections = dict(), dict()

for section in sections:
    if section['course_code'].startswith(course_interest):
        # Course information
        course_code = section['course_code']
        course_name = str(section['course_name'])
        course_credits = 0
        try:
            course_credits = int(section['crds'])
        except:
            course_credits = int(section['course_credits'])

        courses.add((course_code, course_name, course_credits))

        capacity = int(section["capacity"])

        if course_code in amount_sections:
            amount_sections[course_code] += 1
        else:
            amount_sections[course_code] = 1

        if course_code in capacities:
            capacities[course_code].append(capacity)
        else:
            capacities[course_code] = [capacity]

# Based upon capacity and amount of sections, calculate and print availability
# of course
if len(courses)<1:
    print("{} NOT FOUND".format(course_interest))
else:
    print("Course\t\tAvailability\tCredits\tTitle")
    for course in courses:
        course_code = course[0]
        capacity = capacities[course_code]
        ave_capacity = round(sum(capacity)/len(capacity), 2) 
        amount = amount_sections[course_code] 
        availability = round(amount*ave_capacity, 2) 
        print("{}\t{}\t\t{}\t{}".format(course_code, availability, course[2], course[1]))
