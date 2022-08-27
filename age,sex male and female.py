#Ask user to enter age, sex(m or f),marital status (y or n) and then using following rules print their place of service 
#if employee is female , then she will work only in urban ares
#if employee is a male and age is in between 20 to40 then he may work in any where.
#if employee is a male and age is in between 40 to 60 then he in will work in urban areas only.
#And any other input of age should print "ERROR"
age=int(input("enter number"))
sex=input("enter sex")
if sex=="femal":
    print("only in urban area")
elif sex=="male":
    if age>=20 and age<40:
        print("work in any where")
    elif age>=40 and age<60:
        print("only in urban area")
    else:
        print("error")
else:
    print("error")
