#Take two user inputs one one as day and one as meal time. show the folloing table using nested if statement.
#      Day=Monday
#  breakfast=poori sabzi.
#  Lunch=Sambhar Rice.
#  Dinner=Chicken Rice.
#      Day=Tuesday
#  breakfast=Poha
#  Lunch=Rajma Rice'
#  Dinner=Roti Sabji.
day=input("enter day")
mealtime=input(("enter mealtime"))
if day=="Monday":
    if mealtime=="breakfast":
        print("porrisabji")
    elif mealtime==("lunch"):
        print("samber rice")
    elif mealtime==("dinner"):
        print("roti sabji")
    else:
        print("none")
elif day=="Tuesday":
    if mealtime=="breakfast":
        print("poha")
    elif mealtime=="lunch":
        print("rajma rice")
    elif mealtime=="dinner":
        print("roti sabji")
    else:
        print("none")
else:
    print("none")