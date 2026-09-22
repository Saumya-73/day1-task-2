course_fees = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}


def get_course_fee(course_code):
    course_code = course_code.upper()

    if course_code in course_fees:
        return course_fees[course_code]

    return None


def calculate_total(fee1, fee2):
    total = fee1 + fee2
    discount = total * 0.10
    final_amount = total - discount

    return final_amount