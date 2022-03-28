class Calculus:
    def __init__(self,function):
        self.function = function
    def differentiate(self):
        pass
    def integrate(self):
        pass
    def __add__(self, other):
        pass
    def __sub__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __truediv__(self, other):
        pass

def isit_invalidFunction(function):
    variable_count = 0
    ValidVAR =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in ValidVAR:
        if letter in function:
            variable_count += 1
    if variable_count == 1:
        FunctionORNOT = True
    else:
        FunctionORNOT = False
    for i in function:
        if i in ['@','#','$','%','&',':','"',"'",'<','>','?']:
            FunctionORNOT = False
    return FunctionORNOT

def main():
    functionStorage = []
    exitCommands = ['exit','break','quit']
    userInput = input("Enter a function: ")
    Counter = 0
    while userInput.lower() not in exitCommands:
        if isit_invalidFunction(userInput):
            FunctionOF = input("Enter a variable to represent function: ")
            if FunctionOF in userInput:
                print("please enter a valid variable")
                FunctionOF = input("Enter a variable to represent function: ")
            if Counter >= 1:
                for i in functionStorage:
                    if FunctionOF != i[0]:
                        isValidVAR = True
                    else:
                        isValidVAR = False
                if isValidVAR:
                    functionStorage.append([FunctionOF, userInput])
                    print(functionStorage[-1][0], "= ", functionStorage[-1][1])
                    print(functionStorage)
                else:
                    print("it's not valid")
            else:
                functionStorage.append([FunctionOF, userInput])
                print(functionStorage[-1][0], "= ", functionStorage[-1][1])
        else:
            print("invalid function")
        userInput = input("Enter a function: ")
        Counter += 1

if __name__ == '__main__':
    main()