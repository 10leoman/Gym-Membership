regimens_dict = {
'regimen1': {'Mon': 'Chest','Tue': 'Biceps','Wed': 'Rest','Thu': 'Back','Fri': 'Triceps','Sat': 'Rest','Sun': 'Rest'}, 
'regimen2': {'Mon': 'Chest','Tue': 'Biceps','Wed': 'Cardio/Abs','Thu': 'Back','Fri': 'Triceps','Sat': 'Legs','Sun': 'Rest'}, 
'regimen3': {'Mon': 'Chest','Tue': 'Biceps','Wed': 'Abs/Cardio','Thu': 'Back','Fri': 'Triceps','Sat': 'Legs','Sun': 'Cardio'}, 
'regimen4': {'Mon': 'Chest','Tue': 'Biceps','Wed': 'Cardio','Thu': 'Back','Fri': 'Triceps','Sat': 'Cardio','Sun': 'Cardio'}}


member_details_dict = {
"1001":{"Full Name":"Yash Chordia","Age":25,"Gender":"Male","Contact Number":1001,"Email ID":"yc@gmail.com","bmi":22,"Membership Duration":12,"Workout Regimen":"regimen2"},
"1002":{"Full Name":"Manish Pahuja","Age":26,"Gender":"Male","Contact Number":1002,"Email ID":"mp@gmail.com","bmi":45,"Membership Duration":6,"Workout Regimen":"regimen4"}
}

class SuperUser:
    try:
        global member_details_dict
        global regimens_dict


        def __init__(self):
            self.superuser_menu()
            pass


            
        def superuser_menu(self):
            print("Here are your options, SuperUser! \n 1. Create Member\n 2. View Member\n 3. Delete Member\
            \n 4. Create Regimen\n 5. View Regimen\n 6. Delete Regimen\
            \n 7. Exit")
            i = number_check(input("Please enter your choice\n\n"))
            while(i not in range(1,8)):
                if i == 7:
                    login()
                    break
                else:
                    print("Please enter a valid option!\n\n")
                    i = int(input("Please enter your choice, and make sure it's between 1 to 7\n\n"))
            else:     
                if i == 1:
                    self.create_member()
                    self.superuser_menu()
                elif i == 2:
                    self.view_member()
                    self.superuser_menu()
                elif i == 3:
                    self.delete_member(input("Please enter contact number of the Member to be deleted!\n\n"))
                    self.superuser_menu()
                elif i == 4:
                    self.create_regimen()
                    self.superuser_menu() 
                elif i == 5:
                    self.view_regimen()
                    self.superuser_menu()
                elif i == 6:
                    self.delete_regimen()
                    self.superuser_menu()

        def create_member(self):
            print("Okay superuser, let's create a new member!\n\n")
            num = input("Please enter the contact number to check if member does not exist!\n\n")
            while num in member_details_dict:
                print("Sorry it seems like the member already exists\n\n")
                break
            else:
                member_details_dict[num] = {}
                print("Okay seems like the member doesn't exist. Enter the details!\n\n")
                full_name = input("Please enter Full Name of Member!\n\n")
                member_details_dict[num]["Full Name"] = full_name

                age = input("Please enter Age of Member!\n\n")
                while(age.isdigit() == False):
                    age = input("Age has to be a number value!\n\n")
                member_details_dict[num]["Age"] = age

                gender = input("Please enter Gender of Member!\n\n")
                while(gender not in ['Male','MALE','M','m','Female','FEMALE','f','F','Others']):
                    gender = input("Please enter a valid gender('Male', 'Female' or 'Others')!")
                member_details_dict[num]["Gender"] = gender

                member_details_dict[num]["Contact Number"] = num

                email = input("Please enter Email ID of Member!\n\n")
                member_details_dict[num]["Email ID"] = email

                bmi = float(input("Please enter bmi of Member!\n\n"))
                while(isinstance(bmi, float) == False):
                    bmi = float(input("Please enter a correct value for bmi of Member!\n\n"))
                member_details_dict[num]["bmi"] = bmi

                duration = int(input("Please enter Membership Duration in months!\n\n"))
                while duration not in [1,3,6,12]:
                    duration = int(input("Please enter Correct Membership Duration in months! (1,3,6,12)\n\n"))
                member_details_dict[num]["Membership Duration"] = duration

                member_details_dict[num]["Workout Regimen"] = self.select_regimen(bmi)

            print("Lets go back to the Main Menu!\n\n") 


        def select_regimen(self, bmi):
            while(isinstance(bmi,float) == False):
                print("Sorry, Bmi entered is not a correct value!\n\n")
                break
            else:
                if(bmi < 18.5):
                    regimen = regimens_dict['regimen1']
                elif(bmi >= 18.5 and bmi < 25):
                    regimen = regimens_dict['regimen2']
                elif(bmi >= 25 and bmi < 30):
                    regimen = regimens_dict['regimen3']
                elif(bmi >= 30):   
                    regimen = regimens_dict['regimen4']

                return regimen

        def view_member(self):
            check = input("Please enter the Contact Number of the Member!\n\n")
            if check in member_details_dict:
                print("The Details for Member are: ")
                for detail in member_details_dict[check]:
                    if type(member_details_dict[check][detail]) != dict:
                        print('{} : {}'.format(detail, member_details_dict[check][detail]))
                    else:
                        print(detail + ":")
                        for j in member_details_dict[check][detail]:
                            print('{} : {}'.format(j, member_details_dict[check][detail][j]))
            else: 
                print("Sorry, it seems the Member doesn't exist!\n\n")

            print("Lets go back to the Main Menu!\n\n") 

        def delete_member(self, num):
            if num in member_details_dict:
                del member_details_dict[num]
            else:
                print("The member doesn't exist\n\n")
            print("Lets go back to the Main Menu!\n\n") 


        def create_regimen(self):
            plain_regimen = {'Mon': '', 'Tue': '', 'Wed': '', 'Thu': '', 'Fri': '', 'Sat': '', 'Sun': ''}
            print("Okay lets create a new regimen!")
            regimen_name = input('Please give a name to the new regimen!\n\n')
            while(regimen_name in regimens_dict):
                print("Sorry the regimen already exists! Please enter a different name!")
                regimen_name = input('Please give a name to the new regimen!\n\n')
            else:
                regimens_dict[regimen_name] = plain_regimen
                for i in regimens_dict[regimen_name]:
                    print("Enter workout for {}!".format(i))
                    regimens_dict[regimen_name][i] = input()
                print('Workout for {} Regimen is:'.format(regimen_name))
                for i in regimens_dict[regimen_name]:
                    print('{}: {}'.format(i, regimens_dict[regimen_name][i]))
            print("Lets go back to the Main Menu!\n\n")

        def view_regimen(self):
            print('Please choose an option! \n1. View all available regimens\n2. Enter name of regimen to view')
            i = number_check(input("Please enter your choice\n\n"))
            while(i not in range(1,3)):
                print("Please choose a valid option!(Either 1 or 2)")
                i = int(input())
            else:
                if i == 1:
                    for j in regimens_dict:
                        print(j)
                    reg_name = input("Please enter name of regimen you would like to see!\n\n")
                    if reg_name in regimens_dict:
                        print('Workout for {} Regimen is:'.format(reg_name))
                        for reg in regimens_dict[reg_name]:
                            print('{}: {}'.format(reg, regimens_dict[reg_name][reg]))
                    else:
                        print("Incorrect Regimen Name entered!")
                else:
                    reg_name = input("Please enter name of regimen you would like to see!\n\n")
                    if reg_name in regimens_dict:
                        print('Workout for {} Regimen is:'.format(reg_name))
                        for reg in regimens_dict[reg_name]:
                            print('{}: {}'.format(reg, regimens_dict[reg_name][reg]))
                    else:
                        print("Incorrect Regimen Name entered!")

            print("Lets go back to the Main Menu!\n\n") 

        def delete_regimen(self):
            regimen = input("Please enter the name of the regimen you would like to delete!")
            if regimen in regimens_dict:
                del regimens_dict[regimen]
            else:
                print("Seems like the regimen you are looking for already doesn't exist!")

    except:
        print("You must have entered an incorrect value!")
        
class Member:
    def __init__(self):
        self.num = input("Please enter contact number.")
        if self.num in member_details_dict:
            print("Welcome, {} to Yash's gym!".format(member_details_dict[self.num]['Full Name']))
            self.member_menu()
        else:
            print("Sorry it seems, you are not a member!\n Please ask the super user to add your details!")
    
    def member_menu(self):
        try:
            print("Please choose one of the following options!\n1. My Regime\n2. My Profile\n3. Exit Menu.")
            i = int(input())
            while(i not in range(1,3)):
                if i == 3:
                    login()
                    break
                i = int(input("Please enter a valid value!(Either 1 or 2)"))
            else:
                if i == 1:
                    self.member_regimen()
                    self.member_menu()
                elif i ==2:
                    self.member_profile()
                    self.member_menu()
        except:
            print("Please enter a valid value!")

    def member_regimen(self):
        print("Your Workout Regimen is:")
        for i in member_details_dict[self.num]['Workout Regimen']:
            print('{}: {}'.format(i, member_details_dict[self.num]['Workout Regimen'][i]))
            
    def member_profile(self):
        print('Your Complete Profile is:')
        for i in member_details_dict[self.num]:
            if i != 'Workout Regimen':
                print("{}: {}".format(i, member_details_dict[self.num][i]))
            else:
                self.member_regimen()

def number_check(var):
    while (not(var.isnumeric())):
        var = input("Please enter a valid numeric option! \n\n")
    else:
        return int(var)


def login():

    print("------Welcome to Yash's Gym!------")
    i = int(input("Please enter one of the following!\n1. Superuser\n2. Member\n3. Exit\n"))
    while(i not in range(1,3)):
        if i == 3:
            break
        i = int(input("Please enter a valid value!(Either 1 or 2)\n"))
    else:
        if i == 1:
            obj = SuperUser()
        else:
            obj = Member()

login()