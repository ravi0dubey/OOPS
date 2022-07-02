from datetime import date
class Person:
    def __init__(self,name1,surname1,emailid1,year_of_birth1):
        self.name=name1
        self.surname=surname1
        self.emailid= emailid1
        self.year_of_birth= year_of_birth1

# If we create multiple init, it will always take the last one written
    # def __init__(self,name2,surname2):
    #     self.name=name2
    #     self.surname=surname2


    def age(self):
        return  date.today().year - int(self.year_of_birth)

    def email_id_input(self,email_id1):
        return email_id1

    def ask_name(self):
        name = input("Enter your name: ")
        return name
