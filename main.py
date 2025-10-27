from faker import Faker # installing faker and importing it into the code

fake = Faker()
y = input("Would you like me to generate you an person yes/no? ") # my input statement

if y == "yes": 
    print(fake.name())
    print(fake.job())
    print(fake.date())
    print(fake.country())
    print(fake.state())
    print(fake.city())
    print(fake.zipcode())
else:
    print("What would like me to generate then here are some examples I can do random dates ⏱️, time's ⌛ or even phone numbers 📞")
input("date's/dates/date").lower
input("time's/times/time").lower
input("phone number's/phone numbers/phone number").lower
input("")