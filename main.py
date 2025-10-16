from faker import Faker

fake = Faker()
y = input("Would you like me to generate you an person y/n? ")
if y == "y":
    print(fake.name())
    print(fake.job())
    print(fake.date())
    print(fake.country())
    print(fake.state())
    print(fake.city())
    print(fake.zipcode())
else:
    print("Ok")
