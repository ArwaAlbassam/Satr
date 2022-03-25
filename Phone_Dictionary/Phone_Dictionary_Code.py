Telephone_info = {  
    'Amal' : '1111111111' ,
    'Mohammed' : '2222222222' ,
    'Khadijah'  : '3333333333' ,
    'Abdullah'  : '4444444444' ,
    'Rawan'  : '5555555555',         
    'Faisal' : '6666666666' ,
    'Layla' : '7777777777' }
    
def getname(info , num):
    if num.isdigit() and len(num) == 10:    
        for name, number in info.items():
            if num == number:
                print(name)
                break                              
        else:
            print("Sorry the number is not found!")    
    else:
        print("This is invalid number") 

def getnum(info, name_u):
    for name, number in info.items():
        if name_u == name:  
            print(number)  
            break                 
    else: 
        print("Sorry the name is not found!")
       
        
def adduser(info):
    name = input("Please enter the username you want to add: ")
    number = input("Please enter the user number you want to add: ")  
    if number.isdigit() and len(number) == 10:
        info[name] = number
    else:
        print("Invalid number, Please Try Again!") 
    return info
        
ch=int(input("Welcome to the phone dictionary. Please Enter the number: \n 1 if you want to search using phone number. \n 2 if you want to search using the name. \n 3 if you want to add a new user. \n 4 if you want to print the dictionary. \n 5 if you want to Exit \n "))
print("\n")

while ch!=5:
    if ch==1:
        user_val=input("Please, Enter the number: ")
        getname(Telephone_info, user_val)
    elif ch == 2:
        user_val=input("Please, Enter the name: ")
        getnum(Telephone_info,user_val)
    elif ch == 3:
        adduser(Telephone_info)
    elif ch==4:
        print(Telephone_info)
    else:
        print("Please Enter Valid Number")
    ch=int(input("Please Enter the number: \n 1 if you want to search using phone number. \n 2 if you want to search using the name. \n 3 if you want to add a new user. \n 4 if you want to print the dictionary. \n 5 if you want to Exit \n "))

print ("Thank you!")
