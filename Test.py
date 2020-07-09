
def calcMain():
    calculation = input("What Type of caluction would you like to carry out? Add, Subtract, Multiply, Divide ")
    
    if calculation == "Add":
        Adder()
    elif calculation == "Subtract":
        Subtracter()
    elif calculation == "Multiply":
        Multiplyer()
    elif calculation == "Divide":
        Divider()



def Adder():
    Add1 = int(input("Please input the first number you wish to add "))
    Add2 = int(input("Please input the Second number you wish to add "))

    AddResult = Add1 + Add2
    print("The result of the calculation was ", AddResult)

    NewCalc("Add")

def Subtracter():
    Subtract1 = int(input("Please input the number you wish to subtract from "))
    Subtract2 = int(input("Please input the number you wish to subtract "))

    SubResult = Subtract1 - Subtract2
    print("The result of the calculation was ", SubResult)

    NewCalc("Sub")

def Multiplyer():
    Mult1 = int(input("Please input the first number you wish to multiply "))
    Mult2 = int(input("Please input the second number you wish to multiply "))

    MultResult = Mult1 * Mult2
    print("The result of the calculation was ", MultResult)

    NewCalc("Mult")

def Divider():
    Div1 = int(input("Please input the number you wish to divide "))
    Div2 = int(input("Please input the number you wish to divide by "))

    DivResult = Div1 / Div2

    
    print("The result of the calculation was ", DivResult)

    NewCalc("Div")

def Modulo():
    Mod1 = int(input("Please input the number you wish to divide to find the remainder "))
    Mod2 = int(input("Please input the number you wish to divide by "))

    ModResult = Mod1 / Mod2

    
    print("The result of the calculation was ", DivResult)

    NewCalc("Div")

def NewCalc(x): 
    AnotherCalc = input("Would you like to preform another calculation Yes or No? ")
    Type = x

    if AnotherCalc == "Yes":
        WhichCalc = input("Would you like to preform the Same type of calculation or a Different one? ")
        if WhichCalc == "Same":
           
            if Type =="Add":
                Adder()
            elif Type == "Sub":
                Subtracter()
            elif Type == "Mult":
                Multiplyer()
            elif Type == "Div":
                Divider()
            
        elif WhichCalc == "Different":
            calcMain()
    elif AnotherCalc == "No":
        exit()

calcMain()
