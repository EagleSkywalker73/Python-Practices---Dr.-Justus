name = str(input("Pls type your name "))

g1 = float(input("Type your first grade"))
g2 = float(input("Type your second grade"))
g3 = float(input("Type your third grade"))

total = (g1 + g2 + g3 /300)
print("Your total is: ", total)

percentile = (total/300)*100
print("Your percentile is: ", percentile)


if percentile < 100 and percentile >=90:
    print("You got an A")
elif percentile < 90 and percentile >=80:
    print("You got a B")
elif percentile < 80 and percentile >=70:
    print("You got a C")
elif percentile < 70 and percentile >=60:
    print("You got a D")
elif percentile < 60 and percentile >=40:
    print("You got a E")
else:
    print("You got an F")
