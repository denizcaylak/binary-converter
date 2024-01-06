#Remzi Deniz Çaylak 150210081 HW1 Q2

def floatToBinary(floatingNum): #This is my function for converting floating numbers to binary.
    if floatingNum > 1:         #In this part function separates the integer part and the floating part os the input.
        floatingPart = floatingNum%1
        decimalPart = int(floatingNum - floatingPart)
    else:
        floatingPart = floatingNum
        decimalPart = 0
    
    decimalBinary = []
    if decimalPart == 0:    #This is the converting the integer to binary.
        decimalBinary.insert(0,0)
    else:
        while decimalPart!=0:
            decimalBinary.insert(0,(decimalPart%2)) #Checks the mod and adds it to beginning of binary.
            decimalPart = decimalPart //2 #Divides the integer by 2 in order continue with the next decimal of binary. 

    floatingBinary = []
    while floatingPart !=0: #This is the converting the floating part of the number to binary.
        floatingPart = floatingPart*2 #First we multiply by 2 in order the check first decimal after coma.
        if floatingPart >= 1:
            floatingBinary.append(1)  #Checks the next decimals. If the number is greater than 1, adds 1 and continues with the remaining floating number.
            floatingPart = floatingPart - 1
        else:
            floatingBinary.append(0)
    floatingBinary.insert(0,',')
    print("Bİnary version of this floating number is:") #Printing of the full binary.
    for x in range(len(decimalBinary)):
        print (decimalBinary[x], end='')
    for x in range(len(floatingBinary)):
        print (floatingBinary[x], end='')

def rationalToBinary(numerator, denominator): #This is my function for converting rational numbers to binary.
    decimalPart = numerator // denominator #First takes the integer part because rational number may be greater than 1.

    decimalBinary = []
    if decimalPart == 0:        #Converting the integer to binary. Same as other function.
        decimalBinary.insert(0,0)
    else:
        while decimalPart!=0:
            decimalBinary.insert(0,(decimalPart%2))
            decimalPart = decimalPart //2

    divisionBinary = []
    numerator = numerator % denominator #Converting the rational part of the number to binary.
    while numerator != 0:
        numerator*=2
        if numerator >= denominator:    
            divisionBinary.append(1)    #Multiplying the numerator by 2 and checks if it is greater than its denominator.
            numerator = numerator - denominator #If it is greater, adds 1 to binary.
        else:
            divisionBinary.append(0)

    divisionBinary.insert(0,',')
    print("Binary version of this rational number is:") #Printing of the final binary.
    for x in range(len(decimalBinary)):
        print (decimalBinary[x], end='')
    for x in range(len(divisionBinary)):
        print (divisionBinary[x], end='')



while(True):
    select = int(input("For floating point to binary, enter 1. For rational number to binary, enter 2: ")) #Make your decision.
    if select == 1:
        fnumber = float(input("Enter floating number: ")) #Enter the floating number like 14.125.
        floatToBinary(fnumber)
        break
    elif select == 2:
        numeratorNumber = int(input("Enter numerator of rational number: ")) #Enter numerator and denominator separately.
        denominatorNumber = int(input("Enter denominator of rational number: "))
        rationalToBinary(numeratorNumber, denominatorNumber)
        break
    else:
        print("Enter 1 or 2.")

input("\nPress for end the program.")