import re 

def __PasswordValidate(password):
    isValid = True
    if (len(password)<8): 
        isValid = False
    elif not re.search("[A-Z]", password): 
        isValid = False
    elif not re.search("[a-z]", password): 
        isValid = False
    elif not re.search("[0-9]", password): 
        isValid = False
    elif re.search("\s", password): 
        isValid = False

    return isValid

def __main__():
    password = input("Digite a senha: ")
    if(__PasswordValidate(password)):
        print("Essa senha é válida")
    else:
        print("Essa senha não é válida")
        
__main__()