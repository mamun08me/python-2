single_number={
        "phone": "01822222222",
        "total_otp": 13
    }
def banglalink_number(number):
    return number["phone"].startswith("019")

result= banglalink_number(single_number)

if result:
    print(single_number)
else:
    print("not available")