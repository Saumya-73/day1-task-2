course_fees = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

print("College Course Fee - Rule-Based Workflow")
print("Available courses: CS101, AI202, DS303")

course = input("Enter course code: ").upper()

if course in course_fees:
    fee = course_fees[course]
    print("Course Fee: ₹", fee)
else:
    print("Course not found.")