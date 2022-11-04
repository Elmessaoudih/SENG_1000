import math

# Dictionary of paint colors and cost per gallon
paint_colors = {'red': 35,'blue': 25,'green': 23}
print("Enter wall height (feet):")
wall_height=int(input())
print("Enter wall width (feet):")
wall_width=int(input())
wall_area=wall_height*wall_width
print("Wall area: "+str(wall_area)+str(" square feet"))
paint=wall_area/350.0
print("Paint needed:{:.2f} gallons".format(paint))
cans=round(paint)
print("Cans needed: "+str(cans)+" can(s)")
print("Choose a color to paint the wall:")
color=input()
cost=cans*paint_colors[color]
print("Cost of purchasing "+color+" paint: $"+str(cost))
color = input('\nChoose a color to paint the wall:\n')
print("Cost of purchasing",color,"paint: $"+str(cans*paint_colors[color]))