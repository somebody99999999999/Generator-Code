from faker import Faker

fake = Faker()
input("Would you like me to generate you an person y/n? ")
y = input
if input == y:
    print(fake.name())
    print(fake.job())
    print(fake.date())
    print(fake.country())
    print(fake.state())
    print(fake.city())
    print(fake.zipcode())