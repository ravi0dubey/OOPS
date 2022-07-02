from module1 import Person

ravi=Person("Ravi","Dubey","r@gmail.com","1983")
astha =Person("Astha"," ","a@gmail.com","1988")
illisha =Person("Illisha","Dubey","i@gmail.com","2015")
lika =Person("Lika","Dubey","l@gmail.com","2019")

# If we create multiple init, it will always take the last one written
# ravi1=Person("RaviRanjan","Dubey")

#printing first person name
print(f"First name : {ravi.name}")
print(f"Surname : {ravi.surname}")
print(f"Emailid : {ravi.emailid}")
print(f"Year of Birth : {ravi.year_of_birth}")

#printing second person name
print(f"First name : {astha.name}")
print(f"Surname : {astha.surname}")
print(f"Emailid : {astha.emailid}")
print(f"Year of Birth : {astha.year_of_birth}")

#printing Third person name
print(f"First name : {illisha.name}")
print(f"Surname : {illisha.surname}")
print(f"Emailid : {illisha.emailid}")
print(f"Year of Birth : {illisha.year_of_birth}")

#printing Fourth person name
print(f"First name : {lika.name}")
print(f"Surname : {lika.surname}")
print(f"Emailid : {lika.emailid}")
print(f"Year of Birth : {lika.year_of_birth}")

#Concatenation Operation
print(f"{ravi.name} is married to {astha.name}")
print(ravi.name +" "  + "is married to " + astha.name )

#Getting current age
print("Ravi age is " + str(ravi.age()))
print("Astha age is " + str(astha.age()))
print("Illisha age is " + str(illisha.age()))
print("Lika age is " + str(lika.age()))

emailid= input("Enter Emailid : ")
print("Entered email id is :" + ravi.email_id_input(emailid))
print("Entered name is " + ravi.ask_name())