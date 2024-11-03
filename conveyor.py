# Fuction CHECKDATA will be used to check the data.txt file for data before returning the value.
def CHECKDATA():
# Initilaise Values that will be stored in the .txt file. This needs to be done here to ensure that the values are created for all situations.
# For example, if I initliased the variables within the except statement, the programme would fail if, for example, there was only one value stored in the .txt file or it did not exist.
    totalHours = 0
    totalProducts = 0  
# I have used a try statement here to catch foreseeable errors, for example if the text file has a string or does not exist, default values will be used instead.
# The with statement will open the text file for reading.        
    try:
        with open("data.txt", "r") as dataOperations:
            content = dataOperations.read()
            if content:
                value1, value2 = content.split(" ")
                totalHours = int(value1)
                totalProducts = int(value2)
                return totalHours, totalProducts
    except FileNotFoundError:
            with open("data.txt", "r") as dataOperations:
                dataOperations.write(f"{totalHours} {totalProducts}")
    except ValueError:
        pass
    return totalHours, totalProducts


# This function will be used to check which of the 4 Operators is operating the machine and pass their values to the OPERATION function.
# I have used a try statement here to catch foreseeable errors, for example if the text file does not exist, it will be created and a default value of 0 written into it. 
def CHECKOPERATOR():
    op1 = "Mahir"
    op2 = "Mark"
    op3 = "Bethany"
    op4 = "Jordan"
    opProducts = 0

    current = input("Who will be operating the Machine today? ")
# This checks for op1 or "Mahir" in this case
    if current == op1:
            try:
                with open("mahir.txt", "r") as mHours:
                    content = mHours.read().strip()
                    if content:
                        opProducts = int(content)
                        return opProducts, current
            except FileNotFoundError:
                with open("mahir.txt", "r") as mHours:
                    mHours.write(f"{opProducts}")
            except ValueError:
                pass
            return opProducts, current
 # This checks for op2 or "Mark" in this case   
    elif current == op2:
            try:
                with open("mark.txt", "r") as maHours:
                    content = maHours.read().strip()
                    if content:
                        opProducts = int(content)
                        return opProducts, current
            except FileNotFoundError:
                with open("mark.txt", "r") as maHours:
                    maHours.write(f"{opProducts}")
            except ValueError:
                pass
            return opProducts, current
# This checks for op3 or "Bethany" in this case
    elif current == op3:
            try:
                with open("bethany.txt", "r") as bHours:
                    content = bHours.read().strip()
                    if content:
                        opProducts = int(content)
                        return opProducts, current
            except FileNotFoundError:
                with open("bethany.txt", "r") as bHours:
                    bHours.write(f"{opProducts}")
            except ValueError:
                pass
            return opProducts, current
# This checks for op4 or "Jordan" in this case  
    elif current == op4:
            try:
                with open("jordan.txt", "r") as jHours:
                    content = jHours.read().strip()
                    if content:
                        opProducts = int(content)
                        return opProducts, current
            except FileNotFoundError:
                with open("jordan.txt", "r") as jHours:
                    jHours.write(f"{opProducts}")
            except ValueError:
                pass
            return opProducts, current
# If all inputs are incorrect, the programme will ask until a correct Operator is given.
    else:
        print("Operator not found")
        CHECKOPERATOR()





# Function START will be used to begin the programme. The correct code must be input for the machine to start.
def START():
# The values from CHECKDATA() and CHECKOPERATOR() have been stored as a tuple by the return statement. To access these, I created my variables as tuples which are assigned the values from CHECKDATA() and CHECKOPERATOR().
# If I did not do this, I would not be able to access my values from my other functions here.
    opProducts, opName = CHECKOPERATOR()
    totalHours, totalProducts = CHECKDATA()
    code = input("Good Morning! To start production, please enter the correct code: ")
# This code ensures that the programme will only start if the correct value is inputted. If not, it will ask for it again infinitely.    
    ccode = "START"
    if ccode == code:
# The variables totalHours, totalProducts, opProducts and opName are local variables, therefore, to access them in another function, I have passed them as arguments to the OPERATION function        
        OPERATION(totalHours, totalProducts, opProducts, opName)
    else:
        print('Incorrect Code')
        START()

# Function OPERATION will be used to define the operation of the machine. I have assumed a limit of 8 hours a day with each hour producing 4 units and a production limit of 22 before needing service.
# I have set variables for all of the limits so that they can be changed easily. The day limit is the amount of hours. Count is the hourly count for each day. Products is the daily count of production. 
def OPERATION(totalHours, totalProducts, opProducts, opName):
    dayLimit = 8
    count = 0
    products = 0
    productionLimit = 22
# This while loop will run until a full days iteration or until the productionLimit has been hit. All variables have been stored seperately to ensure they can be written into the .txt file.
    while count < dayLimit:
        count += 1
        products += 4
        totalHours += 1
        totalProducts += 4
        opProducts += 4
# This code will test if the production limit has been hit, and if so, it will wipe the.txt file, ready for re-initialisation the next day. This will also update the operators figures which are not wiped, but stored permanantly.
        if totalHours == productionLimit:
            print("Service Required")
            print("Number of hours since last service ", totalHours)
            print("Number of itmes produced since last serive: ", totalProducts)
            print ("Number of items produced by ", opName, "is: ", opProducts)
            open("data.txt", 'w').close()
# As .txt files cannot store integers, we need to convert them back into strings.
            sOpProducts= str(opProducts)
# I have used f' strings here to write back into the txt files as the operators will be dynamic and I cannot hard code which operator will be using the system.
            with open(f"{opName.lower()}.txt", "w") as update:
                update.write(sOpProducts)
            return
        else:
            pass
# This code will update the .txt file with the up to date numbers at the end of the day if the limit has not been hit. This will also update all the values for indivdual operators.
    data = str(totalHours) + " " + str(totalProducts)
    sOpProducts = str(opProducts)
    with open("data.txt", "w") as dataOperations:
        dataOperations.write(data)
    with open(f"{opName.lower()}.txt", "w") as update:
                update.write(sOpProducts)
    print("End of Day!")
    print("Total hours ran since last service: ", totalHours)
    print("Total products produced since last service: ", totalProducts)


START()
