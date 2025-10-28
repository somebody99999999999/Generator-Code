from faker import Faker # installing faker and importing it into the code

fake = Faker()
print("Hello and welcome to my random name generator")
print("Are you a female or male")
m = input("")
if m == "male":
    print("Good to know that your a male/man")
else:
    print("Good to know that your a female/woman")
print("What is your name")
name = input("")
if name == "john":
    print("Your new name is now Johnson")
else:
    print("")















# y = input("Would you like me to generate you an person yes/no? ") # my input statement

# if y == "yes": 
#     print(fake.name())
#     print(fake.date())
#      print(fake.job())
#     print(fake.city())
#     print(fake.state())
#     print(fake.country())
#     print(fake.zipcode())
# else:
#     print("What would like me to generate then here are some examples I can do random dates ⏱️, time's ⌛ or even phone numbers 📞")
# input("date's/dates/date").lower
# input("time's/times/time").lower
# input("phone number's/phone numbers/phone number").lower
# input("")