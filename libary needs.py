#your local libary needs your help!given the expected and actual return dates for a libary books ,creat a program that calculate,s the fine (if any).The fee structure is as follows.
#if the book is returned on or before the excepted return date, no fine will be charge(i.e.fine=0)
#if the book is returned after the expected return but still with in the same calender month and  year as the excepted return date,fine=Rs15*number of day late
#if the book is returned after the excepted return month but still with in the same calender year as the excepted reeturn date the fine=Rs.500*number of days late.
#if the book is returned after the calender year in which is was excepted there is a fxied fine of Rs.10,000.
expected_day=int(input("enter number"))
excepted_month=int(input("enter number"))
excepted_year=int(input("enter number"))
return_day=int(input("enter number"))
return_month=int(("enter number"))
return_year=int(input("enter number"))
if excepted_month==return_month and excepted_year==return_year:
    if return_day<=expected_day:
        print("no charge")