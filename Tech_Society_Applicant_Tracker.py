import re
class Applicant:
    applicant_details=[] #To store the applicant data in the list 
    def __init__(self,name,roll,year,number,mail):
        self.name=name
        self.rollno=roll
        self.year=year
        self.number=number
        self.mail_id=mail
        Applicant.applicant_details.append(self)
    def show_applicant(self):#used to show specific applicant data 
        return(f"Name{self.name}, Rollno-{self.rollno}, Year={self.year}, Phone Number={self.number}, Mail id={self.mail_id}")
    @classmethod
    def show_all_applicant(cls):#used to show all applicant data in one time 
        if len(Applicant.applicant_details)==0:#checking if there are any applicant in the list or not 
            print("There are no applicant")#if not present then print this 
            return
        else:
            for app in cls.applicant_details:#if there are any applicant then it will show this 
                print(app.show_applicant())
    @staticmethod
    def valid_rollno(roll):#used to check if the roll number is valid or not 
        if len(roll)==8:
            return True
        else:
            return False
    @staticmethod
    def valid_mail(mail):#checking if the mail is valid or not using regex
      pattern=bool(re.fullmatch(r"^[0-9]+@kiit\.ac\.in+$",mail))# General mail_id of Kiit is to be matched in the entered roll_number 
      if pattern==True:
        return True
      else :
        return False
   
n=int(input("Enter the number of applicant you want to add: "))#asking the user to entering the total number of applicant 

#used for manual entry of the applicant through terminal 
for applicant in range(n):
    name=input("Enter name: ")
    roll=input("Roll: ")
    year=input("Year: ")
    number=input("Number: ")
    mail=input("Mail id: ")

    if Applicant.valid_rollno(roll):#checking if the roll number is valid or not
        Applicant(name,roll,year,number,mail)#if roll number is valid then an object is created 
            
