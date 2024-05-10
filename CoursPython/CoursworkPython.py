#MY bookMarks
#Different forms of calculate the final mark of a course
#Author: Yessenie Ochoa
#26/04/2024

#Declaration of the list and variables
#########
list10=[] #This is my list or container to store the numbers of the user
numberlist=0 #this is my variable to contain the numbers input for the user
i=1#counter for the for loop
a=0#variable for the median function in case that the module is par
b=0#variable for the median function in case that the module is par
M=0#variable to contain the lean for the median function
N=0#variable to contain the lean for the mean function
S=0#variable to contain the sum for the mean function
me=0#variable to contain the median for the skewness function
mn=0#variable to contain the median for the skewness function
SK=0#variable to contain the result of the skewness function
STD=0#variable to contain the STD for my skewness function


#Storing the User's data
#########
#for i in range(int(AmountNumbers)): //Was a possibility if we know the amount of numbers to input
print("You should add your marks for this course, press 0 to end")#message
#to interact with the user

numberlist = 1000000 #to initialize the variable with a number different
#than 0 and start the loop while
#we decide to do with a while to make to put many numbers as the user want
while numberlist != 0 or len(list10)<2 or numberlist>0: #the loop will work until the user mark 0 
        
        try:#to verify that the condition of the loop is working
            #to verify if there is minimum 2 numbers to work with
            numberlist=int(input("Please bring your " +str(i)+" mark \n"))
            
            
            if numberlist >= 1 :#To do not include the 0 on the list
                i+=1#To identify the number of the data in each input of the user    
                list10.append(numberlist)#to store the user's data in the list10
            else: #If not
                if len(list10)<2: #If the length of the list is les than 2
                    print("You have to input two marks minimum before reach the menu, Negatives numbers are not allowed. ")# to communicate the user that there is an error.
                else: #If not 
                    if numberlist!=0: #If the number is different than 0
                        print("Negatives numbers are not allowed, try again with a positive number")
                    
                    else: #If is 0
                        print("Thanks, now chose an option of the Menu please. ")# to communicate the user that he exit of this part of the program.
            #Raise Exception(If the user do not comply with the estipulate on the while conditional)
        except ValueError as e:# This sent a message of error when we put something
        #Different than a number
            print("There is the error exception, Try again with a number please")#Error message    
             


print("You in " + str(len(list10)) + " marks, those are: ")#to numerate the inputs of the user
print(list10)# to show the list of number stored on the list10


#Declaration of functions
#########
###########################
def In(list10): #to declare a method or function that is going to work with the list10

    numberlist=1000000#To declare  the variable numberlist with a different 
    #Number of cero and start the loop while
    while numberlist != 0 :#while the variable do not have a value 0 it will be asking for more numbers
       
        try:#Verification if the user brings  the correct number
            #Here I am asking for more numbers to add on the list10
            numberlist=int(input("Please bring more marks for this course "))
            #i+=1
            if numberlist != 0:#I am avoiding the value 0 out of our array, to avoid errors
                list10.append(numberlist)#Here i am store the numbers in our list10
        #Exception("Only Integers are allowed")
        except:#If catch an exception it is going to come back  to the loop while to ask again for more numbers
            print("There is the error exception, try again please")# to communicate the user that there is an error
             
         
    
    print("You input " + str(len(list10)) + " marks, those are: ")# to show the length of the list
    #print(list10)
    return list10 #returning the final values of the list
    #with the old numbers and the new numbers for this function


########################
def Mean(list10): #to declare a method or function Mean that is going to work with the list10

    #list10.sort()#for the mean we do not need to order
    S=sum(list10)#to contain the sum of the numbers of the list
    N=len(list10)#to contain the length of the numbers of the list
    print("Mean:")#To make more visual the result of the mean for the user
    return S/N #To return the result of the mean function dividing 
    #the sum and the lenght of the numbers 

#print(Mean(list10))#To check results(please do not activate)


#######################
def Median(list10): #to declare a method or function Median that is going to work with the list10

    print("Remember that the list is sort before the maths operation are done")   
    list10.sort() #To order first the list10 before is make any operation
    print(list10)
    M=len(list10) #to contain the length of the numbers of the list

    if M%2==1: #IMPAR
        #if conditional to verify if the module of the length is par or inpar
        
        print("Median: Impar") #To make more visual the result
        
        return list10[M//2] #To return the result of the median function
        #return list10[M//2]
    
    else:      # PAR
        a=list10[M//2-1]# here we are dividing the leng between 2 and
        #is going to bring an integer number,and is going to bring the middle position of the list menus 1
        b=list10[M//2]# here we are dividing the leng between 2 and
        #is going to bring an integer number, and is going to bring the middle position of the list
        print("Median: Par") #To make more visual the result
        
        return ((a+b)/2) #To return the result of the mean function
        #in this option we are working with a par length of the list#
        #it is doing the mean of the two numbers of the middle's position

#print(median(list10))#To check results(please do not activate)


#######################
def mode(list10): #to declare a method or function Mode that is going to work with the list10

    list10.sort() #To order first the list10 before making any operation

    frequencyNumber=0 #is going to keep the number of repetitions of a number
    counter=2         #is used to compare with frequencyNumber
    index=0           #container of the number

    
    for a in list10: #to run the numbers of the list10
        frequencyNumber=list10.count(a) #contain the number of the repetition of the number
        
        if (frequencyNumber>=counter): #If frequency is mayor than 1
            counter=frequencyNumber #to store the number of repetitions
            index=a #to contain the mode
    if len(set(list10)) == len(list10) : #With set I eliminate the repetition of the numbers
        #after I take the length and make a comparison with the real length of the list withc the if conditional. 
        return "There is no mode" #so if the length is equal, return a message of there is no a mode.
    else:
        print("We have " + str(counter) + " times " + str(index) + ".")
        print ("the mode is: " ) #if not show a message to head the mode return, so make more visible the result.
        return index #To return the result of the mode function.
        
        
#print(mode(list10))#To check results(please do not activate)


########################

def NumberList(list10):#This function Median is to add more numbers in the list, but in horizontal and separate by comas

    numberlist = input("Please add more marks in one line separate by commas 1,2,3,etc \n")# here we are asking for more numbers to input in a plain format separate by comas
    numbers = numberlist.split(",")#It is to store the input of numberlist in a new list called number 
    for i in range(len(numbers)): #to run through the list numbers 
        list10.append(int(numbers[i]))#To store the numbers of the loop on the original list10
    
    return list10 #to return the result of this function. 


##############################
def skewness(list10):#to declare a method or function skewness that is going to work with the list10

    #1)Mean
    mn = Mean(list10)#first we retrieve the result of the function mean in the variable mn
    #print (str(mn)) #To make verify errors//after clear

    #2)STD
    N=len(list10) #Is the len of the list
    num = 0# to initialize the variable num

    for i in range(len(list10)): #to run for every number of the list10
      
        num += ((list10[i]-mn)**2)/N #to igualate each number of the list110 to the mean with and after the square
        #print(num) #To make more visual the result
    STD=num**0.5 #calculation to obtain the standar deviation
    
    #print("The STD is") #To make more visual the result
    #print(STD)#To make more visual the result

    #3)Median
    me = Median(list10) #first we retrieve the result of the function median in the variable me
    #print("The Median is")
    #print(me)

    #4)Skewness
    SK=(((3*(mn-me))/STD)) #calculation to obtain the Skewness
    print("The skewness is:") #To make more visual the result
    return SK #To return the result of the skewness
    

##############################
#********To check************
def ReadFile():#function to function input more numbers separate by coma, from a file stored in our PC hard disk that is going to work with the list10

    try: #To catch any error in case that the file does not exist, or the name or path are wrong
        with open('MyFile.txt') as file: #to open the file
            numberlist =int(file.read()) #to read the content of the file, also we clouse here as well, is not necesary write more code
            #it is retrieving those numbers in the numberlist variable
            numbers = numberlist.split(",") #It is to store the input of numberlist in a new list called number
        for i in range(len(numbers)):#to run through the list numbers
            list10.append(int(numbers[i]))#To store the numbers of the loop on the original list10

        print("You in " + str(len(list10)) + " marks, those are: ")# to show the lengh of the list
        return list10 #to return the result of this function.

    except FileNotFoundError: #Error statement in case that the file is not found
        print("ERROR, The file was no found, try again please") # message of error in case that the file is not found


#Menu to choose which function the user want to use
#########
##############################
def menu(): #declaration of the function for the menu
    print ("1) Print the Mean") #First option of the menu
    print ("2) Print the Median") #Second option of the menu
    print ("3) Print the Mode") #Thirth option of the menu
    print ("4) Input again more numbers") #Fourth option of the menu
    print ("5) Print the Skewness") #Fifth option of the menu
    print ("6) More numbers, plane option, separate by coma") #Sixth option of the menu
    print ("7) Read the number from a file") #seventh option of the menu
    print ("8) EXIT") #Last option of the menu
    
menu() #close of the declaration options
option= int(input("Tell me which option would you like to choose")) #This option is going to capture the input number that the user wants to work


while option != 8 : #A loop to run through the option's case 
    #Here if we press 8 it is going to exit of the loop

    if option == 1 : #conditional if the option is 1
        print("Option1 done")#To make more visual the result
        print(Mean(list10)) #To call the function Mean on the list10 and print the result

    elif option ==2 : #conditional if the option is 2
        print("Option2 done") #To make more visual the result
        print(Median(list10)) #To call the function Median on the list10 and print the result

    elif option ==3 : #conditional if the option is 3
        print("Option3 done") #To make more visual the result
        print(mode(list10)) #To call the function mode on the list10 and print the result

    elif option ==4 : #conditional if the option is 4
        print("Option4 done") #To make more visual the result
        print(In(list10)) #To call the function "In" on the list10 and print the result
    
    elif option ==5 : #conditional if the option is 5
        print("Option5 done") #To make more visual the result
        print(skewness(list10)) #To call the function skewness on the list10 and print the result

    elif option ==6 : #conditional if the option is 6
        print("Option6 done") #To make more visual the result
        print(NumberList(list10)) #To call the function NumberList on the list10 and print the result

    elif option ==7 : #conditional if the option is 7
        print("Option7 done") #To make more visual the result
        print(ReadFile(list10)) #To call the function ReadFile on the list10 and print the result   

    menu()#*******Ask for those more options.
    option= int(input("Tell me which option would you like to choose")) #This line is to come back to the menu again

print("Thanks, Goodbye") #quit sentence

