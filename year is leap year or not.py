# write a python program to check if a year is leap year or not. if  a year is divisible by 4 then it is leap year it is leap year but if the year is century year like 2000,1900,2100then it must be divisible by 400.
year=int(input("enter nummber"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("no leap year")
    else:
        print("no leap year")
else:
    print("no leap year")