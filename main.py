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
if name == "john/John":
    print("Your new name is now Johnson")
else:
    print("Your new name is Jackson")
