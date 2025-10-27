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
    print("What would like me to generate then so examples random dates,times or even phone numbers  ")
