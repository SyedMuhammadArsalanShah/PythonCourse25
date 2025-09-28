print("-"*8)


name= input("Enter Your Name \n")
email= input("Enter Your Email \n")
passs= input("Enter Your Password \n")
contact= input("Enter Your Contact \n")


print("Account Successfully created")
loginEmail= input("Enter Your Login Email \n")
loginPasss= input("Enter Your Login Password \n")

if email==loginEmail and passs==loginPasss:
    print("Account Successfully Login ", name)
   
    eng=float(input("Enter Your Eng Marks "))
    urdu=float(input("Enter Your Urdu Marks "))
    math=float(input("Enter Your Math Marks "))

    obt=eng+urdu+math

    percentage= obt/300*100

    if percentage<=100 and percentage>=80:
        print("Grade A1")
    elif percentage<=79 and percentage>=70:
        print("Grade A")
    elif percentage<=69 and percentage>=60:
        print("Grade B")
    elif percentage<=59 and percentage>=50:
        print("Grade C")
    elif percentage<=49 and percentage>=40:
        print("Grade F")
    else:
        print("Try Again !!")


    num=int(input("Enter Your Number"))
    if num %2==0:
        print("Even",num)
    else:
        print("Odd",num)

    if num<0:
        print("Negative",num)
    else:
        print("Positive",num)

    year = int(input("Enter Your Year"))
    if year %4==0:
        print("Leap Year ",year) 
    else:
        print("Is not a leap year")      
    
    status= "positive" if num >0 else "negative" 
    print(status)


else:
    print("Incorrect Email And Password")