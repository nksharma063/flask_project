import string

#importing string for special charcaters
    
def check_password_strength():
    password = input("Please enter the password with length more than 8, it shoud contain one upper case, one lower case, one special character from  like !, @, #, $, and  a number(0-9): ")
    """
    there are different list declared below to append the password and different category
    """
    uppercase = []
    lowercase = []
    specialCharacter = []
    digits = []
    space = []
    if len(password) <= 8:
        print(f"Please try again length should be atleast 8 character, please try again or click on forget password")
        print()
        print()
        print(check_password_strength())
    else: 
        for each in password:   #itreating over string 
            if each == ' ' or each == '  ':
                space.append(each)
                print("Yes of course i forgot, please do not put any space as well or double spaces, please try again", check_password_strength())
            elif each.isupper(): # if any uppercase
                uppercase.append(each)
            elif each.islower():
                lowercase.append(each)  # if any lower case
            elif each.isdigit():
                digits.append(each)   #if any digit
            elif each in string.punctuation:
                specialCharacter.append(each)  #if any special charcater
            else:
                pass
    
    if (len(uppercase) ==  0):
        print("Please enter one atleast one uppercase, try again")
        print()
        print()
        print(check_password_strength())
    
    elif (len(lowercase) == 0):
        print("Please enter one atleast one lowercase, try again")
        print()
        print()
        print(check_password_strength())
    
    elif (len(digits) == 0):
        print("Please enter one atleast one digit, try again")
        print()
        print()
        print(check_password_strength())
    
    elif (len(space) > 0):
        print("Please dont use any blank spaces while choosing password, try again")
        print()
        print()
        print(check_password_strength())
    
    elif (len(specialCharacter) == 0):
        print("Please enter atleast one special character, try again")
        print()
        print()
        print(check_password_strength())        
    
    elif (len(uppercase) > 0 and len(lowercase) > 0 and len(digits) > 0 and len(specialCharacter) and len(space) == 0):
        return True
    
    else:
        return False

    #    lowercase) > 0 and len(digits) > 0 and len(digits) > 0) or (len(space) ==  0):
    # #     print("Please make atleast one uppercase")
    # elif (len(lowercase) ==  0) and (len(uppercase) > 0 and len(digits) > 0 and len(digits) > 0) and (len(space) ==  0):
    #     print("Please make atleast one lowercase")
    # elif (len(digits) ==  0) and (len(uppercase) > 0 and len(lowercase) > 0 and len(digits) > 0) or (len(space) ==  0):
    #     print("Please make atleast one number")
print(check_password_strength())


